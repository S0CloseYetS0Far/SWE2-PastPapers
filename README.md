# CS392 Question Bank — Software Engineering 2

An interactive practice site built from the past papers in `../Exams`, with every question solved from the lecture decks in `../slides`.

## How to use

Open `index.html` in any browser. No installation or server is needed.

- Pick a chapter (or "All chapters mixed").
- One question per page: **Show solution**, **← Prev**, **Next →** and **⤨ Shuffle** (shuffles the questions after the one you're on).
- Each solution shows the answer, how it is solved, and a **From slides** note with the deck and slide number.
- After the last question you get your score and a **Review my mistakes** button.
- Keys: `←` `→` move, `1`–`4` pick an option, `Enter` shows the solution, `S` shuffles.

## Files

| File | Purpose |
|---|---|
| `index.html` | The website |
| `questions.js` | All questions, answers, explanations, slide references and sources (generated) |
| `img/` | Figures cropped from the exam papers |
| `source/` | The Python files that hold the question data; run `python build.py <website folder>` from `source/` to regenerate `questions.js` |
