# object orientation in python

class Arithematic:           # class definition
    value = 111               # class variable or static variable in c cpp

    def __init__(self, i, j):    # class constructor
        self.no1 = i               # class instance variable
        self.no2 = j               # class instance variable

    def add(self):                      # instance method
        return self.no1+self.no2

    def sub(self):                        # instance method
        return self.no1-self.no2


def main():

    print("value ", Arithematic.value)
    obj1 = Arithematic(11, 21)            # __init__(obj1,11,21)
    obj2 = Arithematic(100, 50)            # __init__(obj2,100,50)

    ret = obj1.add()          # ret=add(obj1)
    print("addition is:", ret)
    ret = obj1.sub()              # ret=sub(obj1)
    print("sub is", ret)

    ret = obj2.add()          # ret=add(obj2)
    print("addition is:", ret)
    ret = obj2.sub()              # ret=sub(obj2)
    print("sub is", ret)


if __name__ == "__main__":
    main()