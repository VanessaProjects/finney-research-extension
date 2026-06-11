import sqlite3
import pandas as pd
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

PROJECT_ROOT = Path(__file__).parent.parent
DB = PROJECT_ROOT / 'sql' / 'finney_competitors.db'
PROC = PROJECT_ROOT / 'data' / 'processed'
PROC.mkdir(parents=True, exist_ok=True)

# Load competitor positioning text from the database
conn = sqlite3.connect(DB)
competitors = pd.read_sql(
    'SELECT id, name, positioning_claim FROM competitors ORDER BY id', conn)
conn.close()

print('Loading model (first run downloads ~80MB, takes a minute)...')
model = SentenceTransformer('all-MiniLM-L6-v2')

# Embed each competitor's positioning claim
texts = competitors['positioning_claim'].fillna('').tolist()
emb = model.encode(texts)
np.save(PROC / 'competitor_embeddings.npy', emb)
np.save(PROC / 'competitor_names.npy', np.array(competitors['name'].tolist()))
print('Competitor embeddings shape:', emb.shape)   # expect (10, 384)

# --- Finney's positioning (YOUR firm, the reference point) ---
# DRAFT — edit this to match how Finney actually positions itself, in your words.
finney_positioning = (
    "Finney Injury Law positions itself as a true trial firm built around three "
    "trial attorneys with explicit former insurance-defense experience, emphasizing "
    "courtroom readiness, verifiable verdicts, and a deliberately selective, "
    "restrained approach rather than high-volume advertising."
)
finney_emb = model.encode(["A selective St. Louis personal injury trial firm built around "
    "three attorneys with explicit former insurance-defense experience, "
    "verifiable individual trial counts, and a deliberately small caseload "
    "that signals genuine trial readiness over high-volume settlement practice."])
np.save(PROC / 'finney_embedding.npy', finney_emb)
print('Finney embedding shape:', finney_emb.shape)  # expect (1, 384)

print('Done. Embeddings saved in data/processed/.')
