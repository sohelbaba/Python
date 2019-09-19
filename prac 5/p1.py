#String class

class String:

    def __init__(self):
        print("Default constructor")

    def set(self,str1=""):
        self.str1 = str1

    def get(self):
        return self.str1

    def length(self):
        return len(self.str1)

    def join(self,str2):
        self.str1 = self.str1 + ' ' + str2
        return  self.str1

    def compare(self,str2):
        return self.str1 == str2

    def reverse(self):
        return self.str1[::-1]

    def palimdrom(self):
        x = self.str1[::-1]
        if self.str1 == x:
            return True
        return False

    def word(self,str2):
        if self.str1 in str2:
            return True
        return False
    


#main--------------------------------------------------
s = String()
s.set("Hello")
print("String  : " ,s.get())
print("Length : ",s.length())
print("Join Two word : ",s.join('Mulla'))
print("After join : ",s.get())
print("Compare two string: ",s.compare("sohel"))
print("reverse : ",s.reverse())
print("Palindrome : ",s.palimdrom())
print("Check Word in String : ",s.word("Hi good morning Hello"))

