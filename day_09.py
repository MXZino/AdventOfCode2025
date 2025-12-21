class Corner:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def prepare_puzzle(data: str):
    corners = []
    with open(data, 'r') as f:
        content = f.read()
        lines = content.strip().split('\n')

        for line in lines:
            parts = line.strip().split(',')
            corner = Corner(int(parts[0]), int(parts[1]))
            corners.append(corner)

    return corners


def get_part_one(corners):
    max_area = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            a = corners[i]
            b = corners[j]
            area = (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)
            max_area = max(max_area, area)

    print("Result " + str(max_area))


corners = prepare_puzzle("puzzles/examples/day_09.txt")
print("Part one example:")
get_part_one(corners)

corners = prepare_puzzle("puzzles/day_09.txt")
print("Part one:")
get_part_one(corners)
