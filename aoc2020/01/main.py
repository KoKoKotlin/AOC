

def main():
    nums = []
    
    with open("nums.txt", "r") as f:
        for line in f:
            nums.append(int(line))

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020: print(nums[i], nums[j], nums[k], nums[i] * nums[j] * nums[k])

if __name__ == "__main__":
    main()