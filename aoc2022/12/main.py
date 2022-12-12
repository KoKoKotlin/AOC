INPUT = "input.txt"
# INPUT = "test_input.txt"

def get_neighbours(arr, idx, w):
    curr = arr[idx]
    x = idx % w
    y = idx // w
    res = []
    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x = x + dx
        new_y = y + dy
        
        if new_x < 0 or new_x >= w or new_y < 0 or new_y >= len(arr) // w:
            continue
        
        if arr[new_x + new_y * w] - 1 <= curr:
            res.append(new_x + new_y * w)      

    return res

def find_shortest_path(vertecies, start_idx, w):
    distances = [float("inf")] * len(vertecies)
    distances[start_idx] = 0
    pred = [None] * len(vertecies)
    ngb = [get_neighbours(vertecies, i, w) for i in range(len(vertecies))]
        
    for _ in range(len(vertecies) - 1):
        dirty = False
        for u in range(len(vertecies)):
            for v in ngb[u]:
                if distances[u] + 1 < distances[v]:
                    dirty = True
                    distances[v] = distances[u] + 1
                    pred[v] = u
        if not dirty:
            return distances, pred

    return distances, pred                    

def parse(lines):
    vertecies = []
    start = None
    goal = None
    
    i = 0
    for line in lines:
        for c in line:
            if c == "S":
                vertecies.append(0)
                start = i
            elif c == "E":
                vertecies.append(ord("z") - ord("a") + 1)
                goal = i
            else: 
                vertecies.append(ord(c) - ord("a") + 1)
            i += 1
    
    return vertecies, start, goal, len(lines[0])

def main():
    with open(INPUT, "r") as f:
        lines = [line.strip() for line in f]
    
    vertecies, start_idx, goal_idx, w = parse(lines)
    dist = find_shortest_path(vertecies, start_idx, w)[0]
    steps = dist[goal_idx]
    print(f"Solution 1: {steps}")
    
    res = []
    for u in range(len(vertecies)):
        if vertecies[u] == 1:
            res.append(find_shortest_path(vertecies, u, w)[0][goal_idx])
    
    print(f"Solution 2: {min(res)}")
    
if __name__ == "__main__":
    main()
