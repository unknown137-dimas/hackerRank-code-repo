import re
def minionGame(s):
    a=0
    b=0
    n=len(s)
    for i in range(n,0,-1):
        for j in range(i):
            if re.findall(r'^[A,I,U,E,O]',s[j:i]):
                a+=1
            else:
                b+=1
    if a==b:
        print('Draw')
    elif a>b:
        print('Kevin',a)
    else:
        print('Stuart',b)
if __name__ == "__main__":
    # s=input()
    s='banana'.upper()
    minionGame(s)