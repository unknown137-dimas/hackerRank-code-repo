from string import ascii_lowercase
def print_rangoli(size):
    # your code goes here
    v=size*2-1
    h=v*2-1
    for i in range(1,v+1):
        i=i-(v//2+1)
        if i<0:
            i=-i
        r='-'.join(''.join(reversed(ascii_lowercase[i+1:size]))+ascii_lowercase[i:size])
        print(('-'*i*2)+r+('-'*i*2))

if __name__ == '__main__':
    # n = int(input())
    n=5
    print_rangoli(n)