mod stress_cpu;
mod async_sync_requests;
mod threads_communication;
mod detect_file_changes;
mod http_requests;
mod fibonacci_threads;
#[tokio::main]
async fn main() {
    fibonacci_threads::main();
}

