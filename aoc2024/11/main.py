from functools import lru_cache
from collections import Counter

# FILE = "test.txt"
FILE = "data.txt"

def blink1(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            left = stone_str[:len(stone_str)//2]
            right = stone_str[len(stone_str)//2:]
            new_stones.append(int(left))
            new_stones.append(int(right))
        else:
            new_stones.append(stone * 2024)
    return new_stones

@lru_cache(maxsize=None)
def blink_one(stone):
    if stone == 0:
        return [1] 
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        left = stone_str[0:len(stone_str)//2]
        right = stone_str[len(stone_str)//2:]
        return [int(left), int(right)]
    else:
        return [stone * 2024]

@lru_cache(maxsize=None)
def blink_rec(stone, counter):
    if counter == 75:
        return 1
    new_stones = blink_one(stone)
    unique_stones = Counter(new_stones)
    res = 0
    for stone in unique_stones.keys():
        res += unique_stones[stone] * blink_rec(stone, counter+1)
    return res
    
def sol1(stones):
    for _ in range(25):
        stones = blink1(stones)
    print("Solution 1:", len(stones))

def sol2(stones):
    res = 0
    for stone in stones:
        res += blink_rec(stone, 0)
    print("Solution 2:", res)

def main():
    with open(FILE, "r") as f:
        stones = list(map(int, next(f).strip().split(" ")))
    sol1(stones)
    sol2(stones)
    
if __name__ == "__main__":
    main()
