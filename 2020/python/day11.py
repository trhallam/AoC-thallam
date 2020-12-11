"""
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

--- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

"""
import re


def parse_input(input: str) -> list:
    """parse the day 8 input"""
    return [i for i in input.split()]


def _patch1(input: list, posj: int) -> str:
    patch = [row[posj - 1 : posj + 2] for row in input]

    patch = "".join(patch)
    adjacent = patch[:4] + patch[5:]
    if patch[4] == ".":
        return "."
    if patch[4] == "#" and adjacent.count("#") >= 4:
        return "L"
    if patch[4] == "L" and adjacent.count("#") == 0:
        return "#"
    return patch[4]


def _patch2(input: list, posi: int, posj: int) -> str:

    # is floor
    if input[posi][posj] == ".":
        return "."

    lh = len(input)
    lw = len(input[0])

    range_right = range(posj + 1, lw, 1)
    range_left = range(posj - 1, -1, -1)
    range_up = range(posi - 1, -1, -1)
    range_down = range(posi + 1, lh, 1)

    up = "".join([input[i][posj] for i in range_up])
    right = "".join([input[posi][j] for j in range_right])
    down = "".join([input[i][posj] for i in range_down])
    left = "".join([input[posi][j] for j in range_left])

    dru = "".join([input[i][j] for i, j in zip(range_up, range_right)])
    drd = "".join([input[i][j] for i, j in zip(range_down, range_right)])
    dlu = "".join([input[i][j] for i, j in zip(range_up, range_left)])
    dld = "".join([input[i][j] for i, j in zip(range_down, range_left)])

    vis_seats = ""
    for direction in [up, right, down, left, dru, drd, dlu, dld]:
        seats = re.findall(r"(L|#)", direction)
        if seats:
            vis_seats += seats[0]

    occupied = vis_seats.count("#")

    if occupied >= 5:
        return "L"
    elif occupied == 0:
        return "#"
    else:
        return input[posi][posj]


def fill_seats(input: list, patch_type: int = 1) -> list:
    # first pad the input with floor
    padded = ["." + row + "." for row in input]
    new_width = len(padded[0])
    padded = ["." * new_width] + padded + ["." * new_width]
    new_height = len(padded)

    output = padded.copy()
    previous_output = []
    while previous_output != output:
        previous_output = output.copy()
        for i in range(1, new_height - 1):
            rows = previous_output[i - 1 : i + 2]
            for j in range(1, new_width - 1):
                if patch_type == 1:
                    pos_is = _patch1(rows, j)
                if patch_type == 2:
                    pos_is = _patch2(previous_output, i, j)
                output[i] = output[i][:j] + pos_is + output[i][j + 1 :]
    return output


if __name__ == "__main__":

    test_empty = """
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    """

    test_end = """
    #.#L.L#.##
    #LLL#LL.L#
    L.#.L..#..
    #L##.##.L#
    #.#L.LL.LL
    #.#L#L#.##
    ..L.L.....
    #L#L##L#L#
    #.LLLLLL.L
    #.#L#L#.##
    """

    diagonal_test = """
    .##.##.
    #.#.#.#
    ##...##
    ...L...
    ##...##
    #.#.#.#
    .##.##.
    """

    one_test = """
    .............
    .L.L.#.#.#.#.
    .............
    """

    all_test = """
    .......#.
    ...#.....
    .#.......
    .........
    ..#L....#
    ....#....
    .........
    #........
    ...#.....
    """

    test = parse_input(test_empty)

    fs = fill_seats(test)

    fs2 = _patch2(parse_input(diagonal_test), 3, 3)
    fs3 = _patch2(parse_input(one_test), 1, 0)
    fs3 = _patch2(parse_input(one_test), 1, 11)
    fs4 = _patch2(parse_input(all_test), 4, 3)

    fs2 = fill_seats(test, 2)

    assert "".join(fs).count("#") == 37
    assert "".join(fs2).count("#") == 26

    # # Answer 1
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 11)

    mt = puzzle.input_data
    mti = parse_input(mt)
    mt_fs = fill_seats(mti)
    mt_fs2 = fill_seats(mti, 2)

    print("Answer 1:", "".join(mt_fs).count("#"))
    print("Answer 2:", "".join(mt_fs2).count("#"))
