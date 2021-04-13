#multiple inheritance 

class Base1:
    def __init__(self):
        self.i=10
        self.j=20
        print("inside base1 constructor")

class Base2:
    def __init__(self):
        self.x=11
        self.y=21
        print("inside base2 constructor")

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        self.a=20
        self.b=30
        print("inside Derived constructor")

def main():
    dobj=Derived()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    print(dobj.a)
    print(dobj.b)

if __name__=="__main__":
    main()


