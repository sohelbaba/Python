#Develop a menu-based python program
#menu items: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Average 6. Find maximum 7. Find minimum
import sys
def PrintMenu():
    print("Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Average")
    print("6. Find maximum")
    print("7. Find minimum")
    print("8.Exit")

def add(list1):
   return sum(list1)

def GetChoice():
    ch = int(input("Enter Choice : "));
    return ch

def sub(list1):
    subtraction=0;
    for i in list1:
        subtraction = int(i) - subtraction

    return subtraction

def mul(list1):
    mult=1
    for i in list1:
        mult = mult * int(i)
    
    return mult

def Div(list1):
    div=1
    div = list1[0]/list1[1]
    return div

def Avg(list1):
    s = sum(list1)
    l = len(list1)
    avg = s/l
    return avg

def Max(list1):
    return max(list1)

def Min(list1):
    return min(list1)

def Choice(ch):
    if ch == 1:
        print("Addition for Numeric List",add(list1))
    elif ch == 2:
        print("Subtraction for Numeric List",sub(list1))
    elif ch == 3:
        print("Multiplication for Numeric List",mul(list1))
    elif ch == 4:
        print("Division for Numeric List",Div(list1))
    elif ch == 5:
        print("Average for Numeric List",Avg(list1))
    elif ch == 6:
        print("Maximum for Numeric List",Max(list1))
    elif ch == 7:
        print("Minimum for Numeric List",Min(list1))
       
    

def repeate():
    while True:
        PrintMenu()
        ch=GetChoice()
        if ch == 8:
            return
        else:
            Choice(ch)



#Program Driver   
list1 = [10,5]
#PrintMenu()
repeate()


