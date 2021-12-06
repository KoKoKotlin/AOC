from pprint import pprint

def decode(id):   
    return [int("".join(list(map(lambda x: "0" if x == "F" else "1", id[0:7]))), 2),
    int("".join(list(map(lambda x: "0" if x == "L" else "1", id[7:]))), 2)]

def getId(parts):
    return parts[0] * 8 + parts[1]

def main():
    ids = []
    
    with open("data.txt", "r") as f:
        for line in f:
            ids.append(line.strip())

    ids = list(map(lambda x: getId(decode(x)), ids))
    
    for i in range(0b0000000, 0b1111111 + 1):
        for j in range(0b000, 0b111 + 1):
            seat_id = i * 8 + j
            if not (seat_id in ids) and ((seat_id + 1) in ids) and ((seat_id - 1) in ids):
                print("Your seat id:", seat_id, "row:", i, "col:", j)

if __name__ == "__main__":
    main()