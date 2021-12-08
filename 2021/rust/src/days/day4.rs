#[derive(Clone)]
struct BingoBoard {
    plays: Vec<Vec<String>>,
}

impl BingoBoard {
    fn remove_number(&mut self, number: &str) {
        self.plays = self
            .plays
            .iter()
            .map(|pl| {
                pl.iter()
                    .filter(|x| *x != number)
                    .map(|s| s.to_string())
                    .collect::<Vec<String>>()
            })
            .collect();
    }

    fn check_plays(&self) -> bool {
        self.plays.iter().any(|pl| pl.is_empty())
    }

    fn get_unmarked(&mut self) -> Vec<String> {
        return self.plays[0..5]
            .iter()
            .cloned()
            .collect::<Vec<Vec<String>>>()
            .concat();
    }
}

pub fn day4(input: Vec<String>) {
    let bingo_numbers: Vec<&str> = input[0].split(",").collect();
    // println!("{:?}", bingo_numbers);

    let mut boards: Vec<BingoBoard> = Vec::new();
    for txt in input[1..input.len()].chunks(6) {
        let mut board = BingoBoard { plays: Vec::new() };
        // add row plays
        for play in txt[1..txt.len()].iter() {
            board.plays.push(
                play.split_whitespace()
                    .into_iter()
                    .map(|x| x.to_string())
                    .collect(),
            )
        }

        let joined: Vec<String> = txt
            .join(" ")
            .split_whitespace()
            .into_iter()
            .map(|x| x.to_string())
            .collect();

        // add column plays
        for i in 0..5 {
            board.plays.push(
                joined
                    .iter()
                    .clone()
                    .skip(i)
                    .step_by(5)
                    .map(|x| x.to_string())
                    .collect::<Vec<String>>(),
            )
        }
        boards.push(board.clone());
    }

    let mut results: Vec<u32> = Vec::new();

    for n in bingo_numbers.iter() {
        let mut finished_boards: Vec<usize> = Vec::new();
        for (i, board) in boards.iter_mut().enumerate() {
            board.remove_number(n);
            if board.check_plays() {
                let unmarked = board.get_unmarked();
                let unmarked_int: Vec<u32> =
                    unmarked.iter().map(|x| x.parse::<u32>().unwrap()).collect();
                //println!("Unmarked: {:?}", unmarked);
                let sum: u32 = unmarked_int.iter().sum();
                results.push(sum * n.parse::<u32>().unwrap());
                finished_boards.push(i);
                // println!("Day 4 Part1: {} * {}", n, result1);
                // println!("Day 4 Part1: {}", result1 ;
                // break;
            }
        }
        for i in finished_boards.into_iter().rev() {
            let _ = boards.remove(i);
        }
    }

    println!("Day 4 Part1: {}", results[0]);
    println!("Day 4 Part2: {:?}", results[results.len() - 1])
}
