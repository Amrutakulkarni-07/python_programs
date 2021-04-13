
# multilevel inheritance

class Base:
    def __init__(self):
        self.i=10
        self.j=20
        print("inside base constructor")


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self.x=30
        self.y=40
        print("inside derived constructor")


class Derived1(Derived):
    def __init__(self):
        Derived.__init__(self)
        self.a=11
        self.b=21
        print("inside Derived1 constructor")

def main():
    dobj = Derived1()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    print(dobj.a)
    print(dobj.b)

if __name__ ==  "__main__":
    main()


