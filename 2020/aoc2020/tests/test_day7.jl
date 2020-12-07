using Revise
using Test
using aoc2020

test1 = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

test2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

test_parsed1 = aoc2020.parse_day7(test1)
test_parsed2 = aoc2020.parse_day7(test2)

@testset "Tests" begin
    @testset "contains_base" begin
        @test aoc2020.contains_base(test_parsed1, "bright white")
        @test aoc2020.contains_base(test_parsed1, "muted yellow")
        @test aoc2020.contains_base(test_parsed1, "dark orange")
        @test aoc2020.contains_base(test_parsed1, "light red")
        @test ~aoc2020.contains_base(test_parsed1, "faded blue")
        @test ~aoc2020.contains_base(test_parsed1, "dark olive")
    end
    @testset "how_many_inside" begin
        @test aoc2020.how_many_inside(test_parsed1, "shiny gold") == 32
        @test aoc2020.how_many_inside(test_parsed2, "shiny gold") == 126
    end
end

working_dir = @__DIR__
cd(working_dir)

aoc2020.contains_base(test_parsed1, "bright white")

using PyCall

py_aocd_models = pyimport("aocd.models")
puzzle = py_aocd_models.Puzzle(2020, 7)

jlinput = aoc2020.parse_day7(puzzle.input_data)

println("Answer 1: ", sum([aoc2020.contains_base(jlinput, bag) for bag in keys(jlinput)]))
println("Answer 2: ", aoc2020.how_many_inside(jlinput, "shiny gold"))
