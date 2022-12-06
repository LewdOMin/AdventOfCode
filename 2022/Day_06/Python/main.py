from typing import List


def read_file(file_path):
    # type: (str) -> List[str]
    with open(file_path, 'r') as f:
        return f.readlines()


def part_one(input_file):
    # type: (List[str]) -> None
    chars_to_check = 4      # type: int
    input_file = input_file[0]      # type: str
    for index in range(chars_to_check, len(input_file)):
        check_range = input_file[index-chars_to_check:index]    # type: str
        checks = [check_range[index2] not in check_range[index2+1:]
                  for index2 in range(0, chars_to_check)]     # type: List[bool]
        if all(checks):
            print('Solution for part one is:', index)
            break


def part_two(input_file):
    # type: (List[str]) -> None
    chars_to_check = 14     # type: int
    input_file = input_file[0]      # type: str
    for index in range(chars_to_check, len(input_file)):
        check_range = input_file[index-chars_to_check:index]    # type: str
        checks = [check_range[index2] not in check_range[index2+1:]
                  for index2 in range(0, chars_to_check)]     # type: List[bool]
        if all(checks):
            print('Solution for part one is:', index)
            break


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
