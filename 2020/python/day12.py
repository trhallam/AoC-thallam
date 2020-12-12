"""
--- Day 12: Rain Risk ---

Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11

These instructions would be handled as follows:

    F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
    N3 would move the ship 3 units north to east 10, north 3.
    F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
    R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
    F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?

--- Part Two ---

Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

    F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
    N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
    F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
    R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
    F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.

After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?

"""
import math


def parse_input(input: str) -> list:
    """parse the day 8 input"""
    return [(i[0], int(i[1:])) for i in input.split()]


class Ferry:

    instr_table = dict(N=(0, 1), S=(0, -1), E=(1, 0), W=(-1, 0))
    bearings = {0: "N", 90: "E", 180: "S", 270: "W"}

    def __init__(self, instructions: list, starting_bearing: int = 90):
        self.instr = instructions
        self.bear = starting_bearing
        self.pos = (0, 0)
        self.way_point = (10, 1)

    def navigate(self):

        for instr, i in self.instr:
            # print(self.pos, self.bear)
            # print(instr, i)
            if instr in "NSEW":
                trnsfm = self.instr_table[instr]
            elif instr == "F":
                trnsfm = self.instr_table[self.bearings[self.bear]]
            elif instr == "R":
                self.bear = (self.bear + i) % 360
                continue
            else:  # instr = "L"
                self.bear = (self.bear - i) % 360
                continue

            self.pos = tuple(p + i * t for p, t in zip(self.pos, trnsfm))

    def _rotate_wp(self, cw_ac, ang):
        i = cw_ac * math.radians(ang)
        wp_x = self.way_point[0] * math.cos(i) - self.way_point[1] * math.sin(i)
        wp_y = self.way_point[0] * math.sin(i) + self.way_point[1] * math.cos(i)
        wp_x = int(round(wp_x, 0))
        wp_y = int(round(wp_y, 0))
        self.way_point = (wp_x, wp_y)

    def navigate_wp(self):

        for instr, i in self.instr:
            if instr in "NSEW":
                trnsfm = self.instr_table[instr]
                self.way_point = tuple(
                    p + i * t for p, t in zip(self.way_point, trnsfm)
                )
            elif instr == "R":
                self._rotate_wp(-1, i)
            elif instr == "L":
                self._rotate_wp(1, i)
            else:  # instr = "F"
                self.pos = tuple(p + i * t for p, t in zip(self.pos, self.way_point))

    def mh_dist(self):
        return abs(self.pos[0]) + abs(self.pos[1])


if __name__ == "__main__":

    test = """
    F10
    N3
    F7
    R90
    F11
    """

    test2 = """
    F1
    N1
    E1
    S1
    W1
    R90
    R180
    R270
    L90
    L180
    L270
    """

    test = parse_input(test)
    tF = Ferry(test)
    tF.navigate()
    tF2 = Ferry(test)
    tF2.navigate_wp()

    assert tF.mh_dist() == 25
    assert tF2.mh_dist() == 286

    # # Answer 1
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 12)

    mt = puzzle.input_data
    mti = parse_input(mt)

    my_ferry = Ferry(mti)
    my_ferry.navigate()

    my_ferry2 = Ferry(mti)
    my_ferry2.navigate_wp()

    print("Answer 1:", my_ferry.mh_dist())
    print("Answer 2:", my_ferry2.mh_dist())
