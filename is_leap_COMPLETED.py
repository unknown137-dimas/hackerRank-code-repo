def is_leap(y):
    leap=False
    if y%4==0:
        if y%100==0:
            if y%400==0:
                leap=True
            else:
                leap=False
        else:
            leap=True
    return leap

y=int(input("year:"))
print(is_leap(y))