if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().split()))
    arr=[1,-1,-2,-1]
    arr.sort()
    print([a for a in arr if a<max(arr)][-1])
    # print(arr)