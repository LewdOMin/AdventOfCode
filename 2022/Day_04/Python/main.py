from typing import List


def read_file(file_path):
    # type: (str) -> List[str]
    with open(file_path, 'r') as f:
        return f.readlines()


def part_one(input_file):
    # type: (List[str]) -> None
    full_overlaps = 0       # type: int
    for line in input_file:
        line = line.replace('\n', '').replace(' ', '')
        pair = line.split(',')      # type: List[str]
        elf_one = [int(c) for c in pair[0].split('-')]      # type: List[int]
        elf_two = [int(c) for c in pair[1].split('-')]      # type: List[int]

        if (elf_one[0] <= elf_two[0] and elf_one[1] >= elf_two[1]) or \
            (elf_one[0] >= elf_two[0] and elf_one[1] <= elf_two[1]):
            full_overlaps += 1

    print('Solution for part one is:', full_overlaps)


def part_two(input_file):
    # type: (List[str]) -> None
    overlaps = 0  # type: int
    for line in input_file:
        line = line.replace('\n', '').replace(' ', '')
        pair = line.split(',')  # type: List[str]
        elf_one = [int(c) for c in pair[0].split('-')]  # type: List[int]
        elf_two = [int(c) for c in pair[1].split('-')]  # type: List[int]

        if elf_one[0] > elf_two[1] or elf_one[1] < elf_two[0]:
            continue

        overlaps += 1

    print('Solution for part two is:', overlaps)


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
