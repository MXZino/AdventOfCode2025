import pandas as pd

def prepare_puzzle(data: str):
    puzzle = pd.read_csv(data, sep=" ", header=None)

    _prepared_puzzle = []

    for row in puzzle.values:
        direction = row[0][0]
        value = row[0][1:]
        _prepared_puzzle.append([direction, value])

    return _prepared_puzzle

def get_part_one(puzzle_data):
    score = 50
    password = 0

    for row in puzzle_data:
        direction = row[0]
        value = int(row[1]) % 100

        if direction == "R":
            score = (score + value) % 100

        if direction == "L":
            tmp = score - value
            if tmp < 0:
                score = tmp + 100
            else:
                score = tmp

        if score == 0:
            password += 1

    print("Password: " + str(password))

def get_part_two(puzzle_data):
    score = 50
    password = 0

    for row in puzzle_data:
        direction = row[0]
        value = int(row[1])
        tmp = score

        password += int(value / 100)
        value = value - int(value / 100) * 100

        if direction == "R":
            tmp += value

        if direction == "L":
            tmp -= value

        if (tmp <= 0 or tmp >= 100) and score != 0:
            password += 1

        score = tmp % 100

    print("Password: " + str(password))

prepared_puzzle = prepare_puzzle("puzzles/examples/day_01.txt")
print("Part one example:")
get_part_one(prepared_puzzle)
print("Part two example:")
get_part_two(prepared_puzzle)

prepared_puzzle = prepare_puzzle("puzzles/day_01.txt")
print("Part one:")
get_part_one(prepared_puzzle)
print("Part two:")
get_part_two(prepared_puzzle)

print("Ok")