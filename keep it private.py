#class creation
class myclass:
    #private variable
    __PrivateVar = 27;
    #private method
    def __privMeth(self):
        print("I'm inside class myclass")
    #Function to print value of private website
    def hello(self):
        print("Private variable value:",myclass.__privateVar)
    #Object creation method call    
        foo = myclass()
        foo.hello()
        foo.__privMeth
        