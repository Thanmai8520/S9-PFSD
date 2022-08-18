class Base():
    def fn1(self):
        print("This is first class")

class Derived1(Base):
    def fn2(self):
        print("this is second class")
class Derived2(Base):
    def fn3(self):
        print("this is third class")


ob1=Derived1()
ob1.fn1()
ob1.fn2()
ob2=Derived2()
ob2.fn1()
ob2.fn3()
