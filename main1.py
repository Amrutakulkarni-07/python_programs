import oddeven

def main():
    no=int(input("enter the number"))
    ret=oddeven.oddeven(no)
    if ret == True:
        print("{} is even number".format(no))
    else:
        print("{} is odd number".format(no))

if __name__=="__main__":
    main()