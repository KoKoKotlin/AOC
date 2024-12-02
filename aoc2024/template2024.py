from functools import reduce

FILE = "data.txt"
#FILE = "test.txt"

def load_data():
    with open(FILE, "r") as f:
        lines = []
        for line in f:
            lines.append(list(map(int, line.split(" "))))
    return lines

def check_save(report):
    is_inc = None
    diffs = list(map(lambda x, y: x - y, zip(report[0:len(report-1)], report[1:])))
    return all(map(lambda x: 1 <= abs(x) <= 3, diffs)) and (all(map(lambda x > 0, diffs)) or all(map(lambda x < 0, diffs)))
    
def sol1():
    lines = load_data()
    res = reduce(lambda acc, r: acc + 1 if check_save(r) else 0, lines, 0) 
    print("Solution 1:", res)

def sol2():
    res = 0
    print("Solution 2:", res)

if __name__ == "__main__":
    sol1()
    sol2()
