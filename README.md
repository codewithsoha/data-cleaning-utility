# Data Cleaning Utility 🧹

## 📌 About
A Python utility that automatically cleans messy datasets using Pandas.

## ✅ What it does
- Detects and fills missing values using median/mean imputation
- Removes duplicate records
- Fixes incorrect data types and parses dates
- Standardizes column names and text formatting
- Generates a cleaning log of all changes made

## 📊 Dataset Used
IBM HR Analytics Attrition Dataset — 1,470 rows, 35 columns

## 🛠️ Tools & Libraries
- Python
- Pandas
- NumPy

## ▶️ How to Run
pip install pandas numpy
python cleaner.py

## 📂 Output
- data/cleaned_data.csv — the cleaned dataset
- cleaning_log.txt — summary of all cleaning operations
