"""Look & feel for the Streamlit app: CSS, hero banner, page headers, plot style."""
import streamlit as st
import matplotlib as mpl

INK, TEAL, TEAL_DK, AMBER, MIST, LINE = "#0F1B2D", "#0B7285", "#095C6B", "#F2A104", "#F3F6F9", "#DDE5EC"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Figtree:wght@400;500;600&display=swap');
html, body, [class*="css"], .stApp {{ font-family: 'Figtree', system-ui, sans-serif; }}
h1, h2, h3, h4 {{ font-family: 'Bricolage Grotesque', 'Figtree', sans-serif !important; color: {INK}; letter-spacing: -0.01em; }}
.block-container {{ padding-top: 2rem; max-width: 1180px; }}
footer, #MainMenu {{ visibility: hidden; }}

/* sidebar */
section[data-testid="stSidebar"] {{ background: {INK}; }}
section[data-testid="stSidebar"] * {{ color: #E6EDF3 !important; }}
section[data-testid="stSidebar"] h1 {{ color: #fff !important; font-size: 1.35rem; }}
section[data-testid="stSidebar"] [role="radiogroup"] label {{
  padding: .55rem .8rem; border-radius: 10px; margin-bottom: 2px; transition: background .15s; }}
section[data-testid="stSidebar"] [role="radiogroup"] label:hover {{ background: rgba(255,255,255,.08); }}
section[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {{ background: {TEAL}; }}
section[data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {{ display: none; }}
section[data-testid="stSidebar"] .stCaption, section[data-testid="stSidebar"] small {{ color: #9FB3C8 !important; }}

/* hero */
.hero {{ position: relative; overflow: hidden; border-radius: 18px; padding: 2rem 2.2rem 1.6rem;
  background: linear-gradient(120deg, {INK} 0%, #12324A 100%); color: #fff; margin-bottom: 1.4rem; }}
.hero h1 {{ color: #fff !important; font-size: 2.3rem; margin: 0 0 .35rem; }}
.hero p {{ color: #B8C7D6; margin: 0; max-width: 560px; font-size: 1.02rem; line-height: 1.5; }}
.hero svg {{ position: absolute; right: 0; bottom: 0; width: 58%; height: 100%; opacity: .95; pointer-events: none; }}
.hero .wave {{ fill: none; stroke: {AMBER}; stroke-width: 2.2; stroke-linecap: round; stroke-dasharray: 1400; stroke-dashoffset: 1400;
  animation: draw 2.4s ease-out forwards; }}
.hero .wave2 {{ stroke: #4FC3D1; stroke-width: 1.6; opacity: .75; animation-delay: .35s; }}
@keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
@media (prefers-reduced-motion: reduce) {{ .hero .wave {{ animation: none; stroke-dashoffset: 0; }} }}
@media (max-width: 700px) {{ .hero svg {{ opacity: .25; width: 100%; }} .hero h1 {{ font-size: 1.7rem; }} }}

/* page header */
.pagehead h2 {{ margin: 0 0 .15rem; font-size: 1.7rem; }}
.pagehead p {{ color: #5B6B7C; margin: 0 0 1.1rem; }}

/* widgets */
div[data-testid="stMetric"] {{ background: {MIST}; border: 1px solid {LINE}; border-left: 4px solid {TEAL};
  border-radius: 12px; padding: .8rem 1rem; }}
div[data-testid="stMetricLabel"] p {{ color: #5B6B7C; }}
div[data-testid="stMetricValue"] {{ font-family: 'Bricolage Grotesque', sans-serif; color: {INK}; }}
div[data-testid="stVerticalBlockBorderWrapper"] {{ border-radius: 14px; }}
.stButton > button, .stDownloadButton > button {{ border-radius: 10px; font-weight: 600; padding: .5rem 1.2rem; transition: transform .1s; }}
.stButton > button:active {{ transform: scale(.98); }}
.stButton > button[kind="primary"] {{ background: {TEAL}; border: 0; }}
.stButton > button[kind="primary"]:hover {{ background: {TEAL_DK}; }}
button[data-baseweb="tab"] {{ font-weight: 600; }}
div[data-testid="stDataFrame"] {{ border: 1px solid {LINE}; border-radius: 12px; overflow: hidden; }}
.stAlert {{ border-radius: 12px; }}
:focus-visible {{ outline: 2px solid {AMBER} !important; outline-offset: 2px; }}
</style>
"""

WAVE = """
<svg viewBox="0 0 600 160" preserveAspectRatio="none" aria-hidden="true">
  <path class="wave2 wave" d="M0 100 C40 40 60 150 100 90 S160 30 200 85 S260 150 300 80 S360 20 400 95 S470 140 510 70 S570 50 600 85"/>
  <path class="wave" d="M0 80 C30 120 55 30 95 70 S150 140 195 60 S255 20 295 90 S355 150 400 55 S465 25 510 100 S570 120 600 60"/>
</svg>"""


def setup():
    st.markdown(CSS, unsafe_allow_html=True)
    mpl.rcParams.update({
        "font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False,
        "axes.edgecolor": "#9AA9B8", "axes.labelcolor": INK, "axes.titleweight": "bold", "axes.titlesize": 10,
        "axes.grid": True, "grid.color": "#E7EDF3", "grid.linewidth": .8, "figure.dpi": 130,
        "axes.prop_cycle": mpl.cycler(color=[TEAL, AMBER, "#D1495B", "#6C5CE7", "#2A9D8F", "#8D99AE", "#264653"]),
    })


def hero():
    st.markdown(f"""<div class="hero"><h1>HAR Transfer Lab</h1>
<p>Train on one dataset, adapt to another, and see which layers actually need to change. Works with your own accelerometer data.</p>{WAVE}</div>""",
                unsafe_allow_html=True)


def page_header(title, sub=""):
    st.markdown(f'<div class="pagehead"><h2>{title}</h2><p>{sub}</p></div>', unsafe_allow_html=True)
