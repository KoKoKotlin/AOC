use std::collections::HashSet;

const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

fn find_first_n_distinct(msg: &str, n: usize) -> Option<usize> {
    for i in n..msg.len() {
        let slice = &msg[i - n..i];
        let hash_set: HashSet<char> = HashSet::from_iter(slice.chars());
        if hash_set.len() == n {
            return Some(i);
        }
    }

    None
}

fn main() {
    let data = INPUT.lines().nth(0).unwrap();
    println!("Solution 1: {}", find_first_n_distinct(data, 4).unwrap());
    println!("Solution 2: {}", find_first_n_distinct(data, 14).unwrap());
}
