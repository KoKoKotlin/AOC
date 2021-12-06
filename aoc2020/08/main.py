from pprint import pprint
from copy import deepcopy

def load_data():
    lines = []
    with open("code.txt", "r") as f:
        for line in f:
            lines.append(line.strip())
    
    return lines

def halts(program):
    acc = 0
    pc = 0
    halts = False
    visited = []

    while True:
        if pc == len(program):
            halts = True
            break
    
        inst = program[pc]
        if pc in visited:
            break

        visited.append(pc)

        if inst[0] == "acc":
            acc += inst[1]
            pc += 1
        elif inst[0] == "jmp":
            pc += inst[1]
        else:
            pc += 1
    
    return acc, halts

def solve1(lines):
    instructions = list(map(lambda x: [x[0], int(x[1])], map(lambda x: x.split(" "), lines)))

    acc, _ = halts(instructions)    
    print(f"Solution 1: {acc}")

def solve2(lines):
    # brute force
    instructions = list(map(lambda x: [x[0], int(x[1])], map(lambda x: x.split(" "), lines)))
    acc = 0
    
    for idx, inst in enumerate(instructions):
        copy_inst = deepcopy(instructions)
        if inst[0] == "nop":
            copy_inst[idx][0] = "jmp"
        elif inst[0] == "jmp":
            copy_inst[idx][0] = "nop"
        
        acc_, h = halts(copy_inst)
        
        if h:
            acc = acc_
            break

    print(f"Solution 2: {acc}")

def main():
    data = load_data()
    solve1(data)
    solve2(data)

if __name__ == "__main__":
    main()