# DMV License Application System

This is a Python project I worked on to practice building a license application system. The program asks for applicant information, checks age eligibility, lets the user choose a license type, and saves the application summaries to a text file.

I used this project to practice functions, loops, dictionaries, input checks, and working with files in Python.

## What it does

- Collects a name, date of birth, address, and SSN
- Checks whether an applicant is at least 16 using a fixed date of October 2, 2025
- Lets the user choose a learner's permit, standard license, or commercial license
- Generates a random application ID
- Shows an application summary with the SSN partially hidden
- Saves application summaries to `dmv_applications.txt`

## What I used

Python, functions, while loops, dictionaries, conditional statements, string methods, the `random` module, and text file writing.

## Project dates

- **Original file:** `dmv_license_application.py`
- **Last modified locally:** October 3, 2025 (based on my saved file's timestamp)
- **Published to GitHub:** October 23, 2026



## How to run it

Download `dmv_license_application.py`, open a terminal in the same folder, and run:

```bash
python dmv_license_application.py
```

Use **made-up information only**. This is a learning project, not a real DMV application system. It does not verify real licensing requirements, and the date used to calculate age is fixed.

## Things I could improve

- Use the actual current date instead of a fixed date
- Validate real calendar dates, not just the basic date format
- Check the exact dash positions in SSNs
- Add separate age rules for different license types
- Avoid asking for SSNs at all in a practice project
- Make the saved application data more structured

I wanted to keep this project as part of my Python progress and document what I learned while working on it.
