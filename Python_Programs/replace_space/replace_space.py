import os

def replace_spaces_with_underscores(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        old_file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(old_file_path):
            continue

        # Replace spaces with underscores
        new_filename = filename.replace(" ", "_")
        new_file_path = os.path.join(directory, new_filename)

        # Rename the file if needed
        if old_file_path != new_file_path:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: '{filename}' -> '{new_filename}'")
        else:
            print(f"No spaces found in: '{filename}'")

if __name__ == "__main__":
    target_directory = input("Enter the directory containing files to rename: ").strip() or os.getcwd()
    replace_spaces_with_underscores(target_directory)
