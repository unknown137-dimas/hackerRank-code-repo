import re
def timeConversion(s):
    x=s.split(':')
    if re.search('AM',x[2]) and x[0]=='12':
        x[0]='00'
    elif re.search('PM',x[2]) and x[0]!='12':
        x[0]=str(int(x[0])+12)
    else:
        return s[:-2]
    return ':'.join(x)[:-2]

if __name__ == '__main__':
    # s = input()
    s='07:54:22PM'
    result = timeConversion(s)
    print(result)