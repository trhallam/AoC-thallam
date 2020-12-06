using Test
using PyCall

working_dir = @__DIR__
cd(working_dir)

py_aocd_models = pyimport("aocd.models")
puzzle = py_aocd_models.Puzzle(2020, 6)

"""
    parse_input(input)

    Takes raw input from aoc and parses to row and column tuple.
"""
function parse_input(input::AbstractString)::Array{Array}
    input = split(input, "\n\n", keepempty=false) .|>
        x -> split.(x)
end


"""
    nunique(group)

    Just find all unique values in each group.
"""
# nunique(group) = sum(length.(reduce.(anyset, group, init=Set())))
nunique(group) = sum(group |> x -> join.(x) |> x -> Set.(x) .|> x -> length(x))

function allset(c, n)
    intersect(c, Set(n))
end

"""
    allsayyes(group)

    After doplershift, initialize the first set by finding the intersect with the output.
    This sets the base line for all subsequent intersects because any answer we count must
    exist in answer 1 for each group.
"""
allsayyes(group) = sum(length.(reduce.(allset, group, init=Set(collect('a':'z')))))

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

test_parsed = parse_input(test)

@testset "Tests" begin
    @testset "Checks" begin
        @test nunique(test_parsed) == 11
        @test allsayyes(test_parsed) == 6
    end
end

my_test = puzzle.input_data;

println("Answer 1: ", nunique(parse_input(my_test)))
println("Answer 2: ", allsayyes(parse_input(my_test)))

