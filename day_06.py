def prepare_puzzle(data: str):
    file = open(data, "r")
    content = file.read()
    file.close()

    rows = content.split("\n")

    for i in range(len(rows)):
        rows[i] = rows[i].split(" ")
        rows[i] = [x for x in rows[i] if x != ""]

    return rows


def prepare_puzzle_part_two(data: str):
    file = open(data, "r")
    content = file.read()
    file.close()

    rows = content.split("\n")
    max_len = max(len(s) for s in rows)

    rows = [s.ljust(max_len) for s in rows]
    rows = [s.ljust(max_len, " ") for s in rows]
    rows_count = len(rows)
    previous_column_idx = -1

    prepared_puzzle = []

    columns_count = len(rows[0])
    for i in range(columns_count):
        empty_chars_count = 0

        for j in range(rows_count):
            if rows[j][i] == " ":
                empty_chars_count += 1

        if empty_chars_count == rows_count or i == columns_count - 1:
            if i == columns_count - 1:
                i = i + 1
            groups = []
            for a in range(rows_count):
                row_values = []
                for b in range(previous_column_idx + 1, i):
                    row_values.append(rows[a][b])
                groups.append(row_values)
            prepared_puzzle.append(groups)
            previous_column_idx = i

    return prepared_puzzle

def get_part_one(puzzle_data):
    sum = 0
    rows_count = len(puzzle_data)
    columns_count = len(puzzle_data[0])

    for column in range(columns_count):

        sign = puzzle_data[rows_count - 1][column]
        if sign == "*":
            partial_score = 1
        else:
            partial_score = 0

        for row in range(rows_count - 1):
            if sign == "*":
                partial_score = partial_score * int(puzzle_data[row][column])
            else:
                partial_score = partial_score + int(puzzle_data[row][column])

        sum += partial_score

    print("Sum " + str(sum))

def get_part_two(puzzle_data):
    sum = 0

    for group in puzzle_data:
        rows_size = len(group)
        sign = group[rows_size - 1][0]
        cols_size = len(group[0])

        if sign == "*":
            partial_score = 1
        else:
            partial_score = 0

        for i in range(cols_size, 0, -1):
            str_num = ""
            for j in range(rows_size - 1):
                value = group[j][i - 1]
                if value != " ":
                    str_num += value

            if sign == "*":
                partial_score = partial_score * int(str_num)
            else:
                partial_score = partial_score + int(str_num)

        sum += partial_score

    print("Sum " + str(sum))

prepared_puzzle = prepare_puzzle("puzzles/examples/day_06.txt")
print("Part one example:")
get_part_one(prepared_puzzle)
prepared_puzzle = prepare_puzzle_part_two("puzzles/examples/day_06.txt")
print("Part two example:")
get_part_two(prepared_puzzle)

prepared_puzzle = prepare_puzzle("puzzles/day_06.txt")
print("Part one:")
get_part_one(prepared_puzzle)
prepared_puzzle = prepare_puzzle_part_two("puzzles/day_06.txt")
print("Part two:")
get_part_two(prepared_puzzle)