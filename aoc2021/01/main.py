
def load_data():
    lines = []
    with open("data.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    return lines

def solve_1(data):
    data_int = list(map(int, data))
    return len(list(filter(lambda x: x > 0, map(lambda t: t[1] - t[0], zip(data_int[0:len(data_int) - 1], data_int[1:])))))

def solve_2(data):
    data_int = list(map(int, data))
    clustered_data = [sum(data_int[i:i+3]) for i in range(len(data_int) - 2)]
    return len(list(filter(lambda x: x > 0, map(lambda t: t[1] - t[0], zip(clustered_data[0:len(clustered_data) - 1], clustered_data[1:])))))


def main():
    data = load_data()
    print(f"Solution 1: {solve_1(data)}")
    print(f"Solution 1: {solve_2(data)}")

if __name__ == "__main__":
    main()