using Test
using PyCall

working_dir = @__DIR__
cd(working_dir)

py_aocd_models = pyimport("aocd.models")
puzzle = py_aocd_models.Puzzle(2020, 4)

"""
    parse_batch_pp(batch)

    batch is the raw input string from AOC containing passports.

"""
function parse_batch_pp(batch::String)::Array{Dict}
    split_batch = split(batch, "\n\n") |> x -> replace.(x, "\n" => " ")
    passports = split.(split_batch)
    output = []
    for pass in passports
        ppd = Dict()
        for pair in pass
            key, val = split(pair, ":")
            ppd[key] = val
        end
        push!(output, ppd)
    end
    return output
end

"""
    check_is_superset(passport)

    Check the passport is a superset of the baseset.
"""
function check_is_superset(passport::Dict)::Bool
    is_superset = Set(keys(passport)) |>
        x -> issubset(Set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]), x)
end


"""
    check_height(height)
"""
function check_height(height::AbstractString)::Bool

    h = tryparse(Int, height[1:end - 2])
    if isnothing(h) return false end

    if endswith(height, "cm")
        return 150 <= h <= 193
    elseif endswith(height, "in")
        return 59 <= h <= 76
    else
        return false
    end
end


"""
    check_eyecol(ecl)
"""
function check_eyecol(ecl::AbstractString)::Bool
    ecl in Set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
end

"""
    check_year(year, minyr, maxyr)
"""
function check_year(year::AbstractString, minyr::Int, maxyr::Int)::Bool
    if ~length(year) == 4
        return False
    end

    year = tryparse(Int, year)
    if isnothing(year) return false end
    if ~(minyr <= year <= maxyr) return false end
    return true
end


"""
    check_haircol(hcl)
"""
function check_haircol(hcl)
    return isnothing(match(r"#[0-9a-fA-F]{6}", hcl)) ? false : true
end


"""
    check_pid(pid)
"""
function check_pid(pid)
    return isnothing(match(r"^\d{9}$", pid)) ? false : true
end


"""
    check_fields(passport)
"""
function check_fields(passport::Dict)::Bool

    if ~check_is_superset(passport) return false end

    return all([
        check_year(passport["byr"], 1920, 2002),
        check_year(passport["iyr"], 2010, 2020),
        check_year(passport["eyr"], 2020, 2030),
        check_height(passport["hgt"]),
        check_haircol(passport["hcl"]),
        check_eyecol(passport["ecl"]),
        check_pid(passport["pid"]),
    ])
end


# Test 1
test = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
"""

test_passports = parse_batch_pp(test)

@testset "Tests" begin
    @testset "Checks" begin
        @test sum([check_is_superset(pp) for pp in test_passports]) == 2
    end
    @testset "Frame Checks" begin
        @test check_year("2002", 1920, 2002)
        @test ~check_year("2003", 1920, 2002)
        @test check_height("60in")
        @test check_height("190cm")
        @test ~check_height("190in")
        @test ~check_height("190")
        @test check_eyecol("brn")
        @test ~check_eyecol("wat")
        @test check_haircol("#123abc")
        @test ~check_haircol("#123abz")
        @test ~check_haircol("123abc")
    end
end

# AOCD Loading
my_test = puzzle.input_data;

my_test_passports = parse_batch_pp(my_test)
println("Answer 1: ", sum([check_is_superset(pp) for pp in my_test_passports]))
println("Answer 2: ", sum([check_fields(pp) for pp in my_test_passports]))


