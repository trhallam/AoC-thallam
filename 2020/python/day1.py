"""
    --- Day 1: Report Repair ---

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""

import pathlib
from itertools import combinations
from math import prod


def product_findsum(a: list, n: int, req_sum: int) -> int:
    """Find the product from a set of n numbers that sum to req_sum.

    Args:
        a (list): [description]
        n (int): [description]
        req_sum ([type]): [description]

    Raises:
        ValueError: [description]

    Returns:
        int: [description]
    """

    for vals in combinations(a, n):
        if sum(vals) == req_sum:
            return prod(vals)

    raise ValueError(f"No pairs sum to {req_sum}")


if __name__ == "__main__":

    # Test 1
    test = [1721, 979, 366, 299, 675, 1456]
    test_result1 = product_findsum(test, 2, 2020)
    assert test_result1 == 514579

    # Answer 1
    cwd = pathlib.Path(".").absolute()
    with open(cwd.parent / "resources/day1_input.txt", "r") as day1:
        my_test = day1.readlines()
    my_test = [int(no) for no in my_test]
    print("Answer 1:", product_findsum(my_test, 2, 2020))

    # Test 2
    test_result2 = product_findsum(test, 3, 2020)
    assert test_result2 == 241861950

    # Answer 2
    print("Answer 2:", product_findsum(my_test, 3, 2020))
