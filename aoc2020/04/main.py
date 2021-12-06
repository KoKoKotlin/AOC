from defaultlist import defaultlist
import re

def checkValidArguments(batch):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # , "cid"]
    return all(map(lambda x: x in batch, keys))

def checkSingleArgumentValid(name, value):
    if name == "byr":
        return len(value) == 4 and int(value) in range(1920, 2003)

    if name == "iyr":
        return len(value) == 4 and int(value) in range(2010, 2021)

    if name == "eyr":
        return len(value) == 4 and int(value) in range(2020, 2031)

    if name == "hgt":
        if "cm" in value:
            return int(value.replace("cm", "")) in range(150, 194)      
        elif "in" in value:
            return int(value.replace("in", "")) in range(59, 77)
        else: return False

    if name == "hcl":
        return len(value) == 7 and re.compile(r"^#[0-9a-f]+$").match(value)
        
    if name == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    if name == "pid":
        return len(value) == 9 and re.compile(r"^[0]*[0-9]+$").match(value)

    if name == "cid":
        return True
    
    return False

def checkValidData(batch):
    if not checkValidArguments(batch): return False

    pairs = list(map(lambda x: x.split(":"), batch.split(" ")[:-1]))
    return all(map(lambda pair: checkSingleArgumentValid(pair[0], pair[1]), pairs))

def main():
    batches = defaultlist(lambda: "")
    
    with open("data.txt", "r") as f:
        i = 0
        for line in f:
            line = line.strip()
            if line != "":
                batches[i] += line + " "
            else:
                i += 1
    
    valid = 0
    for batch in batches:
        valid += 1 if checkValidArguments(batch) else 0
    print("Valid number of argument batches: ", valid)

    valid = 0
    for batch in batches:
        valid += 1 if checkValidData(batch) else 0
    print("Valid data batches: ", valid)



if __name__ == "__main__":
    main()