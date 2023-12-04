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
    games = dict()
    for i in input:
        game, reveals = i.split(": ")

        bab = [{k: int(v) for v, k in (cube.split(" ") for cube in reveal.split(", "))} for reveal in reveals.split("; ")]
        games[int(game.split(" ")[1])] = bab

    return games


def a_solver(input):
    games = parse_input(input)

    question = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum = 0

    for id, reveals in games.items():
        if all([all([question[cube] >= amount for cube, amount in reveal.items()]) for reveal in reveals]):
           sum += id

    return sum


def b_solver(input):
    games = parse_input(input)

    powers = []

    for id, reveals in games.items():
        required = defaultdict(int)
        for reveal in reveals:
            for cube, amount in reveal.items():
                if required[cube] < amount:
                    required[cube] = amount
        powers.append(math.prod(required.values()))

    return sum(powers)


@advent.command()
def test():
    test_input = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ]

    print("A result:", a_solver(test_input))
    print("B result:", b_solver(test_input))


@advent.command()
def solve():
    print("A result:", a_solver(data.splitlines()))
    print("B result:", b_solver(data.splitlines()))


@advent.command()
def submit():
    #aocd_submit(a_solver(data.splitlines()), part="a")
    aocd_submit(b_solver(data.splitlines()), part="b")


if __name__ == "__main__":
    advent()
