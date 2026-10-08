# Student Performance Analytics System

## About the Project

This project is a Python-based Student Performance Analytics System.

It reads student marks and attendance from a CSV file and analyzes their performance using Python, NumPy, and Pandas.

## Technologies Used

- Python
- NumPy
- Pandas

## Features

- Calculate total and average marks
- Assign grades
- Check pass or fail status
- Calculate subject-wise averages
- Find highest and lowest performers
- Find top 3 students
- Calculate class average
- Analyze attendance

## Dataset

The project uses `students.csv` containing 20 student records.

The dataset includes:

- Student ID
- Name
- Department
- Python marks
- NumPy marks
- Pandas marks
- Attendance

## Grading

| Average | Grade |
|---|---|
| 90+ | A+ |
| 80-89 | A |
| 70-79 | B |
| 60-69 | C |
| 50-59 | D |
| 40-49 | E |
| Below 40 | F |

A student passes when all subject marks are at least 40 and attendance is at least 75%.

## Project Files

- `main.py` - Main Python program
- `students.csv` - Student dataset
- `README.md` - Project information
- `AKASH_WALIYA_Project_Documentation.md` - Project documentation

## How to Run

Install the required libraries:

```bash
pip install pandas numpy

## run the program using:

         python main.py