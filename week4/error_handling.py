# Step 1: Ask the user for a filename
filename = input("Enter the filename you want to read: ")

try:
    # Step 2: Try to open and read the file
    with open(filename, "r") as source_file:
        content = source_file.read()

    # Step 3: Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Step 4: Show the result or write to a new file
    print("\nModified content:\n")
    print(modified_content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")