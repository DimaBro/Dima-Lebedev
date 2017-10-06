import random
n=3
a=[]
min=1000
k=int(random.randint(10,99))
for i in range(n): 
	a.append([])
	for j in range(n): 
		a[i].append(k)
		k=int(random.randint(10,99))
for i in a:
	print(i)
for i in range(n): 
	sum=0
	for j in range(n):
		sum=sum+a[i][j]
	if min>sum:
		min=sum
print(min)
for i in range(n): 
	for j in range(n):
		a[i][j]=a[i][j]*min
print
for i in a:
	print(i)
