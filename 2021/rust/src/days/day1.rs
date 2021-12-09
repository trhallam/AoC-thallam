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
        // println!("{:?}", window);
        let a: u16 = window[0..3].iter().sum();
        let b: u16 = window[1..4].iter().sum();
        // println!("{}, {}", a, b);
        if b > a {
            count += 1;
        }
    }
    println!("Slide 6: {}", count);
}

pub fn day1(input: Vec<String>) {
    let input_int = input.iter().map(|x| x.parse::<u16>().unwrap()).collect();
    slide2(&input_int);
    slide4(&input_int);
}
