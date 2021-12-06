use std::fs;

fn load_data() -> Vec<String> {
    let data = fs::read_to_string("data.txt").expect("Couldn't load data!");
    
    let mut lines: Vec<String> = vec![];
    for line in data.split("\n") {
        lines.push(String::from(line));
    }

    lines
}

fn count_neighbours(state: &Vec<String>, pos_x: i64, pos_y: i64) -> usize {
    let line_len = state[0].len();
    let len = state.len();

    let mut n = 0;

    for y_off in -1..1 {
        for x_off in -1..1 {
            let x = (pos_x + x_off) as usize;
            let y = (pos_y + y_off) as usize;

            if (0..line_len).contains(&x) && (0..len).contains(&y) && state[y].chars().nth(x).take().unwrap() == '#' {
                n += 1;
            }
        }
    }

    n
}

fn make_step(state: &Vec<String>) -> Vec<String> {
    let line_len = state[0].len();
    let mut newState = vec![String::with_capacity(line_len); state.len()];
    
    for y in 0..(state.len()) {
        for x in 0..line_len {
            let n = count_neighbours(state, x as i64, y as i64);
            let c = if n == 0 { '#' } else if n >= 4 { 'L' } else { state[y].chars().nth(x).take().unwrap() };          
            newState[y].insert(x, c); 
        }
    }

    newState
}

fn compare_state(state1: &Vec<String>, state2: &Vec<String>) -> bool {
    for i in 0..state1.len() {
        if !(*state1[i]).eq(&state2[i]) {
            return false;
        }
    }

    true
}

fn solve1(lines: &Vec<String>) {

    let mut state = (*lines).clone();
    let mut new_state = make_step(&state);

    while !compare_state(&state, &new_state) {
        let temp = make_step(&state);
        state = new_state;
        new_state = temp;
    }

    let mut occupied = 0;
    for line in state.iter() {
        occupied += line.chars().filter(|c| c == &'#').count();
    }

    println!("Solution 1: {}", occupied);
}


fn solve2(lines: &Vec<String>) {
    println!("Solution 2: {}", 0);
}


fn main() {
    let lines = load_data();
    solve1(&lines);
    solve2(&lines);
}