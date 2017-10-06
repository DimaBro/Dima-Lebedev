from random import random
a=[]
for i in range(16):
	a.append(round(float(random()*10),2))
print(a)
print(a.index(min(a)),min(a))
print(a.index(max(a)),max(a))
