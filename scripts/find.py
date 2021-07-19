"""
遍历单个/多个文件夹下的所有文件（可以使用utf-8 read 的文件）
根据参数中的 targets 在读取的文件中查找 target
如果查找到就把 target 和 文件路径记录到 log 中
"""

import os
import argparse

param_parser = argparse.ArgumentParser()
param_parser.add_argument('-d', '--dirs', nargs='*', type=str, required=False, default=[], help='dirs')
param_parser.add_argument('-t', '--targets', nargs='+', required=True, help='target')
param_parser.add_argument('-l', '--log', type=str, required=False, default='./r.log', help='log file')

params = param_parser.parse_args()
dirs = params.dirs
directions = []
if dirs:
    for d in dirs:
        if os.path.isdir(os.path.abspath(d)):
            directions.append(os.path.abspath(d))
targets = params.targets
log_file = params.log


def read_file(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ''


def write_file(path: str, content: str):
    with open(path, 'a+', encoding='utf-8') as f:
        f.write(content)


os.makedirs(os.path.dirname(os.path.abspath(log_file)), exist_ok=True)

if directions:
    for direction in directions:
        for root, _, files in os.walk(direction):
            for file in files:
                file_path = os.path.join(root, file)
                for target in targets:
                    if target in read_file(file_path):
                        write_file(log_file, '{} {}\n'.format(target, file_path))
