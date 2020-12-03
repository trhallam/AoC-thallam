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
    slope_navigator(spec, Array[String]; )

Check passwords are in spec for sled company

"""
function slope_navigator(slope::String, right::Int; down::Int=1)::Array{String}
    slope_split = [String(s) for s in split(slope, "\n")]
    path = String[]
    for (i, contour) in enumerate(slope_split[1:down:end])
        if contour == ""
            continue
        end
        index = 1 + (i - 1) * right
        contour_l = repeat_contour(contour, index)
        push!(path, contour_l[index:index])
    end
    return path
end

# Test 1
test = (
    "..##.........##.........##.........##.........##.........##.......\n" *
    "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..\n" *
    ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.\n" *
    "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#\n" *
    ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.\n" *
    "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....\n" *
    ".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#\n" *
    ".#........#.#........#.#........#.#........#.#........#.#........#\n" *
    "#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...\n" *
    "#...##....##...##....##...##....##...##....##...##....##...##....#\n" *
    ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#\n"
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
