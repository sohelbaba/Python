#Develop a menu-based python program (menu items: 8. Calculate mean 9. Calculate Median 10. Calculate Mode) for a numeric tuple.

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
    print("8. Calculate mean")
    print("9. Calculate Median")
    print("10.Calculate Mode")
    print("11.Exit")

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

def Mean(list1):
    mean = 0;
    mean = sum(list1)/len(list1)
    return mean

def Median(list1):
    list1.sort()
    l = len(list1)
    if l%2 == 0:
        m = l/2
        return list1[m]
    else:
        m = (l+1)/2
        return lsit1[m]        

def Mode(list1):
    c= []
    for i in list1:
        c.append(list1.count(i))
        

    return list1[3]

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
    elif ch == 8:
        print("Mean for Numeric List",Mean(list1))
    elif ch == 9:
        print("Median for Numeric List",Median(list1))
    elif ch == 10:
        print("Mode for Numeric List",Mode(list1))
       
    

def repeate():
    while True:
        PrintMenu()
        ch=GetChoice()
        if ch == 11:
            return
        else:
            Choice(ch)



#Program Driver   
tup1 = (10,5,5,3,5)
list1 =list(tup1)
#PrintMenu()
repeate()


