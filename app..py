# GST 2.0 - Premium UI Template
# Replace your current CSS/header section with this version.

import streamlit as st

st.set_page_config(page_title="GST 2.0", page_icon="💼", layout="wide")

st.markdown("""
<style>
.stApp{
    background:#f8fafc;
}
.hero{
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:60px;
    border-radius:24px;
    color:white;
    text-align:center;
    margin-bottom:25px;
}
.metric-card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0 10px 30px rgba(0,0,0,.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>GST 2.0</h1>
<p>Accurate Taxation • Compliance Monitoring • Smart GST Insights</p>
</div>
""", unsafe_allow_html=True)

st.info("Use this premium UI section inside your existing GST app.")
