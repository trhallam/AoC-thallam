using Combinatorics
using DelimitedFiles
using Test
using PyCall

working_dir = @__DIR__
cd(working_dir)

py_aocd_models = pyimport("aocd.models")
puzzle = py_aocd_models.Puzzle(2020, 2)

"""
    spec_splitter(spec, String)

    Creates the split array of strings from the input spec

"""
function spec_splitter(spec::String)
    [match.match for match in eachmatch(r"(^.+\d|\w(?=:)|(?<=\s).+$)", spec)]
end

"""
    password_checker_sledco(spec, Array[String]; )

Check passwords are in spec for sled company

"""
function password_checker_sledco(spec::String; debug::Bool=false)

    split_spec = spec_splitter(spec)
    n1, n2 = [parse(Int, n) for n in split(split_spec[1], "-")]
    if debug == true
        println(split_spec)
        println(n1, n2)
        println(count(split_spec[2], split_spec[3]))
    end
    n1 <= count(split_spec[2], split_spec[3]) <= n2
end

"""
    password_checker_tobogganco(spec, Array[String]; debug=false, Bool )

Tobbogan Co Password Policy Checker

Returns:
    [type]: [description]
"""
function password_checker_tobogganco(spec::String; debug::Bool=false)

    split_spec = spec_splitter(spec)
    n1, n2 = [parse(Int, n) for n in split(split_spec[1], "-")]
    if debug == true
        println(split_spec)
        println(n1, n2)
        println(split_spec[3][n1], " ", split_spec[3][n2])
        println(split_spec[3][n1] == split_spec[2][1], split_spec[3][n2] == split_spec[2][1])
    end
    return (split_spec[3][n1] == split_spec[2][1]) != (split_spec[3][n2] == split_spec[2][1])
end


test = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
test_ans_sledco = [true, false, true]
test_ans_tbco = [true, false, false]

@testset "Tests" begin
    @testset "Test1" begin
        for (t, ta) in zip(test, test_ans_sledco)
            @test password_checker_sledco(t, debug=false) == ta
        end
    end
    @testset "Test2" begin
        for (t, ta) in zip(test, test_ans_tbco)
            @test password_checker_tobogganco(t, debug=false) == ta
        end
    end
end

# AOCD Loading
my_test = [String(s) for s in split(puzzle.input_data, "\n")]

# Answer 1
println("Answer 1: ", sum([password_checker_sledco(tst) for tst in my_test]))

# Answer 2
println("Answer 2: ", sum([password_checker_tobogganco(tst, debug=false) for tst in my_test]))
