#prog 5
l =[]

for i in range(1,100):
    if i%2 != 0:
        l.append(i)

od = []
for i in l:
    for j in range(2,i):
        if i%j == 0:
           break
    else:
        od.append(i)
            

print("List  : ",l)
print("List With Prime",od)
