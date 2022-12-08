from typing import List


def read_file(file_path):
    # type: (str) -> List[str]
    with open(file_path, 'r') as f:
        return f.readlines()


def part_one(input_file):
    # type: (List[str]) -> None
    input = []
    for line in input_file:
        line = line.replace('\n', '')
        input.append([])
        for char in line:
            input[-1].append(int(char))

    visible_tree_count = 0

    for y in range(len(input)):
        for x in range(len(input[0])):
            if y == 0 or y == len(input) - 1 or x == 0 or x == len(input[y]) - 1:
                visible_tree_count += 1
                continue

            is_visible = True

            for y_offset in range(y - 1, -1, -1):
                if input[y][x] <= input[y_offset][x]:
                    is_visible = False
                    break

            if not is_visible:
                is_visible = True
                for y_offset in range(y + 1, len(input[y]), 1):
                    if input[y][x] <= input[y_offset][x]:
                        is_visible = False
                        break

            if not is_visible:
                is_visible = True
                for x_offset in range(x - 1, -1, -1):
                    if input[y][x] <= input[y][x_offset]:
                        is_visible = False
                        break

            if not is_visible:
                is_visible = True
                for x_offset in range(x + 1, len(input[x]), 1):
                    if input[y][x] <= input[y][x_offset]:
                        is_visible = False
                        break

            if is_visible:
                visible_tree_count += 1

    print('Solution for part one:', visible_tree_count, 'visible trees')


def part_two(input_file):
    input = []
    for line in input_file:
        line = line.replace('\n', '')
        input.append([])
        for char in line:
            input[-1].append(int(char))

    highest_scenic_score = 0

    for y in range(len(input)):
        for x in range(len(input[0])):
            north = east = south = west = 0

            if y == 0 or x == 0 or y == len(input) - 1 or x == len(input[y]) - 1:
                continue

            for y_offset in range(y - 1, -1, -1):
                north += 1
                if input[y][x] <= input[y_offset][x]:
                    break

            for y_offset in range(y + 1, len(input[y]), 1):
                south += 1
                if input[y][x] <= input[y_offset][x]:
                    break

            for x_offset in range(x - 1, -1, -1):
                east += 1
                if input[y][x] <= input[y][x_offset]:
                    break

            for x_offset in range(x + 1, len(input[x]), 1):
                west += 1
                if input[y][x] <= input[y][x_offset]:
                    break

            score = north * east * south * west

            if score > highest_scenic_score:
                highest_scenic_score = score

    print('Solution for part two:', highest_scenic_score)
    pass


def main():
    example_file = read_file('example.txt')     # type: List[str]
    input_file = read_file('input.txt')         # type: List[str]

    part_one(example_file)
    part_two(example_file)
    print()

    part_one(input_file)
    part_two(input_file)
    print()


if __name__ == '__main__':
    main()
