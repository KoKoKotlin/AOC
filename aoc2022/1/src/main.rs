const INPUT: &'static str = include_str!("input.txt");

fn main() {
    let mut elves: Vec<u32> = vec![];
    let mut current_elv: u32 = 0;
    for line in INPUT.lines() {
        if line.is_empty() {
            elves.push(current_elv);
            current_elv = 0;
        } else {
            current_elv += line.parse::<u32>().unwrap();
        }
    }

    println!("Max: {:?}", elves.iter().max().unwrap());

    elves.sort();
    println!(
        "Max three: {} + {} + {} = {}",
        elves[elves.len() - 3],
        elves[elves.len() - 2],
        elves[elves.len() - 1],
        elves[elves.len() - 3] + elves[elves.len() - 2] + elves[elves.len() - 1]
    );
}
