import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GST HSN/SAC Code Finder",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* ── Color Palette ──────────────────────────────────────────────────────────
   Background:  #0d1117  (rich charcoal-black)
   Surface:     #161b22  (dark slate)
   Card:        #1c2330  (slightly lighter slate)
   Border:      #30363d  (subtle grey border)
   Accent:      #00c9a7  (teal-green — primary)
   Accent2:     #3b82f6  (sky blue — secondary)
   Text primary:  #e6edf3
   Text muted:    #8b949e
   Text dim:      #4d5566
   ─────────────────────────────────────────────────────────────────────── */

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background: #0d1117;
    min-height: 100vh;
}

.block-container {
    padding: 2rem 2.5rem 2rem 2.5rem !important;
    max-width: 1200px;
}

/* ── Header ── */
.main-header {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    margin-bottom: 0.5rem;
}
.main-header h1 {
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(90deg, #00c9a7, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 0.4rem 0;
    letter-spacing: -0.5px;
}
.main-header p {
    color: #8b949e;
    font-size: 1rem;
    margin: 0;
}

/* ── Metric Cards ── */
.metric-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}
.metric-card {
    flex: 1;
    min-width: 150px;
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    text-align: center;
}
.metric-card .num {
    font-size: 2rem;
    font-weight: 800;
    color: #00c9a7;
    line-height: 1;
    margin-bottom: 0.3rem;
}
.metric-card .lbl {
    font-size: 0.75rem;
    color: #8b949e;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* ── Search Section ── */
.search-section {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 1.5rem;
}
.search-label {
    color: #e6edf3;
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.5rem;
}

/* ── Input overrides ── */
input[type="text"], .stTextInput input {
    background: #0d1117 !important;
    border: 1.5px solid #30363d !important;
    border-radius: 12px !important;
    color: #e6edf3 !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    padding: 0.7rem 1rem !important;
    letter-spacing: 0.03em;
}
input[type="text"]:focus, .stTextInput input:focus {
    border-color: #00c9a7 !important;
    box-shadow: 0 0 0 3px rgba(0,201,167,0.15) !important;
}

/* ── Radio buttons ── */
.stRadio > div {
    display: flex;
    flex-direction: row;
    gap: 1rem;
}
.stRadio label {
    color: #e6edf3 !important;
    font-weight: 500 !important;
}
div[data-testid="stHorizontalBlock"] .stRadio {
    margin-top: 0.2rem;
}

/* ── Result Card ── */
.result-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 20px;
    padding: 2rem;
    margin-top: 1rem;
    animation: fadeIn 0.4s ease;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ── Tax Badge ── */
.tax-badge {
    display: inline-block;
    padding: 0.5rem 1.2rem;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 800;
    letter-spacing: 0.02em;
}
.badge-exempt  { background: rgba(0,201,167,0.12); color: #00c9a7; border: 1.5px solid rgba(0,201,167,0.35); }
.badge-5       { background: rgba(59,130,246,0.12); color: #60a5fa; border: 1.5px solid rgba(59,130,246,0.35); }
.badge-12      { background: rgba(99,205,145,0.12); color: #63cd91; border: 1.5px solid rgba(99,205,145,0.35); }
.badge-18      { background: rgba(251,191,36,0.12); color: #fbbf24; border: 1.5px solid rgba(251,191,36,0.35); }
.badge-28      { background: rgba(239,68,68,0.12);  color: #f87171; border: 1.5px solid rgba(239,68,68,0.35); }
.badge-other   { background: rgba(139,148,158,0.12); color: #8b949e; border: 1.5px solid rgba(139,148,158,0.35); }

/* ── Tax Grid ── */
.tax-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 1.5rem 0;
}
.tax-item {
    background: #0d1117;
    border-radius: 14px;
    padding: 1rem;
    text-align: center;
    border: 1px solid #30363d;
}
.tax-item .t-val {
    font-size: 1.6rem;
    font-weight: 800;
    color: #00c9a7;
    line-height: 1;
}
.tax-item .t-lbl {
    font-size: 0.7rem;
    color: #8b949e;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-top: 0.3rem;
}
.tax-item .t-desc {
    font-size: 0.75rem;
    color: #4d5566;
    margin-top: 0.2rem;
}

/* ── Info Rows ── */
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding: 0.75rem 0;
    border-bottom: 1px solid #21262d;
}
.info-row:last-child { border-bottom: none; }
.info-key {
    color: #8b949e;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    min-width: 130px;
}
.info-val {
    color: #e6edf3;
    font-size: 0.95rem;
    font-weight: 500;
    text-align: right;
    flex: 1;
}

/* ── Section Title ── */
.section-title {
    color: #8b949e;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 1.5rem 0 0.8rem 0;
}

/* ── Context Box ── */
.context-box {
    background: rgba(59,130,246,0.07);
    border: 1px solid rgba(59,130,246,0.25);
    border-radius: 14px;
    padding: 1.2rem 1.5rem;
    margin-top: 1.2rem;
}
.context-box .ctx-title {
    color: #60a5fa;
    font-weight: 700;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}
.context-box .ctx-body {
    color: #8b949e;
    font-size: 0.9rem;
    line-height: 1.6;
}

/* ── Not Found ── */
.not-found {
    text-align: center;
    padding: 3rem;
    color: #8b949e;
}
.not-found .icon { font-size: 3rem; }
.not-found h3 { color: #e6edf3; margin: 0.5rem 0; }

/* ── Error ── */
.error-box {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.25);
    border-radius: 12px;
    padding: 1rem 1.5rem;
    color: #f87171;
    font-size: 0.9rem;
}

/* ── Table & Misc ── */
.stDataFrame { border-radius: 12px; overflow: hidden; }
hr { border-color: #21262d !important; }

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
.viewerBadge_container__1QSob { display: none; }

/* Select box */
.stSelectbox > div > div {
    background: #0d1117 !important;
    border: 1.5px solid #30363d !important;
    border-radius: 12px !important;
    color: #e6edf3 !important;
}
</style>
""", unsafe_allow_html=True)


# ── Load Data (cached) ───────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_excel("HSN_SAC_data.xlsx")
    df.columns = [
        "sno", "code", "description", "type",
        "gst_total", "cgst", "sgst", "igst",
        "tax_head", "schedule", "category"
    ]
    df["code"] = df["code"].astype(str).str.strip()
    df["type"] = df["type"].str.strip()
    df["gst_total"] = df["gst_total"].str.strip()
    df["cgst"] = df["cgst"].str.strip()
    df["sgst"] = df["sgst"].str.strip()
    df["igst"] = df["igst"].str.strip()
    df["tax_head"] = df["tax_head"].str.strip()
    df["schedule"] = df["schedule"].str.strip()
    df["category"] = df["category"].str.strip()
    df["description"] = df["description"].str.strip()
    return df

df = load_data()

# ── Stats ────────────────────────────────────────────────────────────────────
total    = len(df)
hsn_cnt  = len(df[df["type"] == "HSN"])
sac_cnt  = len(df[df["type"] == "SAC"])
exempt   = len(df[df["gst_total"] == "NIL / EXEMPT"])

# ── Helper: get badge class ──────────────────────────────────────────────────
def gst_badge(val):
    v = val.upper()
    if "NIL" in v or "EXEMPT" in v:
        return "badge-exempt", "NIL / EXEMPT"
    if "28" in v: return "badge-28", val
    if "18" in v: return "badge-18", val
    if "12" in v: return "badge-12", val
    if "5"  in v: return "badge-5",  val
    return "badge-other", val

def context_advice(role, gst_val, tax_head):
    is_exempt = "NIL" in gst_val.upper() or "EXEMPT" in gst_val.upper()
    if role == "Buyer / Vendor (Purchasing)":
        if is_exempt:
            return ("No GST payable on this purchase.",
                    "This item is GST-exempt. No Input Tax Credit (ITC) can be claimed. "
                    "No reverse charge applies. Purchase at face value.")
        elif "Outside GST" in tax_head:
            return ("Outside GST scope — state levies may apply.",
                    "This item falls outside GST. State-level taxes/levies may be charged by the supplier.")
        else:
            return ("GST payable — ITC can be claimed.",
                    f"As a buyer, you will pay GST ({gst_val}) to your supplier. "
                    "If registered under GST, you can claim Input Tax Credit (ITC) on this purchase. "
                    "For inter-state purchases, IGST applies. For intra-state, CGST + SGST applies.")
    else:  # Supplier/Seller
        if is_exempt:
            return ("No GST to collect from buyer.",
                    "This item is exempt from GST. Do NOT charge GST on your invoice. "
                    "No ITC can be claimed on inputs used for this exempt supply.")
        elif "Outside GST" in tax_head:
            return ("Outside GST scope — do not charge GST.",
                    "This item is outside the GST framework. Do not levy GST. "
                    "State-specific taxes may apply. Consult your tax advisor.")
        else:
            return ("Collect GST from buyer and remit to government.",
                    f"As a supplier, you must charge GST ({gst_val}) on your invoice. "
                    "For intra-state supply: collect CGST + SGST. "
                    "For inter-state supply: collect IGST. "
                    "File GST returns (GSTR-1, GSTR-3B) and remit collected tax.")


# ── HEADER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
  <h1>🧾 GST HSN / SAC Finder</h1>
  <p>Instantly look up tax rates, schedules & compliance info from official GST data</p>
</div>
""", unsafe_allow_html=True)

# ── METRIC CARDS ─────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="metric-row">
  <div class="metric-card">
    <div class="num">{total:,}</div>
    <div class="lbl">Total Codes</div>
  </div>
  <div class="metric-card">
    <div class="num">{hsn_cnt:,}</div>
    <div class="lbl">HSN Codes (Goods)</div>
  </div>
  <div class="metric-card">
    <div class="num">{sac_cnt:,}</div>
    <div class="lbl">SAC Codes (Services)</div>
  </div>
  <div class="metric-card">
    <div class="num">{exempt:,}</div>
    <div class="lbl">Exempt Items</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SEARCH SECTION ───────────────────────────────────────────────────────────
st.markdown('<div class="search-section">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    st.markdown('<div class="search-label">Enter HSN / SAC Code</div>', unsafe_allow_html=True)
    code_input = st.text_input(
        label="code",
        placeholder="e.g. 10061010 or 995411",
        label_visibility="collapsed",
        key="code_search"
    )

with col2:
    st.markdown('<div class="search-label">Your Role</div>', unsafe_allow_html=True)
    role = st.radio(
        label="role",
        options=["Buyer / Vendor (Purchasing)", "Supplier / Seller (Selling)"],
        label_visibility="collapsed",
        horizontal=False
    )

with col3:
    st.markdown('<div class="search-label">Transaction Type</div>', unsafe_allow_html=True)
    txn = st.radio(
        label="txn",
        options=["Intra-State (CGST + SGST)", "Inter-State (IGST)"],
        label_visibility="collapsed",
        horizontal=False
    )

st.markdown('</div>', unsafe_allow_html=True)

# ── LOOKUP & DISPLAY ─────────────────────────────────────────────────────────
if code_input and code_input.strip():
    query = code_input.strip()
    matches = df[df["code"] == query]

    if len(matches) == 0:
        # Try partial / starts-with
        matches = df[df["code"].str.startswith(query)]

    if len(matches) == 0:
        st.markdown(f"""
        <div class="not-found">
          <div class="icon">🔍</div>
          <h3>No results found for "{query}"</h3>
          <p>Check the code and try again. HSN codes are typically 4–8 digits; SAC codes are 6 digits.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # If multiple, show first exact match or let user pick
        if len(matches) == 1:
            row = matches.iloc[0]
        else:
            st.markdown(f'<p style="color:#8b949e;font-size:0.9rem;">🔎 Found <b style="color:#00c9a7">{len(matches)}</b> matching codes. Showing exact match or first result.</p>', unsafe_allow_html=True)
            exact = matches[matches["code"] == query]
            row = exact.iloc[0] if len(exact) > 0 else matches.iloc[0]

        gst_val  = row["gst_total"]
        tax_head = row["tax_head"]
        schedule = row["schedule"]
        code_type = row["type"]
        description = row["description"]
        category = row["category"]
        cgst_v = row["cgst"]
        sgst_v = row["sgst"]
        igst_v = row["igst"]

        badge_cls, badge_txt = gst_badge(gst_val)
        ctx_title, ctx_body  = context_advice(role, gst_val, tax_head)

        # Determine which rate to highlight
        is_inter  = "Inter" in txn
        rate_show = igst_v if is_inter else gst_val

        # ── Result Card ──
        st.markdown(f"""
        <div class="result-card">

          <!-- Top row: code + badge -->
          <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem; margin-bottom:1.2rem;">
            <div>
              <div style="color:#8b949e;font-size:0.75rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;">
                {'HSN Code (Goods)' if code_type == 'HSN' else 'SAC Code (Services)'}
              </div>
              <div style="color:#e6edf3;font-size:2rem;font-weight:800;letter-spacing:0.05em;line-height:1.1;">
                {row['code']}
              </div>
            </div>
            <span class="tax-badge {badge_cls}">{badge_txt}</span>
          </div>

          <!-- Description -->
          <div style="background:#0d1117;border:1px solid #30363d;border-radius:12px;padding:1rem 1.2rem;margin-bottom:1.5rem;">
            <div style="color:#8b949e;font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Description</div>
            <div style="color:#e6edf3;font-size:0.95rem;line-height:1.6;">{description}</div>
          </div>

          <!-- Tax Breakdown -->
          <div class="section-title">📊 Tax Breakdown</div>
          <div class="tax-grid">
            <div class="tax-item">
              <div class="t-val">{gst_val}</div>
              <div class="t-lbl">Total GST</div>
              <div class="t-desc">Combined rate</div>
            </div>
            <div class="tax-item">
              <div class="t-val">{cgst_v}</div>
              <div class="t-lbl">CGST</div>
              <div class="t-desc">Central tax</div>
            </div>
            <div class="tax-item">
              <div class="t-val">{sgst_v}</div>
              <div class="t-lbl">SGST / UTGST</div>
              <div class="t-desc">State / UT tax</div>
            </div>
            <div class="tax-item">
              <div class="t-val">{igst_v}</div>
              <div class="t-lbl">IGST</div>
              <div class="t-desc">Inter-state</div>
            </div>
          </div>

          <!-- Details -->
          <div class="section-title">🗂 Classification Details</div>
          <div class="info-row">
            <span class="info-key">Tax Head</span>
            <span class="info-val">{tax_head}</span>
          </div>
          <div class="info-row">
            <span class="info-key">Schedule</span>
            <span class="info-val">{schedule}</span>
          </div>
          <div class="info-row">
            <span class="info-key">Category</span>
            <span class="info-val">{category}</span>
          </div>
          <div class="info-row">
            <span class="info-key">Applicable Rate ({('Inter-State' if is_inter else 'Intra-State')})</span>
            <span class="info-val" style="color:#00c9a7;font-weight:700;">{igst_v if is_inter else f'CGST {cgst_v} + SGST {sgst_v}'}</span>
          </div>

          <!-- Context Box -->
          <div class="context-box">
            <div class="ctx-title">{'🛒' if 'Buyer' in role else '🏭'} {role} — {ctx_title}</div>
            <div class="ctx-body">{ctx_body}</div>
          </div>

        </div>
        """, unsafe_allow_html=True)

        # ── Show all matches if multiple ──────────────────────────────────────
        if len(matches) > 1:
            st.markdown('<div style="margin-top:2rem;">', unsafe_allow_html=True)
            st.markdown(f'<div class="section-title" style="color:#8b949e;">📋 All {len(matches)} matches for "{query}"</div>', unsafe_allow_html=True)
            display_df = matches[["code","type","description","gst_total","cgst","sgst","igst","schedule","tax_head"]].copy()
            display_df.columns = ["Code","Type","Description","GST Total","CGST","SGST","IGST","Schedule","Tax Head"]
            st.dataframe(
                display_df,
                use_container_width=True,
                height=min(400, 40 + len(display_df)*35),
                hide_index=True
            )
            st.markdown('</div>', unsafe_allow_html=True)

else:
    # Idle state
    st.markdown("""
    <div style="text-align:center;padding:3rem 1rem;color:#4d5566;">
      <div style="font-size:4rem;margin-bottom:1rem;">🔎</div>
      <div style="color:#8b949e;font-size:1.05rem;font-weight:500;">Enter an HSN or SAC code above to get started</div>
      <div style="color:#4d5566;font-size:0.85rem;margin-top:0.5rem;">
        HSN = Harmonized System of Nomenclature (Goods) &nbsp;|&nbsp; SAC = Services Accounting Code
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="margin-top:3rem;">
<div style="text-align:center;color:#4d5566;font-size:0.8rem;padding:1rem 0 2rem;">
  Data sourced directly from uploaded Excel file &nbsp;·&nbsp; 13,172 HSN/SAC codes &nbsp;·&nbsp; GST India
</div>
""", unsafe_allow_html=True)
