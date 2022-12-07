from functools import reduce

INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"

class NodeType:
    DIR = 0
    FILE = 1

class Node:
    ID = 0
    def __init__(self):
        self.name = ""
        self.id = 0
        self.children = []
        self.node_type = None
        self.size = 0
    
    def get_size(self):
        if self.node_type == NodeType.FILE:
            return self.size
        else:
            return reduce(lambda acc, next: acc + next.get_size(), self.children, 0)
            
    def create_dir(name):
        dir = Node()
        dir.name = name
        dir.id = Node.ID
        Node.ID += 1
        dir.node_type = NodeType.DIR
        
        return dir
    
    def create_file(name, size):
        file = Node()
        file.name = name
        file.id = Node.ID
        Node.ID += 1
        file.node_type = NodeType.FILE
        file.size = size
        
        return file
    
    def __repr__(self):
        if self.node_type == NodeType.DIR:
            return f"Dir[name: {self.name}, children{self.children}]"
        else:
            return f"File[name: {self.name}, size: {self.size}]"

def find_parent(root, node):
    candidates = [root]
    
    while not len(candidates) == 0:
        next = candidates.pop()
        
        if node in next.children:
            return next
        
        candidates.extend(next.children)

    return None

def parse(input):
    root = Node.create_dir("/")
    
    current_node = root
    for line in input:
        line = line.strip()
        if line == "$ cd /" or line.startswith("$ ls"): continue
        
        if line.startswith("$ cd "):
            name = line.replace("$ cd ", "")
            if name == "..":
                current_node = find_parent(root, current_node)
            else:
                for node in current_node.children:
                    if node.name == name:
                        current_node = node
            continue
        
        if line.startswith("dir"):
            name = line.replace("dir ", "")
            current_node.children.append(Node.create_dir(name))
            continue
        
        data = line.split(" ")
        file_size = int(data[0])
        file_name = data[1]
        current_node.children.append(Node.create_file(file_name, file_size))
    
    return root

def main():
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
    
    root = parse(lines)
    
    candidates = [root]
    res = 0
    
    sizes = []
    while len(candidates) != 0:
        next = candidates.pop()
        
        if next.node_type != NodeType.FILE:
            if next.get_size() <= 100000:
                res += next.get_size()
            
            sizes.append(next.get_size())
        candidates.extend(next.children)
    
    print(f"Solution 1: {res}")
    
    FREE_SPACE = 70000000 - root.get_size()
    NEEDED_SPACE = 30000000
    diff = NEEDED_SPACE - FREE_SPACE
    for size in sorted(sizes):
        if size > diff:
            print(f"Solution 2: {size}")
            break
        
    
    

if __name__ == "__main__":
    main()