def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(len([i+a for i in apples if s<=i+a<=t]))
    print(len([j+b for j in oranges if s<=j+b<=t]))

if __name__ == '__main__':
    # st = input().split()

    # s = int(st[0])

    # t = int(st[1])

    # ab = input().split()

    # a = int(ab[0])

    # b = int(ab[1])

    # mn = input().split()

    # m = int(mn[0])

    # n = int(mn[1])

    # apples = list(map(int, input().rstrip().split()))

    # oranges = list(map(int, input().rstrip().split()))

    # countApplesAndOranges(s, t, a, b, apples, oranges)
    s,t=7,10
    a,b=4,12
    apples=[2,3,-4]
    oranges=[3,-2,-4]
    countApplesAndOranges(s, t, a, b, apples, oranges)