"""
    parse_day7(input)

    Takes raw input from aoc and parses to row and column tuple.
"""
function parse_day7(input::AbstractString)::Dict

    output = split(strip(input), "\n", keepempty=false) .|>
        x -> strip.(x) |> 
    x -> split.(x, " bags contain ")
    bag_dict = Dict()
    for bag in output
        if bag[2] == "no other bags."
            bag_dict[bag[1]] = Array([["0", "no other"]])
        else
            bag_dict[bag[1]] = [m.captures for m in eachmatch(r"(\d+)\s([\w\s]+)\sbag", bag[2])]
        end
    end

    for (bag, inner_bags) in bag_dict
        bag_dict[bag] = [tuple(parse(Int, ib[1]), ib[2]) for ib in inner_bags]
    end

    return bag_dict
end


"""
    contains_base(all_bags, bag; base="shiny gold")
"""
function contains_base(all_bags::Dict, bag::AbstractString; base::String="shiny gold")
    n, inner_bags = zip(all_bags[bag]...)
    if base in inner_bags
        return true
    elseif all_bags[bag][1][1] == 0
        return false
    else
        return reduce((c, n) -> c | contains_base(all_bags, n), inner_bags, init=false)
    end
end


"""
    how_many_inside(all_bags, bag)
"""
function how_many_inside(all_bags::Dict, bag::AbstractString)::Int
    nbags, inner_bags = zip(all_bags[bag]...)
    if sum(nbags) == 0
        return 0
    else
        return sum(
            [
                nbags[i] + nbags[i] * how_many_inside(all_bags, ib)
                for (i, ib) in enumerate(inner_bags)
            ]
        )
    end
end
