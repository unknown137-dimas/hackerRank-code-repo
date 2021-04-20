def birthdayCakeCandles(ar):
    return ar.count(max(ar))
if __name__ == '__main__':
    # ar = list(map(int, input().rstrip().split()))
    ar=[3,2,1,3]
    result = birthdayCakeCandles(ar)
    print(result)
