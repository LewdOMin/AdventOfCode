from typing import List


def read_file(file_path):
    # type: (str) -> List[str]
    with open(file_path, 'r') as f:
        return f.readlines()


def input_list_to_calorie_list(input_file):
    i = 0  # type: int
    calories = [0]  # type: List[int]
    for line in input_file:
        if line == '\n':
            calories.append(0)
        else:
            calories[-1] += int(line.replace('\n', ''))
    return calories


def part_one(input_file):
    # type: (List[str]) -> None
    calories = input_list_to_calorie_list(input_file)   # type: List[int]
    print('Part One Solution:', max(calories), 'calories')


def part_two(input_file):
    # type: (List[str]) -> None
    calories = input_list_to_calorie_list(input_file)  # type: List[int]
    top_three = sum(sorted(calories)[-3:])
    print('Part Two Solution:', top_three, 'calories')


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
