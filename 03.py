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


def has_symbol(x, y, input):
    if x < 0 or y < 0:
        return
    if x >= len(input[0]):
        return
    if y >= len(input):
        return
    if not input[x][y].isdigit() and input[x][y] != ".":
        return True


def a_solver(input):
    parts = []

    nums = []
    num = ""
    coords = []
    for x, row in enumerate(input):
        for y, r in enumerate(row):
            if r.isdigit():
                num += r
                coords.append((x, y))
            else:
                if num:
                    nums.append((num, coords))
                num = ""
                coords = []

    for num, coords in nums:
        is_machine_part = False
        for x, y in coords:
            for a in range(x-1, x+2):
                for b in range(y-1, y+2):
                    if has_symbol(a, b, input):
                        is_machine_part = True

        if is_machine_part:
            parts.append(int(num))

    return sum(parts)


def b_solver(input):
    gears = []

    nums = []
    num = ""
    coords = []
    potential_gears = []

    for x, row in enumerate(input):
        for y, r in enumerate(row):
            if r == "*":
                potential_gears.append((x, y))
            if r.isdigit():
                num += r
                coords.append((x, y))
            else:
                if num:
                    nums.append((num, coords))
                num = ""
                coords = []

    for pg in potential_gears:
        adjacents = []
        for num, coords in nums:
            is_adjacent = False
            for x, y in coords:
                if math.dist(pg, (x, y)) < 2.0:
                    is_adjacent = True
            if is_adjacent:
                adjacents.append(int(num))

        if len(adjacents) == 2:
            gears.append(math.prod(adjacents))

    return sum(gears)


@advent.command()
def test():
    test_input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
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
