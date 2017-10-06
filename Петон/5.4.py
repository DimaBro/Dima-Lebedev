import random
pmin =1
n = int(input())
if n>10:
    print('Error')
else:
	a = []
	k = round(float(random.uniform(10,99)),2)
	for i in range(n): 
		a.append([])
		for j in range(n): 
			a[i].append(k)
			k = round(float(random.uniform(10,99)),2)
	for i in a:
		print(i)
	for i in range(n): 
		min=100
		for j in range(n):
			if a[j][i]<min:
				min=a[j][i]
		pmin=pmin*min
	print(round(pmin,2));
