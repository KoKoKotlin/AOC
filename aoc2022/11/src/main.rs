use std::str::FromStr;

const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

#[derive(Debug)]
struct Monkey {
    items: Vec<u64>,
    inspections: u64,
    op_type: OperationType,
    operand: u64,
    test_num: u64,
    test_fail_idx: usize,
    test_succ_idx: usize,
}

#[derive(Debug)]
enum OperationType {
    OpMul,
    OpAdd,
    SelfMul,
    SelfAdd,
}

fn parse_last_num<T: FromStr>(line: &str) -> T {
    match line.split(" ").last().unwrap().parse::<T>() {
        Ok(num) => num,
        Err(_) => panic!("Cannot parse last num from: {}", line),
    }
}

fn parse(input: &str) -> Vec<Monkey> {
    let mut lines = input.lines().peekable();
    let mut monkeys: Vec<Monkey> = vec![];
    while lines.peek().is_some() {
        let _ = lines.next().unwrap();
        let items = lines
            .next()
            .unwrap()
            .split(":")
            .nth(1)
            .unwrap()
            .trim()
            .split(", ")
            .map(|token| token.parse::<u64>().unwrap())
            .collect::<Vec<u64>>();

        let operation = lines.next().unwrap();

        let op_type = if operation.contains("old * old") {
            OperationType::SelfMul
        } else if operation.contains("old + old") {
            OperationType::SelfAdd
        } else if operation.contains("*") {
            OperationType::OpMul
        } else {
            OperationType::OpAdd
        };

        let operand = match op_type {
            OperationType::SelfMul | OperationType::SelfAdd => 0,
            OperationType::OpMul | OperationType::OpAdd => parse_last_num(operation),
        };
        let test_num = parse_last_num(lines.next().unwrap());
        let test_succ_idx = parse_last_num(lines.next().unwrap());
        let test_fail_idx = parse_last_num(lines.next().unwrap());
        let _ = lines.next();

        monkeys.push(Monkey {
            items,
            inspections: 0,
            op_type,
            operand,
            test_num,
            test_fail_idx,
            test_succ_idx,
        })
    }

    monkeys
}

impl Monkey {
    fn operate(&self, x: u64) -> u64 {
        match self.op_type {
            OperationType::OpMul => x * self.operand,
            OperationType::OpAdd => x + self.operand,
            OperationType::SelfMul => x * x,
            OperationType::SelfAdd => x + x,
        }
    }
}

fn main() {
    let mut monkeys = parse(INPUT);

    for round in 0..20 {
        for idx in 0..monkeys.len() {
            let monkey = &mut monkeys[idx];
            let new_items = monkey
                .items
                .iter()
                .map(|x| monkey.operate(x.clone()) / 3)
                .collect::<Vec<u64>>();
            let next_idx = new_items
                .iter()
                .map(|x| {
                    if x % monkey.test_num == 0 {
                        monkey.test_succ_idx
                    } else {
                        monkey.test_fail_idx
                    }
                })
                .collect::<Vec<usize>>();
            monkey.inspections += new_items.len() as u64;
            monkey.items.clear();
            new_items
                .iter()
                .zip(next_idx.iter())
                .for_each(|(item, idx)| {
                    let monkey = &mut monkeys[*idx];
                    monkey.items.push(*item);
                });
        }
    }

    let mut inspections = monkeys
        .iter()
        .map(|monkey| monkey.inspections)
        .collect::<Vec<u64>>();
    inspections.sort();
    println!(
        "Solution 1: {}",
        inspections[inspections.len() - 1] * inspections[inspections.len() - 2]
    );

    let mut monkeys = parse(INPUT);

    let mod_number = monkeys
        .iter()
        .fold(1u64, |acc, monkey| acc * monkey.test_num);

    for round in 0..10000 {
        for idx in 0..monkeys.len() {
            let monkey = &mut monkeys[idx];
            let new_items = monkey
                .items
                .iter()
                .map(|x| monkey.operate(x.clone()) % mod_number)
                .collect::<Vec<u64>>();
            let next_idx = new_items
                .iter()
                .map(|x| {
                    if x % monkey.test_num == 0 {
                        monkey.test_succ_idx
                    } else {
                        monkey.test_fail_idx
                    }
                })
                .collect::<Vec<usize>>();
            monkey.inspections += new_items.len() as u64;
            monkey.items.clear();
            new_items
                .iter()
                .zip(next_idx.iter())
                .for_each(|(item, idx)| {
                    let monkey = &mut monkeys[*idx];
                    monkey.items.push(*item);
                });
        }
    }

    let mut inspections = monkeys
        .iter()
        .map(|monkey| monkey.inspections)
        .collect::<Vec<u64>>();
    inspections.sort();
    println!(
        "Solution 2: {}",
        inspections[inspections.len() - 1] * inspections[inspections.len() - 2]
    );
}
