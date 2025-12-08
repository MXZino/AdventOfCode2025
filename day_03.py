import pandas as pd
import numpy as np
from numpy.ma.core import max_val


def prepare_puzzle(data: str):
    file = pd.read_csv(data, sep=" ", header=None)

    _prepared_puzzle = []

    for row in file.values:
        _prepared_puzzle.append(row[0])

    return _prepared_puzzle


def get_part_one(puzzle_data):
    sum = 0
    for row in puzzle_data:
        arr = np.array([int(c) for c in str(row)])

        nums = []

        for i in range(len(arr)):
            if len(nums) < 2:
                nums.append(arr[i])
                continue

            first_compare = int(str(nums[0]) + str(arr[i]))
            second_compare = int(str(nums[1]) + str(arr[i]))
            number_arr = int(str(nums[0]) + str(nums[1]))
            max_num = max([first_compare, second_compare, number_arr])
            nums = [int(c) for c in str(max_num)]

        num = int(str(nums[0]) + str(nums[1]))
        sum += num
        print(num)

    print("Sum " + str(sum))


def get_part_two(puzzle_data):
    sum = 0
    for row in puzzle_data:
        arr = np.array([int(c) for c in str(row)])

        start_idx = 0
        num = ""
        for i in range(12, 0, -1):
            for j in range(9, 0, -1):
                success = False
                for k in range(0, len(arr) - i - start_idx +1, 1):
                    if arr[k+start_idx] == j:
                        num += str(j)
                        start_idx = start_idx + k +1
                        # print(num)
                        success = True
                        break
                if success:
                    break

        print(num)
        sum+=int(num)

    print("Sum " + str(sum))


prepared_puzzle = prepare_puzzle("puzzles/examples/day_03.txt")
print("Part one example:")
get_part_one(prepared_puzzle)
print("Part two example:")
get_part_two(prepared_puzzle)

prepared_puzzle = prepare_puzzle("puzzles/day_03.txt")
print("Part one:")
get_part_one(prepared_puzzle)
print("Part two:")
get_part_two(prepared_puzzle)
