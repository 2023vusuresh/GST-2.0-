import streamlit as st
import pandas as pd
import base64

st.set_page_config(
    page_title="GST HSN/SAC Code Finder",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Encode local images to base64 ───────────────────────────────────────────
def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

img1_b64 = img_to_base64("1780826733620_image.png")
img2_b64 = img_to_base64("1780826759946_image.png")

img1_src = f"data:image/png;base64,{img1_b64}" if img1_b64 else ""
img2_src = f"data:image/png;base64,{img2_b64}" if img2_b64 else ""

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500;600&display=swap');

:root {
  --bg:        #050d1a;
  --surface:   #0c1829;
  --card:      #0f2035;
  --border:    rgba(255,255,255,0.08);
  --gold:      #F5A623;
  --gold-light:#FFD166;
  --teal:      #00C9A7;
  --blue:      #0EA5E9;
  --text:      #E8F0FE;
  --muted:     #6B84A3;
  --danger:    #FF5E7A;
}

html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif;
  color: var(--text);
}

.stApp {
  background: var(--bg);
  min-height: 100vh;
}

.block-container {
  padding: 0 2rem 3rem 2rem !important;
  max-width: 1280px;
}

/* ─── HERO BANNER ─────────────────────────────────────────────────── */
.hero {
  position: relative;
  border-radius: 0 0 32px 32px;
  overflow: hidden;
  margin: 0 -2rem 2.5rem -2rem;
  padding: 0;
  background: linear-gradient(135deg, #020c1b 0%, #0a1f3d 50%, #041226 100%);
  border-bottom: 1px solid rgba(0,201,167,0.25);
}

.hero-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 3rem 3.5rem 2.5rem 3.5rem;
  position: relative;
  z-index: 2;
  gap: 2rem;
}

.hero-glow {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 60% 80% at 70% 50%, rgba(0,201,167,0.08) 0%, transparent 70%),
    radial-gradient(ellipse 40% 60% at 20% 30%, rgba(245,166,35,0.06) 0%, transparent 60%);
  pointer-events: none;
  z-index: 1;
}

.hero-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(0,201,167,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,201,167,0.04) 1px, transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
  z-index: 0;
}

.hero-text { flex: 1; min-width: 260px; }

.hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(0,201,167,0.12);
  border: 1px solid rgba(0,201,167,0.3);
  border-radius: 50px;
  padding: 0.3rem 1rem;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--teal);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 1rem;
}

.hero-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2rem, 4vw, 3.2rem);
  font-weight: 800;
  line-height: 1.1;
  margin: 0 0 1rem 0;
  color: #fff;
}

.hero-title span.acc-gold {
  background: linear-gradient(90deg, #F5A623, #FFD166);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-title span.acc-teal {
  background: linear-gradient(90deg, #00C9A7, #0EA5E9);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-sub {
  color: var(--muted);
  font-size: 1rem;
  line-height: 1.6;
  max-width: 440px;
}

.hero-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1.2rem;
}

.hero-pill {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 6px;
  padding: 0.25rem 0.75rem;
  font-size: 0.75rem;
  color: #8fa8c8;
  font-weight: 500;
}

.hero-images {
  display: flex;
  gap: 1rem;
  flex-shrink: 0;
}

.hero-img-wrap {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.1);
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}

.hero-img-wrap img {
  width: 220px;
  height: 145px;
  object-fit: cover;
  display: block;
  filter: brightness(0.9) saturate(1.1);
}

.hero-img-wrap .img-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(5,13,26,0.5) 0%, transparent 60%);
}

.hero-img-wrap.secondary img {
  width: 170px;
  height: 113px;
}

/* ─── METRICS ─────────────────────────────────────────────────────── */
.metrics-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 2rem;
}

.metric-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 1.2rem 1.4rem;
  position: relative;
  overflow: hidden;
}

.metric-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--teal), var(--blue));
}

.metric-card.gold::before {
  background: linear-gradient(90deg, var(--gold), var(--gold-light));
}

.metric-card .icon {
  font-size: 1.4rem;
  margin-bottom: 0.6rem;
  display: block;
}

.metric-card .num {
  font-family: 'Syne', sans-serif;
  font-size: 2rem;
  font-weight: 800;
  color: #fff;
  line-height: 1;
  margin-bottom: 0.2rem;
}

.metric-card .lbl {
  font-size: 0.72rem;
  color: var(--muted);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.07em;
}

/* ─── SEARCH SECTION ──────────────────────────────────────────────── */
.search-section {
  background: var(--surface);
  border: 1px solid rgba(0,201,167,0.15);
  border-radius: 20px;
  padding: 2rem 2rem 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 40px rgba(0,0,0,0.3);
  position: relative;
  overflow: hidden;
}

.search-section::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(0,201,167,0.5), transparent);
}

.field-label {
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.09em;
  margin-bottom: 0.4rem;
}

/* Override Streamlit inputs */
input[type="text"], .stTextInput input {
  background: rgba(255,255,255,0.05) !important;
  border: 1.5px solid rgba(255,255,255,0.12) !important;
  border-radius: 12px !important;
  color: #fff !important;
  font-size: 1.05rem !important;
  font-weight: 600 !important;
  font-family: 'DM Sans', sans-serif !important;
  padding: 0.7rem 1rem !important;
}
input[type="text"]:focus, .stTextInput input:focus {
  border-color: var(--teal) !important;
  box-shadow: 0 0 0 3px rgba(0,201,167,0.15) !important;
  outline: none !important;
}
input[type="text"]::placeholder { color: #3a5068 !important; }

/* Radio buttons */
.stRadio > div { flex-direction: column; gap: 0.5rem !important; }
.stRadio label span { color: #a0b4cc !important; font-size: 0.9rem !important; }

/* ─── RESULT CARD ─────────────────────────────────────────────────── */
.result-card {
  background: var(--surface);
  border: 1px solid rgba(0,201,167,0.15);
  border-radius: 24px;
  padding: 2rem 2.2rem;
  box-shadow: 0 8px 60px rgba(0,0,0,0.4);
  animation: slideUp 0.4s ease;
  position: relative;
  overflow: hidden;
}

.result-card::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(0,201,167,0.6), rgba(245,166,35,0.4), transparent);
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Code header */
.code-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--border);
}

.code-type-label {
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--teal);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: 0.3rem;
}

.code-number {
  font-family: 'Syne', sans-serif;
  font-size: 2.4rem;
  font-weight: 800;
  color: #fff;
  line-height: 1;
  letter-spacing: 0.03em;
}

/* Tax badge */
.tax-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.5rem 1.4rem;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 700;
  font-family: 'Syne', sans-serif;
}

.badge-exempt { background: rgba(0,201,167,0.12); color: #00C9A7; border: 1.5px solid rgba(0,201,167,0.35); }
.badge-5      { background: rgba(14,165,233,0.12); color: #38BDF8; border: 1.5px solid rgba(14,165,233,0.35); }
.badge-12     { background: rgba(245,166,35,0.12); color: #F5A623; border: 1.5px solid rgba(245,166,35,0.35); }
.badge-18     { background: rgba(251,146,60,0.12); color: #FB923C; border: 1.5px solid rgba(251,146,60,0.35); }
.badge-28     { background: rgba(255,94,122,0.12); color: #FF5E7A; border: 1.5px solid rgba(255,94,122,0.35); }
.badge-other  { background: rgba(107,132,163,0.12); color: #6B84A3; border: 1.5px solid rgba(107,132,163,0.35); }

/* Description block */
.desc-block {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border);
  border-left: 3px solid var(--teal);
  border-radius: 12px;
  padding: 1rem 1.3rem;
  margin-bottom: 1.8rem;
}

.desc-label {
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 0.4rem;
}

.desc-text {
  color: var(--text);
  font-size: 0.95rem;
  line-height: 1.65;
}

/* Section heading */
.sec-head {
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin: 1.6rem 0 0.9rem 0;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.sec-head::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}

/* Tax breakdown grid */
.tax-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.8rem;
  margin-bottom: 0.5rem;
}

.tax-cell {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1rem;
  text-align: center;
  transition: border-color 0.2s;
}

.tax-cell.highlight {
  border-color: rgba(245,166,35,0.4);
  background: rgba(245,166,35,0.06);
}

.tax-cell .t-val {
  font-family: 'Syne', sans-serif;
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--gold-light);
  line-height: 1;
}

.tax-cell.highlight .t-val { color: var(--gold); }

.tax-cell .t-lbl {
  font-size: 0.65rem;
  color: var(--muted);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  margin-top: 0.3rem;
}

.tax-cell .t-desc {
  font-size: 0.7rem;
  color: #4a6380;
  margin-top: 0.15rem;
}

/* Info rows */
.info-table { margin-top: 0.5rem; }

.info-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.7rem 0;
  border-bottom: 1px solid rgba(255,255,255,0.04);
}

.info-row:last-child { border-bottom: none; }

.info-key {
  color: var(--muted);
  font-size: 0.78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  min-width: 140px;
}

.info-val {
  color: var(--text);
  font-size: 0.9rem;
  font-weight: 500;
  text-align: right;
}

.info-val.accent { color: var(--gold); font-weight: 700; }

/* Context advice */
.advice-box {
  background: rgba(0,201,167,0.06);
  border: 1px solid rgba(0,201,167,0.2);
  border-radius: 16px;
  padding: 1.3rem 1.6rem;
  margin-top: 1.5rem;
  display: flex;
  gap: 1rem;
}

.advice-icon { font-size: 1.8rem; flex-shrink: 0; }

.advice-title {
  color: var(--teal);
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  margin-bottom: 0.4rem;
}

.advice-body {
  color: #8fa8c8;
  font-size: 0.88rem;
  line-height: 1.65;
}

/* Not found */
.not-found {
  text-align: center;
  padding: 4rem 2rem;
  background: var(--surface);
  border: 1px dashed rgba(255,94,122,0.25);
  border-radius: 20px;
}

.not-found .nf-icon { font-size: 3.5rem; margin-bottom: 1rem; }
.not-found h3 { color: #a0b4cc; font-family: 'Syne', sans-serif; margin: 0 0 0.5rem; }
.not-found p { color: var(--muted); font-size: 0.9rem; }

/* Idle state */
.idle-state {
  text-align: center;
  padding: 4rem 2rem;
  border: 1px dashed rgba(255,255,255,0.07);
  border-radius: 20px;
  background: rgba(255,255,255,0.02);
}

.idle-icon { font-size: 3rem; margin-bottom: 1rem; }
.idle-main { color: #6B84A3; font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem; }
.idle-sub { color: #3a5068; font-size: 0.85rem; }

/* Footer */
.footer {
  text-align: center;
  padding: 2rem 0 1.5rem;
  color: #2d4460;
  font-size: 0.78rem;
  border-top: 1px solid rgba(255,255,255,0.05);
  margin-top: 3rem;
}

.footer .dot { margin: 0 0.4rem; color: var(--teal); }

/* Dataframe */
.stDataFrame { border-radius: 12px !important; overflow: hidden !important; }

/* Table highlight */
[data-testid="stDataFrame"] th { background: var(--card) !important; }

/* Divider */
hr { border-color: rgba(255,255,255,0.06) !important; }

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
.viewerBadge_container__1QSob { display: none; }

/* Radio */
.stRadio [data-baseweb="radio"] { gap: 0.4rem !important; }
</style>
""", unsafe_allow_html=True)


# ── Load Data ────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_excel("HSN_SAC_data.xlsx")
    df.columns = [
        "sno", "code", "description", "type",
        "gst_total", "cgst", "sgst", "igst",
        "tax_head", "schedule", "category"
    ]
    for col in ["code","type","gst_total","cgst","sgst","igst","tax_head","schedule","category","description"]:
        df[col] = df[col].astype(str).str.strip()
    return df

df = load_data()

total   = len(df)
hsn_cnt = len(df[df["type"] == "HSN"])
sac_cnt = len(df[df["type"] == "SAC"])
exempt  = len(df[df["gst_total"].str.contains("NIL|EXEMPT", case=False, na=False)])


# ── Helpers ──────────────────────────────────────────────────────────────────
def gst_badge(val):
    v = val.upper()
    if "NIL" in v or "EXEMPT" in v: return "badge-exempt", "NIL / EXEMPT"
    if "28" in v: return "badge-28", val
    if "18" in v: return "badge-18", val
    if "12" in v: return "badge-12", val
    if "5"  in v: return "badge-5",  val
    return "badge-other", val

def context_advice(role, gst_val, tax_head):
    is_exempt = "NIL" in gst_val.upper() or "EXEMPT" in gst_val.upper()
    if "Buyer" in role:
        if is_exempt:
            return ("🛒", "No GST payable on this purchase.",
                    "This item is GST-exempt. No Input Tax Credit (ITC) can be claimed. "
                    "No reverse charge applies. Purchase at face value.")
        elif "Outside GST" in tax_head:
            return ("🛒", "Outside GST scope — state levies may apply.",
                    "This item falls outside GST. State-level taxes/levies may be charged by the supplier.")
        else:
            return ("🛒", "GST payable — ITC can be claimed.",
                    f"You will pay GST ({gst_val}) to your supplier. "
                    "If registered under GST, claim Input Tax Credit (ITC). "
                    "Inter-state: IGST applies. Intra-state: CGST + SGST applies.")
    else:
        if is_exempt:
            return ("🏭", "No GST to collect from buyer.",
                    "This item is exempt. Do NOT charge GST on your invoice. "
                    "No ITC can be claimed on inputs used for this exempt supply.")
        elif "Outside GST" in tax_head:
            return ("🏭", "Outside GST scope — do not charge GST.",
                    "This item is outside the GST framework. Do not levy GST. "
                    "State-specific taxes may apply. Consult your tax advisor.")
        else:
            return ("🏭", "Collect GST from buyer and remit to government.",
                    f"Charge GST ({gst_val}) on your invoice. "
                    "Intra-state: collect CGST + SGST. Inter-state: collect IGST. "
                    "File GSTR-1 and GSTR-3B and remit collected tax.")


# ── HERO BANNER ──────────────────────────────────────────────────────────────
img1_html = f'<img src="{img1_src}" alt="GST 2.0">' if img1_src else '<div style="width:220px;height:145px;background:rgba(255,255,255,0.05);border-radius:12px;display:flex;align-items:center;justify-content:center;color:#3a5068;font-size:0.8rem;">GST Image</div>'
img2_html = f'<img src="{img2_src}" alt="GST">' if img2_src else ''

img2_block = f"""
  <div class="hero-img-wrap secondary">
    {img2_html}
    <div class="img-overlay"></div>
  </div>
""" if img2_src else ""

st.markdown(f"""
<div class="hero">
  <div class="hero-grid"></div>
  <div class="hero-glow"></div>
  <div class="hero-inner">
    <div class="hero-text">
      <div class="hero-eyebrow">🇮🇳 India GST Portal 2.0</div>
      <h1 class="hero-title">
        HSN / SAC<br>
        <span class="acc-gold">Code Finder</span>
      </h1>
      <p class="hero-sub">
        Instantly look up tax rates, GST schedules &amp; compliance guidance from
        official India GST data — 13,000+ codes at your fingertips.
      </p>
      <div class="hero-pills">
        <span class="hero-pill">🟢 NIL / Exempt</span>
        <span class="hero-pill">🔵 5% Slab</span>
        <span class="hero-pill">🟡 12% Slab</span>
        <span class="hero-pill">🟠 18% Slab</span>
        <span class="hero-pill">🔴 28% Slab</span>
      </div>
    </div>
    <div class="hero-images">
      <div class="hero-img-wrap">
        {img1_html}
        <div class="img-overlay"></div>
      </div>
      {img2_block}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── METRIC CARDS ─────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="metrics-strip">
  <div class="metric-card">
    <span class="icon">📦</span>
    <div class="num">{total:,}</div>
    <div class="lbl">Total Codes</div>
  </div>
  <div class="metric-card gold">
    <span class="icon">🏷️</span>
    <div class="num">{hsn_cnt:,}</div>
    <div class="lbl">HSN Codes (Goods)</div>
  </div>
  <div class="metric-card">
    <span class="icon">⚙️</span>
    <div class="num">{sac_cnt:,}</div>
    <div class="lbl">SAC Codes (Services)</div>
  </div>
  <div class="metric-card">
    <span class="icon">✅</span>
    <div class="num">{exempt:,}</div>
    <div class="lbl">Exempt Items</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── SEARCH SECTION ────────────────────────────────────────────────────────────
st.markdown('<div class="search-section">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2.5, 2, 2])

with col1:
    st.markdown('<div class="field-label">🔍 Enter HSN / SAC Code</div>', unsafe_allow_html=True)
    code_input = st.text_input(
        label="code",
        placeholder="e.g. 10061010 or 995411",
        label_visibility="collapsed",
        key="code_search"
    )

with col2:
    st.markdown('<div class="field-label">👤 Your Role</div>', unsafe_allow_html=True)
    role = st.radio(
        label="role",
        options=["Buyer / Vendor (Purchasing)", "Supplier / Seller (Selling)"],
        label_visibility="collapsed",
        horizontal=False
    )

with col3:
    st.markdown('<div class="field-label">🔄 Transaction Type</div>', unsafe_allow_html=True)
    txn = st.radio(
        label="txn",
        options=["Intra-State (CGST + SGST)", "Inter-State (IGST)"],
        label_visibility="collapsed",
        horizontal=False
    )

st.markdown('</div>', unsafe_allow_html=True)


# ── RESULT / IDLE ─────────────────────────────────────────────────────────────
if code_input and code_input.strip():
    query = code_input.strip()
    matches = df[df["code"] == query]
    if len(matches) == 0:
        matches = df[df["code"].str.startswith(query)]

    if len(matches) == 0:
        st.markdown(f"""
        <div class="not-found">
          <div class="nf-icon">🔍</div>
          <h3>No results for "{query}"</h3>
          <p>Check the code and try again. HSN codes are typically 4–8 digits; SAC codes are 6 digits.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        if len(matches) > 1:
            st.markdown(f'<p style="color:#6B84A3;font-size:0.88rem;margin-bottom:0.8rem;">🔎 Found <b style="color:var(--gold)">{len(matches)}</b> matching codes — showing best match.</p>', unsafe_allow_html=True)
            exact = matches[matches["code"] == query]
            row = exact.iloc[0] if len(exact) > 0 else matches.iloc[0]
        else:
            row = matches.iloc[0]

        gst_val     = row["gst_total"]
        tax_head    = row["tax_head"]
        schedule    = row["schedule"]
        code_type   = row["type"]
        description = row["description"]
        category    = row["category"]
        cgst_v      = row["cgst"]
        sgst_v      = row["sgst"]
        igst_v      = row["igst"]

        badge_cls, badge_txt     = gst_badge(gst_val)
        adv_icon, ctx_title, ctx_body = context_advice(role, gst_val, tax_head)
        is_inter = "Inter" in txn

        st.markdown(f"""
        <div class="result-card">

          <div class="code-header">
            <div>
              <div class="code-type-label">{'HSN Code — Goods' if code_type == 'HSN' else 'SAC Code — Services'}</div>
              <div class="code-number">{row['code']}</div>
            </div>
            <span class="tax-badge {badge_cls}">{badge_txt}</span>
          </div>

          <div class="desc-block">
            <div class="desc-label">Description</div>
            <div class="desc-text">{description}</div>
          </div>

          <div class="sec-head">📊 Tax Breakdown</div>
          <div class="tax-grid">
            <div class="tax-cell {'highlight' if not is_inter else ''}">
              <div class="t-val">{gst_val}</div>
              <div class="t-lbl">Total GST</div>
              <div class="t-desc">Combined rate</div>
            </div>
            <div class="tax-cell {'highlight' if not is_inter else ''}">
              <div class="t-val">{cgst_v}</div>
              <div class="t-lbl">CGST</div>
              <div class="t-desc">Central tax</div>
            </div>
            <div class="tax-cell {'highlight' if not is_inter else ''}">
              <div class="t-val">{sgst_v}</div>
              <div class="t-lbl">SGST / UTGST</div>
              <div class="t-desc">State / UT tax</div>
            </div>
            <div class="tax-cell {'highlight' if is_inter else ''}">
              <div class="t-val">{igst_v}</div>
              <div class="t-lbl">IGST</div>
              <div class="t-desc">Inter-state</div>
            </div>
          </div>

          <div class="sec-head">🗂 Classification</div>
          <div class="info-table">
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
              <span class="info-key">Applicable Rate<br><small style="font-weight:400;text-transform:none;letter-spacing:0;">({'Inter-State' if is_inter else 'Intra-State'})</small></span>
              <span class="info-val accent">{igst_v + ' (IGST)' if is_inter else f'CGST {cgst_v} + SGST {sgst_v}'}</span>
            </div>
          </div>

          <div class="advice-box">
            <div class="advice-icon">{adv_icon}</div>
            <div>
              <div class="advice-title">{role.split('(')[0].strip()} — {ctx_title}</div>
              <div class="advice-body">{ctx_body}</div>
            </div>
          </div>

        </div>
        """, unsafe_allow_html=True)

        if len(matches) > 1:
            st.markdown('<div style="margin-top:2rem;">', unsafe_allow_html=True)
            st.markdown(f'<div class="sec-head">📋 All {len(matches)} matches for "{query}"</div>', unsafe_allow_html=True)
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
    st.markdown("""
    <div class="idle-state">
      <div class="idle-icon">🧾</div>
      <div class="idle-main">Enter an HSN or SAC code above to get started</div>
      <div class="idle-sub">
        HSN = Harmonized System of Nomenclature (Goods) &nbsp;·&nbsp; SAC = Services Accounting Code
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  Data sourced from official GST India schedule
  <span class="dot">·</span>
  13,172 HSN / SAC codes
  <span class="dot">·</span>
  For guidance only — consult a CA for compliance decisions
</div>
""", unsafe_allow_html=True)
