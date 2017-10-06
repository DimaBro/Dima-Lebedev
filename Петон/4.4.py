s1=str(input())
s2=str(input())
for i in range (0,len(s1)):
	x=0
	for j in range (0,len(s2)): 
		if s1[i]==s2[j]: 
			x=1	
	if x==0:
		print(s1[i])
for i in range (0,len(s2)):
	x=0
	for j in range (0,len(s1)): 
		if s2[i]==s1[j]:
			x=1
	if x==0:
		print(s2[i])
