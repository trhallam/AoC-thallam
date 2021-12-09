pub fn day2(input: Vec<String>) {
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
