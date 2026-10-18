"""Core helpers for NEET Data Hub generators (English).

A generator is ``fn(rng)`` returning one question built with ``Q`` (or None).
``@gen(chapter_id, weight)`` registers it for a syllabus chapter. The same
rules as the School MCQ Bank apply: 4 distinct options, exactly one correct,
numeric answers computed, fact tables checked so no wrong option is also true.
"""
import math
import re

REGISTRY = []


def gen(chapter, weight=1, difficulty=None):
    def deco(fn):
        REGISTRY.append(dict(chapter=chapter, weight=weight, difficulty=difficulty, fn=fn))
        return fn
    return deco


def Q(question, answer, wrongs, explanation="", difficulty=None):
    answer = str(answer).strip()
    seen = {answer.lower()}
    picked = []
    for w in wrongs:
        w = str(w).strip()
        if w and w.lower() not in seen:
            seen.add(w.lower())
            picked.append(w)
        if len(picked) == 3:
            break
    if len(picked) < 3 or not answer:
        return None
    return dict(question=question.strip(), answer=answer, wrongs=picked,
                explanation=explanation.strip(), difficulty=difficulty)


# ---------------------------------------------------------------- numbers

def fmt(x, dec=2):
    if isinstance(x, int):
        return str(x)
    x = round(float(x), dec)
    if x == int(x):
        return str(int(x))
    return f"{x:.{dec}f}".rstrip("0").rstrip(".")


def sig(x, n=3):
    if x == 0:
        return "0"
    d = n - int(math.floor(math.log10(abs(x)))) - 1
    return fmt(round(x, d), max(d, 0))


def sci(x, n=3):
    if x == 0:
        return "0"
    e = int(math.floor(math.log10(abs(x))))
    if -3 <= e <= 5:
        return sig(x, n)
    m = round(x / 10 ** e, n - 1)
    if abs(m) >= 10:
        m /= 10
        e += 1
    return f"{fmt(m, n - 1)} × 10^{e}"


def wrong_nums(rng, x, unit="", n=3, form=sig, factors=(2, 0.5, 4, 0.25, 1.5, 3, 10, 0.1, 1.25, 0.8)):
    """Wrong numeric options: typical slips (doubling, halving, factor of 10...)."""
    target = form(x)
    out = []
    for f in rng.sample(list(factors), len(factors)):
        v = form(x * f)
        if v != target and v not in out and v not in ("0", "-0"):
            out.append(v)
        if len(out) == n:
            break
    return [f"{v}{unit}" for v in out]


def num_q(rng, question, value, unit="", explanation="", form=sig, wrongs=None, difficulty=None):
    """A numeric MCQ: ``wrongs`` may list specific mistake values; the rest are filled in."""
    ans = f"{form(value)}{unit}"
    wl = []
    for w in (wrongs or []):
        s = f"{form(w)}{unit}"
        if s != ans and s not in wl:
            wl.append(s)
    for s in wrong_nums(rng, value, unit, 6, form):
        if s != ans and s not in wl:
            wl.append(s)
    return Q(question, ans, wl[:3] if len(wl) >= 3 else wl, explanation, difficulty)


# ---------------------------------------------------------------- fact tables

def _words(s):
    return set(re.findall(r"[a-z0-9]+", s.lower()))


def similar(rng, answer, pool, k=3, top=6):
    a_digit = bool(re.search(r"\d", answer))
    a_first = answer.lower().split()[0] if answer.split() else ""
    a_words = _words(answer)
    a_len = len(answer.split())
    scored = []
    for p in dict.fromkeys(pool):
        if p.lower() == answer.lower():
            continue
        s = 0.0
        if bool(re.search(r"\d", p)) != a_digit:
            s += 6
        first = p.lower().split()[0] if p.split() else ""
        if first == a_first:
            s -= 2
        s -= 1.5 * len((_words(p) & a_words) - {"a", "an", "the", "of", "and", "in", "to"})
        s += 0.8 * abs(len(p.split()) - a_len) + abs(len(p) - len(answer)) / 12
        s += rng.random() * 1.2
        scored.append((s, p))
    scored.sort()
    best = [p for _, p in scored[:max(top, k)]]
    return rng.sample(best, min(k, len(best)))


def relation(rng, rows, stem, reverse_stem=None, expl=None):
    """Ask about a (key, value[, also-true values]) table, forward or reversed.

    Wrong options come from other rows; values listed as "also true" for a key
    are never offered as its wrong options.
    """
    rows = [(r[0], r[1], set(r[2]) if len(r) > 2 else set()) for r in rows]
    k, v, also = rng.choice(rows)
    e = expl(k, v) if expl else f"{k}: {v}."
    if reverse_stem and rng.random() < 0.5:
        bad = {a for a, b, x in rows if b == v or v in x}
        wrong = [a for a, b, _ in rows if a not in bad]
        if len(set(wrong)) < 3:
            return None
        return Q(reverse_stem.format(v), k, similar(rng, k, wrong), e)
    bad = {b for a, b, _ in rows if a == k} | also
    wrong = [b for a, b, _ in rows if b not in bad]
    if len(set(wrong)) < 3:
        return None
    return Q(stem.format(k), v, similar(rng, v, wrong), e)


def odd_one(rng, groups, label_not, label_is=None):
    """Category question from {category: [members]} (members must not repeat across groups)."""
    cats = [c for c, m in groups.items() if len(m) >= 3]
    cat = rng.choice(cats)
    members = list(dict.fromkeys(groups[cat]))
    others = [x for c, m in groups.items() if c != cat for x in m if x not in members]
    if len(others) < 3:
        return None
    if label_is is None or rng.random() < 0.5:
        out = rng.choice(others)
        oc = next(c for c, m in groups.items() if out in m)
        ins = rng.sample(members, 3)
        return Q(label_not.format(cat), out, ins, f"{', '.join(ins)}: {cat}. {out}: {oc}.")
    inn = rng.choice(members)
    outs = rng.sample(others, 3)
    return Q(label_is.format(cat), inn, outs, f"{inn} belongs to {cat}.")


def table(chapter, rows, stem, reverse_stem=None, weight=1, expl=None):
    """Register a fact table as a generator for ``chapter``."""
    gen(chapter, weight)(lambda rng: relation(rng, rows, stem, reverse_stem, expl))


def groups(chapter, grp, label_not, label_is=None, weight=1):
    gen(chapter, weight)(lambda rng: odd_one(rng, grp, label_not, label_is))


def facts(chapter, true_facts, false_facts, topic, weight=1):
    gen(chapter, weight)(lambda rng: statements(rng, true_facts, false_facts, topic))


def statements(rng, true_facts, false_facts, topic):
    """'Which statement is correct?' from hand-checked true and false statements."""
    if rng.random() < 0.5:
        a = rng.choice(true_facts)
        return Q(f"{topic}: which statement is correct?", a, rng.sample(false_facts, 3), a)
    a = rng.choice(false_facts)
    return Q(f"{topic}: which statement is NOT correct?", a, rng.sample(true_facts, 3),
             f"Incorrect: {a}")
