#Accept N Numbers from users
#anfter  that filter out even number from that number
#and 2 to that every number

#input [1,3,4,6,5,4]
#after filter[2,4,6,4]
#after map[4,6,8,6]
#after reduce 24

import functools

def chkeven(no):
    if no%2==0:
        return True
    else:
        return False

def Increment(no):
    return no+2

def Add(no1,no2):
    return no1+no2

def main():
    arr=[]
    print("enter number of elements")
    size=int(input())

    for i in range(size):
        print("enter the element:",i+1)
        no=int(input())
        arr.append(no)
    print("your enter elements are",arr)

   # newdata=filter(function name,Data)
    newdata=list(filter(chkeven,arr))            #newdata=MarvellousFiler(arr)
    print("after filtering the data",newdata)
    newdata1=list(map(Increment,newdata))       #newdata1=MarvellousMap(newdata)
    print("After mapping data",newdata1)

    newdata2=functools.reduce(Add,newdata1)      #newdata2=MarvellousReduce(newdata1)
    print("after reducing the data",newdata2)

if __name__=="__main__":
    main()
