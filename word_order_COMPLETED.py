n=int(input())
d={}

for _ in range(n):
    x=input()
    if d.get(x):
        d.update({x:d.get(x)+1})
    else:
        d.update({x:1})
print(len(d.keys()))
for i in list(d.values()):
    print(i,end=' ')