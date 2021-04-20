def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:4]),sum(arr[1:]))
if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [7,69,2,221,8974]

    miniMaxSum(arr)