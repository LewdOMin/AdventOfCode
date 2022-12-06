from typing import List


def read_file(file_path):
    # type: (str) -> List[str]
    with open(file_path, 'r') as f:
        return f.readlines()


def get_priority(char):
    # type: (str) -> int
    assert len(char) == 1
    if 65 <= ord(char) <= 90:
        return ord(char) - 38
    elif 97 <= ord(char) <= 122:
        return ord(char) - 96
    raise ValueError


def part_one(input_file):
    # type: (List[str]) -> None
    total_priority = 0      # type: int
    for line in input_file:
        compartment_one = line[:len(line)//2]   # type: str
        compartment_two = line[len(line)//2:]   # type: str

        priority = 0        # type: int

        for char in compartment_one:
            if char in compartment_two:
                priority = get_priority(char)
                break

        total_priority += priority

    print('Solution for part one is:', total_priority)


def part_two(input_file):
    # type: (List[str]) -> None
    total_priority = 0      # type: int
    for index in range(0, len(input_file), 3):
        priority = 0        # type: int
        for char in input_file[index]:
            if char in input_file[index + 1] and char in input_file[index + 2]:
                priority = get_priority(char)
                break

        total_priority += priority

    print('Solution for part two is:', total_priority)


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
