t=(1,3,4,5,6,6,6)
p=[]
for i in t:
    if(t.count(i)>1 and i not in p):
        print(i)
        p.append(i)
print(p)        
