use std::ops::Range;

const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

fn range_contained(first: &Range<u32>, second: &Range<u32>) -> bool {
    first.contains(&second.start) && first.contains(&(second.end - 1))
}

fn range_overlaps(first: &Range<u32>, second: &Range<u32>) -> bool {
    first.contains(&second.start)
        || first.contains(&(second.end - 1))
        || second.contains(&first.start)
        || second.contains(&(first.end - 1))
}

fn parse(line: &str) -> (Range<u32>, Range<u32>) {
    let mut ranges = line
        .split(",")
        .map(|token| {
            let nums = token
                .split("-")
                .map(|num| num.parse::<u32>().unwrap())
                .collect::<Vec<u32>>();
            nums[0]..nums[1] + 1
        })
        .collect::<Vec<Range<u32>>>();

    (ranges.remove(0), ranges.remove(0))
}

fn main() {
    let res = INPUT
        .lines()
        .map(parse)
        .filter(|(r1, r2)| range_contained(r1, r2) || range_contained(r2, r1))
        .count();

    println!("Solution 1: {}", res);

    let res = INPUT
        .lines()
        .map(parse)
        .filter(|(r1, r2)| range_overlaps(r1, r2))
        .count();

    println!("Solution 1: {}", res);
}
