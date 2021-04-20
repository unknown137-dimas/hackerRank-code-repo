# correction
# import operator

# MOD = 1000000007

# # s = input()
# s='122929220340044059596607770004444946877429328334756'
# n = len(s)
# a = []
# p10 = 0
# for i in range(n, 0, -1):
#     p10=(p10*10+1)%MOD
#     a.append(p10*i%MOD)

def substrings(n):
    s=[]
    for i in range(1,len(n)+1):
        for j in range(len(n)+1-i):
            s.append((int(n[j:j+i])))
    print(len(n))
    return str(sum(s)%1000000007)
if __name__ == '__main__':
    # n = input()
    n='12341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234'
    result = substrings(n)
    print(result)
