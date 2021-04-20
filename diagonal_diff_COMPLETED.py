def diagonalDifference(arr):
    # Write your code here
    a=b=0
    for i in range(len(arr)):
        a+=arr[i][i]
        b+=arr[i][(len(arr)-1)-i]
    return abs(a-b)
if __name__ == '__main__':
    # n = int(input().strip())

    arr = [[11,2,4],[3,5,6],[10,8,-12]]

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))
    res=diagonalDifference(arr)
    print(res)