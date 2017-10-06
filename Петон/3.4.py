import math
x=int(input())
y=int(input())
i=0;
if (x==0) and (y==0):
  print('Input error')
else:
  while x!=y:
    if x>y:
      while x>y:     
        x=x-y
    else:
      while y>x:
        y=y-x
print(y)
