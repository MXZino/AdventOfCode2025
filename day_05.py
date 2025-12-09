import numpy as np
import pandas as pd


def prepare_puzzle(data: str):
    file = open(data, "r")
    content = file.read()
    file.close()

    rows = content.split("\n")
    empty_line_idx = rows.index("")

    ranges = []
    for i in range(empty_line_idx):
        ranges.append(rows[i].split("-"))

    values = []
    for i in range(empty_line_idx + 1, len(rows)):
        values.append(rows[i])

    return ranges, values

def get_part_one(ranges, values):
    sum = 0

    for value in values:
        for i in ranges:
            if int(i[0]) <= int(value) <= int(i[1]):
                sum += 1
                break

    print("Sum " + str(sum))

def get_part_two(ranges):
    ranges = sorted(ranges, key=lambda x: int(x[0]))
    merged_ranges = [ranges[0]]

    for i in ranges:
        j = merged_ranges[len(merged_ranges)-1]
        if int(i[0]) > int(j[1]):
            merged_ranges.append([i[0], i[1]])
        elif int(i[0]) <= int(j[1]) <= int(i[1]):
            j[1] = i[1]
        elif int(i[0]) >= int(j[0]) and int(i[1]) <= int(j[1]):
            continue
        else:
            merged_ranges.append([i[0], i[1]])

    sum = 0

    for i in merged_ranges:
        sum += int(i[1]) - int(i[0]) + 1

    print("Unique ids: " + str(sum))

ranges, values = prepare_puzzle("puzzles/examples/day_05.txt")
print("Part one example:")
get_part_one(ranges, values)
print("Part two example:")
get_part_two(ranges)

ranges, values = prepare_puzzle("puzzles/day_05.txt")
print("Part one:")
get_part_one(ranges, values)
print("Part two:")
get_part_two(ranges)