def add(P,Q):
    return P+Q
def subtract (P,Q):
    return P-Q
def multiply (P,Q):
    return P*Q
def divide (P,Q):
    return P/Q
print ("please select the operater")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")
choice = input("please enter choice (a/b/c/d): ")
num_1 = int(input("please enter the first number"))
num_2= int(input("please enter the second number"))
if choice == 'a':
    print ( num_1 , '+',num_2 , '=', add(num1,num_2))
elif choice == 'b':
    print ( num_1 , '-',num_2 , '=', subtract(num1,num_2))
elif choice == 'c':
    print ( num_1 , '*',num_2 , '=', multiply(num1,num_2))
elif choice == 'd':
    print ( num_1 , '/',num_2 , '=', divide(num1,num_2))
else:
    print("this is a Invalid input")