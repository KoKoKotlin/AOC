const INPUT: &'static str = include_str!("input.txt");
// const INPUT: &'static str = include_str!("test_input.txt");

struct TreeGrid {
    trees: Vec<u32>,
    width: usize,
    height: usize,
    seen: Vec<bool>,
}

impl TreeGrid {
    fn get(&self, x: usize, y: usize) -> (u32, bool) {
        let index = x + y * self.width;
        (self.trees[index], self.seen[index])
    }

    fn set_seen(&mut self, x: usize, y: usize) {
        self.seen[x + y * self.width] = true;
    }

    fn row_iter(&self, row: usize) -> Vec<u32> {
        (0..self.width)
            .into_iter()
            .map(|idx| self.get(idx, row).0)
            .collect::<Vec<u32>>()
    }

    fn col_iter(&self, col: usize) -> Vec<u32> {
        (0..self.height)
            .into_iter()
            .map(|idx| self.get(col, idx).0)
            .collect::<Vec<u32>>()
    }
}

fn parse(input: &str) -> TreeGrid {
    let mut trees: Vec<u32> = vec![];
    let mut width = 0;

    let mut i = 0;
    for line in input.lines() {
        width = line.len();
        line.chars()
            .for_each(|token| trees.push(token.to_digit(10).unwrap()));
        i += 1;
    }
    let height = i;

    TreeGrid {
        trees,
        width,
        height,
        seen: vec![false; width * height],
    }
}

#[derive(PartialEq, Eq)]
enum Dir {
    Reversed,
    NotReversed,
}

fn find_dir_max_rows(tree_grid: &mut TreeGrid, row: usize, dir: Dir) -> usize {
    let nums = tree_grid.row_iter(row);
    let nums = match dir {
        Dir::Reversed => nums.into_iter().rev().collect::<Vec<u32>>(),
        Dir::NotReversed => nums,
    };

    let mut max: u32 = 0;
    let mut res: usize = 0;
    for (idx, height) in nums.iter().enumerate() {
        let tree_idx = if dir == Dir::Reversed {
            tree_grid.width - idx - 1
        } else {
            idx
        };
        if height > &max || idx == 0 {
            max = *height;
            if !tree_grid.get(tree_idx, row).1 {
                res += 1;
                tree_grid.set_seen(tree_idx, row);
            }
        }
    }

    res
}

fn find_dir_max_cols(tree_grid: &mut TreeGrid, col: usize, dir: Dir) -> usize {
    let nums = tree_grid.col_iter(col);
    let nums = match dir {
        Dir::Reversed => nums.into_iter().rev().collect::<Vec<u32>>(),
        Dir::NotReversed => nums,
    };

    let mut max: u32 = 0;
    let mut res: usize = 0;
    for (idx, height) in nums.iter().enumerate() {
        let tree_idx = if dir == Dir::Reversed {
            tree_grid.height - idx - 1
        } else {
            idx
        };

        if height > &max || idx == 0 {
            max = *height;
            if !tree_grid.get(col, tree_idx).1 {
                res += 1;
                tree_grid.set_seen(col, tree_idx);
            }
        }
    }

    res
}

fn get_score(tree_grid: &TreeGrid, x: usize, y: usize) -> u32 {
    let curr_height = tree_grid.get(x, y).0;

    // look up
    let mut up_score = 0;
    for offset in 1..tree_grid.height {
        if y < offset {
            break;
        }

        let height = tree_grid.get(x, y - offset).0;
        up_score += 1;
        if height >= curr_height {
            break;
        }
    }

    // look down
    let mut down_score = 0;
    for offset in 1..tree_grid.height {
        if y + offset >= tree_grid.height {
            break;
        }

        let height = tree_grid.get(x, y + offset).0;
        down_score += 1;
        if height >= curr_height {
            break;
        }
    }

    // look left
    let mut left_score = 0;
    for offset in 1..tree_grid.width {
        if x < offset {
            break;
        }

        let height = tree_grid.get(x - offset, y).0;
        left_score += 1;
        if height >= curr_height {
            break;
        }
    }

    // look right
    let mut right_score = 0;
    for offset in 1..tree_grid.width {
        if x + offset >= tree_grid.width {
            break;
        }

        let height = tree_grid.get(x + offset, y).0;
        right_score += 1;
        if height >= curr_height {
            break;
        }
    }

    up_score * down_score * left_score * right_score
}

fn main() {
    let mut tree_grid = parse(INPUT);
    let mut res: usize = 0;
    for row in 0..tree_grid.height {
        res += find_dir_max_rows(&mut tree_grid, row, Dir::NotReversed);
        res += find_dir_max_rows(&mut tree_grid, row, Dir::Reversed);
    }

    for col in 0..tree_grid.width {
        res += find_dir_max_cols(&mut tree_grid, col, Dir::NotReversed);
        res += find_dir_max_cols(&mut tree_grid, col, Dir::Reversed);
    }

    println!("Solution 1: {}", res);

    let mut max_score = 0;
    for y in 0..tree_grid.height {
        for x in 0..tree_grid.width {
            let score = get_score(&tree_grid, x, y);
            if score > max_score {
                max_score = score;
            }
        }
    }

    println!("Solution 2: {}", max_score);
}
