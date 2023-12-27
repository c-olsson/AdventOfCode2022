
fo = open("6/input.txt", "r")

line = fo.readline().strip()

def part1():
    length = 4
    for i in line:
        s = set(line[i:i+length])
        if len(s) == length:
            print(i+length, line[i:i+length])
            break

def part2():
    length = 14
    for i in line:
        s = set(line[i:i+length])
        if len(s) == length:
            print(i+length, line[i:i+length])
            break

# 1625
part1()
# 2250
part2()