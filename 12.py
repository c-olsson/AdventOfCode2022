
import heapq

fo = open("12/input.txt", "r")

grid = []
for line in fo.readlines():
    line = line.strip()
    grid.append(line)
    
'''
def moveUpwards(c, steps, visited):
    global globalMinSteps
    steps += 1
    for d in DIR:
        print(c,d)
        # in border range check
        if not (0 <= c[0]+d[0] < len(grid) and 0 <= c[1]+d[1] < len(grid[0])):
            print("Out of range")
            continue
        
        # possible move, try moving
        c_height = ord(grid[c[0]][c[1]]) if ord(grid[c[0]][c[1]]) != ord('S') else ord('a')
        n = (c[0]+d[0], c[1]+d[1])
        n_height = ord(grid[n[0]][n[1]])
        #print("In border, c and hn heights", c_height, n_height)
        # check finished
        if n_height == ord('E'):
            print("############ Reached target in", steps, "steps")
            print("Visited", visited)
            if steps < globalMinSteps:
                globalMinSteps = steps
            continue
        
        # only move same height or one higher
        if c_height == n_height or c_height+1 == n_height:
            
            # move there if we havent visited before
            if n not in visited:
                print("Moving to ", (c[0]+d[0], c[1]+d[1]), "from", c)
                visited.add(c)
                moveUpwards((c[0]+d[0], c[1]+d[1]), steps, visited)
        else:
            #print("Neighbour to high or low")
            pass
'''                

def getS():
    for ri in range(len(grid)):
        for ci in range(len(grid[0])):
            if grid[ri][ci] == 'S':
                return (ri, ci)
    assert False


DIR = [(0,1),(0,-1),(1,0),(-1,0)]
def getNeighbours(c):
    ret = []
    for d in DIR:
        # in border range check
        n = (c[0]+d[0], c[1]+d[1])
        if not (0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0])):
            continue
        # Check height
        c_height = ord(grid[c[0]][c[1]]) if ord(grid[c[0]][c[1]]) != ord('S') else ord('a')
        n_height = ord(grid[n[0]][n[1]]) if ord(grid[n[0]][n[1]]) != ord('E') else ord('z')
        # add if true tree neighbour ("most one heigher"... so can drop to death if wanted)
        if n_height <= c_height+1:
            ret.append(n)
    return ret


def part1():
    S = getS()
    queue = []
    heapq.heappush(queue, (0, S))
    costs = dict()
    costs[S] = 0
    
    while queue != []:
        c = heapq.heappop(queue)
        #print("visiting", c, grid[c[1][0]][c[1][1]])
        
        if grid[c[1][0]][c[1][1]] == 'E':
            print("########## Reached target in shortest path...")
            print("... cost", costs[c[1]])
            break 
        
        neighbours = getNeighbours(c[1])
        for n in neighbours:
            new_cost = costs[c[1]] + 1 #valid neighbours costs only 1, amount of steps wanted
            if n not in costs: #or new_cost < costs[n] # not possible atm to revisit with lower cost
                costs[n] = new_cost
                heapq.heappush(queue, (new_cost, n))
    
def getAs():
    all_a = []
    for ri in range(len(grid)):
        for ci in range(len(grid[0])):
            if grid[ri][ci] == 'a' or grid[ri][ci] == 'S':
                all_a.append((ri, ci))
    return all_a

def part2():
    all_a = getAs()
    minP2 = 1e99
    
    for a in all_a:
        S = a
        queue = []
        heapq.heappush(queue, (0, S))
        costs = dict()
        costs[S] = 0
        
        while queue != []:
            c = heapq.heappop(queue)
            
            if grid[c[1][0]][c[1][1]] == 'E':
                minP2 = min(minP2, costs[c[1]])
                break
            
            neighbours = getNeighbours(c[1])
            for n in neighbours:
                new_cost = costs[c[1]] + 1 
                if n not in costs:
                    costs[n] = new_cost
                    heapq.heappush(queue, (new_cost, n))
    print(minP2)

# 330
part1()
# 321
part2()