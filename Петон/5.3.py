import random
a=[]
for i in range(9):
	a.append(int(random.uniform(10,99)))
print(a)
	c1=a[i]//10
	c2=a[i]%10
	a[i]=c1*8**1+c2*8**0
print(a)

