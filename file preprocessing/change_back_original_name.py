import os

# Define the main folder containing all CSV files
main_folder = "./eeg2"  # Update with the actual path

# Loop through all files in the folder
for filename in os.listdir(main_folder):
    if filename.endswith(".csv") and "_" in filename:  # Only rename modified files
        original_name = filename.split("_", 1)[1]  # Remove the prefix before "_"
        old_path = os.path.join(main_folder, filename)
        new_path = os.path.join(main_folder, original_name)

        # Rename file to its original name
        os.rename(old_path, new_path)

print("All CSV files have been renamed back to their original names.")
