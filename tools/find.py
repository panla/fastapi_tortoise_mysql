"""
Traverse all files under single or multiple folders (UTF-8 files)
Find the target in the file according to the targets in the parameter
If found, record the target and file path in the log
"""

import argparse
import os
import sys
from pathlib import Path

param_parser = argparse.ArgumentParser()
param_parser.add_argument('-d', '--dirs', nargs='*', type=str, required=True, help='dirs')
param_parser.add_argument('-t', '--targets', nargs='+', required=True, help='target')
param_parser.add_argument('-l', '--log', type=str, required=False, help='log file')

params = param_parser.parse_args().__dict__
dirs = params.get('dirs')
directions = []

if dirs:
    for d in dirs:
        _d = Path(d).absolute()
        if _d.is_dir():
            directions.append(_d)
else:
    sys.stderr.write(f'your input -d/--dirs {dirs} error')
    sys.exit(1)

if not directions:
    sys.stderr.write(f'your input -d/--dirs {directions} error')
    sys.exit(1)

targets = params.get('targets')
if not targets:
    sys.stderr.write(f'your input -t/--targets {targets} error')
    sys.exit(1)

log_file = params.get('log')


def read_file(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ''


def write_file(path: str, content: str):
    with open(path, 'a+', encoding='utf-8') as f:
        f.write(content)



found_data = []
for direction in directions:
    for root, _, files in os.walk(direction):
        for file in files:
            file_path = Path(root, file)
            txt = read_file(file_path)
            for target in targets:
                if target in txt:
                    sys.stdout.write(f'{file_path}\n')
                    found_data.append(f'{target} {file_path}\n')

if log_file:
    Path(log_file).absolute().parent.mkdir(exist_ok=True)
    for found_d in found_data:
        write_file(log_file, found_d)

sys.stdout.write('find done\n')
