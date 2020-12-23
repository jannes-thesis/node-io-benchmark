# Node-IO-benchmark

- node_scripts: workloads
- node-14.15.1: node source
- benchmarking: benchmark with hyperfine
- benchmarking-traced: benchmark with tracing (pidstat and systemtap)
- file_generation: scripts for generating files for benchmarks

## branches

- master: original node v14.15.1 
- adpative: node v14.15.1 with adaptive libuv threadpool

## dependencies

- https://github.com/nodejs/node/blob/master/BUILDING.md
- systemtap module topsysm2 should be in benchmarking-traced folder