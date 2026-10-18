"""Build the NEET Data Hub.

Run:  python build_hub.py
Reads the School MCQ Bank (read-only) and the NEET generators in hub/, then writes:
  output/neet_hub.db    SQLite: tables chapters and questions
  output/neet_hub.csv   all questions for spreadsheets
  docs/data/index.json   syllabus tree with question counts (for the learning space)
  docs/data/c01.json ... c12.json   questions per class
Deterministic: a fixed seed gives the same hub every run.
"""
import csv
import json
import os
import random
import re
import sqlite3
import sys
from collections import Counter, defaultdict

from hub.core import REGISTRY
from hub import gen_bio11, gen_bio12, gen_phys, gen_chem, gen_extra  # noqa: F401  (register generators)
from hub.syllabus import CHAPTERS, NEET_UNITS, chapter_for_bank

ROOT = os.path.dirname(os.path.abspath(__file__))
BANK = r"C:\Users\saiqu\Projects\School_MCQ_Bank\output\mcq_bank.db"
OUT = os.path.join(ROOT, "output")
WEB = os.path.join(ROOT, "docs", "data")
SEED = 20261018
NEW_PER_CHAPTER = {"Biology": 80, "Chemistry": 60, "Physics": 60}
MAX_FAILS = 120


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())


def import_bank(seen):
    rows = []
    con = sqlite3.connect(BANK)
    cur = con.execute("select id, class_level, subject, topic, difficulty, question, option_a, option_b, option_c, option_d, "
                      "correct_option, correct_answer, explanation from questions where subject in ('Physics','Chemistry','Biology','EVS')")
    skipped = Counter()
    for (bid, cls, subj, topic, diff, q, a, b, c, d, co, ca, ex) in cur:
        ch = chapter_for_bank(cls, subj, topic, q)
        if ch is None:
            skipped[(cls, subj, topic)] += 1
            continue
        key = norm(q) + "||" + norm(ca)
        if key in seen:
            continue
        seen.add(key)
        rows.append(dict(chapter_id=ch["id"], difficulty=diff, question=q, opts=[a, b, c, d], correct="ABCD".index(co),
                         explanation=ex or "", source="School MCQ Bank", bank_id=bid))
    con.close()
    return rows, skipped


def generate(seen, rng):
    rows = []
    shortfalls = []
    by_ch = defaultdict(list)
    for g in REGISTRY:
        by_ch[g["chapter"]].append(g)
    for cid in sorted(by_ch):
        ch = CHAPTERS[cid]
        quota = NEW_PER_CHAPTER[ch["subject"]]
        cycle = [g for g in by_ch[cid] for _ in range(g["weight"])]
        fails = defaultdict(int)
        made = 0
        pos = 0
        while made < quota and cycle:
            g = cycle[pos % len(cycle)]
            pos += 1
            try:
                q = g["fn"](rng)
            except (ZeroDivisionError, ValueError, IndexError, OverflowError):
                q = None
            key = norm(q["question"]) + "||" + norm(q["answer"]) if q else None
            if q is None or key in seen:
                fails[id(g)] += 1
                if fails[id(g)] >= MAX_FAILS:
                    cycle = [x for x in cycle if x is not g]
                continue
            fails[id(g)] = 0
            seen.add(key)
            opts = q["wrongs"] + [q["answer"]]
            rng.shuffle(opts)
            rows.append(dict(chapter_id=cid, difficulty=q.get("difficulty") or g.get("difficulty") or "Medium",
                             question=q["question"], opts=opts, correct=opts.index(q["answer"]),
                             explanation=q["explanation"], source="NEET Hub generator", bank_id=None))
            made += 1
        if made < quota:
            shortfalls.append((cid, made, quota))
    return rows, shortfalls


def validate(rows):
    problems = []
    for r in rows:
        if len(r["opts"]) != 4 or len({o.strip().lower() for o in r["opts"]}) != 4:
            problems.append(("options not 4 distinct", r["question"], r["opts"]))
        if not r["question"].strip() or any(not str(o).strip() for o in r["opts"]):
            problems.append(("empty text", r["question"], r["opts"]))
        if r["chapter_id"] not in CHAPTERS:
            problems.append(("unknown chapter", r["chapter_id"], r["question"]))
    return problems


def write(rows):
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(WEB, exist_ok=True)
    order = {cid: i for i, cid in enumerate(CHAPTERS)}
    rows.sort(key=lambda r: (CHAPTERS[r["chapter_id"]]["cls"], order[r["chapter_id"]], r["source"] != "School MCQ Bank"))
    for i, r in enumerate(rows, 1):
        r["id"] = i

    db = os.path.join(OUT, "neet_hub.db")
    if os.path.exists(db):
        os.remove(db)
    con = sqlite3.connect(db)
    con.execute("""CREATE TABLE chapters (id TEXT PRIMARY KEY, class_level INTEGER, subject TEXT, branch TEXT,
                   neet_unit INTEGER, neet_unit_title TEXT, title TEXT, in_neet INTEGER, ecos_link TEXT)""")
    con.execute("""CREATE TABLE questions (id INTEGER PRIMARY KEY, chapter_id TEXT REFERENCES chapters(id), class_level INTEGER,
                   subject TEXT, difficulty TEXT, question TEXT, option_a TEXT, option_b TEXT, option_c TEXT, option_d TEXT,
                   correct_option TEXT, correct_answer TEXT, explanation TEXT, source TEXT, bank_id INTEGER)""")
    con.execute("CREATE INDEX idx_q_chapter ON questions(chapter_id)")
    con.execute("CREATE INDEX idx_q_class_subject ON questions(class_level, subject)")
    used = {r["chapter_id"] for r in rows}
    con.executemany("INSERT INTO chapters VALUES (?,?,?,?,?,?,?,?,?)",
                    [(c["id"], c["cls"], c["subject"], c["branch"], c["unit"], c["unit_title"], c["title"], int(c["neet"]), c["ecos"])
                     for c in CHAPTERS.values() if c["id"] in used])
    con.executemany("INSERT INTO questions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    [(r["id"], r["chapter_id"], CHAPTERS[r["chapter_id"]]["cls"], CHAPTERS[r["chapter_id"]]["subject"], r["difficulty"],
                      r["question"], *r["opts"], "ABCD"[r["correct"]], r["opts"][r["correct"]], r["explanation"], r["source"], r["bank_id"])
                     for r in rows])
    con.commit()
    con.close()

    with open(os.path.join(OUT, "neet_hub.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "class", "subject", "chapter_id", "chapter", "neet_unit", "difficulty", "question", "option_a", "option_b",
                    "option_c", "option_d", "correct_option", "explanation", "source"])
        for r in rows:
            c = CHAPTERS[r["chapter_id"]]
            w.writerow([r["id"], c["cls"], c["subject"], c["id"], c["title"], c["unit_title"], r["difficulty"], r["question"],
                        *r["opts"], "ABCD"[r["correct"]], r["explanation"], r["source"]])

    counts = Counter(r["chapter_id"] for r in rows)
    index = dict(units=NEET_UNITS, chapters=[
        dict(id=c["id"], cls=c["cls"], subject=c["subject"], branch=c["branch"], unit=c["unit"], unitTitle=c["unit_title"],
             title=c["title"], neet=c["neet"], ecos=c["ecos"], count=counts[c["id"]])
        for c in CHAPTERS.values() if counts[c["id"]]])
    with open(os.path.join(WEB, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))
    by_cls = defaultdict(list)
    for r in rows:
        by_cls[CHAPTERS[r["chapter_id"]]["cls"]].append(
            [r["id"], r["chapter_id"], r["difficulty"][0], r["question"], r["opts"], r["correct"], r["explanation"],
             1 if r["source"] == "School MCQ Bank" else 0])
    for cls, qs in by_cls.items():
        with open(os.path.join(WEB, f"c{cls:02d}.json"), "w", encoding="utf-8") as f:
            json.dump(qs, f, ensure_ascii=False, separators=(",", ":"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rng = random.Random(SEED)
    seen = set()
    bank_rows, skipped = import_bank(seen)
    new_rows, shortfalls = generate(seen, rng)
    rows = bank_rows + new_rows
    problems = validate(rows)
    print(f"From School MCQ Bank: {len(bank_rows)} (left out as non-science: {sum(skipped.values())})")
    print(f"New NEET questions:   {len(new_rows)}")
    print(f"Total:                {len(rows)}")
    by = Counter((CHAPTERS[r['chapter_id']]['cls'], CHAPTERS[r['chapter_id']]['subject']) for r in rows)
    for cls in range(1, 13):
        print(f"  Class {cls:2}: " + ", ".join(f"{s} {by[(cls, s)]}" for s in ("Physics", "Chemistry", "Biology") if by[(cls, s)]))
    neet = [r for r in rows if CHAPTERS[r["chapter_id"]]["neet"]]
    print(f"NEET-syllabus questions (Class 11-12): {len(neet)}  " +
          ", ".join(f"{s} {sum(1 for r in neet if CHAPTERS[r['chapter_id']]['subject'] == s)}" for s in ("Physics", "Chemistry", "Biology")))
    if shortfalls:
        print("Chapters where generators ran out before the target:")
        for cid, made, quota in shortfalls:
            print(f"  {cid} {CHAPTERS[cid]['title']}: {made}/{quota}")
    thin = [c for c in CHAPTERS.values() if c["neet"] and sum(1 for r in rows if r["chapter_id"] == c["id"]) < 40]
    for c in thin:
        print(f"THIN NEET CHAPTER: {c['id']} {c['title']}")
    if problems:
        print("PROBLEMS:", len(problems))
        for p in problems[:30]:
            print("  ", p)
        sys.exit(1)
    if "--dry" in sys.argv:
        return
    write(rows)
    print("Written to", OUT, "and", WEB)


if __name__ == "__main__":
    main()
