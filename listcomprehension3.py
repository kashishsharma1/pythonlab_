l1=[1,3,4,2]
l2=[1,4,9,5]
l=[a for a in l1 if a not in l2]
n=[a for a in l2 if a not in l1]
print(l+n)
