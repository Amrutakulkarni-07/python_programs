
class Base1:
    def __init__(self):
        print("inside base1 instructor")
    def fun(self):
        print("inside base 1 fun")

class Base2:
    def __init__(self):
        print("inside base 2 constructor")

    def fun(self):
        print("inside base 2 fun")

class Derived(Base2,Base1):
    def __init__(self):
        Base2.__init__(self)
        Base1.__init__(self)
        print("inside Derived constructor")

    def fun(self):
        print("inside derived fun")

def main():
    dobj=Derived()
    dobj.fun()

if __name__ == "__main__":
    main()

