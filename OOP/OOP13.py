
# single inheritance

class Base:
    def __init__(self):
        self.i=10
        self.j=20
        print("inside Base constructor")

    def fun(self):
        print("inside fun")

    def gun(self):
        print("inside gun")

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self.x=30
        self.y=40
        print("inside derived constructor")

    def sun(self):
        print("inside derived sun")

    def gun(self):                         # overriding
        print("inside derived gun")


def main():
    bobj=Base()
    print(bobj.i)
    print(bobj.j)
    bobj.fun()
    bobj.gun()

    dobj=Derived()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    dobj.fun()
    dobj.sun()
    dobj.gun()          # overriding

if __name__ == "__main__":
    main()

