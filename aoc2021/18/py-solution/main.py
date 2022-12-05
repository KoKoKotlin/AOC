from math import ceil, floor
import sys

class Leaf:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
    
    def __repr__(self):
        return f"{self.value}"

class Node:
    def __init__(self, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent
    
    def __repr__(self):
        return f"[{self.left},{self.right}]"

def add(left, right):
    node = Node(left, right, None)
    left.parent = node
    right.parent = node
    
    while reduce(node): pass    
    
    return node

def reduce(root):
    stack = [root]
    while len(stack) != 0:
        current = stack.pop(0)
        
        if explode(current): 
            print(root, "\t\t\texplode")
            return True
        
        if isinstance(current, Node):
            stack.insert(0, current.right)
            stack.insert(0, current.left)
    
    stack = [root]
    while len(stack) != 0:
        current = stack.pop(0)
        if split(current): 
            print(root, "\t\t\tsplit")
            return True
        
        if isinstance(current, Node):
            stack.insert(0, current.right)
            stack.insert(0, current.left)

    return False  

class Dir:
    LEFT = 0
    RIGHT = 1

def get_child_pointer(node, parent):
    if parent.left == node:
        return Dir.LEFT
    elif parent.right == node:
        return Dir.RIGHT
    else:
        print("parent check failed!")
        exit(-1)    

def split(node):
    if not isinstance(node, Leaf):
        return False
    
    if node.value >= 10:
        parent = node.parent
        if get_child_pointer(node, parent) == Dir.LEFT:
            parent.left = Node(Leaf(floor(node.value / 2), None), Leaf(ceil(node.value / 2), None), parent)
            parent.left.left.parent = parent.left
            parent.left.right.parent = parent.left
        else:
            parent.right = Node(Leaf(floor(node.value / 2), None), Leaf(ceil(node.value / 2), None), parent)
            parent.right.left.parent = parent.right
            parent.right.right.parent = parent.right
            
        return True

    return False

def explode_left(value, node):
    next = node.parent
    dir = get_child_pointer(node, next)
    
    while dir == Dir.LEFT:
        if next.parent == None:
            return

        dir = get_child_pointer(next, next.parent)
        next = next.parent
    
    current = next.left
    while isinstance(current, Node): 
        current = current.right 
    
    current.value += value

def explode_right(value, node):
    next = node.parent
    dir = get_child_pointer(node, next)
    
    while dir == Dir.RIGHT:
        if next.parent == None:
            return

        dir = get_child_pointer(next, next.parent)
        next = next.parent
    
    current = next.right
    while isinstance(current, Node): 
        current = current.left
    
    current.value += value
    
def explode(node):
    if not isinstance(node, Node):
        return False
        
    if get_level(node) != 4:
        return False

    if not isinstance(node.left, Leaf) or not isinstance(node.right, Leaf):
        return False
    
    left_value = node.left.value
    right_value = node.right.value
    parent = node.parent
    
    explode_left(left_value, node)
    explode_right(right_value, node)
    
    if get_child_pointer(node, parent) == Dir.LEFT:
        parent.left = Leaf(0, parent)
    else:
        parent.right = Leaf(0, parent)
        
    return True

def get_level(node):
    level = 0
    while True:
        if node.parent == None:
            return level
        node = node.parent
        level += 1

def parse(line, parent = None):
    try:
        value = int(line)
        return Leaf(value, parent)
    except:
        pass
    
    s = line[1:-1]    
    counter = 0
    for (idx, c) in enumerate(s):
        if c == "[": counter += 1
        elif c == "]": counter -= 1
        elif counter == 0 and c == ",": break
    
    node = Node(parse(s[:idx]), parse(s[idx+1:]), parent)    
    node.left.parent = node
    node.right.parent = node
    
    return node        
        
def parse_line(line):
    root = parse(line)
    
    return root

def magnitude(node):
    if isinstance(node, Node):
        return 3 * magnitude(node.left) + 2 * magnitude(node.right) 
    else:
        return node.value

INPUT = "input.txt"
# INPUT = "test_input.txt"
def main():
    nums = []
    with open(INPUT, "r") as f:
        for line in f:
            nums.append(parse_line(line.strip()))
    
    res = nums[0]
    for i in range(1, len(nums)):
        res = add(res, nums[i])
        print(res, file=sys.stderr)
    print(res)
    print("Magnitude:", magnitude(res))

if __name__ == "__main__":
    main()
