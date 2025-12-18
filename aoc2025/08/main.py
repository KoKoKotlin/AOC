# FILE, NUM_CONNS = "test.txt", 10
FILE, NUM_CONNS = "data.txt", 1000

with open(FILE, "r") as f:
    coords = [list(map(int, line.strip().split(","))) for line in f]

def dist(c1, c2): return sum([(v1 - v2) ** 2 for v1, v2 in zip(c1, c2)])
def ceq(c1, c2): return c1[0] == c2[0] and c1[1] == c2[1] and c1[2] == c2[2]

def find_smallest(l):
    for idx, v in enumerate(l):
        if v: return idx
    return -1    

def get_nbhd(node, edges):
    nbhd = []
    for edge in edges:
        if edge[0] == node: nbhd.append(edge[1])
        if edge[1] == node: nbhd.append(edge[0])
    return nbhd

def find_nbhd_size(node, edges, not_visited):
    if not_visited[node]:
        not_visited[node] = False
        nbhd = get_nbhd(node, edges)
        return 1 + sum((find_nbhd_size(node, edges, not_visited) for node in nbhd))
    else:
        return 0

def find_connected_cpms_sizes(edges, number_of_nodes):
    not_visited = [True] * number_of_nodes
    nbhd_sizes = []
    while any(not_visited):
        idx = find_smallest(not_visited)
        nbhd_sizes.append(find_nbhd_size(idx, edges, not_visited))
    
    return nbhd_sizes
        
def sol1():
    adj_matrix = [(dist(coords[i], coords[j]), i, j) 
                  for i in range(len(coords)) 
                  for j in range(i+1, len(coords)) 
                  if i != j]
    adj_matrix = sorted(adj_matrix, key=lambda x: x[0])
    connections = []
    for i in range(NUM_CONNS):
        _, idx1, idx2 = adj_matrix[i]
        connections.append([idx1, idx2])
    cmps = sorted(find_connected_cpms_sizes(connections, len(coords)), reverse=True)
    print("Solution 1:", cmps[0] * cmps[1] * cmps[2])
    
def sol2():
    adj_matrix = [(dist(coords[i], coords[j]), i, j)
                  for i in range(len(coords)) 
                  for j in range(i+1, len(coords)) 
                  if i != j]
    adj_matrix = sorted(adj_matrix, key=lambda x: x[0])

    cmps = [0] * len(coords)
    last_cmp_idx = 0
    for i in range(len(adj_matrix)):
        _, idx1, idx2 = adj_matrix[i]
        cmp1, cmp2 = cmps[idx1], cmps[idx2]
        if cmp1 == 0 and cmp2 == 0:
            last_cmp_idx += 1
            cmps[idx1] = last_cmp_idx
            cmps[idx2] = last_cmp_idx
        elif cmp1 != 0 and cmp2 == 0:
            cmps[idx2] = cmp1
        elif cmp1 == 0 and cmp2 != 0:
            cmps[idx1] = cmp2
        else:
            if cmp1 == cmp2: continue
            for j in range(len(cmps)):
                if cmps[j] == cmp2: cmps[j] = cmp1
        
        if len(set(cmps)) == 1 and cmps[0] != 0: break
    entry = adj_matrix[i]
    coord1 = coords[entry[1]]
    coord2 = coords[entry[2]]
    print("Solution 2:", coord1[0] * coord2[0])

def main():
    sol1()
    sol2()

if __name__ == "__main__":
    main()