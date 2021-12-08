
def load_data()
    file = File.open("data.txt")
    return file.read.split("\n")
end

def solve1(data)
    puts "Solution 1: #{0}\n"   
end

def solve2(data)
    puts "Solution 2: #{0}\n"
end

def main()
    data = load_data()
    solve1(data)
    solve2(data)
end

main()