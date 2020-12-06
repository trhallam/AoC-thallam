using Revise
using Test
using aoc2020

test = "BFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL\n"

test_parsed = aoc2020.parse_day5(test)

@testset "Tests" begin
    @testset "Checks" begin
        @test test_parsed == [(70, 7), (14, 7), (102, 4)]
    end
end