using Combinatorics
using DelimitedFiles
using Printf
using Test

"""
    product_findsum(a, Array; n, int; req_sum. int)

Calculates the sum of all combinations of int in Array of size n to find req_sum
then returns product of the matching combination.

"""
function product_findsum(a::Array{Int}, n::Int, req_sum::Int)::Int

    for vals = combinations(a, n)
        if sum(vals) == req_sum
            return prod(vals)
        end
    end
end

# Test 1
test = [1721, 979, 366, 299, 675, 1456]

test_result1 = product_findsum(test, 2, 2020)
test_result2 = product_findsum(test, 3, 2020)

@testset "Tests" begin
    @testset "Test1" begin
        @test test_result1 == 514579
        # makesure returned type matches input
        @inferred product_findsum(test, 2, 2020)
    end
    @testset "Test2" begin
        @test test_result2 == 241861950
    end
end

# Setup
my_test_file = open("../resources/day1_input.txt")
my_test = readlines(my_test_file)
my_test = parse.(Int, my_test)

# Alternative Loading
my_test = readdlm("../resources/day1_input.txt", ',', Int)
my_test = vec(my_test)

# Answer 1
println("Answer 1: ", product_findsum(my_test, 2, 2020))

# Answer 2
println("Answer 2: ", product_findsum(my_test, 3, 2020))
