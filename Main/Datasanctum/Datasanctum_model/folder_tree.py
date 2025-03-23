import os

def list_subfolders(folder_path):
    """List all subfolders in the given directory."""
    if not os.path.exists(folder_path):
        print("Error: The folder does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a directory.")
        return

    subfolders = [f.name for f in os.scandir(folder_path) if f.is_dir()]

    if subfolders:
        print("\nSubfolders in:", folder_path)
        for folder in subfolders:
            print(f"- {folder}")
    else:
        print("\nNo subfolders found in:", folder_path)

# Example usage
folder_path = input("Enter the folder path: ")
list_subfolders(folder_path)
