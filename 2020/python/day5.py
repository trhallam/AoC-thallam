"""
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?

"""


def binpart(sequence, n, first_half="F"):
    if not sequence:
        return 0
    n2 = n // 2
    if sequence[0] == first_half:
        return binpart(sequence[1:], n2, first_half)
    else:
        return n2 + binpart(sequence[1:], n2, first_half)


def binpart(sequence: str, n, first_half=1):
    seq = sequence.translate(str.maketrans({"F": "0", "L": "0", "B": "1", "R": "1"}))
    return int(seq, 2)


def parse_bin_seat(sequence):
    row = binpart(sequence[:7], 128)
    col = binpart(sequence[-3:], 8, "L")
    seat_id = row * 8 + col
    return row, col, seat_id


if __name__ == "__main__":

    assert binpart("FFFFFFF", 128) == 0
    assert binpart("BFFFBBF", 128) == 70
    assert binpart("FFFBBBF", 128) == 14
    assert binpart("BBFFBBF", 128) == 102
    assert binpart("BBBBBBB", 128) == 127

    assert binpart("RRR", 8, first_half="L") == 7
    assert binpart("LLL", 8, first_half="L") == 0
    assert binpart("RLL", 8, first_half="L") == 4

    assert parse_bin_seat("FFFFFFFRRR") == (0, 7, 7)
    assert parse_bin_seat("FFFBBBFRRR") == (14, 7, 119)
    assert parse_bin_seat("BBFFBBFRLL") == (102, 4, 820)

    # Answer 1
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 5)

    my_test = puzzle.input_data
    my_tests = my_test.split("\n")

    seat_ids = [parse_bin_seat(test)[2] for test in my_tests]
    seat_ids.sort()
    diff = [a - b for a, b in zip(seat_ids[1:], seat_ids[:-1])]
    for i, val in enumerate(diff):
        if val > 1:
            left_seat = i

    print("Highest Seat ID:", max(seat_ids))

    print("My Seat: ", left_seat + 1 + min(seat_ids))
    print("seat_ids", seat_ids[left_seat:])
    # print("PP1: ", sum(check_deep))

    from julia import aoc2020 as jlaoc

    jlinput = jlaoc.parse_day5(my_test)

    print("Julia Answer 1:", max(jlaoc.as_seat_ids(jlinput)))
    print("Julia Answer 2:", jlaoc.find_missing_seat(jlinput))
