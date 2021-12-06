
def load_data():
    lines = []
    with open("data.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    return lines

def solve_1(data):
    return None

def solve_2(data):
    return None

def main():
    data = load_data()
    print(f"Solution 1: {solve_1(data)}")
    print(f"Solution 1: {solve_2(data)}")

if __name__ == "__main__":
    main()