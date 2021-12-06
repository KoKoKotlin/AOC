

def parseLine(line):
    parts = line.split(" ")
    
    nums = list(map(lambda x: int(x), parts[0].split("-")))
    letter = parts[1].replace(":", "")
    passw = parts[2]

    return [nums, letter, passw]

def checkValid1(num_range, letter, passw):
    num = 0
    for i in range(len(passw)):
        num += 1 if letter == passw[i] else 0

    return num in range(num_range[0], num_range[1] + 1)

def checkValid2(positions, letter, passw):
    return (passw[positions[0] - 1] == letter) ^ (passw[positions[1] - 1] == letter)

def main():

    valid = 0
    with open("pass.txt", "r") as f:
        for line in f:
            data = parseLine(line.strip())           
            # valid += 1 if checkValid1(data[0], data[1], data[2]) else 0
            valid += 1 if checkValid2(data[0], data[1], data[2]) else 0

    print(valid)

if __name__ == "__main__":
    main()