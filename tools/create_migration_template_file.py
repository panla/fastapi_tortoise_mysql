"""
create a blank migration sql file
"""

import argparse
import os
import sys
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', type=str, required=True, help='Migration Dir')
parser.add_argument('-n', '--name', type=str, required=True, help='Migration Name')

params = parser.parse_args()
migration_dir = params.dir
migration_name = params.name

if not os.path.isdir(migration_dir):
    os.makedirs(migration_dir, exist_ok=True)

now = datetime.now().strftime('%Y%m%d%H%M%S')

# get the new latest sql file index
exists_sql_file_names = os.listdir(migration_dir)
if exists_sql_file_names:
    latest_sql_file_index = max([int(f.split('_')[0]) for f in exists_sql_file_names])
    new_latest_sql_file_index = latest_sql_file_index + 1
else:
    new_latest_sql_file_index = 0

# get the new latest sql file name
new_latest_sql_file_name = f'{new_latest_sql_file_index}_{now}_{migration_name}.sql'

data = """-- upgrade --

-- downgrade --

"""

with open(os.path.join(migration_dir, new_latest_sql_file_name), 'w', encoding='utf-8') as f:
    f.write(data)

sys.stdout.write(f'create {migration_name} done\n')
