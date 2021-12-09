fn direct_cost(a: &i32, b:&i32) -> i32 {(a - b).abs()}

fn triangle_cost(a: &i32, &b:&i32) -> i32 {let n = direct_cost(&a, &b); n*(n+1)/2}

fn optimize_fuel(horloc: &Vec<i32>, triangle: bool) -> (i32, i32) {

    let mut fuel_cost: i32 = std::i32::MAX;
    let cost_fn = if triangle {triangle_cost} else {direct_cost};
    let mut opt_pos:i32 = 0;
    let horloc_min: i32 = horloc.iter().copied().min().unwrap();
    let horloc_max: i32 = horloc.iter().copied().max().unwrap();


    for v in horloc_min..horloc_max {
        let v_rel_fuel_cost = horloc.iter().fold(0i32, |acc, x| acc + cost_fn(&x, &v));
        if fuel_cost > v_rel_fuel_cost  {fuel_cost = v_rel_fuel_cost; opt_pos = v}
    }

    return (opt_pos, fuel_cost)
}

pub fn day7(input: Vec<String>) {
    let my_input = input[0].split(",").map(|s| s.parse::<i32>().unwrap()).collect();
    let (opt_pos, fuel_cost) = optimize_fuel(&my_input, false);
    println!("Day 7 Part A: {} {}", opt_pos, fuel_cost);
    let (opt_pos, fuel_cost) = optimize_fuel(&my_input, true);
    println!("Day 7 Part B: {} {}", opt_pos, fuel_cost);
}

#[test]
fn test_direct_cost() {
    assert_eq!(direct_cost(&16, &5), 11);
    assert_eq!(direct_cost(&5, &16), 11);
}

#[test]
fn test_triangle_cost() {
    assert_eq!(triangle_cost(&16, &5), 66);
    assert_eq!(triangle_cost(&1, &5), 10);
}

#[test]
fn test_day7_ab() {
    let ex1: Vec<i32> = vec![16,1,2,0,4,2,7,1,2,14];
    assert_eq!(optimize_fuel(&ex1, false), (2, 37));
    assert_eq!(optimize_fuel(&ex1, true), (5, 168));
}