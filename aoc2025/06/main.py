# FILE = "test.txt"
FILE = "data.txt"

def sol1():
    rows = []
    with open(FILE, "r") as f:
        for line in f:
            row = list(filter(lambda x: not (x.isspace() or x == ""), line.strip().split(" ")))
            try:
                rows.append(list(map(int, row)))
            except:
                ops = row

    res = [0 if op == "+" else 1 for op in ops]
    for row in rows:
        for idx, x in enumerate(row):
            if ops[idx] == "+": res[idx] += x
            if ops[idx] == "*": res[idx] *= x
    print("Solution 1:", sum(res))
    
def sol2():
    lines = []
    with open(FILE, "r") as f:
        lines = [line for line in f]
    
    ops_line = lines[-1]
    ops = []
    idx = 0
    curr_op = ""
    last_start_idx = 0
    while idx < len(ops_line):
        sym = ops_line[idx]
        if not sym.isspace():
            if curr_op == "": 
                curr_op = sym
                idx += 1
                continue
            
            ops.append((curr_op, last_start_idx, idx - last_start_idx - 1))
            curr_op = sym
            last_start_idx = idx
        idx += 1
    ops.append((curr_op, last_start_idx, idx - last_start_idx))

    res = [0 if op == "+" else 1 for (op, _, _) in ops]
    number_lines = lines[0:-1]
    for idx, (op, start_idx, length) in enumerate(ops):
        for i in range(length-1,-1,-1):
            number = ""
            for line in number_lines:
                number += line[start_idx + i]
            if op == "+": res[idx] += int(number)
            if op == "*": res[idx] *= int(number)
    print("Solution 2:", sum(res))

def main():
    sol1()
    sol2()

if __name__ == "__main__":
    main()