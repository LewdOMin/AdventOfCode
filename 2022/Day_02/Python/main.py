from typing import Dict, List


def read_file(file_path):
    # type: (str) -> List[str]
    with open(file_path, 'r') as f:
        return f.readlines()


def part_one(input_file):
    # type: (List[str]) -> None
    wins = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
    }   # type: Dict[str, str]
    draws = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    }   # type: Dict[str, str]
    scores = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }   # type: Dict[str, int]
    total_score = 0     # type: int
    for line in input_file:
        line = line.replace(' ', '').replace('\n', '')  # type: str
        score = scores[line[-1]]                        # type: int

        is_win = wins[line[0]] == line[-1]              # type: bool
        is_draw = draws[line[0]] == line[-1]            # type: bool

        if is_win:
            score += 6
        elif is_draw:
            score += 3

        total_score += score
    print('Solution for part one is:', total_score, 'points.')


def part_two(input_file):
    result = {
        'X': 0,
        'Y': 1,
        'Z': 2,
    }  # type: Dict[str, int]
    wins = {
        'A': 'B',
        'B': 'C',
        'C': 'A',
    }   # type: Dict[str, str]
    draws = {
        'A': 'A',
        'B': 'B',
        'C': 'C',
    }   # type: Dict[str, str]
    losses = {
        'A': 'C',
        'B': 'A',
        'C': 'B',
    }   # type: Dict[str, str]
    select = {
        0: losses,
        1: draws,
        2: wins,
    }   # type: Dict[int, Dict[str, str]]
    scores = {
        'A': 1,
        'B': 2,
        'C': 3,
    }  # type: Dict[str, int]
    total_score = 0  # type: int
    for line in input_file:
        line = line.replace(' ', '').replace('\n', '')  # type: str
        score = 0  # type: int

        selection = select[result[line[-1]]][line[0]]

        score += scores[selection]
        score += result[line[-1]] * 3

        total_score += score
    print('Solution for part two is:', total_score, 'points.')


def main():
    example_file = read_file('example.txt')
    input_file = read_file('input.txt')

    part_one(example_file)
    part_two(example_file)
    print()

    part_one(input_file)
    part_two(input_file)
    print()


if __name__ == '__main__':
    main()
