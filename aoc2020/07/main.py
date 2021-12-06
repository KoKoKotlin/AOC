from pprint import pprint

def parse_rules(rules):
    rules = list(map(lambda x: x.replace("contain ", ":").replace("bags", "").replace("bag", "").replace(".", ""), rules))
    
    parsed_rules = dict()
    for i, rule in enumerate(rules): 
        rule = rule.split(":")

        if "no other" in rule[1]:
            parsed_rules[rule[0].strip()] = []
        else:
            rule[1] = list(map(lambda x: x.strip(), rule[1].split(",")))
            rule[1] = list(map(lambda x: [int(x[0]), x[2:]], rule[1]))
            parsed_rules[rule[0].strip()] = rule[1]
        
    return parsed_rules

def findColors(color, rules):
    result = []
    for key, value in rules.items():
        for item in value:
            if item[1] == color:
                result.append([key, item[0]])
    
    return result

def numberContainedBags(color, rules):
    bags = rules[color]

    res = 1
    for bag in bags:
        res += bag[0] * numberContainedBags(bag[1], rules)

    return res

def main():
    rules = []
    
    with open("rules.txt", "r") as f:
        for line in f:
            rules.append(line.strip())
    
    rules = parse_rules(rules)

    colors = ["shiny gold"]
    found = []

    while len(colors) > 0:
        search = colors.pop()
        res = findColors(search, rules)
        for val in res: 
            color, num = val
            found.append(color)
            colors.append(color)

    print(f"Your bag could be in other bags with {len(set(found))} color!")

    print(f"The shiny gold bag must contain {numberContainedBags('shiny gold', rules) - 1} other bags!")

if __name__ == "__main__":
    main()