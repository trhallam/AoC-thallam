"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?


"""
import re
import functools


def parse_input(input):
    output = [i.strip().split(" bags contain ") for i in input.split("\n") if i.strip()]
    # output = [re.match(r"(.+)\sbags\scontain\s(.+)\sbag", i).groups() for i in output]
    bag_dict = dict()
    for bag in output:
        if bag[1] == "no other bags.":
            bag_dict[bag[0]] = ((0, "no other"),)
        else:
            bag_dict[bag[0]] = re.findall(r"(\d+)\s([\w\s]+)\sbag", bag[1])

    for bag, inner_bags in bag_dict.items():
        bag_dict[bag] = tuple((int(ib[0]), ib[1]) for ib in inner_bags)

    return bag_dict


def contains_base(all_bags, bag, base="shiny gold"):
    inner_bags = functools.reduce(lambda c, n: c + [n[1]], all_bags[bag], list())
    if base in inner_bags:
        return True
    elif all_bags[bag][0][0] == 0:
        return False
    else:
        return functools.reduce(
            lambda c, n: c or contains_base(all_bags, n), inner_bags, False
        )


def how_many_inside(all_bags, bag):
    nbags, inner_bags = zip(*all_bags[bag])
    if sum(nbags) == 0:
        return 0
    else:
        return sum(
            [
                nbags[i] + nbags[i] * how_many_inside(all_bags, ib)
                for i, ib in enumerate(inner_bags)
            ]
        )


if __name__ == "__main__":

    test = """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """

    test2 = """
    shiny gold bags contain 2 dark red bags.
    dark red bags contain 2 dark orange bags.
    dark orange bags contain 2 dark yellow bags.
    dark yellow bags contain 2 dark green bags.
    dark green bags contain 2 dark blue bags.
    dark blue bags contain 2 dark violet bags.
    dark violet bags contain no other bags.
    """

    # Answer 1
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 7)

    my_test = puzzle.input_data
    my_test_parsed = parse_input(my_test)

    test_parsed = parse_input(test)

    assert contains_base(test_parsed, "bright white")
    assert contains_base(test_parsed, "muted yellow")
    assert contains_base(test_parsed, "dark orange")
    assert contains_base(test_parsed, "light red")
    assert ~contains_base(test_parsed, "faded blue")
    assert ~contains_base(test_parsed, "dark olive")

    assert how_many_inside(test_parsed, "shiny gold") == 32
    assert how_many_inside(parse_input(test2), "shiny gold") == 126

    print(
        "Answer 1:", sum([contains_base(my_test_parsed, bag) for bag in my_test_parsed])
    )
    print("Answer 2:", how_many_inside(my_test_parsed, "shiny gold"))

    from julia import aoc2020 as jlaoc

    jlinput = jlaoc.parse_day7(puzzle.input_data)

    print(
        "Julia Answer 1:",
        sum([jlaoc.contains_base(jlinput, bag) for bag in jlinput.keys()]),
    )
    print("Julia Answer 2:", jlaoc.how_many_inside(jlinput, "shiny gold"))
