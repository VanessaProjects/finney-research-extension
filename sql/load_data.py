import pandas as pd
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DB_PATH = PROJECT_ROOT / 'sql' / 'finney_competitors.db'
DATA_DIR = PROJECT_ROOT / 'data' / 'raw'

conn = sqlite3.connect(DB_PATH)

for table in ['competitors', 'ad_copy', 'social_metrics', 'positioning_dimensions']:
    csv_path = DATA_DIR / f'{table}.csv'
    if not csv_path.exists():
        print(f'SKIP: {table}.csv not found')
        continue
    df = pd.read_csv(csv_path)
    df.to_sql(table, conn, if_exists='replace', index=False)
    print(f'Loaded {len(df)} rows into {table}')

conn.close()
print('Done.')