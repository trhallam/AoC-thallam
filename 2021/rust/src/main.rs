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

fn slide2(input: &Vec<u16>) {
    let mut count = 0;
    for window in input.windows(2) {
        if window[1] > window[0] {
            count += 1;
        }
    }
    println!("Slide 2: {}", count);
}

fn slide4(input: &Vec<u16>) {
    let mut count = 0;
    for window in input.windows(4) {
        println!("{:?}", window);
        let a: u16 = window[0..3].iter().sum();
        let b: u16 = window[1..4].iter().sum();
        println!("{}, {}", a, b);
        if b > a {
            count += 1;
        }
    }
    println!("Slide 6: {}", count);
}

fn day1(file: &str) {
    let input = lines_from_file(file); //.expect("Could not load lines");
    let input_int = input.iter().map(|x| x.parse::<u16>().unwrap()).collect();
    slide2(&input_int);
    slide4(&input_int);
}

//fn number_of_increases(input: Vec)

fn day2(file: &str) {
    let input = lines_from_file(file);
    let input_split: Vec<Vec<&str>> = input.iter().map(|x| x.split(" ").collect()).collect();
    println!("{:?}", input_split[0]);

    let mut hor: u32 = 0;
    let mut vert: u32 = 0;
    let mut depth: u32 = 0;

    for dir_dist in input_split.iter() {
        match dir_dist[0] {
            "up" => vert -= dir_dist[1].parse::<u32>().unwrap(),
            "down" => vert += dir_dist[1].parse::<u32>().unwrap(),
            "forward" => {
                hor += dir_dist[1].parse::<u32>().unwrap();
                depth += vert * dir_dist[1].parse::<u32>().unwrap();
            }
            _ => println!("Unknown Dir"),
        }
    }
    println!("hor: {}, vert: {}", hor, vert);
    println!("dist: {}", hor * vert);
    println!("dist2: {}", hor * depth)
}

fn filter_nth(a: Vec<String>, n: usize, mtch: char) -> Vec<String> {
    if a.len() == 1 {
        return a;
    };
    a.into_iter()
        .filter(|x| x.chars().nth(n).unwrap() == mtch)
        .collect()
}

fn one_count(a: &Vec<String>, n: usize) -> u32 {
    let out = a
        .iter()
        .filter(|x| x.chars().nth(n).unwrap() == '1')
        .count();

    return out as u32;
}

fn day3(file: &str) {
    let input = lines_from_file(file);
    let mut oxy = input.clone();
    let mut co2 = input.clone();
    let mut gamma = String::new();
    let mut epsilon = String::new();

    // find half size
    let half = (input.len() as u32) / 2;

    for i in 0..12 {
        let one_count_a = one_count(&input, i);
        let one_count_oxy = one_count(&oxy, i);
        let one_count_co2 = one_count(&co2, i);

        // part a
        if (one_count_a as u32) >= half {
            gamma.push('1');
            epsilon.push('0');
        } else {
            gamma.push('0');
            epsilon.push('1');
        }

        // part b
        if one_count_oxy >= (oxy.len() as u32) - one_count_oxy {
            oxy = filter_nth(oxy, i, '1');
        } else {
            oxy = filter_nth(oxy, i, '0');
        }

        if one_count_co2 < (co2.len() as u32) - one_count_co2 {
            co2 = filter_nth(co2, i, '1');
        } else {
            co2 = filter_nth(co2, i, '0');
        }
        println!(
            "{} {} {} {}",
            one_count_a,
            one_count_oxy,
            one_count_co2,
            one_count_co2 / 2
        )
    }
    let gamma_int = i32::from_str_radix(&gamma, 2).unwrap();
    let epsilon_int = i32::from_str_radix(&epsilon, 2).unwrap();
    let oxy_int = i32::from_str_radix(&oxy[0], 2).unwrap();
    let co2_int = i32::from_str_radix(&co2[0], 2).unwrap();

    println!("Gamma: {}", gamma_int);
    println!("Epsilong: {}", epsilon_int);
    println!("Power Usage: {}", gamma_int * epsilon_int);
    println!("{:?}", oxy);
    println!("{:?}", co2);
    println!("Oxy: {}", oxy_int);
    println!("Co2: {}", co2_int);
    println!("Oxy * Co2: {}", oxy_int * co2_int);

    // println!("{:?}", stack)
}

fn main() {
    let args: Vec<String> = env::args().collect();
    // println!("Day 1\n______");
    // day1(&args[1].to_string());
    // println!("Day 2\n_____");
    // day2(&args[1].to_string())
    println!("Day 3\n_____");
    day3(&args[1].to_string())
}

// "011111110010"
// "011111110111
