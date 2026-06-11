# AI-Augmented Competitive Intelligence: A Case Study

> A methodology study on AI-assisted competitive analysis,
> using the St. Louis personal injury legal market as a case domain.

## Live Dashboard
**[Open the Dashboard](https://finney-research-extension-356xx8tzva9ajiaeqqssdm.streamlit.app/)**

## Key Finding
Goldblatt + Singer is Finney Injury Law's closest positioning competitor —
confirmed by both qualitative analysis and independent NLP validation.

- Cosine similarity to Finney: **0.664** (rank 1 of 10)
- Statistical significance: **p = 0.0000**
- Two independent methods converged on the same answer

## Research Question
How does human-AI collaboration produce competitive analysis outputs
that would otherwise require larger analyst teams, and what are the
methodological tradeoffs of this workflow?

## Methods
Three-layer mixed-methods approach:

1. **Qualitative analysis** with Claude (Anthropic) — 5-archetype
   framework, 23-dimension positioning matrix, Copy/Avoid/Own ad framework
2. **Data engineering** in SQL — 10 firms × 23 dimensions in a
   queryable SQLite database (260 rows across 4 tables)
3. **Quantitative validation** via sentence-embedding similarity —
   statistical confirmation that qualitative findings hold up
   under independent computational measurement

## Reproducing the Analysis
```bash
git clone https://github.com/vanessaprojects/finney-research-extension.git
cd finney-research-extension
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python sql/load_data.py
python src/make_embeddings.py
python src/validate_positioning.py
streamlit run dashboard/app.py
```

## Project Structure
- `/data` — Raw and processed competitor data
- `/sql` — Database schema, ETL pipeline, analytical queries
- `/src` — Python scripts (charts, embeddings, validation)
- `/dashboard` — Streamlit application
- `/manuscript` — Working paper and methodology documents
- `/figures` — Generated visualizations

## Key Results
| Firm | Similarity to Finney |
|------|---------------------|
| Goldblatt + Singer | **0.664** |
| Simon Law | 0.540 |
| DM Law | 0.524 |
| Cofman Townsley | 0.461 |
| Schultz & Myers | 0.430 |
| Morgan & Morgan | 0.427 |
| Bruning | 0.398 |
| Cantor | 0.359 |
| OnderLaw | 0.312 |
| Brown & Crouppen | 0.286 |

## Author
Vanesa  — Marketing Coordinator, Finney Injury Law /
Master of Science in AI candidate, Lindenwood University

## License
MIT — see LICENSE file.