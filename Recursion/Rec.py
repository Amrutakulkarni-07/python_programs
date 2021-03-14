def DisplayI(no):
    for i in range(no):     #iteration
        print("hello")


def DisplayR(no):
    if no!=0:
        no=no-1
        print("hello")
        DisplayR(no)        #recursive call

def main():
        print("enter the number of iterations")
        no=int(input())
        print("calling iterative function")
        DisplayI(no)

        print("calling recursive function")
        DisplayR(no)

if __name__=="__main__":
        main()