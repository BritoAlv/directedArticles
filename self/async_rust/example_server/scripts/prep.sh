#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
cargo build --release --manifest-path connection/Cargo.toml
cargo build --release --manifest-path server/Cargo.toml
cp connection/target/release/connection ./connection_bin
cp server/target/release/server ./server_bin
