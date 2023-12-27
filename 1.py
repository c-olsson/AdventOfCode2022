
fo = open("1/input.txt", "r")
input = []
cr = 0
for line in fo.readlines():
    line = line.strip()
    if line != "":
        cr += int(line)
    else:
        input.append(cr)
        cr = 0

def part1():
    print(max(input))

def part2():
    input.sort()
    print(input[-1]+input[-2]+input[-3])

# 69289
part1()
# 205615
part2()