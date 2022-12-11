import re

from typing import List, Optional


def read_file(file_path):
    # type: (str) -> List[str]
    with open(file_path, 'r') as f:
        return f.readlines()


def part_one(input_file):
    # type: (List[str]) -> None
    instruction_counter = 0             # type: int
    cycle_counter = 0                   # type: int
    register_value = 1                  # type: int
    total_signal_strength = 0           # type: int
    empty_cycles = 0                    # type: int
    last_command = None                 # type: Optional[str]

    ADD_CMD_REGEX = r'addx (-?\d+)'     # type: str
    NOOP_CMD_REGEX = r'noop'            # type: str

    while instruction_counter < len(input_file):
        current_instruction = input_file[instruction_counter].replace('\n', '')
        cycle_counter += 1

        if cycle_counter <= 220 and (cycle_counter - 20) % 40 == 0:
            total_signal_strength += cycle_counter * register_value

        if empty_cycles != 0:
            empty_cycles -= 1

        if empty_cycles == 0:
            if last_command is not None:
                register_value += int(re.fullmatch(ADD_CMD_REGEX, last_command).group(1))
                last_command = None
                continue

            add_match = re.fullmatch(ADD_CMD_REGEX, current_instruction)
            noop_match = re.fullmatch(NOOP_CMD_REGEX, current_instruction)

            if add_match:
                last_command = current_instruction
                empty_cycles += 1
            elif noop_match:
                last_command = None
                empty_cycles += 1

            instruction_counter += 1

    print('Solution for part one is:', total_signal_strength)


def part_two(input_file):
    # type: (List[str]) -> None
    instruction_counter = 0             # type: int
    cycle_counter = 0                   # type: int
    register_value = 1                  # type: int
    empty_cycles = 0                    # type: int
    last_command = None                 # type: Optional[str]
    crt_width = 40                      # type: int             # 0 ... 39
    crt = ['', '', '', '', '', '']      # type: List[str]

    ADD_CMD_REGEX = r'addx (-?\d+)'     # type: str
    NOOP_CMD_REGEX = r'noop'            # type: str

    while instruction_counter < len(input_file):
        current_instruction = input_file[instruction_counter].replace('\n', '')
        cycle_counter += 1

        current_crt_line = (cycle_counter - 1) // 40
        current_crt_index = (cycle_counter - 1) % 40
        crt[current_crt_line] += '#' if register_value - 1 <= current_crt_index <= register_value + 1 else '.'

        if empty_cycles != 0:
            empty_cycles -= 1

        if empty_cycles == 0:
            if last_command is not None:
                register_value += int(re.fullmatch(ADD_CMD_REGEX, last_command).group(1))
                last_command = None
                continue

            add_match = re.fullmatch(ADD_CMD_REGEX, current_instruction)
            noop_match = re.fullmatch(NOOP_CMD_REGEX, current_instruction)

            if add_match:
                last_command = current_instruction
                empty_cycles += 1
            elif noop_match:
                last_command = None
                empty_cycles += 1

            instruction_counter += 1

    print('Solution for part one is:')
    for line in crt:
        print(line)


def main():
    example_file = read_file('example.txt')         # type: List[str]
    input_file = read_file('input.txt')             # type: List[str]

    part_one(example_file)
    part_two(example_file)
    print()

    part_one(input_file)
    part_two(input_file)
    print()


if __name__ == '__main__':
    main()
