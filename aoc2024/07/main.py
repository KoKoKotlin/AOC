# FILE = "test.txt"
FILE = "data.txt"

def parse_line(line):
    line = line.strip()
    eq_res, tail = line.split(":")
    eq_res = int(eq_res)
    nums = list(map(int, tail.strip().split(" ")))
    return eq_res, nums

def sol1(data):
    res = 0
    for (eq_res, nums) in data:
        for i in range(pow(2, len(nums)-1)):
            ceq_res = 0
            for idx, num in enumerate(nums):
                if idx == 0:
                    ceq_res = num
                else:
                    if (i >> (idx-1) & 1) == 0:
                        ceq_res += num
                    else:
                        ceq_res *= num
            if eq_res == ceq_res:
                res += eq_res
                break
    print("Solution 1:", res)

def change_ops(i, ops):
    if ops[i] == "+": ops[i] = "*"
    elif ops[i] == "*": ops[i] = "||"
    else:
        ops[i] = "+"
        change_ops(i+1, ops)

def sol2(data):
    res = 0
    for (eq_res, nums) in data:
        ops = ["+"] * (len(nums) - 1)
        for i in range(pow(3, len(nums)-1)):
            if i != 0: change_ops(0, ops)
            ceq_res = 0
            for idx, num in enumerate(nums):
                if idx == 0:
                    ceq_res = num
                else:
                    if ops[idx-1] == "+":
                        ceq_res += num
                    elif ops[idx-1] == "*":
                        ceq_res *= num
                    else:
                        ceq_res = int(str(ceq_res) + str(num))
            if eq_res == ceq_res:
                res += eq_res
                break
    print("Solution 2:", res)
    
def main():
    with open(FILE, "r") as f:
        data = [parse_line(line) for line in f]
    sol1(data)
    sol2(data)

if __name__ == "__main__":
    main()
