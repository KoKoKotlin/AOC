# FILE = "test.txt"
FILE = "input.txt"

IDS, RANGES = [], []
with open(FILE, "r") as f:
    parse_ranges = True
    for line in f:
        if line.strip() == "":
            parse_ranges = False
            continue

        if parse_ranges:
            RANGES.append(list(map(int, line.strip().split("-"))))
        else:
            IDS.append(int(line.strip()))

def sol1():
    sol = 0

    for id in IDS:
        for range in RANGES:
            if range[0] <= id <= range[1]: 
                sol += 1
                break

    print("Solution 1:", sol)

def sol2():
    sol = 0
    curr = 0
    end = max([r[1] for r in RANGES])

    while curr < end:
        min_idx = -1
        min_start = end
        for i, r in enumerate(RANGES):
            if r[0] > curr and r[0] < min_start:
                min_idx = i
                min_start = r[0]
        
        r = RANGES[min_idx]
        sol += r[1] - r[0]
        curr = r[1]

        dirty = True
        curr_range_idx = min_idx
        while dirty:
            print(curr_range_idx, RANGES[curr_range_idx])
            if RANGES[curr_range_idx][1] == end: break
            dirty = False
            for i, r2 in enumerate(RANGES):
                if i == curr_range_idx: continue

                if r[0] <= r2[0] <= r[1] and r2[1] > r[1]:
                    sol += r2[1] - r[1]
                    curr = r2[1]
                    curr_range_idx = i
                    dirty = True
                    break
    print("Solution 2:", sol)

def main():
    sol1()
    sol2()

if __name__ == "__main__":
    main()