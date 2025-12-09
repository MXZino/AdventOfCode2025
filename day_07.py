def prepare_puzzle(data: str):
    file = open(data, "r")
    content = file.read()
    file.close()

    rows = content.split("\n")

    return [list(row) for row in rows]

def get_part_one(puzzle_data):
    rows_count = len(puzzle_data)
    columns_count = len(puzzle_data[0])
    sum = 0

    for i in range(1, rows_count):
        for j in range(0, columns_count):
            if puzzle_data[i-1][j] == "S":
                puzzle_data[i][j] = "|"
            if puzzle_data[i - 1][j] == "|":
                if puzzle_data[i][j] != "^":
                    puzzle_data[i][j] = "|"
                else:
                    sum += 1
                    if j > 0 and puzzle_data[i][j-1] != "^":
                        puzzle_data[i][j-1] = "|"
                    if j < columns_count - 1 and puzzle_data[i][j+1] != "^":
                        puzzle_data[i][j+1] = "|"

    print("Sum " + str(sum))

def get_part_two(puzzle_data):
    rows_count = len(puzzle_data)
    columns_count = len(puzzle_data[0])

    for i in range(1, rows_count):
        for j in range(0, columns_count):
            if puzzle_data[i-1][j] == "S":
                puzzle_data[i][j] = "|"
            if puzzle_data[i - 1][j] == "|":
                if puzzle_data[i][j] != "^":
                    puzzle_data[i][j] = "|"
                else:
                    if j > 0 and puzzle_data[i][j-1] != "^":
                        puzzle_data[i][j-1] = "|"
                    if j < columns_count - 1 and puzzle_data[i][j+1] != "^":
                        puzzle_data[i][j+1] = "|"

    sum = 0

    for i in range(rows_count):
        if "^" in puzzle_data[i]:
            sum += puzzle_data[i].count("|")

    print("Sum " + str(sum))

prepared_puzzle = prepare_puzzle("puzzles/examples/day_07.txt")
print("Part one example:")
get_part_one(prepared_puzzle)
print("Part two example:")
get_part_two(prepared_puzzle)

prepared_puzzle = prepare_puzzle("puzzles/day_07.txt")
print("Part one:")
get_part_one(prepared_puzzle)
print("Part two:")
get_part_two(prepared_puzzle)