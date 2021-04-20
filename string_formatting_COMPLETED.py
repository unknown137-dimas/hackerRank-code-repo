def print_formatted(number):
    # your code goes here
    w=len('{:b}'.format(number))+1
    for i in range(1,number+1):
        print(str(i).rjust(w-1)+oct(i)[2:].rjust(w)+hex(i)[2:].upper().rjust(w)+bin(i)[2:].rjust(w))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)