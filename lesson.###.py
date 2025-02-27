# Function to print a mirrored right-angled triangle pattern
def print_mirrored_triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + ' *'* i)

# Number of rows for the triangle
rows = int(input("Enter the number of rows: "))
print_mirrored_triangle(rows)
