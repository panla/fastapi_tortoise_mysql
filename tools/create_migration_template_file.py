"""
create a blank migration sql file
"""

import os
import sys
from datetime import datetime

migration_dir = os.environ.get('DIR')
migration_name = os.environ.get('NAME')

if not os.path.isdir(migration_dir):
    os.makedirs(migration_dir, exist_ok=True)

sql_file_names = os.listdir(migration_dir)
if sql_file_names:
    latest_sql_file_index = max([int(f.split('_')[0]) for f in sql_file_names])
    new_latest_sql_file_index = latest_sql_file_index + 1
else:
    new_latest_sql_file_index = 0

now = datetime.now().strftime('%Y%m%d%H%M%S')

new_latest_sql_file_name = f'{new_latest_sql_file_index}_{now}_{migration_name}.sql'

data = """-- upgrade --

-- downgrade --
"""

with open(os.path.join(migration_dir, new_latest_sql_file_name), 'w', encoding='utf-8') as f:
    f.write(data)

sys.stdout.write(f'create {migration_name} done\n')
