# NEET Data Hub and NEET Learning Hub

A question-and-answer data hub for Biology, Chemistry and Physics from Class 1 to Class 12, organised
as a path that ends at NEET-UG, the entrance exam for MBBS in India, plus a free learning website on top of it.

**Learning website:** https://saiqulmodi.github.io/NEET-Learning-Hub/

## What is inside

| Part | Questions |
|---|---|
| Class 1-5 (EVS science strands) | about 1,700 |
| Class 6-10 (Physics, Chemistry, Biology foundation) | about 4,500 |
| Class 11-12 NEET syllabus chapters | about 6,500 (Physics 2,200, Chemistry 1,650, Biology 2,600) |
| Class 11-12 chapters removed from NEET (kept for school) | about 150 |

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
* **My progress**: accuracy by subject, weakest chapters, mock history. Saved in the browser.
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
