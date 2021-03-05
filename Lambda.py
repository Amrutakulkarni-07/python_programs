#name=Lambda parameters:body

def Addition(no1,no2):
    return no1+no2

sum=lambda no1,no2:no1+no2

def fun(name):
    ret=name(10,20)
    print("the value from fun is",ret)

def main():

    value1=int(input("enter first number"))
    value2=int(input("enter second number"))

    ret=Addition(value1,value2)
    print("addition is",ret)

    ret=sum(value1,value2)
    print("Addition with lambda is ",ret)
    #fun(sum)
    #fun(Addition)

if __name__=="__main__":
    main()



#lambda function body should be in one line
#