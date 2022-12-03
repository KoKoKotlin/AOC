use std::collections::HashSet;

// const INPUT: &'static str = include_str!("test_input.txt");
const INPUT: &'static str = include_str!("input.txt");

fn str_to_set(s: &str) -> HashSet<char> {
    let mut hash_set: HashSet<char> = HashSet::new();
    for c in s.chars() {
        hash_set.insert(c);
    }

    hash_set
}

fn char_to_num(c: char) -> u32 {
    if c.is_ascii_lowercase() {
        c as u32 - 'a' as u32 + 1
    } else {
        (c as u32 - 'A' as u32) + 27
    }
}

fn handle_line(line: &str) -> u32 {
    let len = line.len();
    let hash_set1 = str_to_set(&line[0..len / 2]);
    let hash_set2 = str_to_set(&line[len / 2..len]);
    let inter_set = hash_set1.intersection(&hash_set2);

    let c = inter_set.into_iter().nth(0).unwrap();
    char_to_num(*c)
}

fn handle_lines(line1: &str, line2: &str, line3: &str) -> u32 {
    let hash_set1 = str_to_set(line1);
    let hash_set2 = str_to_set(line2);
    let hash_set3 = str_to_set(line3);

    let temp = hash_set1
        .intersection(&hash_set2)
        .map(|c| *c)
        .collect::<HashSet<char>>();
    let inter_set = temp.intersection(&hash_set3);

    let c = inter_set.into_iter().nth(0).unwrap();
    char_to_num(*c)
}

fn main() {
    let res = INPUT.lines().map(|line| handle_line(line)).sum::<u32>();
    println!("Solution 1: {}", res);

    let lines = INPUT.lines().collect::<Vec<&str>>();
    let range1 = (0..lines.len()).step_by(3).into_iter();
    let range2 = (1..lines.len()).step_by(3).into_iter();
    let range3 = (2..lines.len()).step_by(3).into_iter();
    let res: u32 = range1
        .zip(range2)
        .zip(range3)
        .map(|((i1, i2), i3)| handle_lines(lines[i1], lines[i2], lines[i3]))
        .sum();
    println!("Solution 2: {}", res);
}
