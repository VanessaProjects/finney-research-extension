# Data Dictionary

Documentation of the four tables in `sql/finney_competitors.db`. All tables are
loaded from CSVs in `data/raw/` via `sql/load_data.py`. Firm-level tables link
back to `competitors` through `firm_id`.

---

## Table: `competitors`
One row per competitor firm (10 firms). The anchor table; every other table
references its `id`.

| Column | Type | Description | Example | Source |
|--------|------|-------------|---------|--------|
| id | integer | Primary key; unique firm id (1–10) | 1 | Assigned |
| name | text | Firm name | Goldblatt + Singer | Master table |
| founded_year | text | Year founded (some approximate) | 1949 | Master table |
| archetype | text | Positioning archetype (Volume/Legacy/Premium/Boutique/Niche) | Boutique | Analyst classification |
| estimated_size | text | Approximate attorney count | ~7-9 | Master table |
| geographic_focus | text | Primary geography served | Clayton | Master table |
| positioning_claim | text | One-line positioning statement (used for NLP embedding) | _(to be written)_ | Analyst |
| primary_threat_type | text | Competitive threat level to Finney | highest - closest positioning overlap | Master table |
| source_url | text | Firm website | _(to be added)_ | Web |
| date_collected | text | Date the row was compiled (YYYY-MM-DD) | 2026-06-02 | Analyst |

## Table: `ad_copy`
One row per observed ad (10 ads, one per firm at present).

| Column | Type | Description | Example | Source |
|--------|------|-------------|---------|--------|
| id | integer | Primary key; unique ad id | 1 | Assigned |
| firm_id | integer | Foreign key to `competitors.id` | 1 | Mapped |
| phrase | text | The ad headline / copy text | We're the St. Louis Injury Law Firm... | HubSpot export |
| category | text | Copy / Avoid / Own classification | _(to be tagged)_ | Analyst |
| keyword_type | text | Optional keyword tag | _(optional)_ | Analyst |
| source_observation | text | Where the ad was observed | HubSpot competitor ad library | Analyst |
| date_observed | text | Date observed (YYYY-MM-DD) | 2026-04-15 | HubSpot export |

## Table: `social_metrics`
One row per firm per platform (currently Facebook only; some values unknown).

| Column | Type | Description | Example | Source |
|--------|------|-------------|---------|--------|
| id | integer | Primary key | 1 | Assigned |
| firm_id | integer | Foreign key to `competitors.id` | 1 | Mapped |
| platform | text | Social platform | Facebook | Analyst |
| followers | real | Follower/like count (blank where undisclosed) | 8195 | Master table |
| engagement_rate | real | Engagement rate (not yet collected) | _(blank)_ | — |
| posting_cadence | text | Posting frequency (not yet collected) | _(blank)_ | — |
| last_observed | text | Date observed (YYYY-MM-DD) | 2026-06-02 | Analyst |

## Table: `positioning_dimensions`
Long format: one row per firm per dimension (10 firms × 23 dimensions = 230 rows).
Reshaped from `data/master_table_wide.csv` via `sql/build_positioning_dimensions.py`.

| Column | Type | Description | Example | Source |
|--------|------|-------------|---------|--------|
| id | integer | Primary key | 1 | Assigned |
| firm_id | integer | Foreign key to `competitors.id` | 1 | Mapped |
| dimension | text | Positioning dimension name | Brand archetype | Master table |
| value | text | That firm's value on the dimension | Heritage trial firm | Master table |
| notes | text | Optional notes | _(blank)_ | Analyst |

---

## Notes on completeness
- `positioning_claim` (competitors) is intentionally blank pending analyst write-up; it is the text used for the Day 7–8 NLP similarity analysis.
- `category` (ad_copy) is pending the Copy/Avoid/Own classification.
- Several `founded_year` values are approximate (e.g. "1985+", "Multi-decade").
- `social_metrics` follower counts exist only for firms that publicly disclose them; engagement and cadence are not yet collected.
