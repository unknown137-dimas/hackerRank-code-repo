# example input
# x=[['Zack', -57], ['Berry', -57], ['Aiden', -5], ['Akriti', -50], ['Harsh', -50]]
s=[]
for _ in range(int(input())):
    name=input()
    score=float(input())
    s.append([score,name])
# s=[[i[1],i[0]] for i in x]
s.sort()
# print(s)
# magic happend here:)
tmp=[]
fin=0
for i in range(1,len(s)):
    if not fin:
        if s[i][0]>s[0][0]:
            tmp.append(s[i])
            for i in range(len(s)):
                if s[i][0]==tmp[0][0] and s[i][1]!=tmp[0][1]:
                    tmp.append(s[i])
            fin=1

# display result
for i in tmp:
    print(i[1])