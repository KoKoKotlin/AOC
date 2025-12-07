# FILE = "test.txt"
FILE = "input.txt"

with open(FILE, "r") as f:
    RANGES = list(map(lambda x: list(map(int, x.split("-"))), f.readline().strip().split(",")))

def sol1():
    sol = 0
    for range_ in RANGES:
        start, end = range_[0], range_[1]
        for i in range(start, end+1):
            if len(str(i)) % 2 != 0: continue
            j = len(str(i)) // 2
            digits = str(i)[:j]
            test_number = int(digits * 2)
            if i == test_number: 
                sol += test_number
    print("Solution 1:", sol)

def sol2():
    sol = 0
    for range_ in RANGES:
        start, end = range_[0], range_[1]
        for i in range(start, end+1):
            i = str(i)
            for j in range(1, len(i)):
                if len(i) % j != 0: continue
                digits = i[:j]
                test_number = digits * (len(i) // j)
                if i == test_number:
                    sol += int(test_number)
                    break
    print("Solution 2:", sol)

def main():
    sol1()
    sol2()

if __name__ == "__main__":
    main()