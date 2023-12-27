
from functools import cmp_to_key

fo = open("13/input.txt", "r")
input = []

pairs_text = fo.read().split("\n\n")
pairs_dict = {}

for i,p in enumerate(pairs_text):
    ll, lr = p.split("\n")
    ll = eval(ll)
    lr = eval(lr)
    pairs_dict[i] = [ll, lr]   
    
def comparePackets(l, r):
    for i in range(min(len(l), len(r))):
        if l == []:
            return 1
        if r == []:
            return -1
        
        #recursive to go deeper
        rec = -1
        if isinstance(l[i], list) and isinstance(r[i], list):
            rec = 1
            res = comparePackets(l[i], r[i])
            if res != 0:
                return res
        elif isinstance(l[i], int) and isinstance(r[i], list):
            rec = 1
            res = comparePackets([l[i]], r[i])
            if res != 0:
                return res
        elif isinstance(l[i], list) and isinstance(r[i], int):
            rec = 1
            res = comparePackets(l[i], [r[i]])
            if res != 0:
                return res
        
        if rec == -1:
            if l[i] < r[i]:
                return 1
            elif l[i] > r[i]:
                return -1
            else:
                continue
    
    # end of list handle out of numbers    
    if len(l) < len(r):
        return 1
    elif len(l) > len(r):
        return -1
    else:
        # whole list was the same, need to continue, assumes a later separation
        return 0
    

def part1():
    p1 = 0
    for i in range(len(pairs_dict)):
        left = pairs_dict[i][0]
        right = pairs_dict[i][1]
        #print(i+1)
        res = comparePackets(left, right)
        if res == 1:
            p1 += i+1
    print(p1)

def part2():
    list_to_sort = []
    for i in range(len(pairs_dict)):
        left = pairs_dict[i][0]
        right = pairs_dict[i][1]
        list_to_sort.append(left)
        list_to_sort.append(right)
    list_to_sort = sorted(list_to_sort, key=cmp_to_key(comparePackets))
    list_to_sort.reverse()
    
    get_dk1, get_dk2 = False, False
    dk1, dk2 = 0,0
    for i,p in enumerate(list_to_sort):
        #print(i,p)
        if comparePackets([[2]], p) == 1 and not get_dk1:
            get_dk1 = True
            dk1 = i+1
        if comparePackets([[6]], p) == 1 and not get_dk2:
            get_dk2 = True
            dk2 = i+2
    print(dk1*dk2)
            

# 5720
part1()
# 23504
part2()
