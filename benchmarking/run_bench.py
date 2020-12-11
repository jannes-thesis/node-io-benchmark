import json
import sys
from subprocess import Popen, run
from time import sleep
from datetime import datetime
from dataclasses import dataclass
import subprocess
import os


runscript = 'run_benchmark.sh'


@dataclass(frozen=True)
class BenchmarkParameters:
    node_script: str
    files_dir: str
    amount_files: int


def get_bench_params(name):
    with open('benchmarks.json') as f:
        benchmarks_json = json.load(f)
    b = benchmarks_json[name]
    return BenchmarkParameters(b['node_script'], b['files_dir'], int(b['amount_files']))


def execute_config(node_script, files_dir, amount_files, output_json):
    run(['sudo', 'clear_page_cache'])
    sleep(1)
    with Popen(['bash', runscript, node_script, files_dir, amount_files, output_json],
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
    output_json = f'run-{benchmark_name}-{now}.json'
    execute_config(b_params.node_script, b_params.files_dir, 
                   b_params.amount_files, output_json)

    print('benchmark done')
