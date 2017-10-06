s1=str(input())
s2=str(input())
s3=''
x=0
y=0
if len(s1)==len(s2):
	for i in range(0,len(s1)+len(s2)):
		if (i+1)%2==0:
			s3+=s1[x]
			x+=1
		else:
			s3+=s2[y]
			y+=1
print(s3)
