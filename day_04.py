import numpy as np
import pandas as pd


def prepare_puzzle(data: str):
    file = pd.read_csv(data, sep=" ", header=None)

    _prepared_puzzle = []

    for row in file.values:
        row = np.array([c for c in str(row[0])])
        _prepared_puzzle.append(row)

    return _prepared_puzzle


def has_access_to_field(index, total_fields):
    return 0 <= index < total_fields


def get_part_one(puzzle_data):
    sum = 0
    rows_count = len(puzzle_data)
    columns_count = len(puzzle_data[0])

    for row in range(rows_count):
        for col in range(columns_count):
            if puzzle_data[row][col] != "@":
                continue
            paper_count = 0
            for adjacent_row in range(-1, 2, 1):
                for adjacent_col in range(-1, 2, 1):
                    if adjacent_row == 0 and adjacent_col == 0:
                        continue
                    if has_access_to_field(row + adjacent_row, rows_count) and has_access_to_field(col + adjacent_col,
                                                                                                   columns_count):
                        if puzzle_data[row + adjacent_row][col + adjacent_col] == "@":
                            paper_count += 1

            if paper_count <= 3:
                sum += 1

    print("Sum " + str(sum))


def get_part_two(puzzle_data):
    sum = 0
    rows_count = len(puzzle_data)
    columns_count = len(puzzle_data[0])

    while True:
        to_remove = []
        for row in range(rows_count):
            for col in range(columns_count):
                if puzzle_data[row][col] != "@":
                    continue
                paper_count = 0
                for adjacent_row in range(-1, 2, 1):
                    for adjacent_col in range(-1, 2, 1):
                        if adjacent_row == 0 and adjacent_col == 0:
                            continue
                        if has_access_to_field(row + adjacent_row, rows_count) and has_access_to_field(
                                col + adjacent_col,
                                columns_count):
                            if puzzle_data[row + adjacent_row][col + adjacent_col] == "@":
                                paper_count += 1

                if paper_count <= 3:
                    to_remove.append((row, col))
                    sum += 1

        for row, col in to_remove:
            puzzle_data[row][col] = "."

        if len(to_remove) == 0:
            break

    print("Sum " + str(sum))


prepared_puzzle = prepare_puzzle("puzzles/examples/day_04.txt")
print("Part one example:")
get_part_one(prepared_puzzle)
print("Part two example:")
get_part_two(prepared_puzzle)

prepared_puzzle = prepare_puzzle("puzzles/day_04.txt")
print("Part one:")
get_part_one(prepared_puzzle)
print("Part two:")
get_part_two(prepared_puzzle)
