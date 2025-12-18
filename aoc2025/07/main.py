# FILE = "test.txt"
FILE = "data.txt"

from functools import lru_cache

grid = []
W, H = 0, 0
with open(FILE, "r") as f:
    for line in f:
        if W == 0:
            W = len(line.strip())
        grid.extend([c for c in line.strip()])
H = len(grid) // W

def cti(x, y): return x + y * W
def itc(idx): return idx % W, idx // W 

def locate_start(grid):
    for idx in range(H * W):
        if grid[idx] == "S": return idx
    
    assert False, "Start could not be found"

def sol1():
    start_idx = locate_start(grid)
    curr_positions = set([start_idx])
    res = 0
    for curr_y in range(0, H-1):
        next_positions = set()
        for pos in curr_positions:
            x, _ = itc(pos)
            nx, ny = x, curr_y + 1
            npos = cti(nx, ny)
            
            if grid[npos] == "^":
                next_positions.add(cti(nx + 1, ny))
                next_positions.add(cti(nx - 1, ny))
                res += 1
            else:
                next_positions.add(npos)
        curr_positions = next_positions
    print("Solution 1:", res)

@lru_cache
def calc_splits(idx):
    x, y = itc(idx)
    nx, ny = x, y + 1
    npos = cti(nx, ny)
    
    if ny >= H: return 1
    if grid[npos] == "^":
        val1 = calc_splits(cti(nx+1,ny))
        val2 = calc_splits(cti(nx-1,ny))
        return val1 + val2
    else:
        return calc_splits(cti(nx,ny))

def sol2():
    start_idx = locate_start(grid)
    print("Solution 2:", calc_splits(start_idx))

def main():
    sol1()
    sol2()

if __name__ == "__main__":
    main()