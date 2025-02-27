#Take input
print("Half Pyramid Pattern of Stars(*):")
n = int(input("enter the number of rows:"))
#outer loop to handle numbr of rows
for i in range(n):
    #inner loop to handle the columns
    for j in range(i+1):
     #display result  
     print("*",end="")
    print()