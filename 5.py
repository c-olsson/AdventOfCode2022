
fo = open("5/input.txt", "r")
top, bottom = fo.read().split("\n\n")
l1, l2 = [], []

for line in top.split("\n"):
    #init
    if len(l1) == 0:
        for i in range((1+len(line))//4):
            l1.append(list())
            l2.append(list())
    #push items in correct stack, whitespaces provides correct bin
    b = False
    for i in range(1,len(line),4):
        #print(line[i])
        if line[i] == '1':
            b = True
            break
        if line[i] != ' ':
            #print("Index add",(i-1)//4,"of",len(l1))
            l1[(i-1)//4].append(line[i])
            l2[(i-1)//4].append(line[i])
    if b:
        break
for li in l1:
    li.reverse()
for li in l2:
    li.reverse()

for line in bottom.split("\n"):
    line = line.strip().split()
    m,f,t = int(line[1]),int(line[3]),int(line[5])
    
    for i in range(m):
        l1[t-1].append(l1[f-1].pop())
    
    for i in l2[f-1][-m:]:
        l2[t-1].append(i)
    for i in range(m):
        l2[f-1].pop()
    
res1 = ""
for i in l1:
    res1 += i[-1]
res2 = ""
for i in l2:
    res2 += i[-1]
    
# TDCHVHJTG 
print(res1)
# NGCMPJLHV
print(res2)