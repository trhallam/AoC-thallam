using Test
using PyCall

working_dir = @__DIR__
cd(working_dir)

py_aocd_models = pyimport("aocd.models")
puzzle = py_aocd_models.Puzzle(2020, 5)

test = "BFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL\n"

"""
    parse_seats(input)

    Takes raw input from aoc and parses to row and column tuple.
"""
function parse_seats(input::AbstractString)::Array{Tuple{Int64,Int64},1}
    input = replace(input, r"[FL]" => "0") |>
        x -> replace(x, r"[RB]" => "1") |>
        x -> split(x, "\n", keepempty=false) .|>
        x -> tuple(first(x, 7), last(x, 3)) .|>
        x -> parse.(Int, x, base=2)
end

"""
    seat_id(row, col)

    Calculate the seat_id from the row and column number.
"""
function seat_id(row::Int, col::Int)::Int
    row * 8 + col
end


@testset "Tests" begin
    @testset "Checks" begin
        @test parse_seats(test) == [(70, 7), (14, 7), (102, 4)]
    end
end

# AOCD Loading
my_test = puzzle.input_data;
my_test = parse_seats(my_test)

known_seat_ids = map(x -> seat_id(x...), my_test)
sort!(known_seat_ids)

println("Maximum Seat ID: ", max(known_seat_ids...))

missing_seat_index = argmax(known_seat_ids[2:end] .- known_seat_ids[1:end - 1])
println("Missing Seat: ", known_seat_ids[missing_seat_index] + 1)
