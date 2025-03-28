from abc import ABC, Abstractmethod
class absclass (ABC):
    def print(self,x):
        print("Passed value:",x)
    @Abstractmethod
    def task(self):
        print("We are inside Absclass task")
    class test_class(Absclass):
        def task(self):
            print("We are inside test_class task")
    test_obj= test_class()
    test_obj.task()
    test_obj.print(100)       