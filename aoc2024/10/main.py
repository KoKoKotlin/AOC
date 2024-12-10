from queue import Queue

# FILE = "test.txt"
FILE = "data.txt"

def search_starts(grid):
    starts = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0: starts.append([x, y])
    return starts

def score(grid, start):
    w = len(grid[0])
    h = len(grid)
    next_checks = Queue()
    next_checks.put(start)
    score = 0
    visited = set()
    while not next_checks.empty():
        x, y = next_checks.get()
        num = grid[y][x]
        for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            cx, cy = x + dx, y + dy
            if not (0 <= cx < w and 0 <= cy < h): continue
            cnum = grid[cy][cx]
            if num == 8 and cnum == 9 and str([cx, cy]) not in visited:
                visited.add(str([cx, cy]))
                score += 1
                continue
            if cnum == num + 1:
                next_checks.put([cx, cy])
    return score

def score2(grid, start):
    w = len(grid[0])
    h = len(grid)
    next_checks = Queue()
    next_checks.put(start)
    score = 0
    while not next_checks.empty():
        x, y = next_checks.get()
        num = grid[y][x]
        for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            cx, cy = x + dx, y + dy
            if not (0 <= cx < w and 0 <= cy < h): continue
            cnum = grid[cy][cx]
            if num == 8 and cnum == 9:
                score += 1
                continue
            if cnum == num + 1:
                next_checks.put([cx, cy])
    return score


def sol1(grid):
    res = 0
    starts = search_starts(grid)
    for start in starts:
        res += score(grid, start)
    print("Solution 1:", res)

def sol2(grid):
    res = 0
    starts = search_starts(grid)
    for start in starts:
        res += score2(grid, start)
    print("Solution 2:", res)

def main():
    with open(FILE, "r") as f:
        grid = [[int(c) for c in line.strip()] for line in f]
    sol1(grid)
    sol2(grid)

if __name__ == "__main__":
    main()
