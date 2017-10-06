import math
s=int(input())
x=int(input())
i=1
q=0                           
for i in range (1,s):
	q=(x**i)*(math.sin(math.pi/4))+q
print(round(q,2))
