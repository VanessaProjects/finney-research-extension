"""
Finney Competitive Intelligence Dashboard
Interactive view of the St. Louis personal injury competitive landscape.
"""
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title='Finney Competitive Intelligence', layout='wide')

ROOT = Path(__file__).parent.parent
DB = ROOT / 'sql' / 'finney_competitors.db'
PROC = ROOT / 'data' / 'processed'


@st.cache_data
def load():
    conn = sqlite3.connect(DB)
    competitors = pd.read_sql('SELECT * FROM competitors', conn)
    ad_copy = pd.read_sql('SELECT * FROM ad_copy', conn)
    social = pd.read_sql('SELECT * FROM social_metrics', conn)
    dims = pd.read_sql('SELECT * FROM positioning_dimensions', conn)
    conn.close()
    return competitors, ad_copy, social, dims


competitors, ad_copy, social, dims = load()

st.sidebar.title('Navigation')
page = st.sidebar.radio(
    'Go to', ['Overview', 'Competitors', 'Ad Copy', 'Positioning Similarity'])
st.sidebar.markdown('---')
st.sidebar.caption('AI-Augmented Competitive Intelligence - research case study')

if page == 'Overview':
    st.title('Finney Competitive Intelligence Dashboard')
    st.caption('A research case study in AI-augmented marketing analysis')
    c1, c2, c3 = st.columns(3)
    c1.metric('Competitors', len(competitors))
    c2.metric('Ads cataloged', len(ad_copy))
    c3.metric('Positioning data points', len(dims))
    st.markdown('### About')
    st.write('This dashboard accompanies a research case study on AI-augmented '
             'competitive intelligence, using the St. Louis personal injury '
             'legal market as the case domain.')

elif page == 'Competitors':
    st.title('Competitor Explorer')
    options = sorted(competitors['archetype'].dropna().unique())
    chosen = st.multiselect('Filter by archetype', options, default=options)
    view = competitors[competitors['archetype'].isin(chosen)]
    st.dataframe(
        view[['name', 'archetype', 'founded_year', 'estimated_size',
              'geographic_focus', 'positioning_claim']],
        use_container_width=True)
    st.subheader('Archetype distribution')
    st.bar_chart(view['archetype'].value_counts())

elif page == 'Ad Copy':
    st.title('Ad Copy')
    merged = ad_copy.merge(competitors[['id', 'name']],
                           left_on='firm_id', right_on='id', how='left')
    firm = st.selectbox(
        'Firm', ['All'] + sorted(merged['name'].dropna().unique().tolist()))
    show = merged if firm == 'All' else merged[merged['name'] == firm]
    st.dataframe(show[['name', 'phrase', 'category']], use_container_width=True)

elif page == 'Positioning Similarity':
    st.title('Positioning Similarity to Finney')
    st.caption('Cosine similarity of each competitor to Finney. Provisional - '
               'reflects the current positioning text.')
    try:
        emb = np.load(PROC / 'competitor_embeddings.npy')
        names = np.load(PROC / 'competitor_names.npy', allow_pickle=True)
        finney = np.load(PROC / 'finney_embedding.npy')
        sims = cosine_similarity(emb, finney).flatten()
        res = (pd.DataFrame({'Firm': names, 'Similarity to Finney': sims})
                 .sort_values('Similarity to Finney', ascending=False))
        st.dataframe(res, use_container_width=True)
        st.bar_chart(res.set_index('Firm')['Similarity to Finney'])
    except FileNotFoundError:
        st.warning('Embeddings not found - run the Day 7 embeddings script first.')
