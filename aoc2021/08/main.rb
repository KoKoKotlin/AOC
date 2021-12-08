
def load_data()
    file = File.open("data.txt")
    return file.read.split("\n")
end

def solve1(data)
    res = data.map { |line| line.split("|")[1].split(" ").filter { |str| [2, 4, 3, 7].include? str.length } }.flatten().size
    puts "Solution 1: #{res}\n"   
end

# Indices for array:
#   000
#  1   2
#  1   2
#   333
#  4   5
#  4   5
#   666
def solve_one_segment(segment, output)
    chars = ['0', '0', '0', '0', '0', '0', '0']

    # unique sequences
    one   = segment.find { |seq| seq.length == 2 }
    four  = segment.find { |seq| seq.length == 4 }
    seven = segment.find { |seq| seq.length == 3 }
    eight = segment.find { |seq| seq.length == 7 }

    # seq. of length 5 and 6
    l6 = segment.filter { |seq| seq.length == 6 }
    
    # diff. between len 6 
    six = l6.filter { |seq| one.include?((eight - seq)[0]) }[0]
    l6 = l6 - [six]
    nine = l6.filter { |seq| (seq - four).length == 2 }[0]
    zero = l6.filter { |seq| (seq - four).length == 3 }[0]
    ######

    chars[0] = (seven - one)[0]
    chars[2] = (eight - six)[0]
    chars[3] = (eight - zero)[0]
    chars[4] = (eight - nine)[0]
    chars[5] = (one - [chars[2]])[0]
    chars[6] = ((nine - seven) - four)[0]
    chars[1] = (["a", "b", "c", "d", "e", "f", "g"] - chars)[0]
    
    #puts "#{chars} #{chars.uniq().length}\n"
    
    return output.map { |seq| seqToNumber(seq, chars) } 
end

def seqToNumber(seq, chars)
    indices = [ [0, 1, 2, 4, 5, 6],         # 0
                [2, 5],                     # 1
                [0, 2, 3, 4, 6],            # 2
                [0, 2, 3, 5, 6],            # 3
                [1, 2, 3, 5],               # 4
                [0, 1, 3, 5, 6],            # 5
                [0, 1, 3, 4, 5, 6],         # 6
                [0, 2, 5],                  # 7
                [0, 1, 2, 3, 4, 5, 6],      # 8
                [0, 1, 2, 3, 5, 6]          # 9
            ]
    seq1 = seq.map { |c| chars.find_index(c) }
    return indices.find_index(seq1.sort)
end

def solve2(data)
    data = data.map { |line| line.split("|").map { |s| s.split(" ").map { |s1| s1.chars } }  }

    output = 0
    for d in data
        res = solve_one_segment(d[0], d[1])
        
        num = 0
        res.each_with_index do |elem, index|
            num += elem * (10 ** (res.length - index - 1)) 
        end

        output += num
    end

    puts "Solution 2: #{output}\n"
end

def main()
    data = load_data()
    solve1(data)
    solve2(data)
end

main()