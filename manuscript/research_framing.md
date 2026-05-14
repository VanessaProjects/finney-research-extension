# Research Framing: AI-Augmented Competitive Intelligence

**Author**: Vanesa Hodzic
**Date**: May 14, 2026
**Project**: 15-Day Research Extension of the Finney Strategic Case Study

## Research Question

How does human-AI collaboration produce competitive analysis outputs that would traditionally require larger analyst teams, and what are the methodological tradeoffs of this workflow?

### Sub-questions

1. What is the workflow that allows a single analyst with AI assistance to produce team-quality competitive analysis?
2. Do qualitative findings produced through AI-assisted analysis hold up to quantitative validation?
3. Where do the limits of AI-assisted analysis appear, and what kinds of strategic insight still require human judgment?

## Background

As a Masters in AI student at Lindenwood University doing a marketing strategy internship at Finney Injury Law, I noticed something I want to understand better. Traditional competitive intelligence work — the kind that produces positioning recommendations, market segmentation, and strategic frameworks — has historically required teams of three to five analysts working over weeks. But over the course of the Finney project, working alone with Claude as a thought partner, I was able to produce analytical outputs that I'm pretty sure would have required a small consulting team a few years ago. This project documents that workflow honestly — what worked, where AI helped, and where human judgment was still essential.

## Methodology Overview

Mixed-methods approach across three layers:

**Layer 1 — Qualitative Strategic Analysis**: traditional competitive analysis methods including positioning, archetype identification, and ad copy categorization, produced through AI-assisted iteration cycles with Claude.

**Layer 2 — Data Engineering**: structured representation of the competitive landscape in a SQL database with documented schema and queryable analytical layer.

**Layer 3 — Quantitative Validation**: sentence-embedding similarity analysis to test whether qualitative positioning claims hold up to numerical measurement.

## Contributions

1. A documented methodology for AI-augmented competitive analysis (prompt patterns, decision points, iteration cycles)
2. A reproducible case study on real market data — the St. Louis personal injury legal market
3. A quantitative validation framework for qualitative competitive analysis findings
4. A live interactive analytical artifact (Streamlit dashboard)

## Target Venues

- SSRN preprint (primary, Day 15 submission)
- Future submission targets:
  - Information Systems journals (MIS Quarterly, JAIS, JMIS)
  - Marketing analytics journals
  - Applied AI conferences

## Limitations

- Single-case design (one firm, one market)
- Geographic scope (St. Louis only)
- Cross-sectional design (one time point)
- Embedding model limitations (small open-source model)
- Sample size (10 competitor firms)
- Single-analyst study (no inter-rater reliability checks)

## Reproducibility Commitment

All data, code, and documentation publicly available in this repository under an MIT license. A methodology document (to be written Day 9) will provide sufficient detail for independent replication.

## Next Steps

- Day 2: SQL foundation and database schema design
- Day 3: Structured representation of competitor data as CSVs
- Day 4: Python ETL pipeline loading data into SQLite
