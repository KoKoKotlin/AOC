from sympy import symbols, Eq, solve
from typing import List
from dataclasses import dataclass

# FILE = "test.txt"
FILE = "data.txt"

def sol1(games):
    res = 0
    for game in games:
        k, n = symbols("k n", integer=True)
        eq1 = Eq(game.A[0]*k + game.B[0]*n, game.goal[0])
        eq2 = Eq(game.A[1]*k + game.B[1]*n, game.goal[1])
        solutions = solve((eq1, eq2), (k, n), dict=True)
        if len(solutions) > 0:
            res += min(3*sol[k] + 1*sol[n] for sol in solutions)
    print("Solution 1:", res)

def sol2(games):
    res = 0
    for game in games:
        k, n = symbols("k n", integer=True)
        eq1 = Eq(game.A[0]*k + game.B[0]*n, 10000000000000 + game.goal[0])
        eq2 = Eq(game.A[1]*k + game.B[1]*n, 10000000000000 + game.goal[1])
        solutions = solve((eq1, eq2), (k, n), dict=True)
        if len(solutions) > 0:
            res += min(3*sol[k] + 1*sol[n] for sol in solutions)
    print("Solution 2:", res)

@dataclass
class Game:
    A: List[int]
    B: List[int]
    goal: List[int]

def main():
    with open(FILE, "r") as f:
        i = 0
        games = []
        A, B, goal = None, None, None
        for line in f:
            if i == 3:
                i = 0
                continue

            line = line.strip()
            data = line.split(":")[1].split(",")
            if i == 0 or i == 1:
                nums = list(map(lambda x: int(x.split("+")[1]), data))
                if i == 0: A = nums
                if i == 1: B = nums
            elif i == 2:
                nums = list(map(lambda x: int(x.split("=")[1]), data))
                goal = nums
                games.append(Game(A, B, goal))
            i += 1
    sol1(games)
    sol2(games)

if __name__ == "__main__":
    main()
