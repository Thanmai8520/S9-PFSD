class ClassA():
    def fn1(self):
        print("This is first class")

class ClassB():
    def fn2(self):
        print("this is second class")
class ClassC():
    def fn3(self):
        print("this is third class")
class Derived(ClassA,ClassB,ClassC):
    def fn4(self):
        print("This is derived class")

ob=Derived()
ob.fn1()
ob.fn2()
ob.fn3()
ob.fn4()