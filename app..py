
import streamlit as st
import pandas as pd

st.set_page_config(page_title="GST 2.0", page_icon="🧾", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {font-family:'Plus Jakarta Sans',sans-serif;}
.stApp{
background:linear-gradient(180deg,#f8fafc,#eef2ff);
}
.hero{
background:linear-gradient(135deg,#0f172a,#1e3a8a);
padding:3rem;border-radius:24px;color:white;text-align:center;margin-bottom:1.5rem;
}
.card{
background:white;padding:1rem;border-radius:20px;
box-shadow:0 10px 25px rgba(0,0,0,.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>GST 2.0</h1>
<p>Accurate Taxation • Compliance Monitoring • Smart GST Insights</p>
</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4=st.columns(4)
c1.metric("HSN Codes","13K+")
c2.metric("SAC Codes","Thousands")
c3.metric("GST Rates","5/12/18/28")
c4.metric("Coverage","India")

st.subheader("🔍 HSN / SAC Finder")
code=st.text_input("Enter Code")

st.subheader("🧮 GST Calculator")
amt=st.number_input("Amount",min_value=0.0)
rate=st.selectbox("Rate",[5,12,18,28])
gst=amt*rate/100
a,b,c=st.columns(3)
a.metric("Base",f"₹{amt:,.2f}")
b.metric("GST",f"₹{gst:,.2f}")
c.metric("Total",f"₹{amt+gst:,.2f}")

if code:
    st.success(f"Lookup for code: {code}")
    st.info("Connect with your HSN_SAC_data.xlsx dataset for live results.")

st.markdown("---")
st.caption("GST 2.0 • Premium Fintech UI")
