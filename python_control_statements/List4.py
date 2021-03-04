def Addition(LIST):
    sum=0;
    for i in range(len(LIST)):
        sum=sum+LIST[i]
    return sum

def main():
    Arr=[]    # empty list
    print("enter the number of elements")
    size=int(input())

    print("enter the number")
    for i in range(size):
        print("entered element no:",i+1,"index:",i)
        value=int(input())
        Arr.append(value)
    print("Accepted data is ",Arr)
    ret=Addition(Arr)
    print("Addition of all elements is",ret)

if __name__=="__main__":
    main()