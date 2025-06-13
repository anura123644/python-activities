# Open a file in write mode
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python makes file handling easy!")

# Open the same file in read mode
with open("example.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)

# Count the number of words in the file
words = content.split()
print("\nTotal number of words:", len(words))

