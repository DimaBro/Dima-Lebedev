import math
a1=int(input())
b1=int(input())
c1=int(input())
a2=int(input())
b2=int(input())
c2=int(input())
p1=(a1+b1+c1)/2
p2=(a2+b2+c2)/2
if math.sqrt(p1*(p1-a1)*(p1-b1)*(p1-c1)) > math.sqrt(p2*(p2-a2)*(p2-b2)*(p2-c2)):
    print('1>2')
else:
    print('2>1')
