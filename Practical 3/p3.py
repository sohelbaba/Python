#prog 3

def PrintMenu():
    print("STACK Operation")
    print("1.PSUH");
    print("2.POP");
    print("3.PEEP")
    print("4.REVERSE")
    print("5.EXIT")


def getChoice():
    ch = int(input("Enter Choice"))
    return ch

def Push(list1,value):
    return list1.append(value)

def pop(list1):
    return list1.pop()

def peep(list1):
    l=len(list)
    return list1[l-1]

def Rev(list1):
    return list1[::-1]

def Options(ch):
    if ch == 1:
        e = int(input("Enter Element for Push"))
        Push(list1,e)
        print("Element Push",e)
    elif ch == 2:
        x = pop(list1)
        print("Pop : ",x)
    elif ch == 3:
        print("Peep : ",peep())
    elif ch == 4:
        print("Reverse : ",list1)
        
        
def repeat():
    while True:
        PrintMenu()
        ch = getChoice()
        if ch == 6:
            return
        else:
            Options(ch)
        

#Driver
list1 =[]
repeat()
