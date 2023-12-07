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
    seeds = [int(x) for x in input[0].split(": ")[1].split()]
    maps = defaultdict(list)

    keys = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature ",
        "temperature-to-humidity",
        "humidity-to-location"
    ]

    current_key = ""

    for i in input[1:]:
        if not i.strip():
            continue
        new_key = False
        for key in keys:
            if key in i:
                current_key = key
                new_key = True
                continue
        if new_key:
            new_key = False
            continue

        maps[current_key].append([int(x) for x in i.split()])

    return seeds, maps


def a_solver(input):
    seeds, maps = parse_input(input)

    #print(seeds)
    #print(maps)

    outs = []

    for seed in seeds:
        print("##########", seed)
        for k, map in maps.items():
            print(seed, k, map)
            for m in map:
                if seed >= m[1] and seed < m[1] + m[2]:
                    out = m[0] + seed - m[1]
                    print("map", out)
                    seed = out
                    break

        #print(seed)
        outs.append(seed)


    #print(min(outs))
    return min(outs)

def b_solver(input):
    seeds, maps = parse_input(input)

    lowest = None

    for seed, ran in more_itertools.batched(seeds, 2):
        print(seed, ran)
        for r in range(ran):
            cseed = seed + r
            #print("##########", r, seed, cseed)
            for k, map in maps.items():
                #print(seed, k, map)
                for m in map:
                    if cseed >= m[1] and cseed < m[1] + m[2]:
                        cseed = m[0] + cseed - m[1]
                        #print("map", out)
                        break

            #print(seed)
            if not lowest or cseed < lowest:
                lowest = cseed

    #print(check_seeds)
    print("BAAABAB")

    #for seed in check_seeds:


    #print(min(outs))
    return lowest


def b_solver2(input):
    seeds, maps = parse_input(input)

    lowest = None

    for seed, ran in more_itertools.batched(seeds, 2):
        print("######", seed, ran)

        #seeds = [seed,]

        for k, map in maps.items():
            new_ranges = []
            po = [seed, seed+ran]

            for m in map:
                po.append(m[1])
                po.append(m[1] + m[2])

            for start, end in more_itertools.pairwise(sorted(po)):
                print(start, end)
                if start >= seed and end <= seed+ran:
                    print("her")
                    was_mapped = False
                    for m in map:
                        if start >= m[1] and end <= m[1]+m[2]:
                            print("mapping")
                            new_ranges.append((m[0] + start - m[1], end - start))
                            was_mapped = True
                    if not was_mapped:
                        new_ranges.append((start, end - start))

            print(new_ranges)


                # for start, end in more_itertools.pairwise(po):
                #     print(start, end)
                #     if start <= seed <= end:
                #         if start <= m[1] <= end:
                #             #map
                #             print("map seed", seed)
                #         # tag det med
                #         print("map seed", seed)
                #         new_ranges.append((start, end-start))

                #break
        break
        print("BERAAA", seed, ran)


    #print(check_seeds)
    print("BAAABAB")

    #for seed in check_seeds:


    #print(min(outs))
    return lowest

import threading


def b_solver(input):
    seeds, maps = parse_input(input)

    lowest = None

    for seed, ran in more_itertools.batched(seeds, 2):
        print(seed, ran)
        for r in range(ran):
            cseed = seed + r
            #print("##########", r, seed, cseed)
            for k, map in maps.items():
                #print(seed, k, map)
                for m in map:
                    if cseed >= m[1] and cseed < m[1] + m[2]:
                        cseed = m[0] + cseed - m[1]
                        #print("map", out)
                        break

            #print(seed)
            if not lowest or cseed < lowest:
                lowest = cseed

    #print(check_seeds)
    print("BAAABAB")

    #for seed in check_seeds:


    #print(min(outs))
    return lowest

@advent.command()
def test():
    test_input = [
        "seeds: 79 14 55 13",
        " ",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        " ",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "" ,
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        " ",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        " ",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        " ",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        " ",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]

    #print("A result:", a_solver(test_input))
    #print("B result:", b_solver(test_input))
    print("B result:", b_solver3(test_input))


@advent.command()
def solve():
    #print("A result:", a_solver(data.splitlines()))
    print("B result:", b_solver3(data.splitlines()))


@advent.command()
def submit():
    aocd_submit(a_solver(data.splitlines()), part="a")
    aocd_submit(b_solver(data.splitlines()), part="b")


if __name__ == "__main__":
    advent()
