def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def main():
    print("Enter first number")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    ret = add(value1, value2)
    print("Addition is :", ret)

    ret = sub(value1, value2)
    print("Substraction is :", ret)


if __name__ == "__main__":
    main()