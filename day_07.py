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


class Peak:
    def __init__(self):
        self.children = []

def get_part_two(puzzle_data):
    columns = len(puzzle_data[0])
    rows = len(puzzle_data)

    s_position = puzzle_data[0].index('S')

    starting_peak = Peak()

    node_cache = {}

    def move_ray(row_index, column_index, parent_peak):
        if column_index < 0 or column_index >= columns:
            return

        if row_index >= rows:
            state = (row_index, column_index)
            if state not in node_cache:
                node_cache[state] = Peak()
            parent_peak.children.append(node_cache[state])
            return

        char = puzzle_data[row_index][column_index]

        if char == "^":
            state = (row_index, column_index)
            if state not in node_cache:
                peak = Peak()
                node_cache[state] = peak

                move_ray(row_index + 1, column_index - 1, peak)
                move_ray(row_index + 1, column_index + 1, peak)

            parent_peak.children.append(node_cache[state])
        else:
            move_ray(row_index + 1, column_index, parent_peak)

    move_ray(1, s_position, starting_peak)

    memo_count = {}

    def count_ways(peak):
        if peak in memo_count:
            return memo_count[peak]

        if not peak.children:
            return 1

        total = 0
        for child in peak.children:
            total += count_ways(child)

        memo_count[peak] = total
        return total

    result = count_ways(starting_peak)
    print("Result " + str(result))

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