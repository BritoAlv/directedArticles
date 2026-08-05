use std::{thread, time::Instant};

use crate::stress_cpu;


pub fn measure_time_fb_one_thread() {
    let start = Instant::now();
    let _ = stress_cpu::fibonacci(30);
    let duration = start.elapsed();
    println!("fibonacci(50) in {:?}", duration);
}

pub fn measure_time_fbs_four_threads() {
    let start = Instant::now();
    let mut handles = vec![];
    for _ in 0..4 {
        let handle = thread::spawn(|| stress_cpu::fibonacci(30));
        handles.push(handle);
    }
    for handle in handles {
        let _ = handle.join();
    }
    let duration = start.elapsed();
    println!("4 threads fibonacci(50) took {:?}", duration);
}

pub fn main() {
    measure_time_fb_one_thread();
    measure_time_fbs_four_threads();
}