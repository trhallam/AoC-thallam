using DataStructures

"""
    parse_day10(input)

    Takes raw input from aoc and parses to row and column tuple.
"""
function parse_day10(input::AbstractString)
    instructions = input |> 
        x -> split(x, "\n", keepempty=false) |> x -> parse.(Int, x)
    return instructions
end

function count_sequence_lengths(arr)
    one_ntuples = DefaultDict{Int,Int}(0)
    is_1 = false
    num_1s = 0
    for i in arr
        if i == 1
            is_1 = true
            num_1s += 1
        else
            is_1 = false
            one_ntuples[num_1s] += 1
            num_1s = 0
        end
    end
    one_ntuples
end

function day_10part2(data)

    data = vcat([0], data, [maximum(data) + 3])
    diffs = data |> sort |> diff
    # must find all sequences with multiple 1 next to each other, there can be leavout
    one_ntuples = count_sequence_lengths(diffs)
    num_leavouts = 1
    for (key, val) in one_ntuples
        key < 2 && continue
        println(key, " ", val, " ", binomial(key - 1, 1), " ", binomial(key - 1, 2))
        num_leavouts *= (binomial(key - 1, 1) + binomial(key - 1, 2) + 1)^val
    end

    num_leavouts
end