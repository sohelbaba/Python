#TUPLE LIST

tup = (1,23,(1,2,3,4),[1,23,5,],41,1)

print("Orignal",tup)
l = list(tup)

for i in range(len(l)):
    if type(l[i]) == 'list' or type(l[i]) == 'tuple':
        del(l[i])

print("List",l)
    
