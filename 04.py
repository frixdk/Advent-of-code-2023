import math
from collections import Counter, defaultdict

import click
from aocd import data
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def parse_input(input):
    cards = []

    for i in input:
        name, numbers = i.split(": ")
        winning, my = numbers.split(" | ")
        winning = winning.split()
        my = my.split()

        cards.append((winning, my))
    return cards


def a_solver(input):
    games = parse_input(input)

    total_points = 0

    for winning, my in games:
        points = 0
        matches = len([v for v in my if v in winning])
        if matches == 1:
            points = 1
        elif matches > 1:
            points = int(math.pow(2, matches-1))

        total_points += points

    return total_points


def b_solver(input):
    games = parse_input(input)

    matches = [(len([v for v in my if v in winning]), 1) for winning, my in games]

    for i, (win, cards) in enumerate(matches):
        for c in range(win):
            matches[c+i+1] = (matches[c+i+1][0], matches[c+i+1][1] + cards)

    return sum([m[1] for m in matches])


@advent.command()
def test():
    test_input = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
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
