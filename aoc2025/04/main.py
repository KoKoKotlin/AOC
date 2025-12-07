#FILE = "test.txt"
FILE = "input.txt"

with open(FILE, "r") as f:
    FIELD = [[c for c in line.strip()] for line in f]
print(FIELD)
def count_nbhd(x, y, w, h):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0: continue
            nx = x + dx
            ny = y + dy

            if 0 <= nx < w and 0 <= ny < h:
                if FIELD[ny][nx] == "@": count += 1
    return count

def sol1():
    sol = 0
    w = len(FIELD[0])
    h = len(FIELD)
    for y in range(h):
        for x in range(w):
            if FIELD[y][x] == "@" and count_nbhd(x, y, w, h) < 4: 
                sol += 1
    print("Solution 1:", sol)

def sol2():
    sol = 0
    w = len(FIELD[0])
    h = len(FIELD)
    dirty = True
    while dirty:
        dirty = False
        for y in range(h):
            for x in range(w):
                if FIELD[y][x] == "@" and count_nbhd(x, y, w, h) < 4: 
                    dirty = True
                    FIELD[y][x] = "."
                    sol += 1

    print("Solution 2:", sol)

def main():
    sol1()
    sol2()

if __name__ == "__main__":
    main()