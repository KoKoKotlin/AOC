from typing import List

INPUT: str = "input.txt"
# INPUT: str = "test_input.txt"

WIDTH: int = 7

DIM: List[List[int]] = [[4, 1], [3, 3], [3, 3], [1, 4], [2, 2]]

ROCKS: List[List[int]] = [
    [1, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

MAX_HEIGHT: int = 1000000
ARENA: List[int] = [0] * WIDTH * MAX_HEIGHT

def idx(x: int, y: int, width: int=WIDTH) -> int:
    return x + y * width

def bnds_chk(rock, dim, x, y):
    if x < 0 or x > WIDTH - dim[0]:
        return False
    
    if y - (dim[1] - 1) < 0:
        return False

    return True

def coll_chk(rock, dim, x, y):    
    for dx in range(dim[0]):
        for dy in range(dim[1]):
            ax = x + dx
            ay = y - dy
            
            if ARENA[idx(ax, ay)] == 1 and rock[idx(dx, dy, dim[0])] == 1:
                return False
    return True
 
def get_start_y(start_y = MAX_HEIGHT - 1):
    for y in range(start_y, -1, -1):
        for x in range(WIDTH):
            if ARENA[idx(x, y)] != 0:
                return y + 3 + 1
    
    return 3
      
def write_rock(rock, dim, x, y):
    global ARENA
    for dx in range(dim[0]):
        for dy in range(dim[1]):
            ax = x + dx
            ay = y - dy
            if rock[idx(dx, dy, dim[0])]:
                ARENA[idx(ax, ay)] = rock[idx(dx, dy, dim[0])]

def print_arena(rows):
    for y in range(rows):
        for x in range(WIDTH):
            print("." if ARENA[idx(x, rows - y - 1)] == 0 else "#", end="")
        print()

ITERATIONS = 2

def solve1(line: str):
    global ARENA
    
    jet_idx: int = 0
    
    for i in range(ITERATIONS):
        rock_idx = i % len(ROCKS)
        rock: List[int] = ROCKS[rock_idx]
        dim: List[int] = DIM[rock_idx]
        y_off: int = dim[1] - 1
        
        y = get_start_y() + y_off
        x = 2
        print(x, y)
        while True:
            dx = -1 if line[jet_idx] == "<" else 1
            x += dx
            if not (bnds_chk(rock, dim, x, y) and coll_chk(rock, dim, x, y)):
                x -= dx
            
            jet_idx = (jet_idx + 1) % len(line)
            
            y -= 1
            if not (bnds_chk(rock, dim, x, y) and coll_chk(rock, dim, x, y)):
                y += 1
                write_rock(rock, dim, x, y)
                break
    return get_start_y() - 3

def coll_chk2(rock, dim, x, y, arena):
    for dx in range(dim[0]):
        for dy in range(dim[1]):
            ax = x + dx
            ay = y - dy                
            if arena[ax] == ay and rock[idx(dx, dy, dim[0])] == 1:
                return False
    
    return True

def write_rock2(rock, dim, x, y, arena):
    for dy in range(dim[1]):
        for dx in range(dim[0]):
            ax = x + dx
            ay = y - dy
            rock_val = rock[idx(dx, dy, dim[0])]
            if rock_val == 1 and arena[ax] < ay:
                arena[ax] = ay
                continue
                            
ITERATIONS2 = 10000000
def solve2(line: str):
    jet_idx: int = 0
    arena = [-1] * WIDTH

    for i in range(ITERATIONS2):
        rock_idx = i % len(ROCKS)
        rock: List[int] = ROCKS[rock_idx]
        dim: List[int] = DIM[rock_idx]
        y_off: int = dim[1] - 1
        
        y = max(arena) + 3 + 1 + y_off
        x = 2

        while True:
            dx = -1 if line[jet_idx] == "<" else 1
            x += dx
            if not (bnds_chk(rock, dim, x, y) and coll_chk2(rock, dim, x, y, arena)):
                x -= dx
            
            jet_idx = (jet_idx + 1) % len(line)      
            
            y -= 1
            if not (bnds_chk(rock, dim, x, y) and coll_chk2(rock, dim, x, y, arena)):
                y += 1
                write_rock2(rock, dim, x, y, arena)
                break
    return max(arena)
        
def main():
    with open(INPUT, "r") as f:
        line = f.readline().strip()
    
    # print(f"Solution 1: {solve1(line)}")
    print(f"Solution 2: {solve2(line)}")

if __name__ == "__main__":
    main()
