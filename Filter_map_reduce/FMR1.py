#Accept N Numbers from users
#anfter  that filter out even number from that number
#and 2 to that every number
#

#input [1,3,4,6,5,4]
#after filter[2,4,6,4]
#after map[4,6,8,6]
#after reduce 24
def chkeven(no):
    if no%2==0:
        return True
    else:
        return False

def Filter(arr):
    brr=[]
    for i in range(len(arr)):
        if chkeven(arr[i]) ==True:
            brr.append(arr[i])
    return brr

def MarvellousMap(arr):
    for i in range(len(arr)):
        arr[i]=arr[i]+2
    return arr

def MarvellousReduce(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    return sum

def main():
    arr=[]
    print("enter number of elements")
    size=int(input())

    for i in range(size):
        print("enter the element:",i+1)
        no=int(input())
        arr.append(no)
    print("your enter elements are",arr)

    newdata=Filter(arr)
    print("after filtering data:",newdata)

    newdata1=MarvellousMap(newdata)
    print("after mapping the data",newdata1)

    newdata2=MarvellousReduce(newdata1)
    print("after reduce result is",newdata2)

if __name__=="__main__":
    main()
