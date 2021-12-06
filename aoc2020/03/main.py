
def getTree(lines, x, y, width):
    return lines[y][x % width] == "#"

def main():
    lines = []
    with open("trees.txt", "r") as f:
        for line in f:
            lines.append(line.strip())
    
    width = len(lines[0])

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    res = 1
    for x_slope, y_slope in slopes:
        x_pos = x_slope

        trees = 0
        for y_pos in range(y_slope, len(lines), y_slope):
            trees += 1 if getTree(lines, x_pos, y_pos, width) else 0
            x_pos += x_slope

        res *= trees
        print("Trees hit :", trees, " for slope ", x_slope, y_slope)

    print("Result: ", res)

if __name__ == "__main__":
    main()