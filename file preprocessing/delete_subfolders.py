import os
import shutil

# Define the main folder
main_folder = "./eeg2"  # Update this with your actual path


for folder in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder)

    # Check if it's a directory
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".csv"):  # Move only CSV files
                old_path = os.path.join(folder_path, file)

                # Rename file to prevent conflicts (e.g., "1/1.csv" → "1_1.csv")
                new_filename = f"{folder}_{file}"
                new_path = os.path.join(main_folder, new_filename)

                # Move the CSV file to the main folder
                shutil.move(old_path, new_path)

        # Remove the now-empty folder
        os.rmdir(folder_path)

print("All CSV files moved to the main 'eeg' folder and renamed to avoid conflicts.")