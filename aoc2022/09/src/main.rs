use std::collections::HashSet;

const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

#[derive(Debug)]
enum Dir {
    Right,
    Left,
    Up,
    Down,
}

#[derive(Debug)]
struct Instruction {
    dir: Dir,
    amount: i32,
}

impl Instruction {
    fn execute(&self, head_pos: &mut Position, tail_pos: &mut Vec<Position>) -> Vec<Position> {
        let mut tail_positions = vec![];

        let (dx, dy) = match self.dir {
            Dir::Right => (1, 0),
            Dir::Left => (-1, 0),
            Dir::Up => (0, -1),
            Dir::Down => (0, 1),
        };

        for _ in 0..self.amount {
            head_pos.move_pos(dx, dy);
            tail_pos[0].follow(head_pos);
            for i in 0..tail_pos.len() - 1 {
                let head = tail_pos[i];
                tail_pos[i + 1].follow(&head);
            }
            tail_positions.push(tail_pos[tail_pos.len() - 1].clone());
        }

        tail_positions
    }
}

#[derive(Copy, Clone, Debug, PartialEq, Eq, Hash)]
struct Position {
    x: i32,
    y: i32,
}

impl Position {
    fn is_adjacent(&self, other: &Position) -> bool {
        (self.x - other.x).abs() <= 1 && (self.y - other.y).abs() <= 1
    }

    fn move_pos(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }

    fn follow(&mut self, other: &Position) {
        if !self.is_adjacent(other) {
            if self.x == other.x {
                let dy = other.y - self.y;
                self.move_pos(0, dy.signum());
            } else if self.y == other.y {
                let dx = other.x - self.x;
                self.move_pos(dx.signum(), 0);
            } else {
                let dy = other.y - self.y;
                let dx = other.x - self.x;
                self.move_pos(dx.signum(), dy.signum());
            }
        }
    }
}

fn parse_line(line: &str) -> Instruction {
    let parts = line.split(" ").collect::<Vec<&str>>();
    let dir = match parts[0] {
        "R" => Dir::Right,
        "L" => Dir::Left,
        "U" => Dir::Up,
        "D" => Dir::Down,
        _ => unreachable!(),
    };
    let amount = parts[1].parse::<i32>().unwrap();

    Instruction { dir, amount }
}

fn main() {
    let mut head_pos = Position { x: 0, y: 0 };
    let mut tail_pos = vec![Position { x: 0, y: 0 }];
    let mut tail_positions = HashSet::new();
    INPUT.lines().map(parse_line).for_each(|inst| {
        let new_tail_positions = inst.execute(&mut head_pos, &mut tail_pos);
        tail_positions.extend(new_tail_positions);
    });

    println!("Solution 1: {}", tail_positions.len());

    let mut head_pos = Position { x: 0, y: 0 };
    let mut tail_pos = vec![Position { x: 0, y: 0 }; 9];
    let mut tail_positions = HashSet::new();
    INPUT.lines().map(parse_line).for_each(|inst| {
        let new_tail_positions = inst.execute(&mut head_pos, &mut tail_pos);
        tail_positions.extend(new_tail_positions);
    });

    println!("Solution 2: {}", tail_positions.len());
}
