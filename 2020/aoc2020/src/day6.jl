"""
    parse_day6(input)

    Takes raw input from aoc and parses to row and column tuple.
"""
function parse_day6(input::AbstractString)::Array{Array}
    input = split(input, "\n\n", keepempty=false) .|>
        x -> split.(x)
end

"""
    nunique(group)

    Just find all unique values in each group.
"""
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
allsayyes(group) = sum([Set.(g) for g in group] .|> x -> intersect(x...) |> x -> length(x))
# allsayyes(group) = sum(length.(reduce.((c, n) -> allset, group, init=Set(collect('a':'z')))))
# with direct sets
