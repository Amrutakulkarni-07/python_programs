
def Display(LIST):
    icnt=0
    for icnt in range(len(LIST)):
        print(icnt)
        print(LIST[icnt])


def main():
    Arr=[10,20,30,40]
    Display(Arr)

if __name__=="__main__":
    main()