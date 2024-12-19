from dataclasses import dataclass

#FILE, S, THRESHOLD = "test.txt", 7, 12
FILE, S, THRESHOLD = "data.txt", 71, 1024

@dataclass
class Node:
    x: int
    y: int
    priority: int

def nbh(x, y, grid, nodes):
    nbhs = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        cx, cy = x+dx, y+dy
        if not(0 <= cx < S and 0 <= cy < S): continue
        if grid[cy][cx] == "#": continue
        nbhs.append(nodes[cy][cx])
    return nbhs

def sol1(grid):
    nodes = [[Node(x, y, -1) for x in range(S)] for y in range(S)]
    endx, endy = [S-1, S-1]
    nodes[0][0].priority = 0
    queue = [nodes[0][0]]
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
    print("Solution 1:", nodes[S-1][S-1].priority)

def sol2(grid, bs):
    i = THRESHOLD
    while True:
        x, y = bs[i]
        grid[y][x] = "#"
        nodes = [[Node(x, y, -1) for x in range(S)] for y in range(S)]
        endx, endy = [S-1, S-1]
        nodes[0][0].priority = 0
        queue = [nodes[0][0]]
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
        if nodes[S-1][S-1].priority == -1: break
        i += 1
    print("Solution 2:", *bs[i])

def main():
    grid = [["." for i in range(S)] for j in range(S)]
    coords = []
    with open(FILE, "r") as f:
        for line in f:
            coords.append(list(map(int, line.split(","))))

    for i in range(THRESHOLD):
        x, y = coords[i]
        grid[y][x] = "#"
    sol1(grid)
    sol2(grid, coords)
    
if __name__ == "__main__":
    main()
