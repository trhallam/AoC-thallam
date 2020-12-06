"""
--- Day 6: Custom Customs ---

As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?


--- Part Two ---

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

"""
from collections import defaultdict


def parse_input(input: str) -> list:
    input = input.split("\n\n")
    return [i.split() for i in input]


def count_unique_yes(input):
    return sum([len(set("".join(group))) for group in input])


def group_distograms(input):
    output = []
    for group in input:
        counter = defaultdict(lambda: 0)
        for person in group:
            for char in person:
                counter[char] = counter[char] + 1
        counter["NPEOPLE"] = len(group)
        output.append(counter)
    return output


def nunique(distrogram):
    cumsum = 0
    for dist in distrogram:
        n = dist.pop("NPEOPLE")
        for val in dist.values():
            if val / n == 1:
                cumsum += 1
    return cumsum


if __name__ == "__main__":

    test = """
    abc

        a
        b
        c

        ab
        ac

        a
        a
        a
        a

        b
    """

    test_parsed = parse_input(test)
    n = count_unique_yes(test_parsed)
    test_parsed2 = parse_input(test)
    test_dist = group_distograms(test_parsed2)
    n2 = nunique(test_dist)

    assert n == 11

    # Answer 1
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 6)

    my_test = puzzle.input_data
    print("Answer 1: ", count_unique_yes(parse_input(my_test)))
    print("Answer 2: ", nunique(group_distograms(parse_input(my_test))))
