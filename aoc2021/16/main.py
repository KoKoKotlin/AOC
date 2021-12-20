from functools import reduce

def load_data():
    lines = []
    with open("data.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    return lines

def read_bits(bits, length):
    result = int(bits[0:length], 2)
    bits = bits[length:]
    return result, bits

def read_literal(bytes_):
    last = False
    result = 0
    read_nums = 0
    while not last:
        bits, bytes_ = read_bits(bytes_, 5)
        result = (result << 4) + (bits & 0xF)
        last = not bits >> 4 
        read_nums += 1
    
    return result, bytes_

class Packet:
    def __init__(self, version, id_, subs = None, *, value=0):
        self.version = version
        self.id = id_
        self.value = value
        self.subs = subs
    
    def eval(self):
        values = None
        if self.id != 4: values = list(map(lambda x: x.eval(), self.subs))

        if self.id == 0:
            return sum(values)
        elif self.id == 1:
            return reduce(lambda x, y: x * y, values)
        elif self.id == 2:
            return min(values)
        elif self.id == 3:
            return max(values)
        elif self.id == 4:
            return self.value
        elif self.id == 5:
            return 1 if values[0] > values[1] else 0
        elif self.id == 6:
            return 1 if values[0] < values[1] else 0
        elif self.id == 7:
            return 1 if values[0] == values[1] else 0
    def __str__(self):
        return f"Packet[version: {self.version}, id: {self.id}, subs: {self.subs}, value: {self.value}]"
    
    def __repr__(self):
        return self.__str__()

def traverse_packets(packet):
    ps = [packet]
    result = 0

    while len(ps) > 0:
        current = ps.pop()

        if current.subs:
            ps.extend(current.subs)
        
        result += current.version

    return result

def read_packet(bytes_):
    version, bytes_ = read_bits(bytes_, 3)
    id_, bytes_ = read_bits(bytes_, 3)
    packets = None
    if id_ == 4:
        value, bytes_ = read_literal(bytes_)
        packet = Packet(version, 4, value=value)
    else:
        length_type_id, bytes_ = read_bits(bytes_, 1)
        length, bytes_ = read_bits(bytes_, 15 if length_type_id == 0 else 11)
        subs = []        
        if length_type_id == 0:
            start_len = len(bytes_)
            while start_len - len(bytes_) < length:
                packet, bytes_ = read_packet(bytes_)
                subs.append(packet)
        else:
            for _ in range(length):
                packet, bytes_ = read_packet(bytes_)
                subs.append(packet)

        packet = Packet(version, id_, subs)
    
    return packet, bytes_

def solve_1(data):
    bytes_ = ""
    
    line = data[0]

    for c in line:
        bits = "{0:b}".format(int(c, 16))
        bytes_ += "0" * (4 - len(bits)) + bits
    
    p, _ = read_packet(bytes_)
    
    return traverse_packets(p)

def solve_2(data):
    bytes_ = ""
    
    line = data[0]

    for c in line:
        bits = "{0:b}".format(int(c, 16))
        bytes_ += "0" * (4 - len(bits)) + bits
    
    p, _ = read_packet(bytes_)
    
    return p.eval() 


def main():
    data = load_data()
    print(f"Solution 1: {solve_1(data)}")
    print(f"Solution 1: {solve_2(data)}")

if __name__ == "__main__":
    main()
