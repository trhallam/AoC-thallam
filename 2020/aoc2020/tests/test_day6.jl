using Revise
using Test
using aoc2020

test = """
abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b
"""

test_parsed = aoc2020.parse_day6(test)

@testset "Tests" begin
    @testset "Checks" begin
        @test aoc2020.nunique(test_parsed) == 11
        @test aoc2020.allsayyes(test_parsed) == 6
    end
end