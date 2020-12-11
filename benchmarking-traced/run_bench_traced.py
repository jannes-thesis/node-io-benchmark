from subprocess import run
import json
import sys
from subprocess import Popen
from time import sleep
from datetime import datetime
from typing import List
from dataclasses import dataclass
import subprocess
import os


runscript = 'single_run_with_metrics.sh'


@dataclass(frozen=True)
class BenchmarkParameters:
    deno_script: str
    io_threads: List[int]
    files_dir: str


def get_bench_params(name):
    with open('benchmarks.json') as f:
        benchmarks_json = json.load(f)
    b = benchmarks_json[name]
    return BenchmarkParameters(b['deno_script'], b['io_threads'], b['files_dir'])


def execute_config(deno_script, amount_threads, output_dir, files_dir):
    prefix = f'{output_dir}/t={amount_threads}'
    run(['sudo', 'clear_page_cache'])
    sleep(1)
    with Popen(['bash', runscript, str(amount_threads), deno_script, files_dir, prefix],
               text=True, stdout=subprocess.PIPE) as proc:
        # while running continously obtain stdout and buffer it
        while proc.poll() is None:
            out, _ = proc.communicate()
            print(out)


if __name__ == '__main__':

    print('dont forget to run \'sudo -v\' before')
    if len(sys.argv) != 2:
        print('usage: ./run_benchmark.py [benchmark name]')
        exit(1)

    benchmark_name = sys.argv[1]
    b_params = get_bench_params(benchmark_name)

    now = datetime.today().strftime('%Y-%m-%d-%H:%M')
    output_dir = f'run-{benchmark_name}-{now}'
    os.mkdir(output_dir)

    for amount in b_params.io_threads:
        execute_config(b_params.deno_script, amount, output_dir, b_params.files_dir)

    print('benchmark done')
