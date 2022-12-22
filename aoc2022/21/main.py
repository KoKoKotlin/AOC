from copy import deepcopy

INPUT = "input.txt"
# INPUT = "test_input.txt"

def parse(lines):
    monkeys = {}
    
    for line in lines:
        if any(map(lambda x: x in line, ["+", "-", "*", "/"])):
            data = line.split(":")
            data[1] = data[1].strip()
            monkeys[data[0]] = [data[1][0:4], data[1][7:], data[1][5]]
        else:
            data = line.split(":")
            monkeys[data[0]] = int(data[1].strip())
    return monkeys


    return equations, list(set(symbols))

def solve1(monkeys):
    while True:
        for (key, value) in monkeys.items():
            if isinstance(value, int):
                if key == "root": return value
                else: continue
            
            value1 = monkeys[value[0]]
            value2 = monkeys[value[1]]
            
            if isinstance(value1, int) and isinstance(value2, int):
                monkeys[key] = int(eval(f"{value1} {value[2]} {value2}"))

def get_div(humn, monkeys, target1, target2):
    monkeys["humn"] = humn
    
    while True:
        dirty = False        
        for (key, value) in monkeys.items():
            if isinstance(value, int): continue

            value1 = monkeys[value[0]]
            value2 = monkeys[value[1]]
            
            if isinstance(value1, int) and isinstance(value2, int):
                dirty = True
                monkeys[key] = int(eval(f"{value1} {value[2]} {value2}"))

        if not dirty:
            break
    
    return monkeys[target1] - monkeys[target2]

def solve2(monkeys):
    target1, target2 = monkeys["root"][0], monkeys["root"][1]
    del monkeys["root"]
    del monkeys["humn"]
    
    i = 0
    while i < 10000:
        i += 1
        for (key, value) in monkeys.items():
            if isinstance(value, int):
                if key == "root": return value
                else: continue

            if value[0] == "humn" or value[1] == "humn":
                continue
            
            value1 = monkeys[value[0]]
            value2 = monkeys[value[1]]
            
            if isinstance(value1, int) and isinstance(value2, int):
                monkeys[key] = int(eval(f"{value1} {value[2]} {value2}"))
    
    humn = 0    
    while True:
        div = get_div(humn, deepcopy(monkeys), target1, target2)
        
        if div == 0:
            return humn
        
        if div > 100:
            humn += int(div / 100)
        else:
            humn += int(div / abs(div))
            
def main():
    with open(INPUT, "r") as f:
        lines = [line.strip() for line in f]
    
    monkeys = parse(lines)   
    print(f"Solution 1: {solve1(deepcopy(monkeys))}") 
    print(f"Solution 2: {solve2(monkeys)}") 

if __name__ == "__main__":
    main()