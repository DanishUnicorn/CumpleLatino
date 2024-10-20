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

# Check that it reads the file correctly
guest_list = load_guest_list()
print(guest_list)

# Create a list of two random groups
def create_two_random_groups(guest_list):
    random.shuffle(guest_list)  # Shuffle the guest list randomly
    mid_index = len(guest_list) // 2  # Find the halfway point
    grupo_navidad = guest_list[:mid_index]  # First half goes into grupo_navidad
    grupo_carnaval = guest_list[mid_index:]  # Second half goes into grupo_carnaval
    return grupo_navidad, grupo_carnaval

# Generate the groups
grupo_navidad, grupo_carnaval = create_two_random_groups(guest_list)

# Printing the groups
print(f"Grupo Navidad: {grupo_navidad}")
print(f"Grupo Carnaval: {grupo_carnaval}")

