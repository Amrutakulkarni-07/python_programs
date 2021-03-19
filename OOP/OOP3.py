# introduction to concept of class and object

class Arithematic:
    def __init__(self):      # special word self is like this keyword
        print("inside constructor")


def main():
    obj1 = Arithematic()  # Arithematic(obj)     -> __init__(obj)
    obj2 = Arithematic()


if __name__=="__main__":
    main()