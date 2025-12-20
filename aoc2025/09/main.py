FILE = "test.txt"
FILE = "data.txt"

coords = []
with open(FILE, "r") as f:
    for line in f:
        coords.append(list(map(int, line.strip().split(","))))

def sol1():
    max_area = 0
    for i in range(len(coords)):
        coord1 = coords[i]
        for j in range(i+1, len(coords)):
            coord2 = coords[j]
            area = ((abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1))
            if area > max_area: max_area = area
    print("Solution 1:", max_area)

def sol2():
    pass

def main():
    sol1()
    sol2()

if __name__ == "__main__":
    main()