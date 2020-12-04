using Test
using PyCall

working_dir = @__DIR__
cd(working_dir)

py_aocd_models = pyimport("aocd.models")
puzzle = py_aocd_models.Puzzle(2020, 3)

"""
    repeat_contour(contour, String; req_len, Int)

    Repeats contour until <= req_len

"""
function repeat_contour(contour::String, req_len::Int)
    if (lastindex(contour) < req_len)
        return repeat_contour(contour * contour, req_len)
    else
        return contour
    end
end


"""
    slope_navigator(slope::String, right::Int; down::Int=1)::Array{String}

Return all the cells visited in the slop by traversing right and down from  cell (1,1).

"""
function slope_navigator(slope::String, right::Int; down::Int=1)::Array{String}
    slope_split = [String(s) for s in split(slope, "\n")]
    width = length(slope_split[1])
    path = String[]
    for (i, contour) in enumerate(slope_split[1:down:end])
        if contour == ""
            continue
        end
        index = 1 + mod((i - 1) * right, width)
        # contour_l = repeat_contour(contour, index)
        push!(path, contour[index:index])
    end
    return path
end

# Test 1
test = (
    "..##.......\n" *
    "#...#...#..\n" *
    ".#....#..#.\n" *
    "..#.#...#.#\n" *
    ".#...##..#.\n" *
    "..#.##.....\n" *
    ".#.#.#....#\n" *
    ".#........#\n" *
    "#.##...#...\n" *
    "#...##....#\n" *
    ".#..#...#.#\n"
)

slope_navigator(test, 3)

@testset "Tests" begin
    @testset "Test1" begin
        @test sum(slope_navigator(test, 3) .== "#") == 7
        @test count(==("#"), slope_navigator(test, 3)) == 7
    end
end

# AOCD Loading
my_test = puzzle.input_data

test_test = my_test |>
    replace(_, "." => "0") |>
    x -> replace(x, "#" => "1") |>
    x -> split(x, '\n') |>
    y -> [parse.(Int, split(x, "")) for x in y] |>
    x -> hcat(x...)

# Answer 1
println("Answer 1: ", count(==("#"), slope_navigator(my_test, 3)))

# # Answer 2
trees2 = Int[]
for (right, down) in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2])
    push!(
        trees2,
        count(==("#"), slope_navigator(my_test, right, down=down))
    )
end
println("Answer 2: ", prod(trees2))
