"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n  scores. Store them in a list and find the score of the runner-up."""
lis=list(map(int, input("").strip().split()))
lis=set(lis)
lis=list(lis)
lis.sort()
c=len(lis)
print(lis[c-2])
