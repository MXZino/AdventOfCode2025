import math


class Circuit:
    def __init__(self, boxes=None):
        if boxes is None:
            self.boxes = set()
        else:
            self.boxes = set(boxes)


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.connected_boxes = []
        self.circuit = Circuit({self})

    def calculate_distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def connect_to(self, other):
        self.connected_boxes.append(other)


def prepare_puzzle(data: str):
    with open(data, 'r') as f:
        content = f.read()

    lines = content.strip().split('\n')
    boxes = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 3:
            boxes.append(Box(int(parts[0]), int(parts[1]), int(parts[2])))
    return boxes


def get_sorted_distances(boxes):
    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            b1 = boxes[i]
            b2 = boxes[j]
            dist = b1.calculate_distance_to(b2)
            distances.append((b1, b2, dist))

    distances.sort(key=lambda x: x[2])
    return distances


def get_part_one(boxes, pairs):
    sorted_distances = get_sorted_distances(boxes)

    for i in range(min(pairs, len(sorted_distances))):
        b1, b2, _ = sorted_distances[i]

        if b2 in b1.circuit.boxes:
            continue

        b1.connect_to(b2)
        b2.connect_to(b1)

        new_boxes = b1.circuit.boxes.union(b2.circuit.boxes)
        new_circuit = Circuit(new_boxes)

        for b in new_boxes:
            b.circuit = new_circuit

    unique_circuits = {id(b.circuit): b.circuit for b in boxes}.values()
    sorted_circuits = sorted(unique_circuits, key=lambda c: len(c.boxes), reverse=True)

    result = 1
    for i in range(min(3, len(sorted_circuits))):
        result *= len(sorted_circuits[i].boxes)

    print("Result " + str(result))


def get_part_two(boxes):
    sorted_distances = get_sorted_distances(boxes)

    for b1, b2, _ in sorted_distances:
        if b2 in b1.circuit.boxes:
            continue

        b1.connect_to(b2)
        b2.connect_to(b1)

        new_boxes = b1.circuit.boxes.union(b2.circuit.boxes)

        if len(new_boxes) == len(boxes):
            result = b1.x * b2.x
            print("Result " + str(result))
            return

        new_circuit = Circuit(new_boxes)
        for b in new_boxes:
            b.circuit = new_circuit


prepared_puzzle = prepare_puzzle("puzzles/examples/day_08.txt")
print("Part one example:")
get_part_one(prepared_puzzle, 10)

prepared_puzzle = prepare_puzzle("puzzles/examples/day_08.txt")
print("Part two example:")
get_part_two(prepared_puzzle)

prepared_puzzle = prepare_puzzle("puzzles/day_08.txt")
print("Part one:")
get_part_one(prepared_puzzle, 1000)

prepared_puzzle = prepare_puzzle("puzzles/day_08.txt")
print("Part two:")
get_part_two(prepared_puzzle)
