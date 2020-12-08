"""
    parse_day8(input)

    Takes raw input from aoc and parses to row and column tuple.
"""
function parse_day8(input::AbstractString)::Tuple
    instructions = input |> 
        x -> split(x, "\n", keepempty=false) .|>
        x -> match(r"(\w{3})\s([+-])(\d+)$", x).captures |>
        x -> (x[1], x[2], parse(Int, x[3]))
    return tuple(instructions...)
end

function ops(op)
    if op == "+"
        return (x, y) -> x + y
    elseif op == "-"
        return (x, y) -> x - y
    end
end

"""
    new_boot(input; return_pos=false)

    This function executes the boot instructions using new operations.
"""
function new_boot(input::Tuple; return_pos::Bool=false)
    visited = zeros(Int, length(input))
    pos = 1
    acc = 0

    while true
        pos > length(input) ? break : ""

        visited[pos] += 1
        visited[pos] > 1 ? break : ""

        instr, op, val = input[pos]

        if instr == "acc"
            acc = ops(op)(acc, val)
            pos += 1
        elseif instr == "jmp"
            pos = ops(op)(pos, val)
        elseif instr == "nop"
            pos += 1
        end
    end

    if return_pos
        return (acc, pos)
    else
        return acc
    end
end


"""
    bad_instr_finder(input)

    Changes one instruction at a time to find the bad instruction.
"""
function bad_instr_finder(input)

    replacer = Dict("jmp" => "nop", "nop" => "jmp", "acc" => "acc")
    len_input = length(input)

    for (i, inp) in enumerate(input)
        check_input = [input...]
        cmd, op, val = inp
        check_input[i] = (replacer[cmd], op, val)
        acc, pos = new_boot(tuple(check_input...), return_pos=true)
        if pos >= len_input
            return acc
        end
    end
end