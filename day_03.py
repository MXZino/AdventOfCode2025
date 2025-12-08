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

        size = len(arr)
        max_num = arr[-12:]
        max_val = 0

        for i in range(size - 12, 0, -1):
            nums_to_compare = []
            for j in range(0, 12, 1):
                new_number = np.append(np.append(max_num[:j], arr[i-1]),  max_num[j:])[:12]
                nums_to_compare.append(int("".join(map(str, new_number))))
                tmp = max_num.copy() #[j] = arr[i-1]
                tmp[j] = arr[i-1]
                nums_to_compare.append(int("".join(map(str, tmp))))

            max_val = max(nums_to_compare)
            max_num = np.array([int(c) for c in str(max_val)])


        print(max_val)
        sum += max_val

    print("Sum " + str(sum))


prepared_puzzle = prepare_puzzle("puzzles/examples/day_03.txt")
print("Part one example:")
get_part_one(prepared_puzzle)
print("Part two example:")
get_part_two(prepared_puzzle)

# prepared_puzzle = prepare_puzzle("puzzles/day_03.txt")
# print("Part one:")
# get_part_one(prepared_puzzle)
