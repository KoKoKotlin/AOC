from functools import reduce
from copy import deepcopy

FILE = "data.txt"
# FILE = "test.txt"

def load_data():
    with open(FILE, "r") as f:
        lines = []
        for line in f:
            lines.append(list(map(int, line.split(" "))))
    return lines

def check_save(report):
    is_inc = None
    diffs = list(map(lambda p: p[0] - p[1], zip(report[0:len(report)-1], report[1:])))
    return all(map(lambda x: 1 <= abs(x) <= 3, diffs)) and (all(map(lambda x: x > 0, diffs)) or all(map(lambda x: x < 0, diffs)))

def search_problem(diffs):
    parity = diffs[0] > 0
    for i in range(len(diffs)):
        diff = diffs[i]
        if parity and diff < 0: return i
        elif not parity and diff > 0: return i

        if not(1 <= abs(diff) <= 3): return i
    return -1

def get_diffs(report):
    diffs = list(map(lambda p: p[0] - p[1], zip(report[0:len(report)-1], report[1:])))
    return diffs

def check_save2(report):
    is_inc = None
    diffs = get_diffs(report)
    for i in range(len(report)):
        report1 = deepcopy(report)
        del report1[i]
        if check_save(report1): return True
    return False

def sol1():
    lines = load_data()
    safe = 0
    for report in lines:
        if check_save(report): safe += 1
    print("Solution 1:", safe)

def sol2():
    lines = load_data()
    safe = 0
    for report in lines:
        if check_save2(report): safe += 1
    print("Solution 2:", safe)

if __name__ == "__main__":
    sol1()
    sol2()
