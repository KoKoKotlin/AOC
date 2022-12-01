const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");
// const INPUT: &'static str = "0\n17,x,13,19";
// const INPUT: &'static str = "0\n67,7,59,61";
// const INPUT: &'static str = "1\n67,x,7,59,61";
// const INPUT: &'static str = "1\n1789,37,47,1889";

#[derive(Debug, Copy, Clone)]
struct Data {
    bus_id: u64,
    time_passed: u64,
    remainder: u64,
}

fn read_input(input_str: &str) -> (u32, Vec<u32>) {
    let lines: Vec<&str> = input_str.lines().collect();
    let wait_time = lines[0].parse::<u32>().unwrap();

    let bus_ids: Vec<u32> = lines[1]
        .split(",")
        .map(|token| {
            if token != "x" {
                Some(token.parse::<u32>().unwrap())
            } else {
                None
            }
        })
        .filter(|x| x.is_some())
        .map(|x| x.unwrap())
        .collect();

    (wait_time, bus_ids)
}

fn read_input2(input_str: &str) -> Vec<Data> {
    let line = input_str.lines().nth(1).unwrap();

    let tokens: Vec<&str> = line.split(",").collect();
    tokens
        .iter()
        .zip(1u32..=(tokens.len() as u32))
        .filter(|x| String::from(*x.0) != String::from("x"))
        .map(|x| (x.0.parse::<u32>().unwrap(), x.1))
        .map(|x| Data {
            bus_id: x.0 as u64,
            time_passed: x.1 as u64,
            remainder: (x.0 as u64) - ((x.1 % x.0) as u64),
        })
        .collect()
}

fn main() {
    let (wait_time, bus_ids) = read_input(INPUT);
    println!("{:?}, {:?}", wait_time, bus_ids);

    let min = bus_ids
        .iter()
        .map(|bus_id| {
            (
                bus_id,
                if wait_time % bus_id != 0 {
                    bus_id - wait_time % bus_id
                } else {
                    0
                },
            )
        })
        .min_by_key(|x| x.1)
        .unwrap();

    println!("Res: {}", min.0 * min.1);

    let mut bus_ids: Vec<Data> = read_input2(INPUT);
    bus_ids.sort_by_key(|x| x.remainder);
    println!("{:?}", bus_ids);

    let largest = bus_ids[bus_ids.len() - 1];
    let mut solution: u64 = largest.remainder;
    loop {
        if bus_ids
            .iter()
            .all(|data| solution % data.bus_id == data.remainder)
        {
            break;
        }

        solution += largest.bus_id;
    }

    println!("{}", solution + 1);
}
