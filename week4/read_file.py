# Step 1: Open the original file and read its content
with open("original.txt", "r") as source_file:
    content = source_file.read()

# Step 2: Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Step 3: Write the modified content to a new file
with open("modified.txt", "w") as target_file:
    target_file.write(modified_content)

#print("✅ File has been read, modified, and saved successfully!")