import pandas as pd
import os

# File paths
column_names_file = "columnLabels.csv.csv"  # Path to the column names file
data_folder = "./eeg2"  # Folder containing the CSV files

# Read the column names file (assume it's a single row)
column_names_df = pd.read_csv(column_names_file, header=None)
column_names = column_names_df.iloc[0].tolist()  # Convert to list

# Loop through all CSV files in the folder
for filename in os.listdir(data_folder):
    if filename.endswith(".csv") and filename != "column_names.csv":  # Skip column names file
        file_path = os.path.join(data_folder, filename)

        # Read the data file without headers
        data_df = pd.read_csv(file_path, header=None)

        # Convert column names to a DataFrame and append data
        column_names_row = pd.DataFrame([column_names])  # Convert list to DataFrame
        updated_df = pd.concat([column_names_row, data_df], ignore_index=True)  # Add names as first row

        # Overwrite the existing file
        updated_df.to_csv(file_path, index=False, header=False)

        print(f"Updated: {filename} ✅")

print("All CSV files in the folder have been updated successfully! 🎯")
