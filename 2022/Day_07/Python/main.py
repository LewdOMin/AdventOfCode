import pprint
import re

from typing import Dict, List, Optional


from file_system import File, Filesystem, Folder


def read_file(file_path):
    # type: (str) -> List[str]
    with open(file_path, 'r') as f:
        return f.readlines()


def part_one(input_file):
    # type: (List[str]) -> None
    CHANGE_DIR_REGEX = r'\$ cd (.+)'

    filesystem = Filesystem()

    for line in input_file:
        line = line.replace('\n', '')
        if not line.startswith('$'):
            if line.startswith('dir'):
                new_dir = line.split(' ')[1]
                filesystem.make_directory(new_dir)
            else:
                file_data = line.split(' ')
                filesystem.make_file(file_data[1], int(file_data[0]))
            continue

        match = re.fullmatch(CHANGE_DIR_REGEX, line)

        if match:
            next_dir = match.group(1)
            filesystem.change_directory(next_dir)

    total_size = 0
    for item in filesystem:
        if type(item) is Folder:
            size = item.get_size()

            if size <= 100000:
                total_size += size

    print('Solution for part one is:', total_size)


def part_two(input_file):
    # type: (List[str]) -> None
    CHANGE_DIR_REGEX = r'\$ cd (.+)'

    filesystem = Filesystem()

    for line in input_file:
        line = line.replace('\n', '')
        if not line.startswith('$'):
            if line.startswith('dir'):
                new_dir = line.split(' ')[1]
                filesystem.make_directory(new_dir)
            else:
                file_data = line.split(' ')
                filesystem.make_file(file_data[1], int(file_data[0]))
            continue

        match = re.fullmatch(CHANGE_DIR_REGEX, line)

        if match:
            next_dir = match.group(1)
            filesystem.change_directory(next_dir)

    smallest_valid_size = filesystem.get_size()
    file_system_size = 70_000_000
    update_size = 30_000_000
    current_free_space = file_system_size - filesystem.get_size()
    needed_size = update_size - current_free_space
    for item in filesystem:
        if type(item) is Folder:
            size = item.get_size()

            if needed_size <= size < smallest_valid_size:
                smallest_valid_size = size

    print('Solution for part one is:', smallest_valid_size)


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
