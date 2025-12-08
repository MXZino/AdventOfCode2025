def prepare_puzzle(data: str):
    file = open(data, "r")
    content = file.read()
    file.close()

    _prepared_puzzle = []

    ranges = content.split(",")
    for item in ranges:
        idx = item.split("-")
        _prepared_puzzle.append([idx[0], idx[1]])

    return _prepared_puzzle

def get_part_one(puzzle_data):
    sum = 0
    for row in puzzle_data:
        num = int(row[0])
        end = int(row[1])
        while num <= end:
            num_str = str(num)
            str_len = len(num_str)
            if str_len % 2 == 0:
                half = str_len // 2
                ok = True
                for i in range(half):
                    if num_str[i] != num_str[half + i]:
                        ok = False
                        break
                if ok:
                    sum += num
            num += 1
    print("Sum " + str(sum))

def get_part_two(puzzle_data):
    sum = 0
    for row in puzzle_data:
        num = int(row[0])
        end = int(row[1])
        while num <= end:
            num_str = str(num)
            str_len = len(num_str)
            half = str_len // 2
            for i in range(half):
                ok = True
                if str_len % (i +1) != 0:
                    continue
                substr = num_str[0 : i+1]
                substr_len = len(substr)
                compares = str_len // substr_len - 1
                for comp in range(compares):
                    start_idx = (comp+1) * substr_len
                    end_idx = (comp+2) * substr_len
                    to_compare = num_str[start_idx:end_idx]
                    if substr != to_compare:
                        ok = False
                        break

                if ok:
                    sum += num
                    break

            num += 1

    print("Sum " + str(sum))

prepared_puzzle = prepare_puzzle("puzzles/examples/day_02.txt")
print("Part one example:")
get_part_one(prepared_puzzle)
print("Part two example:")
get_part_two(prepared_puzzle)

prepared_puzzle = prepare_puzzle("puzzles/day_02.txt")
print("Part one:")
get_part_one(prepared_puzzle)
print("Part two:")
get_part_two(prepared_puzzle)
print("Ok")
