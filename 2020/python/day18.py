"""
--- Day 18: Operation Order ---

As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71

Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51

Here are a few more examples:

    2 * 3 + (4 * 5) becomes 26.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?

--- Part Two ---

You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231

Here are the other examples from above:

    1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
    2 * 3 + (4 * 5) becomes 46.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

What do you get if you add up the results of evaluating the homework problems using these new rules?

"""
from collections import deque
import copy


def parse_input(input):
    input = input.replace(" ", "")
    # if not re.findall(r"\(|\}", input):
    #     return list(input)
    # else:
    open = 0
    bracketed = ""
    split = []
    for char in input:
        if char == "(":
            open += 1
            bracketed += char
        elif char == ")":
            open -= 1
            if open == 0:
                split.append(parse_input(bracketed[1:]))
                bracketed = ""
            else:
                bracketed += char
        elif open > 0:
            bracketed += char
        else:
            split.append(char)

    return split


def calculator(input):

    ops = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
    }

    input = deque(input)
    left = input.popleft()
    while input:
        op = input.popleft()
        right = input.popleft()

        if isinstance(left, list):
            left = calculator(left)
        else:
            left = int(left)
        if isinstance(right, list):
            right = calculator(right)
        else:
            right = int(right)

        left = ops[op](left, right)

    return left


def calculator2(input):
    adds = [i for i, val in enumerate(input) if val == "+"]

    output = copy.deepcopy(input)
    while adds and len(output) > 3:
        m = adds[0]
        output = output[: m - 1] + [output[m - 1 : m + 2]] + output[m + 2 :]
        adds = [i for i, val in enumerate(output) if val == "+"]
    output = [calculator2(v) if isinstance(v, list) else v for v in output]
    return calculator(output)


if __name__ == "__main__":

    t1 = "1 + 2 * 3 + 4 * 5 + 6"
    t2 = "1 + (2 * 3) + (4 * (5 + 6))"
    t3 = "2 * 3 + (4 * 5)"
    t4 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
    t5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    t6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

    assert calculator(parse_input(t1)) == 71
    assert calculator(parse_input(t2)) == 51
    assert calculator(parse_input(t3)) == 26
    assert calculator(parse_input(t4)) == 437

    assert calculator2(parse_input(t2)) == 51
    assert calculator2(parse_input(t3)) == 46
    assert calculator2(parse_input(t4)) == 1445
    assert calculator2(parse_input(t5)) == 669060
    assert calculator2(parse_input(t6)) == 23340

    print(calculator2(parse_input(t6)))

    # Answer 1
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 18)

    mti = puzzle.input_data

    mtip = [parse_input(t) for t in mti.split("\n")]
    mtic = [calculator(i) for i in mtip]
    mtic2 = [calculator2(i) for i in mtip]

    print("Answer 1: ", sum(mtic))
    print("Answer 2: ", sum(mtic2))
