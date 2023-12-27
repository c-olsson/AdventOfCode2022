
fo = open("9/input.txt", "r")

input = []
for line in fo.readlines():
    input.append(line)

def move(h,t):
    if abs(h[0]-t[0]) > 1 or abs(h[1]-t[1]) > 1:
        dx,dy = 0,0
        if h[0] > t[0]:
            dx = 1
        elif h[0] < t[0]:
            dx = -1
        if h[1] > t[1]:
            dy = 1
        elif h[1] < t[1]:
            dy = -1
        return [t[0]+dx,t[1]+dy]
    else:
        return t

def part1():
    visited = set()
    h, t = [0,0],[0,0]
    for l in input:
        d,v = l.split()
        v = int(v)
        for s in range(v):
            if d == 'U':
                h[1] += 1
            elif d == 'D':
                h[1] -= 1
            elif d == 'R':
                h[0] += 1
            elif d == 'L':
                h[0] -= 1
            t = move(h,t)
            tup = (t[0],t[1])
            visited.add(tup)
    print(len(visited))

def part2():
    visited = set()
    h = [0,0]
    rope = [h]
    for i in range(9):
        rope.append([0,0])
    for l in input:
        d,v = l.split()
        v = int(v)
        for s in range(v):
            if d == 'U':
                h[1] += 1
            elif d == 'D':
                h[1] -= 1
            elif d == 'R':
                h[0] += 1
            elif d == 'L':
                h[0] -= 1
            for i in range(1,len(rope)):
                rope[i] = move(rope[i-1],rope[i])
            tup = (rope[-1][0],rope[-1][1])
            visited.add(tup)
    print(rope)
    print(len(visited))

# 6023
part1()
# 2533
part2()