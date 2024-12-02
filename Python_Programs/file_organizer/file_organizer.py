import os
import shutil

def organize_files(directory):
    # Define categories
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
        "Others": []  # Catch-all for files with unknown extensions
    }
    
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Create folders for categories if not already present
    for category in file_categories.keys():
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Move files based on their extensions
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, category, filename))
                moved = True
                break

        # If no match, move to 'Others'
        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", filename))
    
    print(f"Files in '{directory}' have been organized.")

if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ").strip()
    organize_files(target_directory)
