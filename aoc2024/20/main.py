from dataclasses import dataclass
from copy import deepcopy

FILE = "test.txt"
FILE = "data.txt"

@dataclass
class Node:
    x: int
    y: int
    priority: int

def nbh(x, y, grid, nodes):
    w, h = len(grid[0]), len(grid)
    nbhs = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        cx, cy = x+dx, y+dy
        if not(0 <= cx < w and 0 <= cy < h): continue
        if grid[cy][cx] == "#": continue
        nbhs.append(nodes[cy][cx])
    return nbhs

def dijkstra(grid, start, end):
    w, h = len(grid[0]), len(grid)
    nodes = [[Node(x, y, -1) for x in range(w)] for y in range(h)]
    startx, starty = start
    endx, endy = end
    nodes[starty][startx].priority = 0
    queue = [nodes[starty][startx]]
    while len(queue) > 0:
        node = queue.pop(0)
        if node.x == endx and node.y == endy: break
        for n in nbh(node.x, node.y, grid, nodes):
            if n.priority != -1 and n.priority < node.priority + 1:
                continue
            n.priority = node.priority + 1
            if n not in queue:
                queue.append(n)
            queue = list(sorted(queue, key=lambda x: x.priority))
    return nodes[endy][endx].priority

def sol1(grid, start, end):
    w, h = len(grid[0]), len(grid)
    baseline = dijkstra(grid, start, end)
    cgrid = deepcopy(grid)
    res = 0
    for y in range(h):
        for x in range(w-1):
            cgrid[y][x] = "."
            cgrid[y][x+1] = "."
            l = dijkstra(cgrid, start, end)
            cgrid[y][x] = grid[y][x]
            cgrid[y][x+1] = grid[y][x+1]

            if baseline - l >= 100:
                print(baseline - l, "saved")
                res += 1

    for y in range(h-1):
        for x in range(w):
            cgrid[y][x] = "."
            cgrid[y+1][x] = "."
            l = dijkstra(cgrid, start, end)
            cgrid[y][x] = grid[y][x]
            cgrid[y+1][x] = grid[y+1][x]

            if baseline - l >= 100:
                print(baseline - l, "saved")
                res += 1

    print("Solution 1:", res)

def main():
    with open(FILE, "r") as f:
        grid = [[c for c in line.strip()] for line in f]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = [x, y]
            elif grid[y][x] == "E":
                end = [x, y]
    sol1(grid, start, end)

if __name__ == "__main__":
    main()
