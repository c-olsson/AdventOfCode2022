
totPointsPart1 = 0
totPointsPart2 = 0
for line in open("4/input.txt", "r").readlines():
    l,r = line.strip().split(",")
    ll,lr = map(int, l.split("-"))
    rl,rr = map(int, r.split("-"))
    
    if ll <= rl and lr >= rr:
        totPointsPart1 += 1
    elif rl <= ll and rr >= lr:
        totPointsPart1 += 1
    
    if ll in range(rl,rr+1):
        totPointsPart2 += 1
    elif lr in range(rl,rr+1):
        totPointsPart2 += 1
    elif rl in range(ll,lr+1):
        totPointsPart2 += 1
    elif rr in range(ll,lr+1):
        totPointsPart2 += 1
    
# 477 and 830
print(totPointsPart1)
print(totPointsPart2)