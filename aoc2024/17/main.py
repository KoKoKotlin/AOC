import time
import random

#FILE = "test.txt"
FILE = "data.txt"

def combo(A, B, C, operand):
    if operand < 4: return operand
    elif operand == 4: return A
    elif operand == 5: return B
    elif operand == 6: return C
    elif operand == 7:
        print("Invalid program. Combo 7")
        exit(-1)

def itos(i, o, A, B, C, pc):
    match i:
        case 0: return "ADV " + otos(o, A, B, C)
        case 1: return "BXL " + str(o)
        case 2: return "BST " + otos(o, A, B, C)
        case 3: return f"JNZ pc=" + str(o)
        case 4: return "BXC"
        case 5: return "OUT " + otos(o, A, B, C)
        case 6: return "BDV " + otos(o, A, B, C)
        case 7: return "CDV " + otos(o, A, B, C)

def otos(i, A, B, C):
    match i:
        case 0: return "0"
        case 1: return "1"
        case 2: return "2"
        case 3: return "3"
        case 4: return f"A={A}"
        case 5: return f"B={B}"
        case 6: return f"C={C}"
        case 7: return "RES"

def sol1(A, B, C, program):
    pc = 0
    out = []
    while pc < len(program):
        opcode = program[pc]
        operand = program[pc+1]

        match opcode:
            case 0: #adv combo
                A = A//(2**combo(A, B, C, operand))
            case 1: #bxl literal
                B = B ^ operand
            case 2: #bst combo
                B = combo(A, B, C, operand) % 8
            case 3: #jnz literal
                if A != 0:
                    pc = operand-2
            case 4: #bxc -
                B = B ^ C
            case 5: #out combo
                out.append(str(combo(A, B, C, operand) % 8))
            case 6: #bdv combo
                B = A//(2**combo(A, B, C, operand))
            case 7: #cdv combo
                C = A//(2**combo(A, B, C, operand))
            case _:
                print("Unknown opcode:", opcode)
                exit(-1)
        pc += 2
    print("Solution 1:", ",".join(out))

def solve1(A, B, C, program):
    pc = 0
    out = []
    while pc < len(program):
        opcode = program[pc]
        operand = program[pc+1]

        match opcode:
            case 0: #adv combo
                A = A//(2**combo(A, B, C, operand))
            case 1: #bxl literal
                B = B ^ operand
            case 2: #bst combo
                B = combo(A, B, C, operand) % 8
            case 3: #jnz literal
                if A != 0:
                    pc = operand-2
            case 4: #bxc -
                B = B ^ C
            case 5: #out combo
                out.append(str(combo(A, B, C, operand) % 8))
            case 6: #bdv combo
                B = A//(2**combo(A, B, C, operand))
            case 7: #cdv combo
                C = A//(2**combo(A, B, C, operand))
            case _:
                print("Unknown opcode:", opcode)
                exit(-1)
        pc += 2
    return out

def solve2(A):
    out = []
    while A > 0:
        tmp = (A % 8) ^ 1
        B = tmp ^ (A // (2**tmp)) ^ 4
        A = A//8
        out.append(str(B % 8))
    return out

def sol2(program):
    prog = ",".join(str(c) for c in program)
    digits = [str(c) for c in range(10)]
    while True:
        candidate = ""
        for i in range(14):
            candidate += random.choice(digits)
        A = int("".join(candidate))

        print(A, out:=solve2(A)) 
        if ",".join(out) == prog:
            break
    print("Solution 2:", A)

def main():
    with open(FILE, "r") as f:
        A = int(next(f).split(":")[1].strip())
        B = int(next(f).split(":")[1].strip())
        C = int(next(f).split(":")[1].strip())
        next(f)
        program = list(map(int, next(f).split(":")[1].strip().split(",")))
    sol1(A, B, C, program)
    sol2(program)
       
if __name__ == "__main__":
    main()
