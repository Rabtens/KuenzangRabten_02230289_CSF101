# Kuenzang Rabten — CSF101 Assignment 1

**Author:** Kuenzang Rabten (02230289)

**Course:** CSF101 — Programming Methodology

This repository contains two Python programs for Assignment 1: a set of small utility functions (Part A) and two simple interactive games (Part B). The code targets Python 3 and uses only the standard library.

---

## Repository contents

- `KuenzangRabten_02230289_A1_PA.py` — Part A: functions and an interactive menu.
- `KuenzangRabten_02230289_A1_PB.py` — Part B: two simple games (guess-the-number, rock-paper-scissors).
- `README.md` 

---

## Requirements

- Python 3.6 or later
- No third-party packages required

---

## How to run

Run Part A (functions menu):

```bash
python3 KuenzangRabten_02230289_A1_PA.py
```

Run Part B (games menu):

```bash
python3 KuenzangRabten_02230289_A1_PB.py
```

Both programs present a text menu and are interactive. Follow the on-screen prompts.

---

## Part A — Functions 

The Part A program implements several small command-line utilities accessible from a menu:

1. Perfect number sum — find perfect numbers within a range and print their sum.
2. Weight unit converter — convert between kilograms and pounds.
3. Vowel counter — count vowels in a string (case-insensitive).
4. Average and range finder — compute average and range (max - min) for entered numbers.
5. String reverser + word count — reverse a string and report the word count (handles multiple spaces).
6. Specific-word counter — count occurrences of specific words (example words: `kuzu`, `laso`, `tashi`, `yangchen`) in a text source. The code shows how to read from a URL using `urllib.request`.

---

## Part B — Games 

1. Guess Number Game — the computer chooses a random integer (1–100); the user guesses until correct. The program gives hints and counts attempts.
2. Rock Paper Scissors — play rounds against the computer; the program keeps score and supports quitting.

Both games use the `random` module from the standard library.

---

## Notes

- Input validation and basic error handling are included in the programs. Non-numeric inputs where numbers are expected will be handled with prompts or error messages.
- To modify the specific-word counter to read from a local file instead of a URL, replace the `urllib.request` read with a standard file open/read.

---

## Repository



---

## Author

Kuenzang Rabten — Student number: 02230289

College of Science and Technology
Royal University of Bhutan

---

