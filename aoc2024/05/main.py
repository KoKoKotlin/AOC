# FILE = "test.txt"
FILE = "data.txt"

from collections import defaultdict
from copy import deepcopy
from functools import cmp_to_key

def parse_input(lines):
    parse_rules = True
    rules = defaultdict(lambda: deepcopy([]))
    updates = []

    for line in lines:
        if line.isspace():
            parse_rules = False
            continue
        if parse_rules:
            nums = list(map(int, line.split("|")))
            rules[nums[0]].append(nums[1])
        else:
            updates.append(list(map(int, line.split(","))))
    return rules, updates

def check_update(update, rules):
    for idx, num in enumerate(update):
        nums_after = rules.get(num, [])
        if not all(map(lambda x: x not in update or idx < update.index(x), nums_after)): return False
    return True

def sol1(rules, updates):
    res = 0
    for update in updates:
        res += update[len(update)//2] if check_update(update, rules) else 0
    print("Solution 1:", res)

def cmp(rules, v1, v2):
    if v1 == v2: return 0
    return -1 if v2 in rules[v1] else 1

def sol2(rules, updates):
    res = 0
    for update in updates:
        if not check_update(update, rules):
            update = list(sorted(update, key=cmp_to_key(lambda v1, v2: cmp(rules, v1, v2))))
            res += update[len(update)//2]
    print("Solution 2:", res)

def main():
    with open(FILE, "r") as f:
        rules, updates = parse_input([line for line in f])
    sol1(rules, updates)
    sol2(rules, updates)

if __name__ == "__main__":
    main()
