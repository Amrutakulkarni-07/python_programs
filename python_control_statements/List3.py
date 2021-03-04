
def Display(LIST):
    icnt=0
    sum=0
    for icnt in range(len(LIST)):
        sum=sum+LIST[icnt]
    return sum

def main():
    Arr=[10,20,30,40]
    ret=Display(Arr)
    print("sum of list elements:",ret)

if __name__=="__main__":
    main()