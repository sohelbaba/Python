#Demonstrate creation and usage of Lambda functions

class Student:

    def input(self,rno,name,c_marks,cpp_marks,java_marks,python_marks):
        self.rno = rno
        self.name = name
        self.c_marks = c_marks
        self.cpp_marks = cpp_marks
        self.java_marks = java_marks
        self.python_marks = python_marks

    def show(self):
        print("Roll Number : ",self.rno)
        print("Name : ",self.name)
        print("C_Marks : ",self.c_marks)
        print("Cpp_Marks : ",self.cpp_marks)
        print("Java Marks : ",self.java_marks)
        print("Python Marks : ",self.python_marks)

    def tot(self):
        total = self.c_marks + self.cpp_marks+self.java_marks + self.python_marks
        return total

    def per(self):
        self.m_tot = self.tot()
        percentage =self.m_tot // 4
        return percentage

    def Grade(self):
        self.per = self.per()
        if self.per  > 75:
            return 'A'
        elif self.per > 60:
            return 'B'
        elif self.per > 50:
            return 'C'
        elif self.per > 33:
            return 'Pass'
        



#driver
s = Student()
s.input(1,"Sohel",88,84,96,86)
s.show()
print("Total = ",s.tot())
print("Percentage = ",float(s.per()))
print("Grade = ",s.Grade())

