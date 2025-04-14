import json
import os

# Define the file path
json_file_path = r"D:\DST\material\Lable_n_meaning.json"

# Function to load existing data from the JSON file
def load_data():
    if os.path.exists(json_file_path):
        with open(json_file_path, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# Function to save data to the JSON file
def save_data(data):
    with open(json_file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Main program loop
def main():
    data = load_data()
    
    while True:
        print("\nOptions:")
        print("1. Add Label and Meaning")
        print("2. View Labels")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            label = input("Enter label (e.g., econ.EM): ").strip()
            meaning = input("Enter meaning: ").strip()
            
            if label and meaning:
                data[label] = meaning
                save_data(data)
                print("Label added successfully!")
            else:
                print("Label and meaning cannot be empty!")
        
        elif choice == "2":
            if data:
                print("\nSaved Labels:")
                for label, meaning in data.items():
                    print(f"{label}: {meaning}")
            else:
                print("No labels found!")
        
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
