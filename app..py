import streamlit as st
import pandas as pd

st.set_page_config(page_title='GST 2.0', page_icon='🧾', layout='wide')

st.title('🧾 GST 2.0')
st.subheader('Accurate Taxation • Compliance Monitoring • Smart GST Insights')

query = st.text_input('Search HSN / SAC Code')

st.image(
    'https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1200&q=80',
    use_container_width=True
)

if query:
    st.success(f'Search received: {query}')
else:
    st.info('Enter an HSN or SAC code to begin.')
