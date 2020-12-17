"""
--- Day 17: Conway Cubes ---

As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the following rules:

    If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###

Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......

After the full six-cycle boot process completes, 112 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?


--- Part Two ---

For some reason, your simulated results don't match what the experimental energy source engineers expected. Apparently, the pocket dimension actually has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, the cube at x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules for cycle updating still apply: during each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even though the pocket dimension is 4-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1x1 region of the 4-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z and w coordinate:

Before any cycles:

z=0, w=0
.#.
..#
###


After 1 cycle:

z=-1, w=-1
#..
..#
.#.

z=0, w=-1
#..
..#
.#.

z=1, w=-1
#..
..#
.#.

z=-1, w=0
#..
..#
.#.

z=0, w=0
#.#
.##
.#.

z=1, w=0
#..
..#
.#.

z=-1, w=1
#..
..#
.#.

z=0, w=1
#..
..#
.#.

z=1, w=1
#..
..#
.#.


After 2 cycles:

z=-2, w=-2
.....
.....
..#..
.....
.....

z=-1, w=-2
.....
.....
.....
.....
.....

z=0, w=-2
###..
##.##
#...#
.#..#
.###.

z=1, w=-2
.....
.....
.....
.....
.....

z=2, w=-2
.....
.....
..#..
.....
.....

z=-2, w=-1
.....
.....
.....
.....
.....

z=-1, w=-1
.....
.....
.....
.....
.....

z=0, w=-1
.....
.....
.....
.....
.....

z=1, w=-1
.....
.....
.....
.....
.....

z=2, w=-1
.....
.....
.....
.....
.....

z=-2, w=0
###..
##.##
#...#
.#..#
.###.

z=-1, w=0
.....
.....
.....
.....
.....

z=0, w=0
.....
.....
.....
.....
.....

z=1, w=0
.....
.....
.....
.....
.....

z=2, w=0
###..
##.##
#...#
.#..#
.###.

z=-2, w=1
.....
.....
.....
.....
.....

z=-1, w=1
.....
.....
.....
.....
.....

z=0, w=1
.....
.....
.....
.....
.....

z=1, w=1
.....
.....
.....
.....
.....

z=2, w=1
.....
.....
.....
.....
.....

z=-2, w=2
.....
.....
..#..
.....
.....

z=-1, w=2
.....
.....
.....
.....
.....

z=0, w=2
###..
##.##
#...#
.#..#
.###.

z=1, w=2
.....
.....
.....
.....
.....

z=2, w=2
.....
.....
..#..
.....
.....

After the full six-cycle boot process completes, 848 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. How many cubes are left in the active state after the sixth cycle?

"""
import functools
import itertools


def parse_input(input: str, is_4d=False):
    z0 = [[i for i in z.strip()] for z in input.split("\n") if z.strip()]
    active = []
    for x, row in enumerate(z0):
        for y, char in enumerate(row):
            if char == "#" and not is_4d:
                active.append((x, y, 0))
            elif char == "#" and is_4d:
                active.append((x, y, 0, 0))
    return active


def get_minmax(state, d):
    dmin = functools.reduce(lambda c, n: min(c, n[d]), state, state[0][d])
    dmax = functools.reduce(lambda c, n: max(c, n[d]), state, state[0][d])
    return dmin, dmax


def create_neighbours(*args):
    ranges = [range(i - 1, i + 2) for i in args]
    full = set(itertools.product(*ranges))
    return full.difference(set([args]))


def simulate(state):

    dims = len(state[0])
    dim_ranges = [get_minmax(state, d) for d in range(dims)]
    dim_ranges = [range(d[0] - 2, d[1] + 2) for d in dim_ranges]

    coordinates = itertools.product(*dim_ranges)

    state = set(state)
    new_state = list()

    for coord in coordinates:
        current = set([coord])
        active = True if current.intersection(state) else False
        neighbours_active = len(create_neighbours(*coord).intersection(state))
        # print(x, y, z, active, neighbours_active)
        if active and (2 <= neighbours_active <= 3):
            new_state += [*tuple(current)]
        elif not active and neighbours_active == 3:
            new_state += [*tuple(current)]

    return new_state


def printer(state):
    print(len(state[0]))
    zmin, zmax = get_minmax(state, 2)
    ymin, ymax = get_minmax(state, 1)
    xmin, xmax = get_minmax(state, 0)

    state = set(state)
    print(xmin, xmax, ymin, ymax, zmin, zmax)
    for z in range(zmin, zmax + 1):
        print(f"z = {z}")
        for y in range(ymin, ymax + 1):
            line = ""
            for x in range(xmin, xmax + 1):
                current = set([(x, y, z)])
                if current.intersection(state):
                    line += "#"
                else:
                    line += "."
            print(line)


def boot(init_state, cycles=6):
    for _ in range(cycles):
        init_state = simulate(init_state)
    return init_state


if __name__ == "__main__":

    test1 = """
    .#.
    ..#
    ###
    """

    # print(parse_input(test1))
    tp = parse_input(test1)

    tpc = simulate(tp)
    # printer(tpc)
    print(len(boot(tp)))

    # Answer 1
    from aocd.models import Puzzle

    puzzle = Puzzle(2020, 17)

    print("Answer 1: ", len(boot(parse_input(puzzle.input_data))))

    print("Answer 1: ", len(boot(parse_input(puzzle.input_data, is_4d=True))))