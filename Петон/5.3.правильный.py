import random
a = []
b=0
c=0
while c!=9:
    b=int(random.uniform(10,99))
    if (b//10<=7) and (b%10<=7):
        a.append(b)
        c=c+1
print(a)
for i in range(9):
    c1=a[i]//10
    c2=a[i]%10
    a[i]=c1*8**1+c2*8**0
print(a)

