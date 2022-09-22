"""Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
question link:-https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""
n,m= map(int,input().split())
for i in range(1,n,2):
    print(('.|.'*i).center(m+1, "-"))
print("WELCOME".center(m,'-'))
for j in range(1,n,2):
    print(('.|.'*j).center(m+1,'_'))
    