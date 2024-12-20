from queue import PriorityQueue
from dataclasses import dataclass, field

FILE = "test2.txt"
#FILE = "data.txt"

@dataclass(order=True)
class Node:
    priority: int
    x: int
    y: int
    viewing_dir: any=field(compare=False)

def turn_clockwise(cdir):
    if cdir == WEST: return SOUTH
    elif cdir == SOUTH: return EAST
    elif cdir == EAST: return NORTH
    elif cdir == NORTH: return WEST
    print("Unreachable")
    exit(-1)

def turn_counterclockwise(cdir):
    if cdir == WEST: return NORTH
    elif cdir == NORTH: return EAST
    elif cdir == EAST: return SOUTH
    elif cdir == SOUTH: return WEST
    printf("Unreachable")
    exit(-1)

def get_neighbors(node, grid):
    w = len(grid[0])
    h = len(grid)
    nodes = []
    dx, dy = node.viewing_dir
    x, y = node.x, node.y
    cx, cy = x+dx, y+dy
    if 0 <= cx < w and 0 <= cy < h and grid[cy][cx] != "#": 
        nodes.append([cx, cy, 1, node.viewing_dir])
    nodes.append([x, y, 1000, turn_clockwise(node.viewing_dir)])
    nodes.append([x, y, 1000, turn_counterclockwise(node.viewing_dir)])
    return nodes

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (-1, 0)
WEST = (1, 0)

def vtoc(vdir):
    if vdir == NORTH: return "^"
    elif vdir == SOUTH: return "v"
    elif vdir == EAST: return "<"
    elif vdir == WEST: return ">"

def sol1(grid, start, end):
    endx, endy = end
    startx, starty = start
    queue = []
    queue.append(Node(0, startx, starty, EAST))
    ends = []
    current_min = -1
    while len(queue) > 0:
        node = queue.pop(0)
        if node.x == endx and node.y == endy:
            ends.append(node)
            if node.priority < current_min or current_min == -1:
                current_min = node.priority
            continue
        if node.priority > current_min and current_min != -1:
            continue

        for x, y, weight, viewing_dir in get_neighbors(node, grid):
            cn = Node(node.priority + weight, x, y, viewing_dir)    
            queue.append(cn)
    print(ends)
    print("Solution 1:", node.priority)

def main():
    grid = []
    with open(FILE, "r") as f:
        y = 0
        for line in f:
            grid.append([c for c in line.strip()])
            y += 1

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = [x, y]
            elif grid[y][x] == "E":
                end = [x, y]

    sol1(grid, start, end)
    
if __name__ == "__main__":
    main()
