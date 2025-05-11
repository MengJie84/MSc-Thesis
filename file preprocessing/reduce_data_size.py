import pandas as pd

# File paths
column_names_file = "../testing/columnLabels.csv"  # Replace with actual path
data_file = "../testing/1.1.csv"  # This file will be updated in place
columns_to_keep = ["subject", "trial", "condition", "sample", "Fz", "FCz", "Cz", "CPz", "Pz"]

def rewrite_file_with_column_name():
    # Read the column names file (assume it's a single row)
    column_names_df = pd.read_csv(column_names_file, header=None)
    column_names = column_names_df.iloc[0].tolist()  # Convert to list

    # Read the data file without headers
    data_df = pd.read_csv(data_file, header=None)

    # Convert column names to a DataFrame and append data
    column_names_row = pd.DataFrame([column_names])  # Convert list to DataFrame
    updated_df = pd.concat([column_names_row, data_df], ignore_index=True)  # Add names as first row

    # Overwrite the existing file
    updated_df.to_csv(data_file, index=False, header=False)

    print(f"File '{data_file}' has been updated with column names as the first row.")


def keep_relevent_features():
    df = pd.read_csv(data_file)

    # Keep only the relevant columns (ignore missing columns)
    df = df[[col for col in columns_to_keep if col in df.columns]]

    # Overwrite the existing file with filtered data
    df.to_csv(data_file, index=False)

    print(f"File '{data_file}' has been updated with only relevant columns.")

# rewrite_file_with_column_name()
# keep_relevent_features()

