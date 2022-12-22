INPUT = "input.txt"
# INPUT = "test_input.txt"

def solve1(points):
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    max_z = max(points, key=lambda p: p[2])[2]
    
    min_x = min(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    min_z = min(points, key=lambda p: p[2])[2]
    
    res = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y+1):
            for z in range(min_z, max_z+1):
                if [x, y, z] not in points:
                    continue
                res += len(list(filter(lambda x: x not in points, [[x+1,y,z],[x-1,y,z],[x,y+1,z],[x,y-1,z],[x,y,z+1],[x,y,z-1]])))
    return res

def is_free(point):
    x, y, z = point[0], point[1], point[2]
    return not(0 <= x <= 30) or not(0 <= y <= 30) or not (0 <= z <= 30)

def get_ngb(p):
    x, y, z = p[0], p[1], p[2]
    return [[x+1,y,z],[x-1,y,z],[x,y+1,z],[x,y-1,z],[x,y,z+1],[x,y,z-1]]

def flood(points, x, y, z):
    next = [[x,y,z]]
    filled = []
    
    while len(next) > 0:
        p = next.pop(0)
        filled.append(p)
        
        if is_free(p):
            return []
        
        ngb = get_ngb(p)
        for n in ngb:
            if n not in points and n not in next and n not in filled:
                next.append(n)

    return filled

def solve2(points):
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    max_z = max(points, key=lambda p: p[2])[2]
    
    min_x = min(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    min_z = min(points, key=lambda p: p[2])[2]

    print_slice(5, points)
    points.extend(flood(points, 10, 10, 5))

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y+1):
            for z in range(min_z, max_z+1):
                p = [x, y, z]
                if p not in points and all(map(lambda p: p in points, get_ngb(p))):
                    points.append(p)
    
    for z in range(0, 30):
        print_slice(z, points)

    res = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y+1):
            for z in range(min_z, max_z+1):
                if [x, y, z] not in points:
                    continue
                res += len(list(filter(lambda p: p not in points, [[x+1,y,z],[x-1,y,z],[x,y+1,z],[x,y-1,z],[x,y,z+1],[x,y,z-1]])))
    return res

def print_slice(z, points):   
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    
    min_x = min(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    
    for y in range(30):
        for x in range(30):
            print("#" if [x, y, z] in points else ".", end="")
        print()
            

def main():
    points = []
    with open(INPUT, "r") as f:
        for line in f:
            points.append(list(map(int, line.split(","))))
    
    print(f"Solution 1: {solve1(points)}")
    print(f"Solution 2: {solve2(points)}")
    
if __name__ == "__main__":
    main()
