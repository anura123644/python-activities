#Using a try and except
try:
    number=int(input("Enter a number:"))
    print("The number entered is",number)
#Using value errr
except ValueError as ex:
    print ("Exception:",ex)
    3