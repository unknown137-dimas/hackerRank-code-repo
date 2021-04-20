if __name__ == "__main__":
    # n,m=map(int, input().split())
    n=11
    m=n*3
    # for i in range(n//2):
    #     print()
    
    # traditional way
    # for i in range(n//2):
    #     print(('---'*(n//2-i))+('.|.'*(1+(i*2)))+('---'*(n//2-i)))
    # print(('-'*((m-7)//2))+'WELCOME'+('-'*((m-7)//2)))
    # for i in reversed(range(n//2)):
    #     print(('---'*(n//2-i))+('.|.'*(1+(i*2)))+('---'*(n//2-i)))

    # 1 loop way
    for i in range(1,n+1):
        i=i-(n//2+1)
        if i<0: i=-i 
        if i==0:
            print(('-'*((m-7)//2))+'WELCOME'+('-'*((m-7)//2)))
        else:
            print(('---'*i)+('.|.'*(m//3-2*i))+('---'*i))