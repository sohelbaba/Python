#inheritance
from Person import Person
from Student import Student
import datetime

class Employee(Person):

    def __init__(self,name='', bdate='', gender='',basic=''):
        super().__init__(name,bdate,gender)
        self.basic =basic
    

    def set(self,name='',  bdate='', gender='',basic=''):
         super().set(name,bdate,gender)
         self.basic = basic

    def cal_da(self):
       if self.gender == 'male':
           self.da = self.basic * 0.80
           return self.da
       else:
           self.da = self.basic * 0.70
           return self.da


    def cal_hra(self):
       if self.gender == 'male':
           self.hra = self.basic * 0.10
           return self.hra
       else:
           self.hra = self.basic * 0.15
           return self.hra

    def cal_total(self):
        self.tot = self.basic + self.cal_da() + self.cal_hra()
        return self.tot
    
           
    def show(self):
        super().show()
        print("Basic : ",self.basic)
        print("Monthly Salary : ",self.cal_total())

#-------------------main
e = Employee()
e.set('sohel',datetime.date(1998,4,10),'male',50000)
e.show()
today = datetime.datetime.today()
d3 = today.strftime("%y/%m/%d")
print(d3)
