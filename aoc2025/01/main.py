# FILE = "test.txt"
FILE = "input.txt"
with open(FILE, "r") as f:
    DATA = [line.strip() for line in f]

def sol1():
    sol = 0
    pos = 50
    for data in DATA:
        dir = data[0]
        distance = int(data[1:])
        if dir == "L":
            pos -= distance
        elif dir == "R":
            pos += distance
        else:
            assert False, "Unknown direction"
        
        if pos % 100 == 0: sol += 1

    print("Solution 1:", sol)


def sol2():
    sol = 0
    pos = 50
    for data in DATA:
        dir = data[0]
        distance = int(data[1:])
        for _ in range(distance):
            if dir == "L": pos -= 1
            elif dir == "R": pos += 1
            else: assert False, "Unknown direction"
            if pos % 100 == 0: sol += 1
    print("Solution 2:", sol)

def main():
    sol1()
    sol2()

if __name__ == "__main__":
    main()