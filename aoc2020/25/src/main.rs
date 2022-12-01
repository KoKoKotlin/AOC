const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

fn parse_input(input: &str) -> (u64, u64) {
    let values: Vec<u64> = input.lines().map(|x| x.parse::<u64>().unwrap()).collect();

    (values[0], values[1])
}

const MAGIC_VALUE: u64 = 20201227;

fn find_loop_number(pub_key: u64, subject_number: u64) -> u64 {
    let mut value: u64 = 1;
    let mut counter = 0;
    loop {
        value *= subject_number;
        value = value % MAGIC_VALUE;
        counter += 1;

        if value == pub_key {
            break;
        }
    }

    counter
}

fn transform(subject_number: u64, loop_number: u64) -> u64 {
    let mut res = 1;
    for _ in 0..loop_number {
        res *= subject_number;
        res = res % MAGIC_VALUE;
    }

    res
}

fn main() {
    let (card_pub, door_pub) = parse_input(INPUT);
    println!("Card pub: {}, Door pub: {}", card_pub, door_pub);

    let card_loop_nr = find_loop_number(card_pub, 7);
    let door_loop_nr = find_loop_number(door_pub, 7);
    println!(
        "Card loop nr: {}, Door loop nr: {}",
        card_loop_nr, door_loop_nr
    );

    let priv_key = transform(door_pub, card_loop_nr);
    println!("Priv key: {}", priv_key);
}
