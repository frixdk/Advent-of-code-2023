from collections import Counter, defaultdict

import click
from aocd import data
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def a_solver(input):
    bab = [[d for d in i if d.isdigit()] for i in input]
    tal = [int(b[0] + b[-1]) for b in bab]

    return sum(tal)


def b_solver(input):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,

    } | {str(n): n for n in range(1, 10)}

    f = []
    for i in input:
        all_matches = [item for row in [((i.find(n), v), (i.rfind(n), v)) for n, v in numbers.items()] for item in row]
        valid_matches = [t[1] for t in sorted(all_matches) if t[0] > -1]

        f.append(valid_matches[0]*10 + valid_matches[-1])

    return sum(f)


@advent.command()
def test():
    test_input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]

    #print("A result:", a_solver(test_input))
    print("B result:", b_solver(test_input))


from timeit import default_timer as timer


@advent.command()
def solve():
    print("A result:", a_solver(data.splitlines()))
    print("B result:", b_solver(data.splitlines()))


@advent.command()
def submit():
    pass
    #aocd_submit(a_solver(lines), part="a")
    #aocd_submit(b_solver(lines), part="b")


if __name__ == "__main__":
    advent()
