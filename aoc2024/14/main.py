from functools import reduce
from pprint import pprint
from collections import Counter

#FILE = "test.txt"
FILE = "data.txt"

#W, H = 11, 7
W, H = 101, 103

# NOTE: solved part 2 by saving the output to file and manually searching the file

def sol1(vals):
    quadrants = [0] * 4
    final_pos = []
    for val in vals:
        x, y = val[0]
        vx, vy = val[1]
        x += vx*100
        y += vy*100
        if x >= 0: x = x % W
        else: x = (x + W*(-x//W + 1)) % W
        if y >= 0: y = y % H
        else: y = (y + H*(-y//H + 1)) % H
        final_pos.append([x, y])

    for x, y in final_pos:
        if x < W//2 and y < H//2:   # TL
            quadrants[0] += 1
        elif x > W//2 and y < H//2: # TR
            quadrants[1] += 1
        elif x < W//2 and y > H//2: # BL
            quadrants[2] += 1
        elif x > W//2 and y > H//2: # BR
            quadrants[3] += 1
    res = reduce(lambda acc, x: acc * x, quadrants, 1)
    print("Solution 1:", res)  
            
def sol2(vals):
    for i in range(1000):
        t = 4943 + i*101
        final_pos = []
        print(f"____________ i = {t} ______________")
        for val in vals:
            x, y = val[0]
            vx, vy = val[1]
            x += vx*t
            y += vy*t
            if x >= 0: x = x % W
            else: x = (x + W*(-x//W + 1)) % W
            if y >= 0: y = y % H
            else: y = (y + H*(-y//H + 1)) % H
            final_pos.append([x, y])

        for y in range(H):  
            for x in range(W):
                if [x, y] in final_pos: print("#", end="")
                else: print(".", end="")
            print()
        print("____________________________________")
        
def main():
    vals = []
    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split(" ")
            vals.append(list(map(lambda x: list(map(int, x[2:].split(","))), data)))
    sol1(vals)
    sol2(vals)

if __name__ == "__main__":
    main()
