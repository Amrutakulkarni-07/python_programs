class Marvellous:
    value=11

    def __init__(self,no1,no2):
        self.i=no1
        self.j=no2
        print("inside construtor")

    def __del__(self):
        print("inside destructor")

    def fun(self):
        print("inside fun")
        print("value of j",self.j)


def main():
    obj1 = Marvellous(10,20)
    obj2 = Marvellous(40,50)
    print("value of i of obj1",obj1.i)
    print("value of i of obj2", obj2.i)

    obj1.fun()
    obj2.fun()

    del obj1
    del obj2

if __name__ == "__main__":
    main()

