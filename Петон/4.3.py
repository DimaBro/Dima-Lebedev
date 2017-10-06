def invert (s,s1,s2):
	s=s[s1:s2]
	y= ""
	x=len(s)
	while x>0:
		y=y+s[x-1]
		x=x-1
	return y;
q=input();
q=q+" ";
i = 0;
w= -1;
e= "";
while i < len(q):
	if (q[i]!=' ' and w<0):
		w=i
	if (q[i]==' ' and w>= 0):
		e=e+ invert(q,w,i) + " "
		w=-1
	i=i+1
print(e);
