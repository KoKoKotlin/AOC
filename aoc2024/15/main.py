from copy import deepcopy

#FILE = "test2.txt"
FILE = "data.txt"

def make_move(pos, grid, inst):
    match inst:
        case "^": dx, dy = 0, -1
        case ">": dx, dy = 1, 0
        case "<": dx, dy = -1, 0
        case "v": dx, dy = 0, 1
    x, y = pos
    cx, cy = x + dx, y + dy

    if grid[cy][cx] == ".":
        grid[cy][cx] = "@"
        grid[y][x] = "."
        return [cx, cy]
    elif grid[cy][cx] == "O":
        while grid[cy][cx] == "O":
            cx, cy = cx + dx, cy + dy
        if grid[cy][cx] != "#":
            grid[y][x] = "."
            grid[y+dy][x+dx] = "@"
            grid[cy][cx] = "O"
            return [x+dx, y+dy]
        else:
            return [x, y]
    else:
        return [x, y]

def move_box(cgrid, grid, dx, dy, pos_l, p=False):
    x1, y1 = pos_l
    x2, y2 = x1 + 1, y1
    cx1, cy1 = x1 + dx, y1 + dy
    cx2, cy2 = x2 + dx, y2 + dy
    cc1 = grid[cy1][cx1] 
    cc2 = grid[cy2][cx2] 
    if p: print("pos_l", pos_l, "dx", dx, "dy", dy, "x1", x1, "y1", y1, "x2", x2, "y2", y2, "cx1", cx1, "cy1", cy1, "cx2", cx2, "cy2", cy2, "cc1", cc1, "cc2", cc2)
    if cc1 == "#" or cc2 == "#":
        return False
    res = True
    if cc1 == "[" and dy != 0:
        res = res and move_box(cgrid, grid, dx, dy, [cx1, cy1], p)
    if cc1 == "]" and (dy != 0 or dx < 0):
        res = res and move_box(cgrid, grid, dx, dy, [cx1-1, cy1], p)
    if cc2 == "[" and (dy != 0 or dx > 0):
        res = res and move_box(cgrid, grid, dx, dy, [cx2, cy2], p)
    if cc2 == "]" and dy != 0:
        res = res and move_box(cgrid, grid, dx, dy, [cx2-1, cy2], p)
    if p: print_grid(cgrid)
    cgrid[y1][x1] = "."
    cgrid[y2][x2] = "."
    cgrid[cy1][cx1] = "["
    cgrid[cy2][cx2] = "]"
    if p: print_grid(cgrid)
    
    return res

def make_move2(pos, grid, inst, p=False):
    match inst:
        case "^": dx, dy = 0, -1
        case ">": dx, dy = 1, 0
        case "<": dx, dy = -1, 0
        case "v": dx, dy = 0, 1
    x, y = pos
    cx, cy = x + dx, y + dy
    if p: print(x, y, cx, cy)
    if grid[cy][cx] == ".":
        grid[cy][cx] = "@"
        grid[y][x] = "."
        return grid, [cx, cy], False
    elif grid[cy][cx] in "[]":
        cgrid = deepcopy(grid)
        sx, sy = cx, cy
        apply = False
        if grid[cy][cx] == "[":
            if p: print("[")
            apply = move_box(cgrid, grid, dx, dy, [cx, cy], p)
        if grid[cy][cx] == "]":
            if p: print("]")
            apply = move_box(cgrid, grid, dx, dy, [cx-1, cy], p)
        if p: print_grid(cgrid)
        if apply:
            grid = cgrid
            grid[y+dy][x+dx] = "@"
            grid[y][x] = "."
            if p: print_grid(cgrid)
            return grid, [cx, cy], True
        else:
            return grid, [x, y], True
    else:
        return grid, [x, y], False

def find_pos(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@": return x, y

def sol1(grid, inst):
    pos = find_pos(grid)
    for i in inst:
        pos = make_move(pos, grid, i)

    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O": res += x + 100*y

    print("Solution 1:", res)

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end="")
        print() 

def count_boxes(grid):
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "[" and grid[y][x+1] == "]":
                res += 1
    return res

def sol2(grid, inst):
    new_grid = []
    for y in range(len(grid)):
        line = [] 
        for x in range(len(grid[0])):
            match grid[y][x]:
                case ".": s = ".."
                case "#": s = "##"
                case "O": s = "[]"
                case "@": s = "@."
            line.extend([c for c in s])
        new_grid.append(line)
    grid = new_grid
    print(count_boxes(grid))
    pos = find_pos(grid)
    last_countboxes = 600
    last_grid = []
    for i in inst:
        grid, pos, moved = make_move2(pos, grid, i)
        if count_boxes(grid) != last_countboxes:
            print(pos, i, count_boxes(grid), last_countboxes)
            make_move2(pos, last_grid, i, True)
        last_grid = deepcopy(grid)
        last_countboxes = count_boxes(grid)
        
    print(count_boxes(grid))
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end="")
            if grid[y][x] == "[": res += x + 100*y
        print()

    print("Solution 2:", res)

def main():
    with open(FILE, "r") as f:
        parse_grid = True
        grid, instructions = [], []
        for line in f:
            if not line.isspace():
                if parse_grid:
                    grid.append([c for c in line.strip()])
                else:
                    instructions.extend([c for c in line.strip()])
            else:
                parse_grid = False
    sol1(deepcopy(grid), instructions)
    sol2(grid, instructions)
if __name__ == "__main__":
    main()
