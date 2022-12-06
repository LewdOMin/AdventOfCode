import re
from typing import List, Tuple


def read_file(file_path):
    # type: (str) -> List[str]
    with open(file_path, 'r') as f:
        return f.readlines()


def convert_input_to_stacks_and_instructions(input_list):
    # type: (List[str]) -> Tuple[List[List[str]], List[str]]
    stack_list = []         # type: List[str]
    instruction_list = []   # type: List[str]
    is_stack_list = True    # type: bool
    for line in input_list:
        if line.replace('\n', '') == '':
            is_stack_list = False
            continue
        if is_stack_list:
            stack_list.append(line)
        else:
            instruction_list.append(line)

    stack_list = stack_list[:-1]
    stack_list = stack_list[::-1]

    stacks = []   # type: List[List[str]]
    for line in stack_list:
        index2 = 0
        for index in range(1, len(line) + 1, 4):
            if line[index] != ' ':
                if len(stacks) <= index2:
                    stacks.append([line[index]])
                else:
                    stacks[index2].append(line[index])
            index2 += 1

    return stacks, instruction_list


def part_one(input_file):
    # type: (List[str]) -> None
    stacks, instructions = convert_input_to_stacks_and_instructions(input_file)
    regex = r'move (\d+) from (\d+) to (\d+)'     # type: str

    for line in instructions:
        match = re.match(regex, line)
        count = int(match.group(1))
        from_crate = int(match.group(2)) - 1
        to_crate = int(match.group(3)) - 1

        for _ in range(count):
            stacks[to_crate].append(stacks[from_crate].pop(len(stacks[from_crate]) - 1))

    print('Solution for part one is:', [stack[-1] for stack in stacks])


def part_two(input_file):
    # type: (List[str]) -> None
    stacks, instructions = convert_input_to_stacks_and_instructions(input_file)
    regex = r'move (\d+) from (\d+) to (\d+)'     # type: str

    for line in instructions:
        match = re.match(regex, line)
        count = int(match.group(1))
        from_crate = int(match.group(2)) - 1
        to_crate = int(match.group(3)) - 1

        stacks[to_crate].extend(stacks[from_crate][-count:])

        for _ in range(count):
            stacks[from_crate].pop(len(stacks[from_crate]) - 1)

    print('Solution for part one is:', [stack[-1] for stack in stacks])


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
