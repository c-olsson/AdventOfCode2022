
fo = open("10/input.txt", "r")
input = []

for line in fo.readlines():
    line = line.strip()
    input.append(line)
    
CHECK = [20, 60, 100, 140, 180, 220, 999]

def part1():
    stack = []
    stack.append(0)
    for l in input:
        if l[0] == 'n':
            stack.append(0)
        else:
            _, v = l.split()
            stack.append(0)
            stack.append(int(v))
            
    x = 1
    sum = 0
    c_index = 0
    print(len(stack))
    for i, v in enumerate(stack):
        x += v
        if i+1 == CHECK[c_index]:
            signal_strength = x*CHECK[c_index]
            sum += signal_strength
            c_index += 1
    print(sum)

CHECK2 = [0, 40, 80, 120, 160, 200, 999]

def part2():
    stack = []
    stack.append(0)
    for l in input:
        if l[0] == 'n':
            stack.append(0)
        else:
            _, v = l.split()
            stack.append(0)
            stack.append(int(v))
            
    x = 1
    row = 0
    crt_row = ' '*40
    for i, v in enumerate(stack):
        # update sprite register
        x += v
        
        # draw on current row
        current_col_pos = i-CHECK2[row]
        #print("Col pos",current_col_pos)
        if x-1 <= current_col_pos <= x+1:
            crt_row = crt_row[:current_col_pos] + "#" + crt_row[current_col_pos+1:]
        
        # update to new row
        if i+1 == CHECK2[row+1]:
            row += 1
            #print(i,v,x)
            print(crt_row)
            crt_row = ' '*40
    print(crt_row)

# 14860
#part1()
# RGZEHURK
part2()