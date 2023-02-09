use std::fs::File;
use std::io::{ BufRead, BufReader};

fn read_input() -> Vec<String> {
    let file = File::open("../input.txt").expect("No such file...");
    let buffer = BufReader::new(file);
    let mut input: Vec<String> = Vec::new();
    for line in buffer.lines(){
        match line {
            Ok(v) => input.push(v),
            Err(e) => {
                println!("There was an error while reading the line {}", e);
                ()
            }
        }
    }
    return input;
}

#[allow(dead_code)]
fn part_one() {
    let input = read_input();
    let mut max_calories = 0;
    let mut current_calorie = 0;
    for calorie in input {
        if calorie == ""{
            if current_calorie > max_calories{
                max_calories = current_calorie;
            }
            current_calorie = 0;
        }else {
            current_calorie += calorie.parse::<i32>().unwrap();
        }
    }
    println!("max calories {}", max_calories);

}

fn part_two() {
    let input = read_input();
    let mut current_calorie = 0;
    let mut current_calories = [0,0,0];
    for calorie in input {
        if calorie == ""{
            let (value,min_index) = current_calories.iter().enumerate().map(|(x,y)| (y, x)).min().unwrap();
            if current_calorie > value.to_owned() {
                current_calories[min_index] = current_calorie;
            }
            current_calorie = 0;
        }else {
            current_calorie += calorie.parse::<i32>().unwrap();
        }
    }
    let max_calories: i32 = current_calories.iter().sum();
    println!("max calories {}", max_calories);
}



fn main() {
    //part_one();
    part_two();
}

