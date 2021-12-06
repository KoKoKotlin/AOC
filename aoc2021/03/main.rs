use std::fs;

fn load_data() -> Vec<String> {
    let data = fs::read_to_string("data.txt").expect("Couldn't load data!");
    
    let mut lines: Vec<String> = vec![];
    for line in data.split("\n") {
        lines.push(String::from(line));
    }

    lines
}

fn calc_balance(list: &Vec<&String>, pos: usize) -> i32 {
    let mut balance = 0;
    for line in list.iter() {
        let c = line.chars().nth(pos).take().unwrap();
        
        match c {
            '0' => balance -= 1,
            '1' => balance += 1,
            _   => balance += 0,
        }
    }

    balance
}

fn solve1(lines: &Vec<String>) {
    
    let line_len = lines[0].len();

    let mut gamma = 0;
    let mut epsilon = 0;

    let mut list1: Vec<&String> = vec![];
    for i in 0..lines.len() {
        list1.push(&lines[i]);
    }

    for char_pos in 0..line_len {
        let balance = calc_balance(&list1, char_pos);

        if balance > 0 {
            gamma = 1 << (line_len - char_pos - 1) | gamma;
        } else {
            epsilon = 1 << (line_len - char_pos - 1) | epsilon;
        }
    }
    
    println!("Solution 1: {}", gamma * epsilon);
}


fn solve2(lines: &Vec<String>) {

    let line_len = lines[0].len();

    let mut list1: Vec<&String> = vec![];
    let mut list2: Vec<&String> = vec![];

    for i in 0..lines.len() {
        list1.push(&lines[i]);
        list2.push(&lines[i]);
    }
        
    for char_pos in 0..line_len {
        let pos = char_pos;
        let balance1 = calc_balance(&list1, pos);
        let balance2 = calc_balance(&list2, pos);
        
        let c1 = if balance1 >= 0 { '1' } else { '0' };
        let c2 = if balance2 <  0 { '1' } else { '0' };

        if list1.len() != 1 {
            list1 = list1.into_iter()
                .filter(|line| line.chars().nth(pos).take().unwrap() == c1)
                .collect::<Vec<&String>>();
        }

        if list2.len() != 1 {
            list2 = list2.into_iter()
                .filter(|line| line.chars().nth(pos).take().unwrap() == c2)
                .collect::<Vec<&String>>();
        }
    }

    let num1 = i32::from_str_radix(list1[0].as_str(), 2).unwrap();
    let num2 = i32::from_str_radix(list2[0].as_str(), 2).unwrap();

    println!("Solution 2: {}", num1 * num2);
}


fn main() {
    let mut lines = load_data();
    solve1(&mut lines);
    solve2(&mut lines);
}