const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

#[derive(Debug)]
struct Rect {
    start_x: i32,
    end_x: i32,
    start_y: i32,
    end_y: i32,
}

fn parse_input(line: &str) -> Rect {
    let start = line.find("=").unwrap();
    let end = line.find(",").unwrap();
    let xs = line[start + 1..end]
        .split("..")
        .map(|token| token.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    let start = line.rfind("=").unwrap();
    let ys = line[start + 1..]
        .split("..")
        .map(|token| token.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    let (start_x, start_y, end_x, end_y);

    start_x = xs[0];
    end_x = xs[1];
    start_y = ys[0];
    end_y = ys[1];

    Rect {
        start_x,
        end_x,
        start_y,
        end_y,
    }
}

const MAX_ITER: usize = 1000;
const MAX_Y: i32 = 1000;
const MAX_X: i32 = 1000;

fn solve1(rect: &Rect) -> i32 {
    let range = rect.start_y..=rect.end_y;

    let mut res = 0;
    for start_vel_y in 1i32..MAX_Y {
        let mut pos_y = 0i32;
        let mut vel_y = start_vel_y;

        let mut i = 0;
        let mut greatest_y = 0;
        let mut is_valid = false;
        while i < MAX_ITER {
            pos_y += vel_y;
            if greatest_y < pos_y {
                greatest_y = pos_y;
            }

            if range.contains(&pos_y) {
                is_valid = true;
            }

            vel_y -= 1;
            i += 1;
        }

        if is_valid {
            res = greatest_y;
        }
    }

    res
}

fn solve2(rect: &Rect) -> u32 {
    let x_range = rect.start_x..=rect.end_x;
    let y_range = rect.start_y..=rect.end_y;

    let mut res: u32 = 0;

    let min_x = (0i32..MAX_X)
        .filter(|x| x_range.contains(&(x * (x + 1) / 2)))
        .min()
        .unwrap();
    let max_x = rect.end_x + 1;
    let min_y = rect.start_y - 1;
    for start_vel_x in min_x..max_x {
        for start_vel_y in min_y..MAX_Y {
            let mut pos_x = 0i32;
            let mut pos_y = 0i32;

            let mut vel_x = start_vel_x;
            let mut vel_y = start_vel_y;

            let mut i = 0;
            let mut is_valid = false;

            while i < MAX_ITER {
                pos_y += vel_y;
                pos_x += vel_x;

                if vel_x == 0 && !x_range.contains(&pos_x) {
                    break;
                }

                if y_range.contains(&pos_y) && x_range.contains(&pos_x) {
                    is_valid = true;
                    break;
                }

                vel_y -= 1;
                if vel_x != 0 {
                    vel_x += if vel_x < 0 { 1 } else { -1 };
                }
                i += 1;
            }

            if is_valid {
                res += 1;
                print!("{},{}\t", start_vel_x, start_vel_y);
                if res % 9 == 0 && res != 0 {
                    print!("\n");
                }
            }
        }
    }

    print!("\n");
    res
}

fn main() {
    let line = INPUT.lines().nth(0).unwrap();
    let target_rect = parse_input(line);

    println!("Solution 1: {}", solve1(&target_rect));
    println!("Solution 2: {}", solve2(&target_rect));
}
