#import Arithmetic         -----------first Way
#import  Arithmetic as AR  -----------second way

#from Arithmetic import  Addition,Substraction -------third way

from Arithmetic import *       #----fourth way

def main():
    print("__name__ from main is",__name__)
    print("Enter the first number")
    value1=int(input())
    print("enter second number")
    value2=int(input())

    #ret1=Arithmetic.Addition(value1,value2)   -----first way
    #ret2=Arithmetic.Substraction(value1,value2)

    #ret1 = AR.Addition(value1, value2)        ------second way
    #ret2=AR.Substraction(value1,value2)

    #ret1 = Addition(value1, value2)           -------third way
    #ret2=Substraction(value1,value2)

    ret1 = Addition(value1, value2)            #------fourth way
    ret2=Substraction(value1,value2)

    print("Addition is",ret1)
    print("Subtraction is",ret2)


#code starter
if __name__=="__main__":
    main()

