import random
import os  # Import os to check if the file exists

# Load the guest list from the file 'guest_list.txt' in the 'Txt' folder
def load_guest_list():
    file_path = r'C:\Users\lucas\iCloudDrive\Desktop\Folders\Coding\CumpleLatino\Txt\guest_list.txt'
    print(f"Looking for file at: {file_path}")  # Print the file path
    if os.path.exists(file_path):  # Check if the file exists
        with open(file_path, 'r') as f:
            content = f.read()
            print(f"File content:\n{content}")  # Print the content of the file
            return content.splitlines()  # Split by lines
    else:
        print("File does not exist.")
        return []

# Example usage
guest_list = load_guest_list()
print(guest_list)
