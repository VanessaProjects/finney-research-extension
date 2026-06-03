import sqlite3
import pandas as pd
from pathlib import Path

DB = Path(__file__).parent.parent / 'sql' / 'finney_competitors.db'
conn = sqlite3.connect(DB)

def show(title, sql):
    print('\n' + '=' * 60)
    print(title)
    print('=' * 60)
    print(pd.read_sql(sql, conn).to_string(index=False))

show('1. Firms per archetype',
    "SELECT archetype, COUNT(*) AS n FROM competitors GROUP BY archetype ORDER BY n DESC")

show('2. Facebook followers by firm (where known)',
    "SELECT c.name, s.followers FROM competitors c "
    "JOIN social_metrics s ON c.id = s.firm_id ORDER BY s.followers DESC")

show('3. Dimensions recorded per firm (should be 23 each)',
    "SELECT c.name, COUNT(*) AS dimensions FROM competitors c "
    "JOIN positioning_dimensions p ON c.id = p.firm_id GROUP BY c.name")

show('4. The distinct positioning dimensions tracked',
    "SELECT DISTINCT dimension FROM positioning_dimensions ORDER BY dimension")

show('5. Each firm with its archetype and FB followers',
    "SELECT c.name, c.archetype, s.followers FROM competitors c "
    "JOIN social_metrics s ON c.id = s.firm_id ORDER BY c.archetype, c.name")

conn.close()