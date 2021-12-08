use regex::Regex;
use std::collections::HashMap;

#[derive(PartialEq, Eq, Hash, Debug)]
struct Coord {
    x: u32,
    y: u32,
}

struct VentMap {
    count_map: HashMap<Coord, u32>,
}

impl VentMap {
    fn new(vent_lines: Vec<String>) -> Self {
        let mut count = HashMap::new();

        let lines = vent_lines.into_iter().map(|x| String::from(x)).collect();
        let proc = process_input(lines);
        let coords = get_coords(proc);

        for coord in coords.into_iter() {
            *count.entry(coord).or_insert(0) += 1
        }

        Self { count_map: count }
    }

    fn danger_count(&self) -> u32 {
        let mut dc: u32 = 0;
        for (_, val) in self.count_map.iter() {
            if val >= &(2 as u32) {
                dc += 1
            }
        }
        return dc;
    }
}

fn good_range(a: u32, b: u32) -> Vec<u32> {
    if a < b {
        return (a..=b).map(|x| x as u32).collect();
    } else {
        return (b..=a).map(|x| x as u32).collect();
    }
}

// Take the input Vector of lines and convert to sequence of numbers.
fn process_input(input: Vec<String>) -> Vec<u32> {
    let re = Regex::new(r"(\d+),(\d+) -> (\d+),(\d+)").unwrap();
    let mut output: Vec<u32> = Vec::new();
    for line in input.iter() {
        let groups = re.captures(line).unwrap();
        let mut sub = groups
            .iter()
            .skip(1)
            .map(|cap| cap.unwrap().as_str().parse::<u32>().unwrap())
            .collect::<Vec<u32>>();
        output.append(&mut sub);
        // println!("h {:?}", output);
    }
    return output;
}

fn get_coords(vals: Vec<u32>) -> Vec<Coord> {
    let mut coords: Vec<Coord> = Vec::new();
    for vset in vals.chunks_exact(4) {
        if vset[0] == vset[2] {
            for i in good_range(vset[1], vset[3]) {
                coords.push(Coord { x: vset[0], y: i })
            }
        } else if vset[1] == vset[3] {
            for i in good_range(vset[0], vset[2]) {
                coords.push(Coord { x: i, y: vset[1] })
            }
        }
    }
    return coords;
}

pub fn day5(input: Vec<String>) {
    let vm = VentMap::new(input);
    println!("Day 5 Part 1: {:?}", vm.danger_count());
}

#[test]
fn test_a() {
    let raw_lines = vec![
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ];
    let lines = raw_lines.into_iter().map(|x| String::from(x)).collect();
    let proc = process_input(lines);
    let coords = get_coords(proc);
    println!("{:?}", coords);
    // assert!(
    //     coords
    //         == vec![
    //             Coord { x: 0, y: 2 },
    //             Coord { x: 0, y: 3 },
    //             Coord { x: 0, y: 4 }
    //         ]
    // )
    assert!(false)
}
