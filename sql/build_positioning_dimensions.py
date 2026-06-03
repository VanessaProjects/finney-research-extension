import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
WIDE = PROJECT_ROOT / 'data' / 'master_table_wide.csv'
OUT  = PROJECT_ROOT / 'data' / 'raw' / 'positioning_dimensions.csv'

# firm name -> firm_id (must match competitors.csv)
firm_id = {
    'Goldblatt + Singer': 1, 'Cantor': 2, 'Simon Law': 3,
    'Schultz & Myers': 4, 'Cofman Townsley': 5, 'Bruning': 6,
    'Brown & Crouppen': 7, 'Morgan & Morgan': 8, 'OnderLaw': 9, 'DM Law': 10,
}

wide = pd.read_csv(WIDE)

# reshape wide -> long: each (dimension, firm) becomes its own row
long = wide.melt(id_vars='dimension', var_name='firm', value_name='value')
long['firm_id'] = long['firm'].map(firm_id)

# warn if any firm column header didn't match the map
unmapped = long[long['firm_id'].isna()]['firm'].unique()
if len(unmapped):
    print('WARNING: unrecognized firm columns:', list(unmapped))

long = long.sort_values('firm_id').reset_index(drop=True)
long['notes'] = ''
long.insert(0, 'id', range(1, len(long) + 1))
out = long[['id', 'firm_id', 'dimension', 'value', 'notes']]

out.to_csv(OUT, index=False)
print(f'Wrote {len(out)} rows to positioning_dimensions.csv')
print(out.head(8).to_string(index=False))
