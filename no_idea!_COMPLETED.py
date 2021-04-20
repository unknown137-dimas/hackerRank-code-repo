n,m=map(int, input().split())
arr=list(map(int, input().split()))
a=set(map(int, input().split()))
b=set(map(int, input().split()))

print(len([ar for ar in arr if ar in a])-len([ar for ar in arr if ar in b]))