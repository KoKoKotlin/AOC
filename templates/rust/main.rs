use std::fs;

fn load_data() -> Vec<String> {
    let data = fs::read_to_string("data.txt").expect("Couldn't load data!");
    
    let mut lines: Vec<String> = vec![];
    for line in data.split("\n") {
        lines.push(String::from(line));
    }

    lines
}

fn solve1(lines: &Vec<String>) {
    println!("Solution 1: {}", 0);
}


fn solve2(lines: &Vec<String>) {
    println!("Solution 2: {}", 0);
}


fn main() {
    let mut lines = load_data();
    solve1(&mut lines);
    solve2(&mut lines);
}