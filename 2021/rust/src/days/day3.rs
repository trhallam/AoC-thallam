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

pub fn day3(input: Vec<String>) {
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
