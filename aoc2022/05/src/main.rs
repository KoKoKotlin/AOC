use std::collections::VecDeque;

const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

#[derive(Debug)]
struct Instruction {
    amount: u32,
    start: u32,
    dest: u32,
}

type Stacks = Vec<VecDeque<char>>;

fn parse_stacks(stack_data: &str) -> Stacks {
    let lines = stack_data.split("\n").collect::<Vec<&str>>();
    let last_line = lines[lines.len() - 1];
    let stack_count = last_line
        .trim()
        .split("   ")
        .map(|token| token.parse::<u32>().unwrap())
        .max()
        .unwrap();

    let mut stacks: Stacks = vec![VecDeque::new(); stack_count as usize];
    let lines = &lines[..lines.len() - 1];

    for i in 0..lines.len() {
        let idx = lines.len() - 1 - i;

        for (c_idx, c) in lines[idx].chars().enumerate() {
            if c.is_alphabetic() {
                let stack_idx = (c_idx - 1) / 4;
                stacks[stack_idx].push_front(c);
            }
        }
    }

    stacks
}

fn parse_inst(inst_data: &str) -> Vec<Instruction> {
    inst_data
        .lines()
        .map(|line| {
            let nums = line
                .split(" ")
                .filter(|token| token.parse::<u32>().is_ok())
                .map(|digit| digit.parse::<u32>().unwrap())
                .collect::<Vec<u32>>();

            Instruction {
                amount: nums[0],
                start: nums[1] - 1,
                dest: nums[2] - 1,
            }
        })
        .collect::<Vec<Instruction>>()
}

fn parse_input(input: &str) -> (Stacks, Vec<Instruction>) {
    let mut lines = input.split("\n\n");
    let stacks = lines.nth(0).unwrap();
    let instructions = lines.nth(0).unwrap();
    let stacks = parse_stacks(stacks);
    let instructions = parse_inst(instructions);

    (stacks, instructions)
}

fn main() {
    let (mut stacks, instructions) = parse_input(INPUT);

    for inst in instructions {
        for _ in 0..inst.amount {
            let start = &mut stacks[inst.start as usize];
            let elem = start.pop_front().unwrap();
            drop(start);
            let dest = &mut stacks[inst.dest as usize];
            dest.push_front(elem);
        }
    }

    print!("Solution 1: ");
    for stack in stacks.iter_mut() {
        print!("{}", stack.pop_front().unwrap());
    }
    print!("\n");

    let (mut stacks, instructions) = parse_input(INPUT);

    for inst in instructions {
        let mut stack = VecDeque::new();
        for _ in 0..inst.amount {
            let start = &mut stacks[inst.start as usize];
            let elem = start.pop_front().unwrap();
            stack.push_front(elem);
        }

        for _ in 0..inst.amount {
            let dest = &mut stacks[inst.dest as usize];
            dest.push_front(stack.pop_front().unwrap());
        }
    }

    print!("Solution 2: ");
    for stack in stacks.iter_mut() {
        print!("{}", stack.pop_front().unwrap());
    }
    print!("\n");
}
