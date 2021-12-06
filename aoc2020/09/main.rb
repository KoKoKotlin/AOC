
def load_data()
    file = File.open("data.txt")
    return file.read.split("\n")
end

def solve1(data)
    ints = data.map { |line| line.to_i } 
    
    current_idx = 25

    while current_idx < ints.length
        last_preamble = ints[(current_idx - 25)..(current_idx-1)]
        
        found = false
        for p1 in last_preamble
            num = ints[current_idx] - p1
            if num != p1 and last_preamble.include? num
                found = true
                break
            end
        end
        
        if !found     
            puts "Solution 1: #{ints[current_idx]}\n"
            return
        end

        current_idx += 1
    end
end

def solve2(data)
    ints = data.map { |line| line.to_i }     
    invalid_number = 27911108

    # find a contiguous set of numbers in the list ints that adds up to invalid_number
    # solution is the max + min of this set

    current_idx = 0
    offset = 0
    while current_idx < ints.length
        offset = 0
        residue = invalid_number
        while residue > 0
            residue -= ints[current_idx + offset]
            offset += 1
        end

        if residue == 0
            break
        end

        current_idx += 1
    end

    solution_set = ints[current_idx..(current_idx + offset)]

    puts "Solution 2: #{solution_set.max() + solution_set.min()}\n"
end

def main()
    data = load_data()
    solve1(data)
    solve2(data)
end

main()