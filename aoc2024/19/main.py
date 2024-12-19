from functools import lru_cache

#FILE = "test.txt"
FILE = "data.txt"

def check_design(design, towels):
    for towel in towels:
        if not design.startswith(towel): continue
        if len(towel) > len(design): continue
        if len(towel) == len(design): return True
        if check_design(design[len(towel):], towels): return True
    return False

TOWELS = []

@lru_cache(maxsize=None)
def check_design2(design):
    res = 0
    for towel in TOWELS:
        if not design.startswith(towel): continue
        if len(towel) > len(design):
            continue
        elif len(towel) == len(design):
            res += 1
        else:
            res += check_design2(design[len(towel):])
    return res

def sol1(towels, designs):
    valid_designs = [design for design in designs if check_design(design, towels)]
    res = len(valid_designs)
    print("Solution 1:", res)

def sol2(towels, designs):
    global TOWELS 
    res = 0
    TOWELS = towels
    res = sum(check_design2(design) for design in designs)
    print("Solution 2:", res)

def main():
    with open(FILE, "r") as f:
        towels = next(f).strip().split(", ")
        next(f)
        designs = [line.strip() for line in f]
    sol1(towels, designs) 
    sol2(towels, designs) 

if __name__ == "__main__":
    main()
