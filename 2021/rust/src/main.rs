mod days {
    automod::dir!(pub "src/days");
}

use std::{
    env,
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let day = &args[1].parse::<u16>().unwrap();
    let input_file = format!("inputs/2021-{}.txt", day);
    println!("AOCD 2021 Day {}\n Loading input from: {}", day, input_file);
    let input = lines_from_file(input_file);

    match day {
        1 => days::day1::day1(input),
        2 => days::day2::day2(input),
        3 => days::day3::day3(input),
        4 => days::day4::day4(input),
        5 => days::day5::day5(input),
        6 => days::day6::day6(input),
        7 => days::day7::day7(input),
        _ => println!("Unknown Day"),
    }
    // println!("Day 1\n______");
    // day1(&args[1].to_string());
    // println!("Day 2\n_____");
    // day2(&args[1].to_string())
    // println!("Day 3\n_____");
    // day3(&args[1].to_string())

    // let a = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    // let b: Vec<&char> = a.iter().skip(2).step_by(2).collect();
    // println!("{:?}", b);

    // let a = "abcdefghi";
}

// "011111110010"
// "011111110111
