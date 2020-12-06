"""
    parse_seats(input)

    Takes raw input from aoc and parses to row and column tuple.
"""
function parse_day5(input::AbstractString)::Array{Tuple{Int64,Int64},1}
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

"""
    as_seat_ids(scans)

    Map an array of scans::String to seat IDs
"""
as_seat_ids(scans) = map(x -> seat_id(x...), scans)

"""
    find_missing_seat(scans)

    Find the missing seat ID
"""
function find_missing_seat(scans)
    known_seat_ids = as_seat_ids(scans)
    sort!(known_seat_ids)
    missing_seat_index = argmax(known_seat_ids[2:end] .- known_seat_ids[1:end - 1])
    known_seat_ids[missing_seat_index] + 1
end