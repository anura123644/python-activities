# Open a file in write mode and add content
with open("example.txt", "w") as file:
    file.write("Hello, this is a new file!\n")

# Open the file in read mode and display content
with open("example.txt", "r") as file:
    content = file.read()
    print("File content after writing:\n", content)

# Open the file in append mode and add more data
with open("example.txt", "a") as file:
    file.write("Appending more data...\n")

# Open the file in read mode again
with open("example.txt", "r") as file:
    content = file.read()
    print("File content after appending:\n", content)

# Open the file in read/write mode and modify it
with open("example.txt", "r+") as file:
    content = file.read()
    file.seek(0)  # Move the cursor to the beginning
    file.write("Modified first line!\n")
    file.truncate()  # Remove any leftover data
    print("File content after modification:\n", content)

