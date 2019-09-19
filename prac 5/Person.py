class Person:
    def __init__(self,name='', bdate='', gender=''):
        self.name=name
        self.bdate= bdate
        self.gender = gender

    def set(self,name='',bdate='', gender=''):
        self.name=name
        self.bdate= bdate
        self.gender = gender

    def get(self):
        return self.name,self.bdate,self.gender

    def show(self):
        print("Name : ",self.name)
        print("Birth date : ",self.bdate)
        print("Gender : ",self.gender)
