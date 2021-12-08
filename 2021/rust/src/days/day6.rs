fn solution1(fish: &mut Vec<i64>, days: i64) -> i64 {
    if days == 0 {
        return fish.len() as i64;
    }
    let count_zero = fish.iter().filter(|&&f| f == 0).count();
    fish.iter_mut()
        .for_each(|f| if *f == 0 { *f = 6 } else { *f -= 1 });
    // let mut new_fish = ;
    fish.append(&mut vec![8 as i64; count_zero]);
    // println!("{:?}", fish);
    solution1(fish, days - 1)
}

fn solution2(fish: &Vec<i64>, days: i64) -> i64 {
    let mut fish_list: Vec<i64> = vec![0; 9];
    // initialize
    for f in fish {
        fish_list[*f as usize] += 1;
    }
    println!("{:?}", fish_list);
    for i in 1..=days {
        let birthing = fish_list.remove(0);
        fish_list.push(birthing);
        fish_list[6] += birthing;
        // println!("{} {:?}", i, fish_list);
    }
    return fish_list.iter().sum();
}

pub fn day6(input: Vec<String>) {
    let mut initial_state: Vec<i64> = input[0]
        .split(",")
        .map(|x| x.parse::<i64>().unwrap())
        .collect();
    println!("Day 6 Part A: {}", solution2(&initial_state, 80));
    println!("Day 6 Part A: {}", solution2(&initial_state, 256))
}

#[test]
fn test_a() {
    let mut initial_state = vec![3, 4, 3, 1, 2];
    assert_eq!(solution1(&mut initial_state, 18), 26);
    // let mut initial_state = vec![3, 4, 3, 1, 2];
    assert_eq!(solution1(&mut initial_state, 80 - 18), 5934);
    let mut initial_state = vec![3, 4, 3, 1, 2];
    assert_eq!(solution2(&initial_state, 18), 26);
    assert_eq!(solution2(&initial_state, 80), 5934);
}
