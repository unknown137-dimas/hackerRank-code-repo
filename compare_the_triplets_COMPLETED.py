def compare(a,b):
    res=[0,0]
    for i in range(len(a)):
        if a[i]>b[i]:
            res[0]+=1
        elif a[i]<b[i]:
            res[1]+=1
    return res
a=list(map(int,input().split()))
b=list(map(int,input().split()))

print(' '.join(map(str,compare(a,b))))

