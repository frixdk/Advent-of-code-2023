import functools
import math
from collections import Counter, defaultdict
from itertools import combinations_with_replacement

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


STR = {c: v for v, c in enumerate(["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"])}
BSTR = {c: v for v, c in enumerate(["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"])}


def rank(hand):
    counter = Counter(hand)

    if counter.most_common()[0][1] == 5:
        return 6

    first, second = counter.most_common(2)
    rank = 0

    if first[1] == 5:
        rank = 6
    elif first[1] == 4:
        rank = 5
    elif first[1] == 3 and second[1] == 2:
        rank = 4
    elif first[1] == 3:
        rank = 3
    elif first[1] == 2 and second[1] == 2:
        rank = 2
    elif first[1] == 2:
        rank = 1

    return rank


def compare(hand1, hand2):
    rank1 = rank(hand1[0])
    rank2 = rank(hand2[0])

    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return -1
    else:
        for c1, c2 in zip(hand1[0], hand2[0]):
            if STR[c1] > STR[c2]:
                return 1
            elif STR[c1] < STR[c2]:
                return -1


def a_solver(input):
    hands = [i.split() for i in input]
    winnings = 0

    for rank, (hand, bid) in enumerate(sorted(hands, key=functools.cmp_to_key(compare))):
        print(rank+1, hand, bid)
        winnings += (rank+1)*int(bid)

    return winnings


def brank(hand):
    #print(hand)
    counter = Counter(hand)

    # THERE IS A SMARTER WAY BUT IM GONNAN TRY ALL COMBINANTOIONS
    jokers = [c for c in hand if c == "J"]
    rest = "".join([c for c in hand if c != "J"])

    #print("JOKERS. REST", jokers, rest)

    replacements = [c for c in STR.keys() if c != "J"]

    best_rank = 0

    for combination in combinations_with_replacement(replacements, len(jokers)):
        card_rank = rank(rest + "".join(combination))
        if card_rank > best_rank:
            best_rank = card_rank
    # stuff
    #print("hand", best_rank)
    return best_rank


def bcompare(hand1, hand2):
    rank1 = hand1[2]
    rank2 = hand2[2]

    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return -1
    else:
        for c1, c2 in zip(hand1[0], hand2[0]):
            if BSTR[c1] > BSTR[c2]:
                return 1
            elif BSTR[c1] < BSTR[c2]:
                return -1


def b_solver(input):
    hands = [i.split() for i in input]
    winnings = 0

    hands = [(hand, bid, brank(hand)) for hand, bid in hands]

    for rank, (hand, bid, crank) in enumerate(sorted(hands, key=functools.cmp_to_key(bcompare))):
        print(rank+1, hand, bid)
        winnings += (rank+1)*int(bid)

    return winnings


@advent.command()
def test():
    test_input = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"
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
