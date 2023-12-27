
fo = open("11/input.txt", "r")
monkeys = fo.read().split("\n\n")

monkey_lists = {}
monkey_operation = {}
monkey_throw_count = []
for i,m in enumerate(monkeys):
    for line in m.split("\n"):
        if "Starting" in line:
            split1 = line.strip().split(": ")
            split2 = split1[1].split(", ")
            monkey_lists[i] = split2
            monkey_throw_count.append(0)
        elif "Operation" in line:
            split = line.strip().split()
            o = split[4:]
            monkey_operation[i] = o
        elif "Test" in line:
            split = line.strip().split()
            monkey_operation[i].append(int(split[-1]))
        elif "If true" in line:
            split = line.strip().split()
            monkey_operation[i].append(int(split[-1]))
        elif "If false" in line:
            split = line.strip().split()
            monkey_operation[i].append(int(split[-1]))


def monkey_throws(mi):
    for old in monkey_lists[mi]:
        # new operation
        if monkey_operation[mi][1] == 'old':
            rt = int(old)
        else:
            rt = int(monkey_operation[mi][1])
        if monkey_operation[mi][0] == '+':
            new = int(old) + rt
        else:
            new = int(old) * rt
        # divide
        new = new//3
        # throw to receiver
        if new % monkey_operation[mi][2] == 0:
            mi_receiver = monkey_operation[mi][3]
        else:
            mi_receiver = monkey_operation[mi][4]
        monkey_lists[mi_receiver].append(new)
        # update throw count
        monkey_throw_count[mi] += 1
    # No monkey throws to itself, empty own list
    monkey_lists[mi] = []

def part1():
    global monkey_throw_count
    for i in range(20):
        for m in range(len(monkey_lists)):
            monkey_throws(m)
    print(monkey_lists)
    monkey_throw_count.sort()
    monkey_business = monkey_throw_count[-1] * monkey_throw_count[-2]
    print(monkey_throw_count)
    print(monkey_business)

CGD = 1
for m in range(len(monkey_lists)):
    CGD *= monkey_operation[m][2]

def monkey_throws2(mi):
    for old in monkey_lists[mi]:
        # new operation
        if monkey_operation[mi][1] == 'old':
            rt = int(old)
        else:
            rt = int(monkey_operation[mi][1])
        if monkey_operation[mi][0] == '+':
            new = int(old) + rt
        else:
            new = int(old) * rt
        # no divide...
        # ...
        # throw to receiver
        if new % monkey_operation[mi][2] == 0:
            mi_receiver = monkey_operation[mi][3]
        else:
            mi_receiver = monkey_operation[mi][4]
        # reduce by the greatest common devider for all monkeys devisors
        new = new % CGD
        monkey_lists[mi_receiver].append(new)
        # update throw count
        monkey_throw_count[mi] += 1
    # No monkey throws to itself, empty own list
    monkey_lists[mi] = []

def part2():
    for i in range(10000):
        #print("Iteration", i)
        for m in range(len(monkey_lists)):
            monkey_throws2(m)
    print("Common greatest monkey divider", CGD)
    print(monkey_lists)
    print(monkey_throw_count)
    monkey_throw_count.sort()
    monkey_business = monkey_throw_count[-1] * monkey_throw_count[-2]
    print(monkey_business)

# 58056
#part1()
# 15048718170, part 2 depends on correct initialization. TODO impl. reset/init
part2()