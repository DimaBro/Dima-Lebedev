import math
n=int(input())        
i=1
for i in range(1, n):
 	while n%2==0:
 		print(2,);
 		n=n//2
i=3			
while i<=n:
 	if n%i==0:
 		print(i,)
 		n=n//i
 	else:
 		i=i+2
