import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).parent.parent
PROC = PROJECT_ROOT / 'data' / 'processed'
FIG = PROJECT_ROOT / 'figures'
FIG.mkdir(exist_ok=True)

comp   = np.load(PROC / 'competitor_embeddings.npy')
names  = np.load(PROC / 'competitor_names.npy', allow_pickle=True)
finney = np.load(PROC / 'finney_embedding.npy')

sims = cosine_similarity(comp, finney).flatten()
df = pd.DataFrame({'firm': names, 'similarity_to_finney': sims}) \
       .sort_values('similarity_to_finney', ascending=False).reset_index(drop=True)

print('Positioning similarity to Finney (highest = closest):')
print(df.to_string(index=False))
print()

gs_mask  = df['firm'].str.contains('Goldblatt')
gs_score = df.loc[gs_mask, 'similarity_to_finney'].values[0]
others   = df.loc[~gs_mask, 'similarity_to_finney'].values
rank     = int(gs_mask.idxmax()) + 1
t_stat, p_value = stats.ttest_1samp(others, gs_score)

print(f"Goldblatt + Singer: {gs_score:.4f}  (rank {rank} of 10)")
print(f"Mean of other 9:    {others.mean():.4f}")
print(f"SD of other 9:      {others.std(ddof=1):.4f}")
print(f"t = {t_stat:.3f}, p = {p_value:.4f}")
print("Result:", "G+S significantly closer (p < 0.05)." if p_value < 0.05
      else "G+S NOT significantly different from the cohort (p >= 0.05).")

order = df.sort_values('similarity_to_finney')
colors = ['#B85042' if 'Goldblatt' in f else '#408FA2' for f in order['firm']]
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(order['firm'], order['similarity_to_finney'], color=colors)
ax.set_xlabel('Cosine similarity to Finney positioning')
ax.set_title('Figure 4: Positioning Similarity to Finney (G+S highlighted)')
for i, v in enumerate(order['similarity_to_finney']):
    ax.text(v + 0.005, i, f'{v:.3f}', va='center')
plt.tight_layout()
plt.savefig(FIG / 'similarity_to_finney.png', dpi=150)
plt.close()
print('\nSaved figure: similarity_to_finney.png')