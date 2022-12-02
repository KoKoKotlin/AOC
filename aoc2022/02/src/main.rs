const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

fn handle_single_line(line: &str) -> u64 {
    let symbols = line.split(" ").collect::<Vec<&str>>();

    let opponent = symbols[0];
    let player = symbols[1];

    let points = match player {
        "X" => 1,
        "Y" => 2,
        "Z" => 3,
        _ => unreachable!(),
    } + match (player, opponent) {
        ("X", "A") => 3,
        ("X", "B") => 0,
        ("X", "C") => 6,
        ("Y", "A") => 6,
        ("Y", "B") => 3,
        ("Y", "C") => 0,
        ("Z", "A") => 0,
        ("Z", "B") => 6,
        ("Z", "C") => 3,
        _ => unreachable!(),
    };

    points
}

fn handle_single_line2(line: &str) -> u64 {
    let symbols = line.split(" ").collect::<Vec<&str>>();

    let opponent = symbols[0];
    let player = symbols[1];

    // A == rock (+1), B == paper (+2), C == scissors (+3)
    // X == loose, Y == draw, Z == win
    let points = match (player, opponent) {
        ("X", "A") => 0 + 3,
        ("X", "B") => 0 + 1,
        ("X", "C") => 0 + 2,
        ("Y", "A") => 3 + 1,
        ("Y", "B") => 3 + 2,
        ("Y", "C") => 3 + 3,
        ("Z", "A") => 6 + 2,
        ("Z", "B") => 6 + 3,
        ("Z", "C") => 6 + 1,
        _ => unreachable!(),
    };

    points
}

fn main() {
    let nums = INPUT
        .lines()
        .map(|line| handle_single_line(line))
        .collect::<Vec<u64>>();

    println!("Total Score 1: {}", nums.iter().sum::<u64>());

    let nums = INPUT
        .lines()
        .map(|line| handle_single_line2(line))
        .collect::<Vec<u64>>();

    println!("Total Score 2: {}", nums.iter().sum::<u64>());
}
