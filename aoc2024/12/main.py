from queue import Queue

FILE = "test3.txt"
# FILE = "data.txt"

def unreachable(*args):
    print("Unreachable", *args)
    exit(-1)

def get_nbhs(x, y, grid):
    cell = grid[y][x]
    w = len(grid[0])
    h = len(grid)
    nbhs = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        cx, cy = x + dx, y + dy
        if not(0 <= cx < w and 0 <= cy < h): continue
        if cell == grid[cy][cx]:
            nbhs.append([cx, cy])
    return nbhs

def calc_region_perim(region, grid): 
    boundaries = 0
    w = len(grid[0])
    h = len(grid)
    for cell in region:
        x, y = cell
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            cx, cy = x + dx, y + dy
            if not(0 <= cx < w and 0 <= cy < h):
                boundaries += 1
                continue

            if grid[y][x] != grid[cy][cx]:
                boundaries += 1    
    return boundaries

def get_regions(grid):
    done_cells = set()
    w = len(grid[0])
    h = len(grid)
    regions = []
    for y in range(h):
        for x in range(w):
            curr_cell = [x, y]
            if str(curr_cell) in done_cells: continue
            
            next_cells = Queue()
            next_cells.put(curr_cell)
            curr_region = []
            while not next_cells.empty():
                cell = next_cells.get()
                if str(cell) in done_cells: continue
                curr_region.append(cell)
                done_cells.add(str(cell))
                for ncell in get_nbhs(*cell, grid):
                    next_cells.put(ncell)
            regions.append(curr_region)
    return regions

def sol1(grid):
    regions = get_regions(grid)
    res = sum(len(region) * calc_region_perim(region, grid) for region in regions)
    print("Solution 1:", res)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def dirToStr(dx, dy):
    match (dx, dy):
        case (0, -1): return "UP"
        case (0, 1): return "DOWN"
        case (-1, 0): return "LEFT"
        case (1, 0): return "RIGHT"
        case _: unreachable()

def count_sides(region):
    sides = 0
    next_cells = Queue()
    next_cells.put(region[0])
    done_cells = set()
    walls = {
        "UP": [],
        "DOWN": [],
        "LEFT": [],
        "RIGHT": [],
    }
    while not next_cells.empty():
        x, y = next_cells.get()
        done_cells.add(str([x, y]))
        for dx, dy in [UP, DOWN, LEFT, RIGHT]:
            cx, cy = x + dx, y + dy
            if [cx, cy] in region and str([cx, cy]) not in done_cells:
                next_cells.put([cx, cy])
            else:
                w = walls[dirToStr(dx, dy)]
                if (dx, dy) in [LEFT, RIGHT] and [cx, cy+1] not in w and [cx, cy-1] not in w:
                    sides += 1
                elif (dx, dy) in [UP, DOWN] and [cx+1, cy] not in w and [cx-1, cy] not in w:
                    sides += 1
                walls[dirToStr(dx, dy)].append([cx, cy])
    return sides
def sol2(grid):
    w = len(grid[0])
    h = len(grid)
    regions = get_regions(grid)
    res = sum(len(region) * count_sides(region) for region in regions)
    print("Solution 2:", res)
    
def main():
    with open(FILE, "r") as f:
        grid = [[c for c in line.strip()] for line in f]
    sol1(grid)
    sol2(grid)

if __name__ == "__main__":
    main()
