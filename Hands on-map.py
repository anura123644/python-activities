numbers1=[1,2,3]
numbers2=[4,5,6]
numbers3=[7,8,9]
result=map(lambda x,y,z:x+y+z,numbers1,numbers2,numbers3)
print("Addition of three lists")
print(list(result))
nums=[1,2,3,4,5,6,7,7,8,9]
def sq(n):
    return n*n
square = list(map(sq,nums))
print("Square of numbers in list")
print(square)
