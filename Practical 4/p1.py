#Develop a menu-based python program (menu items: 1. String length 2. Join strings 3. Compare strings 4. Reverse string
# 5. Check string is palindrome or not 6. Check word in sentence) by means of user defined functions

class String:
    
    def __init__(self,str1):
        self.str1 = str1

    def Option(self):
        print("Select Option")
        print("1. String length ")
        print("2. Join strings")
        print("3. Compare strings")
        print("4. Reverse string")
        print("5. Check string is palindrome or not")
        print("6. Check word in sentence")
        print("7. Exit")

    def Get_Choice(self):
        ch = int(input("Ente Choice : "))
        return ch
        

    def Length(self):
        return len(self.str1)

    def Join_Str(self,str2):
        return self.str1+" " +str2

    def Compare_str(self,str2):
        return self.str1 == str2

    def Reverese(self):
        return self.str1[::-1]

    def Palindrom(self):
        r = self.str1[::-1]
        return r
        
    def check(self,str2):
        return str2 in self.str1
        
    





#Main Program 
S = String("Hello")

while True:
    S.Option()
    ch = S.Get_Choice()
    if ch  == 1:
        l = S.Length()
        print("Lenght  = ",l)
    elif ch == 2:
        j = input("Enter Str to join")
        s =S.Join_Str(j)
        print("Join: ",s)
    elif ch == 3:
        c = input("Enter Str to compare")
        b = S.Compare_str(c)
        if(b == True):
            print("String is same")
        else:
            print("String are not same")
    elif ch == 4:
        r = S.Reverese()
        print("Reverse Str = ",r)

    elif ch == 5:
        p =S.Palindrom()
        if S.str1 == p:
            print("String is palindrom")
        else:
            print("String is not palindrom")

    elif ch == 6:
        f=input("Check word")
        c = S.check(f)
        if c == True:
            print("Word found")
        else :
            print("Word is not Found")

    elif ch == 7:
        break


        
     

