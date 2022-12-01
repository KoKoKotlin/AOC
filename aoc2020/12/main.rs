use std::{fmt::Debug, str::FromStr};

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Dir {
    North,
    East,
    South,
    West,
    Forward,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, Ord, PartialOrd)]
enum FacingDir {
    North,
    East,
    South,
    West,
}

#[derive(Debug)]
enum RotationDir {
    Left,
    Right,
}

#[derive(Debug)]
enum Instruction {
    Move(Dir, u16),
    Rotation(RotationDir, u16),
}

#[derive(Debug)]
struct Ship {
    posX: i32,
    posY: i32,
    facing_dir: FacingDir,
}

#[derive(Debug)]
struct Waypoint {
    posX: i32,
    posY: i32,
}

fn parser_expect<U, V>(res: Result<U, V>, input_str: &str) -> U
where
    V: Debug,
{
    res.expect(format!("Error while parsing {}!", input_str).as_str())
}

impl FromStr for Instruction {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let opcode = &s[0..1];
        let number = &s[1..];

        match opcode {
            "N" | "S" | "E" | "W" | "F" => {
                let dir = parser_expect(Dir::from_str(opcode), opcode);
                let number = parser_expect(number.parse::<u16>(), number);
                Ok(Instruction::Move(dir, number))
            }
            "R" | "L" => {
                let rot_dir = parser_expect(RotationDir::from_str(opcode), opcode);
                let number = parser_expect(number.parse::<u16>(), number);
                Ok(Instruction::Rotation(rot_dir, number))
            }
            _ => Err(()),
        }
    }
}

impl Into<Dir> for FacingDir {
    fn into(self) -> Dir {
        match self {
            FacingDir::North => Dir::North,
            FacingDir::East => Dir::East,
            FacingDir::South => Dir::South,
            FacingDir::West => Dir::West,
        }
    }
}

fn rotate(x: i32, y: i32, angle: i32) -> (i32, i32) {
    match angle {
        -270 | 90 => (-y, x),
        -180 | 180 => (-x, -y),
        -90 | 270 => (y, -x),
        _ => unreachable!(),
    }
}

impl Instruction {
    fn execute(&self, ship: &mut Ship) {
        let dirs = vec![
            FacingDir::North,
            FacingDir::East,
            FacingDir::South,
            FacingDir::West,
        ];
        match &self {
            &Instruction::Move(dir, amount) => {
                let dir: Dir = if *dir != Dir::Forward {
                    *dir
                } else {
                    ship.facing_dir.into()
                };
                match dir {
                    Dir::North => {
                        ship.posY += *amount as i32;
                    }
                    Dir::East => {
                        ship.posX += *amount as i32;
                    }
                    Dir::South => {
                        ship.posY -= *amount as i32;
                    }
                    Dir::West => {
                        ship.posX -= *amount as i32;
                    }
                    _ => {
                        unreachable!();
                    }
                }
            }
            &Instruction::Rotation(dir, amount) => {
                let offset: i32 = match dir {
                    &RotationDir::Left => match amount {
                        90 => -1,
                        180 => -2,
                        270 => -3,
                        _ => {
                            unreachable!()
                        }
                    },
                    &RotationDir::Right => match amount {
                        90 => 1,
                        180 => 2,
                        270 => 3,
                        _ => {
                            unreachable!()
                        }
                    },
                };
                let current_dir_index = dirs.binary_search(&ship.facing_dir).unwrap();
                let new_index = current_dir_index as i32 + offset;
                let new_index = if new_index < 0 {
                    new_index + 4
                } else {
                    new_index % 4
                };
                let new_dir = dirs[new_index as usize];
                ship.facing_dir = new_dir;
            }
        }
    }

    fn execute2(&self, ship: &mut Ship, waypoint: &mut Waypoint) {
        match &self {
            &Instruction::Move(dir, amount) => match dir {
                Dir::North => {
                    waypoint.posY += *amount as i32;
                }
                Dir::East => {
                    waypoint.posX += *amount as i32;
                }
                Dir::South => {
                    waypoint.posY -= *amount as i32;
                }
                Dir::West => {
                    waypoint.posX -= *amount as i32;
                }
                Dir::Forward => {
                    ship.posX += (*amount as i32) * waypoint.posX;
                    ship.posY += (*amount as i32) * waypoint.posY;
                }
            },
            &Instruction::Rotation(dir, amount) => {
                let rotated_pos = match dir {
                    RotationDir::Left => rotate(waypoint.posX, waypoint.posY, *amount as i32),
                    RotationDir::Right => rotate(waypoint.posX, waypoint.posY, -(*amount as i32)),
                };
                waypoint.posX = rotated_pos.0;
                waypoint.posY = rotated_pos.1;
            }
        }
    }
}

impl FromStr for Dir {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "N" => Ok(Dir::North),
            "E" => Ok(Dir::East),
            "S" => Ok(Dir::South),
            "W" => Ok(Dir::West),
            "F" => Ok(Dir::Forward),
            _ => Err(()),
        }
    }
}

impl FromStr for RotationDir {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "L" => Ok(RotationDir::Left),
            "R" => Ok(RotationDir::Right),
            _ => Err(()),
        }
    }
}

const input: &'static str = include_str!("input.txt");
// const input: &'static str = include_str!("test_input.txt");

fn abs(x: i32) -> i32 {
    if x < 0 {
        -x
    } else {
        x
    }
}

fn main() {
    let instructions: Vec<Instruction> = input
        .lines()
        .map(|x| Instruction::from_str(x).unwrap())
        .collect();

    let mut ship = Ship {
        posX: 0,
        posY: 0,
        facing_dir: FacingDir::East,
    };

    for instruction in instructions.iter() {
        instruction.execute(&mut ship);
    }

    let x = abs(ship.posX);
    let y = abs(ship.posY);
    println!("{:?}, 1Norm ship pos: {}", ship, x + y);

    let mut ship = Ship {
        posX: 0,
        posY: 0,
        facing_dir: FacingDir::East,
    };

    let mut waypoint = Waypoint { posX: 10, posY: 1 };

    for instruction in instructions {
        instruction.execute2(&mut ship, &mut waypoint);
        println!("{:?}, {:?}, {:?}", instruction, ship, waypoint);
    }
    let x = abs(ship.posX);
    let y = abs(ship.posY);
    println!("{:?}, {:?}, 1Norm waypoint pos: {}", ship, waypoint, x + y);
}
