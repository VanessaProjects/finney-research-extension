import sqlite3
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # save charts to files without needing a popup window
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DB = PROJECT_ROOT / 'sql' / 'finney_competitors.db'
FIG = PROJECT_ROOT / 'figures'
FIG.mkdir(exist_ok=True)

conn = sqlite3.connect(DB)

# Chart 1 — archetype distribution
arch = pd.read_sql(
    "SELECT archetype, COUNT(*) AS n FROM competitors GROUP BY archetype ORDER BY n", conn)
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(arch['archetype'], arch['n'], color='#408FA2')
ax.set_xlabel('Number of firms')
ax.set_title('Figure 1: Competitor Distribution by Archetype')
for i, v in enumerate(arch['n']):
    ax.text(v + 0.03, i, str(v), va='center')
plt.tight_layout()
plt.savefig(FIG / 'archetype_distribution.png', dpi=150)
plt.close()
print('Saved archetype_distribution.png')

# Chart 2 — Facebook followers (firms that disclose a number)
fb = pd.read_sql(
    "SELECT c.name, s.followers FROM competitors c "
    "JOIN social_metrics s ON c.id = s.firm_id "
    "WHERE s.followers IS NOT NULL ORDER BY s.followers", conn)
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(fb['name'], fb['followers'], color='#142D54')
ax.set_xlabel('Facebook followers')
ax.set_title('Figure 2: Facebook Followers by Firm (where disclosed)')
for i, v in enumerate(fb['followers']):
    ax.text(v + 60, i, f'{int(v):,}', va='center')
plt.tight_layout()
plt.savefig(FIG / 'facebook_followers.png', dpi=150)
plt.close()
print('Saved facebook_followers.png')

conn.close()
print('Done. Charts saved in the figures/ folder.')
