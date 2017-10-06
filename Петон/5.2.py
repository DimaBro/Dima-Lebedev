from random import random
a=[]
max=-1
for i in range(10):
	a.append(int(random()*10))
for i in range(10):
	if a[i]>0 and a[i]%2!=0:
		if a[i]>max:
			max=a[i]
			max1=i
print(a)
print(max1,max)
