
import re

fo = open("15/input.txt", "r")

S = []
B = []

for line in fo.readlines():
    pattern = re.compile("x=(.*), y=(.*): .*x=(.*), y=(.*)")
    m = pattern.search(line)
    S.append([int(m.group(1)),int(m.group(2))])
    B.append([int(m.group(3)),int(m.group(4))])
#print(S)
#print(B)
    
P1_Y=2000000
#P1_Y=10
p1_reach = set()
b_to_substract = set()

def get_overreach(sx,sy,dist, y_level):
    overreach = -1
    if sy <= y_level <= sy+dist:    # Line "above"/lower value
        overreach = sy+dist-y_level
        #print("Hit1",sx,sy, "Extra:", overreach)
    elif sy-dist <= y_level <= sy:  # Line "below"/higher value
        overreach = abs(sy-dist-y_level)
        #print("Hit2",sx,sy, "Extra:", overreach)
    return overreach

def part1():
    # naive approach (bad part2?), check wanted line (P1_Y) and sensors overreaching that line in there search
    for i,s in enumerate(S):
        sx,sy = s[0],s[1]
        bx,by = B[i][0],B[i][1]
        if by == P1_Y:
            b_to_substract.add(bx)
        dist = abs(sx-bx)+abs(sy-by)
        #print(sx,sy,bx,by)
        overreach = get_overreach(sx,sy,dist,P1_Y)
        assert(overreach>-2)
        if overreach >= 0:
            for xi in range(sx-overreach,sx+overreach+1):
                p1_reach.add(xi)
        else:
            print("No hit")
    #print(p1_reach)
    print(len(p1_reach)-len(b_to_substract))
    print(max(p1_reach),min(p1_reach))



P2_Y_MIN = 0
#P2_Y_MAX = 20
P2_Y_MAX = 4000000
def part2():
    s_dist = []
    for i,s in enumerate(S):
        sx,sy = s[0],s[1]
        bx,by = B[i][0],B[i][1]
        dist = abs(sx-bx)+abs(sy-by)
        s_dist.append(dist)
    print(s_dist)
    # Check dist to scanner, can't reach... then gold
    # Iterating all possible possition would take over 3 years...
    # Skip the known distance for that row, check next scanner untill boarder reach... next row
    yi = 0
    xi = 0
    while yi <= P2_Y_MAX:
        if yi % 100000 == 0:
            print("yi=",yi)
        while xi <= P2_Y_MAX:
            #print("xi=",xi)
            no_hit = True
            for i,s in enumerate(S):
                sx,sy = s[0],s[1]
                dist_current = abs(sx-xi)+abs(sy-yi)
                if dist_current <= s_dist[i]:
                    no_hit = False
                    # Skip to next unknown xi and recheck all scanners
                    overreach = get_overreach(sx,sy,s_dist[i],yi)
                    assert(overreach>-1)
                    xi = sx+overreach+1
                    break
            if no_hit:
                print("No reach", xi,yi, xi*4000000+yi)
                return
        # try out next row... TODO find out how to jump more rows
        yi += 1
        xi = 0
    
# 5176944, ~1 second
part1()
# 13350458933732 (x=3337614, y=2933732), ~60 seconds
#part2()