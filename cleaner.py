import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Step 1 - Drop rows where ALL values are missing
    df.dropna(how='all', inplace=True)

    # Step 2 - Fix numeric columns
    numeric_cols = ['Age', 'DailyRate', 'DistanceFromHome', 'MonthlyIncome', 'MonthlyRate']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Step 3 - Fill missing numeric values with median
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())

    # Step 4 - Fill missing text values
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna('Unknown')

    # Step 5 - Remove duplicates
    df.drop_duplicates(inplace=True)

    # Step 6 - Standardize column names
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

    # Step 7 - Standardize text columns that exist
    text_columns = ['department', 'jobrole', 'businesstravel',
                    'educationfield', 'gender', 'maritalstatus', 'overtime']
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].str.strip().str.title()

    return df

def save_output(df, output_path, log_path):
    df.to_csv(output_path, index=False)
    with open(log_path, "w") as f:
        f.write("=== DATA CLEANING LOG ===\n\n")
        f.write(f"Final shape: {df.shape}\n")
        f.write("Operations performed:\n")
        f.write("  - Dropped fully empty rows\n")
        f.write("  - Numeric columns converted and filled with median\n")
        f.write("  - Text columns filled with 'Unknown'\n")
        f.write("  - Duplicates removed\n")
        f.write("  - Column names standardized to lowercase with underscores\n")
        f.write("  - Text columns title-cased and stripped\n\n")
        f.write("=== END OF LOG ===\n")
    print("✅ Done! Cleaned data and log saved.")

# Run
df = load_data("data/raw_data.csv")
df = clean_data(df)
save_output(df, "data/cleaned_data.csv", "cleaning_log.txt")