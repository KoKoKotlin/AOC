from functools import reduce

FILE = "data.txt"
#FILE = "test.txt"

def parse_line(line):
    return list(map(int, line.split(" " * 3)))

def load_data():
    list1, list2 = [], []
    with open(FILE, "r") as f:
        for line in f:
            d = parse_line(line)
            list1.append(d[0])
            list2.append(d[1])
    return list1, list2

def sol1():
    list1, list2 = load_data()
    res = reduce(lambda acc, t: acc + abs(t[0] - t[1]), zip(sorted(list1), sorted(list2)), 0)
    print("Solution 1:", res) 

def sol2():
    list1, list2 = load_data()
    res = reduce(lambda acc, x: acc + x * list2.count(x), list1, 0)
    print("Solution 2:", res)
    
if __name__ == "__main__":
    sol1()
    sol2()
