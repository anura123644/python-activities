# Open the file in read mode
with open("example.txt", "r") as file:
    # Read the entire content of the file
    full_content = file.read()
    print("Full Content:\n", full_content)

# Open the file again to read line by line
with open("example.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())  # Using strip() to remove newline characters

# Using readline() to read a single line
with open("example.txt", "r") as file:
    first_line = file.readline()
    print("\nFirst Line:\n", first_line)

# Using readlines() to get all lines as a list
with open("example.txt", "r") as file:
    all_lines = file.readlines()
    print("\nAll Lines as List:\n", all_lines)

