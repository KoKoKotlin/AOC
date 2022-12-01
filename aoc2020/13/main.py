from scipy.optimize import root

INPUT = "src/input.txt"
INPUT = "src/test_input.txt"

def read_input(input):
    with open(input) as f:
        data = f.readlines()[1]
        return list(map(lambda x: [int(x[0]), int(x[0]) - (x[1] % int(x[0]))], filter(lambda x: x[0] != "x", zip(data.split(","), range(len(data.split(",")))))))
        

def scalar_prod(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res
 
def next_conf(coeffs, coeff_max):
    i = 0
    while i < len(coeffs):
        coeffs[i] += 1
        if coeffs[i] > coeff_max:
            coeffs[i] = 1
            i += 1
        else:
            return coeffs
    
    return None
def main():
    data = read_input(INPUT)
    values = [data[i][0] for i in range(len(data))]
    coeffs = [1 for _ in range(len(data))]
    def f(coeffs, data):
        def g(x):
            sum = 0
            product = 1
            for i in range(len(data)):
                sum += data[i][0] * coeffs[0]
                product *= x - data[i][1]
            return product - sum
        return g
    
    
    initial_guess = (scalar_prod(values, coeffs)) ** (1/5)
    MAX = 10
    while True:
        coeffs = next_conf(coeffs, MAX)
        if not coeffs:
            break
        
        print(root(f(coeffs, data), initial_guess)["x"])
    
if __name__ == "__main__":
    main()
