# FILE = "test.txt"
FILE = "input.txt"

with open(FILE, "r") as f:
    BANKS = [line.strip() for line in f]

def sol1():
    sol = 0
    for bank in BANKS:
        max = 0
        for i in range(0, len(bank)):
            for j in range(i+1, len(bank)):
                joltage = int(bank[i] + bank[j])
                if joltage > max: max = joltage
        sol += max
    print("Solution 1:", sol)

def choose_next(subbank: str, digit: int, depth: int = 1) -> str:
    try: idx = subbank.index(str(digit))
    except: return None

    if depth == 12: return subbank[idx]
    
    digit = 9
    while (joltage := choose_next(subbank[idx+1:], digit, depth+1)) == None and digit > 0: digit -= 1
    if joltage == None: return None
    return subbank[idx] + joltage

def sol2():
    sol = 0
    for bank in BANKS:
        digit = 9
        while (joltage := choose_next(bank, digit)) == None and digit > 0: digit -= 1
        if joltage == None:
            print(bank)
            continue

        sol += int(joltage)
    print("Solution 2:", sol)

def main():
    sol1()
    sol2()

if __name__ == "__main__":
    main()