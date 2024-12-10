from collections import defaultdict

#FILE = "test.txt"
FILE = "data.txt"

def get_antinodes(pt1, pt2):
    dx, dy = pt2[0] - pt1[0], pt2[1] - pt1[1]
    return [[pt1[0] - dx, pt1[1] - dy], [pt2[0] + dx, pt2[1] + dy]]

def get_antinodes2(pt1, pt2, w, h):
    dx, dy = pt2[0] - pt1[0], pt2[1] - pt1[1]
    antinodes = []
    i = 0
    while True:
        cx = pt1[0] + i*dx
        cy = pt1[1] + i*dy
        if check_bounds(cx, cy, w, h): antinodes.append([cx, cy])
        else: break
        i += 1
    i = -1    
    while True:
        cx = pt1[0] + i*dx
        cy = pt1[1] + i*dy
        if check_bounds(cx, cy, w, h): antinodes.append([cx, cy])
        else: break
        i -= 1
    return antinodes

def check_bounds(x, y, w, h):
    return 0 <= x < w and 0 <= y < h

def sol1(grid):
    res = 0
    antennas = defaultdict(lambda: [])

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != ".":
                antennas[grid[y][x]].append([x, y])

    antinodes = set()
    for pts in antennas.values():
        for i in range(len(pts)-1):
            for j in range(i+1, len(pts)):
                at1, at2 = pts[i], pts[j]
                a1, a2 = get_antinodes(at1, at2)
                if check_bounds(*a1, len(grid[0]), len(grid)):
                    antinodes.add(str(a1))
                if check_bounds(*a2, len(grid[0]), len(grid)):
                    antinodes.add(str(a2))
    print("Solution 1:", len(antinodes))

def sol2(grid):
    res = 0
    antennas = defaultdict(lambda: [])

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != ".":
                antennas[grid[y][x]].append([x, y])

    antinodes = set()
    for pts in antennas.values():
        if len(pts) < 2: continue
        for i in range(len(pts)-1):
            for j in range(i+1, len(pts)):
                at1, at2 = pts[i], pts[j]
                for a in get_antinodes2(at1, at2, len(grid[0]), len(grid)):
                    antinodes.add(str(a))
    print("Solution 2:", len(antinodes))

def main():
    with open(FILE, "r") as f:
        grid = [[c for c in line if c != "\n"] for line in f] 
    sol1(grid)
    sol2(grid)

if __name__ == "__main__":
    main()
