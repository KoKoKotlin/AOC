from dataclasses import dataclass
from copy import deepcopy

FILE = "test.txt"
FILE = "data.txt"

def sol1(nums):
    res = 0
    frepr = []
    isfile = True
    for idx, n in enumerate(nums):
        if isfile:
            frepr += [str(idx//2)] * n
        else:
            frepr += ["."] * n
        isfile = not isfile
    
    for i in range(len(frepr)):
        idx = len(frepr) - 1 - i
        to_idx = frepr.index(".")
        if idx < to_idx: break

        frepr[to_idx] = frepr[idx]
        frepr[idx] = "."

    for idx, c in enumerate(frepr):
        if c == ".": break
        res += idx * int(c)
    print("Solution 1:", res)

@dataclass
class File:
    start: int
    end: int
    length: int
    file_id: int
    moved: bool

def search_gap(files, start):
    for i in range(len(files)-1):
        if files[i].end >= start and files[i].end != files[i+1].start - 1:
            return (i, files[i].end + 1, files[i+1].start - files[i].end - 1)
    return None, None, None

def get_next(files):
    for i in range(len(files)):
        idx = len(files) - i - 1
        if not files[idx].moved: return idx
    return None

def ltorepri(files):
    frepr = []
    last_end = 0
    for f in files:
        if f.start != last_end + 1:
            frepr += [0] * (f.start - last_end - 1)
        frepr += [f.file_id] * f.length
        last_end = f.end
    return frepr

def sol2(nums):
    res = 0
    files = []
    isfile = True
    start = 0
    for idx, n in enumerate(nums):
        if isfile:
            files.append(File(start, start+n-1, n, idx//2, False))
        start += n
        isfile = not isfile

    while True:
        idx = get_next(files)
        if idx is None: break

        i, gap_start, gap_len = search_gap(files, 0)
        while gap_len is not None and gap_len < files[idx].length:
            i, gap_start, gap_len = search_gap(files, gap_start+1)
            
        if gap_start is None or gap_start > files[idx].start:
            files[idx].moved = True
            continue
        
        files[idx].start = gap_start
        files[idx].end = files[idx].start + files[idx].length - 1
        files[idx].moved = True
        files.insert(i+1, files[idx])
        del files[idx+1]

    for idx, c in enumerate(ltorepri(files)):
        res += idx * c

    print("Solution 2:", res)

def main():
    with open(FILE, "r") as f:
        nums = list(map(int, next(f).strip()))
    sol1(nums) 
    sol2(nums) 

if __name__ == "__main__":
    main()
