# Kirundi Words

This is an open source project to gather all possible words in Kirundi.

Please open a PR and help us to add more words and correct the existing one.

The first draft of words has been added thanks to the Kirundi words gathered by Rowan Seymour in this [project](http://amajambo.ijuru.com/)

More words have added after integrated all words used in Kirundi Bible.


## Script: `clean.py`

**Features:**
- Loads and flattens word lists from CSV and TXT files.
- Merges multiple sources into a single list.
- Cleans each word: lowercases, removes unwanted characters, strips accents.
- Filters words by specified letter count (default: 8).
- Saves cleaned data to CSV.

**Input files:**
- `amajambo.csv` — base word list.
- `amajambo_8.txt` — additional words to merge.

**Output files:**
- `amajambo_cleanedV1.csv` — final cleaned and merged word list.
- `amajambo_8.csv` — processed additional list.

## How to Use

1. **Install dependencies:**
    ```bash
    pip install pandas
    ```
2. **Place your word lists in the `script/` directory.**
3. **Run the script:**
    ```bash
    python script/clean.py
    ```
4. **Find results in the output CSV files.**

## Customization

- Edit the `five_letter()` function or related code to change the desired word length.

## Author

Any-Arlene Niyubahwe

---

*This tool helps organize and clean Kirundi vocabulary for NLP and linguistics work.*
