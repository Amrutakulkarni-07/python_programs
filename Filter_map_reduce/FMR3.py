#Accept N Numbers from users
#anfter  that filter out even number from that number
#and 2 to that every number

#input [1,3,4,6,5,4]
#after filter[2,4,6,4]
#after map[4,6,8,6]
#after reduce 24

import functools
ChkEven=lambda no:(no%2==0)

Increment=lambda no:no+2

add=lambda no1,no2:no1+no2

def main():
    arr=[]
    print("enter the number of elements")
    size=int(input())

    for i in range(size):
        print("enter element number:",i+1)
        no=int(input())
        arr.append(no)

    print("your enter elements are",arr)

    #newdata=filter(function_name,data)
    newdata=list(filter(ChkEven,arr))
    print("after filtering the data",newdata)
    newdata1=list(map(Increment,newdata))
    print("after mapping data",newdata1)

    newdata2=functools.reduce(add,newdata1)
    print("after reducing the data",newdata2)

if __name__=="__main__":
    main()
