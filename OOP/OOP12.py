class student:
    school = "abhinav"   # class variable

    def __init__(self,no1,no2,no3):  # constructor
        self.i = no1
        self.j = no2
        self.k = no3

    def Instance_total(self):    # instance method
        print("inside instance method ")
        return self.i +self.j+ self.k

    @classmethod   #decorator

    def Class_displayschool(cls):          #class method
        print("school name is ", cls.school)

    @staticmethod

    def Static_info():   #static method
        print("this method contains info school")

def main():
    student.Class_displayschool()     # calling class method
    obj1=student(10,20,30)                 # object creation
    obj2=student(40,50,60)
    ret=obj1.Instance_total()          # calling instance method
    print("instant total of obj1 is ",ret)

    student.Static_info()                  # calling static method using class name

if __name__ == "__main__":
    main()



