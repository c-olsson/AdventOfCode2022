
fo = open("8/input.txt", "r")
grid = []

for line in fo.readlines():
    line = line.strip()
    l = []
    for t in line:
        l.append(int(t))
    grid.append(l)

def visibleLeft(x,y):
    for xi in range(x):
        if grid[y][xi] >= grid[y][x]:
            return 0
    #print("vis left", xi, x, y, grid[y][xi], grid[y][x])
    return 1

def visibleRight(x,y):
    for xi in range(x+1,len(grid[0])):
        if grid[y][xi] >= grid[y][x]:
            return 0
    #print("vis right", xi, x, y, grid[y][xi], grid[y][x])
    return 1

def visibleUp(x,y):
    for yi in range(y):
        if grid[yi][x] >= grid[y][x]:
            return 0
    #print("vis up", yi, x, y, grid[y][yi], grid[y][x])
    return 1

def visibleDown(x,y):
    for yi in range(y+1,len(grid)):
        if grid[yi][x] >= grid[y][x]:
            return 0
    #print("vis down", yi, x, y, grid[y][yi], grid[y][x])
    return 1

#ex, left 2 right 3 up 2 down 1

def part1():
    p1 = 2*len(grid)+2*len(grid[0])-4
    for x in range(1,len(grid[0])-1):
        for y in range(1,len(grid)-1):
            visible = 0
            visible = max(visibleLeft(x,y), visible)
            visible = max(visibleRight(x,y), visible)
            visible = max(visibleUp(x,y), visible)
            visible = max(visibleDown(x,y), visible)
            p1 += visible
    print(p1)


def seeLeft(x,y):
    step = -1
    while x+step > -1 and grid[y][x+step] < grid[y][x]:
        step -= 1
    if x+step == -1:
        step += 1
    return abs(step)

def seeRight(x,y):
    step = 1
    while x+step < len(grid[0]) and grid[y][x+step] < grid[y][x]:
        step += 1
    if x+step == len(grid[0]):
        step -= 1
    return step

def seeUp(x,y):
    step = -1
    while y+step > -1 and grid[y+step][x] < grid[y][x]:
        step -= 1
    if y+step == -1:
        step += 1
    return abs(step)

def seeDown(x,y):
    step = 1
    while y+step < len(grid) and grid[y+step][x] < grid[y][x]:
        step += 1
    if y+step == len(grid):
        step -= 1
    return step

def countScore(x,y):
    sl = seeLeft(x,y)
    sr = seeRight(x,y)
    su = seeUp(x,y)
    sd = seeDown(x,y)
    #print("scoring", sl,sr,su,sd)
    return sl*sr*su*sd

def part2():
    p2 = 0
    #print(countScore(1,2))
    # this assumes no edge tree would have best score... lucky it didnt
    # TODO add check of edge scores
    for x in range(1,len(grid[0])-1):
        for y in range(1,len(grid)-1):
            score = countScore(x,y)
            #print("score:", score, x, y)
            p2 = max(score, p2)
    print(p2)

# 1669
part1()
# 331344
part2()