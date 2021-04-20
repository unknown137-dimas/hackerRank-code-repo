t=int(input())
res=[]
for i in range(t):
    na=int(input())
    a=set(input())
    nb=int(input())
    b=set(input())
    res.append(a.issubset(b))

for r in res:
    print(r)
import random

random.