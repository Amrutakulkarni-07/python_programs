def oddeven(num):
    if num %2==0:
        return True
    else:
        return False

def main():
    no=int(input("enter the number"))
    ret=oddeven(no)
    if ret == True:
        print("{} is even number".format(no))
    else:
        print("{} is odd number".format(no))

if __name__=="__main__":
    main()
