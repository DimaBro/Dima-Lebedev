import math
k=int(input())
p1=1
s1=0							
for j in range(-1,k):
	if j!=0 and j!=4 and j-j**2!=0:
		p1=(((j-j**2)*k)/(j-4))*p1
		for i in range(j,k+2):
			if i!=0 and i!=5 and i!=7:
				s1=(((abs(i-5))**1/3)/abs(i-7))+s1
				P=p1*s1 		
print(round(P,2))

