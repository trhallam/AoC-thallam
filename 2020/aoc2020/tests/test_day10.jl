using Revise
using Test
using aoc2020

test = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

test_parsed = aoc2020.parse_day10(test)

data = vcat([0], test_parsed, [maximum(test_parsed) + 3])
diffs = data |> sort |> diff
aoc2020.day_10part2(test_parsed)
# @testset "Tests" begin
#     @testset "new_boot" begin
#         @test aoc2020.new_boot(test_parsed) == 5
#         @test aoc2020.bad_instr_finder(test_parsed) == 8
#     end
# end

# working_dir = @__DIR__
# cd(working_dir)

# using PyCall

# py_aocd_models = pyimport("aocd.models")
# puzzle = py_aocd_models.Puzzle(2020, 10)

# jlinput = aoc2020.parse_day8(puzzle.input_data)

# println("Answer 1: ", aoc2020.new_boot(jlinput))
# println("Answer 2: ", aoc2020.bad_instr_finder(jlinput))
