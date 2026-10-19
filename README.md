# NEET Data Hub and NEET Learning Hub

A question-and-answer data hub for Biology, Chemistry and Physics from Class 1 to Class 12, organised
as a path that ends at NEET-UG, the entrance exam for MBBS in India, plus a free learning website on top of it.

**Learning website:** https://saiqulmodi.github.io/NEET-Learning-Hub/

## What is inside

| Part | Questions |
|---|---|
| Class 1-5 (EVS science strands) | about 1,700 |
| Class 6-10 (Physics, Chemistry, Biology foundation) | about 4,500 |
| Class 11-12 NEET syllabus chapters | 19,459 (Physics 7,156, Chemistry 4,781, Biology 7,522) |
| Class 11-12 chapters removed from NEET (kept for school) | about 150 |
| **Total** | **25,765**, of which 2,352 are NEET formats (978 match-the-list, 992 multi-statement, 382 assertion-reason) and 10,629 are high-yield NEET topics |

* **High-yield NEET topics** (`hub/gen_hy_*.py` and the second batch `hub/gen_hy2_*.py`, source "NEET high-yield topics"): 10,629 original questions on the
  problem types and facts that NEET (and AIPMT before it) has asked again and again over the last 20 years, such as
  projectile, Atwood machine, Carnot, YDSE, photoelectric and decay numericals; Ksp, pH, colligative, Nernst-type and
  half-life calculations; named reactions; hybridisation; taxonomy, physiology values, genetics ratios and
  Hardy-Weinberg. They are **not** copies of past papers: the questions are written fresh on those topics, numerical
  answers are computed, and facts follow NCERT. Each batch is added after all earlier questions, so existing ids never change.

* **NEET question formats** (`hub/core.py`, `hub/gen_ar.py`): match List I with List II, "how many statements are
  correct" / "which statements are correct", and assertion-reason (curated pairs plus pairs built from checked
  statements). The `question_type` column says which format a question is (`mcq`, `match`, `multi`, `ar`).
* **Revision notes** (`hub/notes.py`, `notes_hi.py`, `notes_bn.py`): 6 key points for each of the 79 NEET chapters
  in English, Hindi and Bengali. Chapter and unit names are translated in `hub/titles_i18n.py`.

* **Syllabus map** (`hub/syllabus.py`): the 50 NMC NEET-UG units (20 Physics, 20 Chemistry, 10 Biology) linked to
  every NCERT Class 11-12 chapter (79 chapters, Biology split into Botany and Zoology as in the exam).
* **School MCQ Bank questions**: every science question from `School_MCQ_Bank` (read-only), mapped to its chapter.
* **New NEET-level questions** (`hub/gen_*.py`): NCERT-accurate fact tables, checked true/false statements and
  computed numericals (answers calculated, wrong options are typical mistakes). All questions are original.
* Every question has 4 distinct options, exactly one correct answer and an explanation.

## Learning website (`docs/`)

* **Path**: Class 1 -> 12 -> NEET ladder; every chapter with question count, your progress and accuracy.
* **Practice**: 10 questions at a time per chapter; unseen and previously missed questions come first; instant
  explanation after each answer.
* **Mock tests** in the NEET-UG pattern: Physics 45, Chemistry 45, Botany 45, Zoology 45 (180 questions,
  180 minutes, +4/-1), plus half and quick versions. OMR-style answer sheet, mark for review, timer, and the test is
  saved as you go. Results show section scores and a review of every wrong or blank question.
* **Weekly Mock Day**: one full-length paper per week (seeded by the ISO week, so everyone gets the same paper),
  a weekly streak, and a line chart of full-length mock scores over time.
* **Revise**: the revision notes for each chapter, then straight into practice; "NEET formats" practises only
  match, statement and assertion-reason questions; "high-yield" practises only the high-yield NEET-topic questions.
* **Languages**: the site is in English, Hindi and Bengali (picker in the top bar). Question texts stay in English.
* **Disclaimer and reporting**: "Answers are AI-generated. Please confirm them with your mentor or teacher." appears
  under every explanation, at the top of the Path page and in the footer. Every question has a "Report a problem"
  link that opens a prefilled GitHub issue with the question id.
* **My progress**: accuracy by subject, weakest chapters, the score chart and mock history. Saved in the browser.
* Chapters taught by the Ecos-Synthetica game link to it, and the game's quiz draws on this hub.

## Build

```
python build_hub.py          # writes output/neet_hub.db, output/neet_hub.csv and docs/data/*.json
python build_hub.py --dry    # counts and checks only
```

The build is deterministic and refuses to write if any question fails validation. Add content by adding
`table(...)`, `facts(...)` or `@gen(...)` generators for a chapter id in `hub/gen_*.py`.

## Database

`output/neet_hub.db` (SQLite) has two tables:

* `chapters(id, class_level, subject, branch, neet_unit, neet_unit_title, title, in_neet, ecos_link)`
* `questions(id, chapter_id, class_level, subject, difficulty, question, option_a..option_d, correct_option,
  correct_answer, explanation, source, bank_id)`

```sql
SELECT question, option_a, option_b, option_c, option_d, correct_option
FROM questions q JOIN chapters c ON c.id = q.chapter_id
WHERE c.in_neet = 1 AND q.subject = 'Biology' ORDER BY RANDOM() LIMIT 10;
```
