use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;

fn first_part(){
    let file = File::open("../input.txt").expect("No such file...");
    let buffer = BufReader::new(file);
    let mut current_chars:Vec<char> = Vec::new();
    let mut counter = 0;
    for line in buffer.lines() {
        for char in line.expect("Unable to read line").chars () {
            if current_chars.len() < 4 {
                current_chars.push(char);
            }else if check_unique(&current_chars, 4) {
                println!("Sequence occurs at char {}", counter);
                return;
            }else{
                current_chars.remove(0);
                current_chars.push(char);
            }
        counter += 1;
        }
    }
}

fn check_unique(current_chars: &Vec<char>, length: usize) -> bool {
    let mut seen: HashSet<char> = HashSet::new();
    for c in current_chars.to_owned() {
        seen.insert(c);
    }
    return seen.len() == length;
}

fn second_part(){
    let file = File::open("../input.txt").expect("No such file...");
    let buffer = BufReader::new(file);
    let mut current_chars:Vec<char> = Vec::new();
    let mut counter = 0;
    for line in buffer.lines() {
        for char in line.expect("Unable to read line").chars () {
            if current_chars.len() < 14 {
                current_chars.push(char);
            }else if check_unique(&current_chars, 14) {
                println!("Sequence occurs at char {}", counter);
                return;
            }else{
                current_chars.remove(0);
                current_chars.push(char);
            }
        counter += 1;
        }
    }
}

fn main() {
    //first_part();
    second_part();
}

