import string

fo = open("3/input.txt", "r")

input = []

def part1():
    for line in fo.readlines():
        line = line.strip()
        left, right = line[:int(len(line)/2)], line[int(len(line)/2):]
        
        unique = set()
        for l in left:
            if l in right:
                unique.add(l)
        #print(unique)
        for u in unique:
            prio = ord(u)-ord('a')+1
            if u in string.ascii_uppercase:
                prio = ord(u)-ord('a')+59
            print(u, prio)
            input.append(prio)
    print(sum(input))

input2 = []
def part2():
    group = []
    for line in fo.readlines():
        line = line.strip()
        group.append(line)
        if len(group) == 3:
            print(group)
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    prio = ord(c)-ord('a')+1
                    if c in string.ascii_uppercase:
                        prio = ord(c)-ord('a')+59
                    print(c, prio)
                    input2.append(prio)
                    break
            group = []
    print(sum(input2))
            
#part1()
part2()
