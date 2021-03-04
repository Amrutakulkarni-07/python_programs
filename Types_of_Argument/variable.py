def fun(*value):
    print("the number of arguments",len(value))

def main():
    fun(10,20)
    fun()
    fun(10,"amruta","hii",400)

if __name__=="__main__":
    main()
