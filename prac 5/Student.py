from Person import Person
class Student(Person):

    def __init__(self,name='', bdate='', gender='',py_marks ='',java_marks='',php_marks=''):
        super().__init__(name,bdate,gender)
        self.py_marks = py_marks
        self.java_marks = java_marks
        self.php_marks = php_marks

    def set(self,name='', bdate='', gender='',py_marks ='',java_marks='',php_marks=''):
        super().set(name,bdate,gender)
        self.py_marks = py_marks
        self.java_marks = java_marks
        self.php_marks = php_marks

    def get(self):
        return self.py_marks,self.java_marks,self.php_marks

    def cal_total(self):
        self.total = self.py_marks+self.java_marks+self.php_marks
        self.total
    
    def per(self):
        self.per = self.total / 3

    def grade(self):
        if self.per() > 75:
            self.g= 'A'
        elif self.per() > 60:
            self.g=  'B'
        elif self.per() > 45:
            self.g=  'C'
        elif self.per() > 33:
            self.g=  'Pass'
        elif self.per() < 33:
            self.g=  'Fail'

    def show(self):
        super().show()
        print("Python Marks : ",self.py_marks)
        print("Java Marks :",self.java_marks)
        print("Php Marks : ",self.php_marks)
        print("Total : ",self.total)
        print("Percentage %.3f" %self.per)
        print("Grade : ",self.g)

