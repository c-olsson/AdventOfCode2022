
fo = open("14/input.txt", "r")
input = []

occupied = {}
maxY = 0
minX,maxX = 1e99,0
for line in fo.readlines():
    dots = line.strip().split(" -> ")
    for i in range(len(dots)-1):
        x1,y1 = list(map(int,dots[i].split(",")))
        x2,y2 = list(map(int,dots[i+1].split(",")))
        dx = x2-x1
        dy = y2-y1
        if dx != 0 and dy == 0:
            for x in range(min(x1,x2), max(x1,x2)+1):
                occupied[(x,y1)] = "#"
        if dx == 0 and dy != 0:
            for y in range(min(y1,y2), max(y1,y2)+1):
                occupied[(x1,y)] = "#"
        maxY = max(maxY,y1,y2)
        minX = min(minX,x1,x2)
        maxX = max(maxX,x1,x2)

DIR = [(0,1), (-1,1), (1,1)]
def moveDown(dot, isPart2):
    if dot[1] == maxY and not isPart2:
        print("Max depth reached")
        return 2
    # TODO Add ENUM: 0 toAdd, 1 added, 2 maxReached
    added_dot = 0
    for d in DIR:
        xn,yn = (dot[0]+d[0]), (dot[1]+d[1])
        if (xn,yn) not in occupied and added_dot == 0:
            added_dot = moveDown((xn,yn), isPart2)
            if added_dot != 0:
                return added_dot
    if added_dot == 0:
        if isPart2:
            occupied[dot] = 'o'
        elif dot[1] < maxY:
            occupied[dot] = 'o'
        return 1

def printGridPart1():
    # print some observability of grid
    print("...............+............")
    for yi in range(1,12):
        line = ""
        for xi in range(485,513):
            if (xi,yi) not in occupied:
                line += "."
            else:
                line += occupied[(xi,yi)]
        print(line)
def printGridPart2():
    # print some observability of grid
    print("..........................................+.......................................")
    for yi in range(1,maxY+4):
        line = ""
        for xi in range(458,540):
            if (xi,yi) not in occupied:
                line += "."
            else:
                line += occupied[(xi,yi)]
        print(line)

def part1():
    start = (500,0)
    # add drops until no new is added
    p1 = 0
    #for i in range(28):
    #    moveDown(start)
    while moveDown(start, False) != 2:
        p1 += 1
        #print("Added:", p1)
        #printGridPart1()
        
    print(p1)

def part2():
    # add "infinite" floor, needs to be wider than maximum base, so like max diagonal from start
    infinite_securer = maxY + (maxX-minX)//2
    for xi in range(minX-infinite_securer,maxX+infinite_securer):
        occupied[(xi,maxY+2)] = "#"
    
    # add drops until filled up all from floor to start
    start = (500,0)
    while start not in occupied:
    #for i in range(50):
        res = moveDown(start, True)
        #printGridPart1()
        assert(res != 2)
        
    # count 'o' in occupied
    p2 = 0
    for dot_char in occupied.values():
        if dot_char == 'o':
            p2 += 1
    printGridPart2()
    print(p2)

# 828
part1()
# 25500
part2()