def count_substring(string, sub_string):
    c=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            c+=1
    return c
if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string='abcdcdc'
    sub_string='cdc'
    
    count = count_substring(string, sub_string)
    print(count)