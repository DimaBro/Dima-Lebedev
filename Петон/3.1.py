import math
a=float(input())
n=1
s=0
if a>1:
	while s<=a:
		s=s+1/n
		n= n+1
	print(n-1,round(s,2));
else:
	print('a<1')
