from defaultlist import defaultlist
from functools import reduce
import string

def main():
    answers_combined = defaultlist(lambda: "")
    answers_extra = defaultlist(lambda: [])

    with open("data.txt", "r") as f:
        i = 0
        for line in f:
            line = line.strip()
            if line != "":
                answers_combined[i] += line
                answers_extra[i].append(set(line))
            else:
                i += 1
    
    # ored questions
    print("Sum of answers of each group (or):", reduce(
        lambda x, y: x + y, 
        map(lambda x: len(set(x)), answers_combined),
        0
    ))

    # and questions
    print("Sum of answers of each group (and):", 
        reduce(
            lambda x, y: x + len(y),
            map(lambda s: reduce(
                        lambda x, y: x.intersection(y),
                        s,
                        set(string.ascii_lowercase)
                      ), 
            answers_extra),
            0
        )
    )

if __name__ == "__main__":
    main()