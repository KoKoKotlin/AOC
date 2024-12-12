from queue import Queue

# FILE = "test.txt"
FILE = "data.txt"

UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3

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

def sol1(grid):
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
    res = sum(len(region) * calc_region_perim(region, grid) for region in regions)
    print("Solution 1:", res)

def sol2(grid):
    pass

def main():
    with open(FILE, "r") as f:
        grid = [[c for c in line.strip()] for line in f]
    sol1(grid)
    sol2(grid)

if __name__ == "__main__":
    main()
