
fo = open("7/input2.txt", "r")

# TODO use full path as key in dic, original input has not unique folders
tree_value = {}
tree_children = {}
cds = []
children = []

#looks as if cmd in input are provided as depth first, lets be sure
#Important, however folder names are not unique, e.g. three/four 'cd jrzcqs, nzmddp, sfpqf' with different ls content
exited = set()

for line in fo.readlines():
    line = line.strip().split()
    if line[0] == "$":
        cmd = line[1]
        if cmd == "ls":
            children = []
        elif cmd == "cd":
            move_to = line[2]
            print("Moving", move_to)
            print(cds)
            print(exited)
            if move_to != "..":
                tree_value[move_to] = 0
                cds.append(move_to)
                # TODO, feels wrong, add children if there is any
                #if len(children) > 0 and cds[-2] not in tree_children:
                #    tree_children[cds[-2]] = children
            else:
                # going up one step, assume no later return
                # Do accumelate for parent dir, current_dir=cds[-1], recursively all those folders content should be calculated
                current_dir = cds[-1]
                if current_dir not in exited:
                    exited.add(current_dir)
                    tree_value[cds[-2]] += tree_value[current_dir]
                    cds.pop()
                else:
                    #Should only visit once in a deep search
                    assert(False)
    elif line[0] == "dir":
        d = line[1]
        children.append(d)
    else:
        size = int(line[0])
        tree_value[cds[-1]] += size
 
# pop last folders to exit and add theirs tot sums 
print("cds",cds)
while len(cds) > 1:
    tree_value[cds[-2]] += tree_value[cds[-1]]
    print("Added size", tree_value[cds[-1]])
    exited.add(cds[-1])
    cds.pop()
print("cds",cds)

print("CHECK proper navigation made (man add for root, happens once)",len(tree_value), len(exited)+1)
assert(len(tree_value) == len(exited)+1)
#print("CHECK trees match in size",len(tree_value), len(tree_children))
#assert(len(tree_value) == len(tree_children))

p1 = 0
for t in tree_value:
    if tree_value[t] <= 100000:
        p1 += tree_value[t]
        print(t,"has lower than 100k")
print(tree_value)

#max possible is 34 031 644 due to tot files sizes in input.txt
# 1141028
print(p1)

# p2
disk_space          = 70000000
needed_unused_space = 30000000
used_space = tree_value["/"]
unused_space = disk_space - used_space
min_to_remove = needed_unused_space - unused_space

rem_candidate = disk_space
for f in tree_value:
    if min_to_remove <= tree_value[f] < rem_candidate:
        rem_candidate = tree_value[f]

# 8278005
print(rem_candidate)