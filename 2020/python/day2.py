"""
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

"""
import re

PWD_SPEC = re.compile(r"(^.+\d|\w(?=:)|(?<=\s).+$)")


def password_checker_sledco(spec: str, debug:bool=False) -> bool:
    """Check passwords are in spec for sled company

    Args:
        spec ([type]): [description]
    """
    split = tuple(PWD_SPEC.findall(spec))
    n1, n2 = (int(n) for n in split[0].split("-"))
    if debug:
        print(split)
        print(n1, n2)
        print(split[2].count(split[1]))
    return n1 <= split[2].count(split[1]) <= n2


def password_checker_tobogganco(spec: str, debug:bool=False):
    """Tobbogan Co Password Policy Checker

    Args:
        spec ([type]): [description]
        debug (bool, optional): [description]. Defaults to False.

    Returns:
        [type]: [description]
    """
    split = tuple(PWD_SPEC.findall(spec))
    n1, n2 = (int(n) for n in split[0].split("-"))
    n1 -= 1
    n2 -= 1
    if debug:
        print(split)
        print(n1, n2)
        print(split[2][n1] == split[1], split[2][n2] == split[1])
    return (split[2][n1] == split[1]) != (split[2][n2] == split[1])


if __name__ == "__main__":

    # Test 1
    test = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    test_ans_sledco = [True, False, True]
    test_ans_tbco = [True, False, False]

    for t, ta in zip(test, test_ans_sledco):
        assert password_checker_sledco(t) == ta

    for t, ta in zip(test, test_ans_tbco):
        assert password_checker_tobogganco(t, debug=True) == ta

    # Answer 1
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 2)

    my_test = puzzle.input_data.split("\n")

    passwords_ok_sledco = [password_checker_sledco(t) for t in my_test]
    passwords_ok_tbco = [password_checker_tobogganco(t) for t in my_test]
    print("SledCo Sum: ", sum(passwords_ok_sledco))
    print("TobogganCo Sum: ", sum(passwords_ok_tbco))
