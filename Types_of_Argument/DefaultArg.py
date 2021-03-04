def AreaCircle(radius,PI=3.14):
    print("the value of PI",PI)
    return radius*radius*PI

def main():
    ret1=AreaCircle(4)
    print("area of circle 1:",ret1)
    ret2=AreaCircle(5,3.3)
    print("area of circle 2",ret2)

if __name__=="__main__":
    main()
