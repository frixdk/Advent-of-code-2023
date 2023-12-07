import math
from collections import Counter, defaultdict

import click
import more_itertools
from aocd import data
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def parse_input(input):
    pass


def a_solver(input):
    time = [int(x) for x in input[0].split(":")[1].split()]
    distance = [int(x) for x in input[1].split(":")[1].split()]

    total = 1

    for time, record in zip(time, distance):
        win = 0
        for speed in range(1, time+1):

            distance = (time - speed) * speed
            if distance > record:
                win += 1

        total = total*win

    return total


def b_solver(input):
    time = int(input[0].split(":")[1].replace(" ", ""))
    record = int(input[1].split(":")[1].replace(" ", ""))

    total = 1

    print(time, record)
    win = 0
    for speed in range(1, time+1):

        distance = (time - speed) * speed
        if distance > record:
            win += 1

    total = total*win

    return total


@advent.command()
def test():
    test_input = [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]

    print("A result:", a_solver(test_input))
    print("B result:", b_solver(test_input))


@advent.command()
def solve():
    print("A result:", a_solver(data.splitlines()))
    print("B result:", b_solver(data.splitlines()))


@advent.command()
def submit():
    aocd_submit(a_solver(data.splitlines()), part="a")
    aocd_submit(b_solver(data.splitlines()), part="b")


if __name__ == "__main__":
    advent()
