"""In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive."""
def count_substring(string, sub_string):
    slis=list(string)
    ssub=sub_string
    O=len(ssub)
    n=0
    for i in range(0,len(slis)-O+1):
        k=slis[i:i+O]
        k=''.join(k)
        if (k==ssub):
            n+=1
    return n
            

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
