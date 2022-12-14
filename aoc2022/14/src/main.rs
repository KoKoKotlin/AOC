use std::cmp::{max, min};

const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

const ARENA_WIDTH: u64 = 1000;
const ARENA_HEIGHT: u64 = 1000;

#[derive(Debug, Clone, PartialEq, Eq)]
enum State {
    Free,
    Blocked,
}

fn conv_idx(x: u64, y: u64) -> usize {
    (x + ARENA_WIDTH * y) as usize
}

fn parse(line: &str, arena: &mut Vec<State>) -> u64 {
    let points = line
        .split(" -> ")
        .map(|token| {
            token
                .split(",")
                .map(|num| num.parse::<u64>().unwrap())
                .collect::<Vec<u64>>()
        })
        .collect::<Vec<Vec<u64>>>();

    let mut curr_x = points[0][0];
    let mut curr_y = points[0][1];
    let mut max_y = 0;
    for point in points.iter().skip(1) {
        let next_x = point[0];
        let next_y = point[1];

        if next_y > max_y {
            max_y = next_y;
        }

        if curr_y == next_y {
            let x_start = min(curr_x, next_x);
            let x_end = max(curr_x, next_x);
            for x in x_start..=x_end {
                arena[conv_idx(x, curr_y)] = State::Blocked;
            }
        } else if curr_x == next_x {
            let y_start = min(curr_y, next_y);
            let y_end = max(curr_y, next_y);
            for y in y_start..=y_end {
                arena[conv_idx(curr_x, y)] = State::Blocked;
            }
        } else {
            unreachable!();
        }

        curr_x = next_x;
        curr_y = next_y;
    }
    max_y
}

fn make_floor(arena: &mut Vec<State>, y: u64) {
    for x in 0..ARENA_WIDTH {
        arena[conv_idx(x, y)] = State::Blocked;
    }
}

#[derive(Debug)]
enum DirFree {
    Left,
    Right,
    Free,
    Blocked,
}

fn collision_check(arena: &Vec<State>, x: u64, y: u64) -> DirFree {
    if arena[conv_idx(x, y)] == State::Free {
        DirFree::Free
    } else if arena[conv_idx(x - 1, y)] == State::Free {
        DirFree::Left
    } else if arena[conv_idx(x + 1, y)] == State::Free {
        DirFree::Right
    } else {
        DirFree::Blocked
    }
}

fn solve1(arena: &mut Vec<State>) -> u64 {
    let start_x = 500;
    let start_y = 0;

    let mut i = 0;
    loop {
        let mut curr_x = start_x;
        let mut curr_y = start_y;
        let mut end = false;
        loop {
            curr_y += 1;

            if curr_y >= ARENA_HEIGHT {
                end = true;
                break;
            }

            let res = collision_check(arena, curr_x, curr_y);
            match res {
                DirFree::Free => {}
                DirFree::Left => curr_x -= 1,
                DirFree::Right => curr_x += 1,
                DirFree::Blocked => {
                    curr_y -= 1;
                    break;
                }
            }
        }

        if end {
            break;
        }

        arena[conv_idx(curr_x, curr_y)] = State::Blocked;
        i += 1;
    }

    i
}

fn solve2(arena: &mut Vec<State>) -> u64 {
    let start_x = 500;
    let start_y = 0;

    let mut i = 0;
    loop {
        let mut curr_x = start_x;
        let mut curr_y = start_y;
        loop {
            curr_y += 1;

            let res = collision_check(arena, curr_x, curr_y);
            match res {
                DirFree::Free => {}
                DirFree::Left => curr_x -= 1,
                DirFree::Right => curr_x += 1,
                DirFree::Blocked => {
                    curr_y -= 1;
                    if curr_y == 0 {
                        return i + 1;
                    }
                    break;
                }
            }
        }

        arena[conv_idx(curr_x, curr_y)] = State::Blocked;
        i += 1;
    }
}

fn main() {
    let mut arena = vec![State::Free; (ARENA_WIDTH * ARENA_HEIGHT) as usize];
    INPUT.lines().map(|line| parse(line, &mut arena)).max();

    println!("Solution 1: {}", solve1(&mut arena));

    let mut arena = vec![State::Free; (ARENA_WIDTH * ARENA_HEIGHT) as usize];
    let max_y = INPUT
        .lines()
        .map(|line| parse(line, &mut arena))
        .max()
        .unwrap();
    make_floor(&mut arena, max_y + 2);

    println!("Solution 2: {}", solve2(&mut arena));
}
