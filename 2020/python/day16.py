"""
--- Day 16: Ticket Translation ---

As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'

Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12

It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?

--- Part Two ---

Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9

Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?

"""

import re
import functools


def parse_input(input: str):
    header, ticket, other_tickets = input.split("\n\n")
    header = header.split("\n")
    ticket = ticket.split("\n")
    other_tickets = other_tickets.split("\n")

    header = [
        re.findall(r"([\s\w]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)", h.strip())[0]
        for h in header
        if ":" in h
    ]

    ticket = [int(i) for i in ticket[1].split(",")]

    other_tickets = [
        [int(i) for i in tick.split(",")] for tick in other_tickets[1:] if "," in tick
    ]
    return header, ticket, other_tickets


def check_invalid(header: list, other_tickets: list):
    valid_ranges = set(
        functools.reduce(
            lambda c, n: c
            + list(range(int(n[1]), int(n[2]) + 1))
            + list(range(int(n[3]), int(n[4]) + 1)),
            header,
            [],
        )
    )
    other_nums = list(functools.reduce(lambda c, n: c + n, other_tickets, []))
    bad_nums = set(other_nums) - valid_ranges
    return [on for on in other_nums if on in bad_nums]


def filter_invalid(invalid: list, other_tickets: list):
    invalid = set(invalid)
    return [tick for tick in other_tickets if not set(tick).intersection(invalid)]


def find_field_order(header: list, tickets: list):
    l = len(header)
    h_invalids_full = list()
    for h in header:
        h_invalids = []
        for fieldn in range(l):
            nums = functools.reduce(lambda c, n: c + [[n[fieldn]]], tickets, [])
            if check_invalid([h], nums):
                h_invalids.append(fieldn)
        h_invalids_full.append(h_invalids)

    valid_options = [(i, l - len(op), op) for i, op in enumerate(h_invalids_full)]
    valid_options = sorted(valid_options, key=lambda x: x[1])

    base = set(range(l))
    used = set()
    order = dict()

    for option in valid_options[1:]:
        h = header[option[0]][0]
        valids = option[2]
        pos = base.difference(set(valids).union(used))
        used = used.union(pos)
        order[h] = list(pos)[0]

    return order


def label_ticket(ticket, fields: dict):
    output = dict()
    for field in fields:
        output[field] = ticket[fields[field]]

    return output


if __name__ == "__main__":

    test1 = """
    class: 1-3 or 5-7
    row: 6-11 or 33-44
    seat: 13-40 or 45-50

    your ticket:
    7,1,14

    nearby tickets:
    7,3,47
    40,4,50
    55,2,20
    38,6,12
    """

    test2 = """
    class: 0-1 or 4-19
    row: 0-5 or 8-19
    seat: 0-13 or 16-19

    your ticket:
    11,12,13

    nearby tickets:
    3,9,18
    15,1,5
    5,14,9
    """

    t1h, t1t, t1ot = parse_input(test1)
    t1_invalid = check_invalid(t1h, t1ot)
    print(t1_invalid)
    print(sum(t1_invalid))

    print(filter_invalid(t1_invalid, t1ot))

    t2h, t2t, t2ot = parse_input(test2)
    t2_invalid = check_invalid(t2h, t2ot)
    t2ot_valid = filter_invalid(t2_invalid, t2ot)
    t2ot_valid.append(t2t)

    t2or = find_field_order(t2h, t2ot_valid)
    print(label_ticket(t2t, t2or))

    # Answer 1
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 16)

    mth, mtt, mtot = parse_input(puzzle.input_data)
    mt_invalid = check_invalid(mth, mtot)
    mtot_valid = filter_invalid(mt_invalid, mtot)
    mtot_valid.append(mtt)
    print("Answer 1:", sum(mt_invalid))

    mtor = find_field_order(mth, mtot_valid)
    mttl = label_ticket(mtt, mtor)

    from math import prod

    mtt1 = [mttl[v] for v in mttl if "departure" in v]
    print("Answer 2:", prod(mtt1))
