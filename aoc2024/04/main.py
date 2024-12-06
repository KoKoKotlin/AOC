#FILE = "test.txt"
FILE = "data.txt"

def checknbhd(x, y, grid):
    res = 0
    width = len(grid[0])
    height = len(grid)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx, dy) in [(0, 0)]: continue
            string = ""
            for i in range(4):
                cx = x + i*dx
                cy = y + i*dy
                if not ((0 <= cx <= (width-1)) and (0 <= cy <= (height-1))):
                    break
                string += grid[cy][cx]
            if string == "XMAS":
                res += 1
    return res

def sol1(grid):
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            res += checknbhd(x, y, grid)
    print("Solution 1:", res)

def sol2(grid):
    res = 0
    width = len(grid[0])
    height = len(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if not (y + 2 < height and x + 2 < width): continue 
            str1 = grid[y][x] + grid[y+1][x+1] + grid[y+2][x+2]
            str2 = grid[y][x+2] + grid[y+1][x+1] + grid[y+2][x]
            if "MAS" in [str1, str1[::-1]] and "MAS" in [str2, str2[::-1]]:
                res += 1 
    print("Solution 2:", res)
    
def main():
    lines = []
    with open(FILE, "r") as f:
        for line in f:
            lines.append(line.strip())

    grid = [[line[x] for x in range(len(line))] for line in lines]
    sol1(grid)
    sol2(grid)

if __name__ == "__main__":
    main()
