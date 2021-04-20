import math

def plusMinus(arr):
    c=[0,0,0]
    c[2]=sum(i==0 for i in arr)
    c[0]=sum(i>0 for i in arr)
    c[1]=sum(i<0 for i in arr)
    for x in c:
        print('{:.6f}'.format(x/n))

if __name__ == "__main__":
    # n=int(input())

    # arr=list(map(int,input().rstrip().split()))
    arr=[5,0,-6,5,-5,-6]
    n=len(arr)
    plusMinus(arr)