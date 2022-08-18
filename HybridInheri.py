class Base():
    def fn1(self):
        print("This is first class")

class Derived1(Base):
    def fn2(self):
        print("this is second class")
class Derived2(Base):
    def fn3(self):
        print("this is third class")
class NewDerived(Derived1,Derived2):
    def fn4(self):
        print("this is final derived class")


ob=NewDerived()
ob.fn1()
ob.fn2()
ob.fn3()
ob.fn4()
