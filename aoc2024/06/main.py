from enum import Enum
from functools import reduce
from copy import deepcopy

# HINT: Run with pypy or it will be slooooow

#FILE = "test.txt"
FILE = "data.txt"

class Dir(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def intToDir(i):
    match i:
        case 0: return Dir.UP
        case 1: return Dir.RIGHT
        case 2: return Dir.DOWN
        case 3: return Dir.LEFT
    
DIRS = ["^", ">", "v", "<"]

WIDTH = 0
HEIGHT = 0

def step(grid, currpos):
    x, y = currpos
    c = grid[y][x]
    currdir = intToDir(DIRS.index(c))
    dx, dy = 0, 0
    match currdir:
        case Dir.UP:
            dx = 0
            dy = -1
        case Dir.LEFT:
            dx = -1
            dy = 0
        case Dir.RIGHT:
            dx = 1
            dy = 0
        case Dir.DOWN:
            dx = 0
            dy = 1
    nx = x + dx
    ny = y + dy
    
    if not (0 <= nx < WIDTH and 0 <= ny < HEIGHT):
        grid[y][x] = "X"
        return None
    nextpos = grid[ny][nx]
    if nextpos in [".", "X"]:
        grid[y][x] = "X"
        grid[ny][nx] = c
        return [nx, ny] 
    else:
        nc = DIRS[(DIRS.index(c) + 1) % len(DIRS)]
        grid[y][x] = nc
        return currpos

def step2(grid, currpos):
    x, y = currpos
    c = grid[y][x]
    currdir = intToDir(DIRS.index(c))
    dx, dy = 0, 0
    match currdir:
        case Dir.UP:
            dx = 0
            dy = -1
        case Dir.LEFT:
            dx = -1
            dy = 0
        case Dir.RIGHT:
            dx = 1
            dy = 0
        case Dir.DOWN:
            dx = 0
            dy = 1
    nx = x + dx
    ny = y + dy
    
    if not (0 <= nx < WIDTH and 0 <= ny < HEIGHT):
        grid[y][x] = "."
        return None
    nextpos = grid[ny][nx]
    if nextpos in ".":
        grid[y][x] = "."
        grid[ny][nx] = c
        return [nx, ny] 
    else:
        nc = DIRS[(DIRS.index(c) + 1) % len(DIRS)]
        grid[y][x] = nc
        return currpos

def flatten(lst):
    return [x for xs in lst for x in xs]

def sol1(grid, startpos):
    pos = startpos
    while (pos := step(grid, pos)) is not None: pass 
    res = sum(map(lambda x: 1 if x == "X" else 0, flatten(grid)))
    print("Solution 1:", res)

def sol2(grid, startpos):
    sx, sy = startpos
    sc = grid[sy][sx]
    res = 0
    threshold = WIDTH * HEIGHT 
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] == "#" or sx == x and sy == y: continue
            pos = startpos
            grid[y][x] = "#"
            steps = 0
            
            while (pos := step2(grid, pos)) is not None and steps < threshold: steps += 1
            if pos:
                cx, cy = pos
                grid[cy][cx] = "." 
                res += 1

            grid[y][x] = "."
            grid[sy][sx] = sc
    print("Solution 2:", res)
def main():
    global WIDTH, HEIGHT
    
    grid = []
    with open(FILE, "r") as f:
        lines = [line.strip() for line in f]
    grid = [[c for c in line] for line in lines]
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    for y in range(HEIGHT):
        for x in range(WIDTH):
           if grid[y][x] in DIRS:
               startpos = [x, y]
    sol1(deepcopy(grid), startpos)
    sol2(grid, startpos)

if __name__ == "__main__":
    main()
