#static
class Student:

    count = 0
    def __init__(self):
        Student.count = Student.count + 1
    
    def input(self,name,course):
        self.name = name;
        self.course = course;

    def show(self):
        print("Name : ",self.name)
        print("Course :",self.course)

    @classmethod
    def showclass(cls,s):
        print("Class Method called",s)
        
    def showcount():
        print("Total Studnet  : ",Student.count)


#-----------main
Student.showclass('hello')

s1 = Student()
s1.input('sohel','mca')
s1.show()

s2 = Student()
s2.input('Samir','Mca')
s2.show()
Student.showcount()
