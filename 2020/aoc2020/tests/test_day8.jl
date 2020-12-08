using Revise
using Test
using aoc2020

test = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

test_parsed = aoc2020.parse_day8(test)

@testset "Tests" begin
    @testset "new_boot" begin
        @test aoc2020.new_boot(test_parsed) == 5
        @test aoc2020.bad_instr_finder(test_parsed) == 8
    end
end

working_dir = @__DIR__
cd(working_dir)

using PyCall

py_aocd_models = pyimport("aocd.models")
puzzle = py_aocd_models.Puzzle(2020, 8)

jlinput = aoc2020.parse_day8(puzzle.input_data)

println("Answer 1: ", aoc2020.new_boot(jlinput))
println("Answer 2: ", aoc2020.bad_instr_finder(jlinput))
