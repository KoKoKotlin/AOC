from functools import cmp_to_key

class Num:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return str(self.value)

class List:
    def __init__(self, values):
        self.values = values
    
    def __repr__(self):
        return f"[" + ", ".join(map(repr, self.values)) + "]"
    
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, i):
        return self.values[i]

def parse(line):
    try:
        num = int(line)
        return Num(num)
    except:
        pass
    
    values = []
    curr = 1
    
    while curr < len(line) and line[curr] != "]":
        if line[curr] == "[":
            start = curr
            bracket_count = 1
            while bracket_count > 0:
                curr += 1
                if line[curr] == "]":
                    bracket_count -= 1
                elif line[curr] == "[":
                    bracket_count += 1

            curr += 1
            token = line[start:curr]
            values.append(parse(token))
        else:
            start = curr
            while line[curr] not in ["]", ","]:
                curr += 1
            token = line[start:curr]
            values.append(parse(token))
        curr += 1
    
    return List(values)

Eq = 0
Less = -1
Greater = 1

def compare(left, right):
    if isinstance(left, Num) and isinstance(right, Num):
        if left.value < right.value:
            return Less
        elif left.value == right.value:
            return Eq
        else:
            return Greater
    
    if isinstance(left, Num):
        return compare(List([left]), right)
    
    if isinstance(right, Num):
        return compare(left, List([right]))
    
    i = 0
    while True:
        if i == len(left) and i == len(right):
            return Eq
        elif i >= len(left) and i < len(right):
            return Less
        elif i >= len(right):
            return Greater
        else:
            left_elem = left[i]
            right_elem = right[i]
            res = compare(left_elem, right_elem)
            if res == Less:
                return Less
            elif res == Greater:
                return Greater

            i += 1
    
INPUT = "input.txt"
# INPUT = "test_input.txt"
        
def main():
    with open(INPUT, "r") as f:
        input = ""
        for line in f:
            input += line
    
    pairs = input.split("\n\n")
    pairs = list(map(lambda x: [parse(x.split("\n")[0]), parse(x.split("\n")[1])], pairs))    
    
    res = 0
    for idx, pair in enumerate(pairs):
        if compare(pair[0], pair[1]) == Less:
            res += idx + 1
    
    print(f"Solution 1: {res}")
    
    packets = list(map(parse, filter(lambda x: x.strip() != "", input.split("\n"))))
    packets.extend([parse("[[2]]"), parse("[[6]]")])
    
    sorted_packets = list(sorted(packets, key=cmp_to_key(compare)))
    res = 1
    for idx, packet in enumerate(sorted_packets):
        if repr(packet) in ["[[2]]", "[[6]]"]:
            res *= (idx + 1)
    print(f"Solution 2: {res}")

if __name__ == "__main__":
    main()
