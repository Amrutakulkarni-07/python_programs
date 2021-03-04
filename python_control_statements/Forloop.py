def displayF(value):     # for loop
    icnt=0
    for icnt in range(0,value):
        print("Jay Ganesh")
        icnt=icnt+1

def displayW(value):    # while loop
    icnt=0
    while icnt<value:
        print("jay Ganesh")
        icnt=icnt+1


def main():
    print("enter the number of iteration")
    no=int(input())
    print("output for loop")
    displayF(no)
    print("output for while")
    displayW(no)

if __name__=="__main__":
    main()
