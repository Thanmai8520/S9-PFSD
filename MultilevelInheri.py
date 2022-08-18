class ClassA():
    def fn1(self):
        print("This is first class")

class ClassB(ClassA):
    def fn2(self):
        print("this is second class")
class ClassC(ClassB):
    def fn3(self):
        print("this is third class")
ob=ClassC()
ob.fn1()
ob.fn2()
ob.fn3()