"""
pages/02_Quality_Assessment.py
TELADAN — Quality Assessment Module
CDK4/6 Inhibitors & T-Cell SLR — Studi Kasus UNIMUS 2026
Tools: CASP · JBI · RoB 2 · SYRCLE · ROBINS-I · GRADE
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import random

st.set_page_config(
    page_title="Quality Assessment — TELADAN",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Brand CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.page-title {
    font-family:'Playfair Display',serif; color:#0F2B46;
    font-size:2.2rem; border-bottom:3px solid #C9A227;
    display:inline-block; padding-bottom:0.4rem; margin-bottom:0.5rem;
}
.tool-badge {
    display:inline-block; padding:0.25rem 0.85rem;
    border-radius:20px; font-size:0.8rem; font-weight:600;
    letter-spacing:0.06em; margin:0.2rem;
}
.grade-high   { background:#dcfce7; color:#166534; border:1px solid #86efac; }
.grade-mod    { background:#fef9c3; color:#854d0e; border:1px solid #fde047; }
.grade-low    { background:#ffedd5; color:#9a3412; border:1px solid #fdba74; }
.grade-vlow   { background:#fee2e2; color:#991b1b; border:1px solid #fca5a5; }
.qa-card {
    background:#F4F6F8; border-radius:12px; padding:1.25rem 1.5rem;
    border-left:5px solid #C9A227; margin-bottom:0.85rem;
}
.qa-card h4 { color:#0F2B46; font-family:'Playfair Display',serif;
    font-size:1.1rem; margin-bottom:0.3rem; }
.qa-card p  { color:#64748b; font-size:0.88rem; margin:0; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏛️ TELADAN")
    st.caption("Quality Assessment Module")
    st.markdown("---")
    tool_sel = st.radio(
        "Pilih Tool / Tahap",
        [
            "📋 Overview & Tool Map",
            "🔬 In Vitro — JBI + Custom",
            "🐭 In Vivo — SYRCLE",
            "💊 Clinical RCT — RoB 2",
            "📈 Clinical Non-RCT — ROBINS-I",
            "🏅 GRADE Evidence Profile",
            "📊 Summary Heatmap",
        ],
        index=0,
    )
    st.markdown("---")
    st.markdown("""
    **Studi Included:** 68  
    **In vitro:** 17 studi  
    **In vivo (murine):** 31 studi  
    **Clinical RCT:** 8 studi  
    **Clinical Non-RCT:** 12 studi
    """)
    st.markdown("---")
    st.link_button("← SLR Demo", "https://teladan.streamlit.app/SLR_Demo", use_container_width=True)
    st.link_button("🏛️ TELADAN Home", "https://teladan.streamlit.app", use_container_width=True)

# ══════════════════════════════════════════════════════════════════
# TAB 0 — OVERVIEW & TOOL MAP
# ══════════════════════════════════════════════════════════════════
if tool_sel.startswith("📋"):
    st.markdown('<h2 class="page-title">📋 Quality Assessment — Overview</h2>', unsafe_allow_html=True)
    st.caption("Pemilihan tool berdasarkan desain studi · PRISMA-P Item 14")

    st.markdown("""
    Quality assessment dilakukan oleh **dua reviewer independen** (DWTS & MK).
    Ketidaksepakatan diselesaikan melalui diskusi; jika tidak tercapai konsensus, arbiter ketiga dilibatkan.
    """)

    # Tool mapping table
    st.markdown("### 🗺️ Peta Tool per Desain Studi")
    tool_map = pd.DataFrame([
        {"Desain Studi": "In vitro (primary T cells / cell lines)",
         "Tool": "JBI Critical Appraisal + Custom In Vitro Domains",
         "Jumlah Studi": 17, "Skor Max": 12,
         "Referensi": "JBI 2020; Moher et al."},
        {"Desain Studi": "In vivo — animal tumour models",
         "Tool": "SYRCLE Risk of Bias Tool",
         "Jumlah Studi": 31, "Skor Max": 10,
         "Referensi": "Hooijmans et al. 2014"},
        {"Desain Studi": "Clinical — Randomised (RCT)",
         "Tool": "RoB 2 (Cochrane)",
         "Jumlah Studi": 8, "Skor Max": "5 domains",
         "Referensi": "Sterne et al. 2019"},
        {"Desain Studi": "Clinical — Non-randomised (NRSI)",
         "Tool": "ROBINS-I",
         "Jumlah Studi": 12, "Skor Max": "7 domains",
         "Referensi": "Sterne et al. 2016"},
    ])
    st.dataframe(tool_map, use_container_width=True, hide_index=True)

    # Inter-rater agreement
    st.markdown("### 🤝 Inter-Rater Agreement")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Cohen's κ — In vitro", "0.81", "Almost perfect")
    c2.metric("Cohen's κ — SYRCLE", "0.76", "Substantial")
    c3.metric("Cohen's κ — RoB 2", "0.88", "Almost perfect")
    c4.metric("Cohen's κ — ROBINS-I", "0.79", "Substantial")

    # Decision rules
    st.markdown("### 📏 Decision Rules")
    st.markdown("""
    | Skor Total | Interpretasi | Tindakan |
    |-----------|-------------|---------|
    | **≥ 75%** | Kualitas Tinggi | Include, bobot penuh dalam sintesis |
    | **50–74%** | Kualitas Sedang | Include, flagged dalam analisis sensitivitas |
    | **< 50%** | Kualitas Rendah | Exclude atau analisis sensitivitas terpisah |
    """)

    # Flowchart quality gate
    st.info("""
    **⚙️ TELADAN Quality Gate (otomatis)**  
    Setelah skor diinput, TELADAN otomatis:  
    1. Flag studi kualitas rendah (merah) pada harvest plot  
    2. Jalankan analisis sensitivitas: sintesis dengan/tanpa studi kualitas rendah  
    3. Update GRADE rating jika ≥50% studi kualitas sedang/rendah
    """)

# ══════════════════════════════════════════════════════════════════
# TAB 1 — IN VITRO (JBI + Custom)
# ══════════════════════════════════════════════════════════════════
elif tool_sel.startswith("🔬"):
    st.markdown('<h2 class="page-title">🔬 In Vitro — JBI + Custom Domains</h2>', unsafe_allow_html=True)
    st.caption("17 studi in vitro · Skor 0–12 · Threshold ≥9 = High Quality")

    domains_iv = [
        "1. Cell source jelas (primer vs line)",
        "2. Aktivasi protokol terstandardisasi",
        "3. Konsentrasi obat dilaporkan (nM/µM)",
        "4. Durasi eksposur dilaporkan (jam)",
        "5. Kontrol negatif/kendaraan ada",
        "6. Kontrol positif ada",
        "7. Replikasi biologis ≥3",
        "8. Replikasi teknis dijelaskan",
        "9. Blinding pada outcome assessment",
        "10. Metode statistik sesuai",
        "11. Ukuran efek + CI dilaporkan",
        "12. Konflik kepentingan dideklarasikan",
    ]

    random.seed(42)
    studies_iv = [f"Studi-{i+1}" for i in range(17)]
    labels = {0: "❌ Tidak", 1: "✅ Ya", 2: "❓ Unclear"}
    color_map = {0: "#dc2626", 1: "#16a34a", 2: "#C9A227"}

    # Generate scores
    scores_iv = []
    for s in studies_iv:
        row = [random.choices([0, 1, 2], weights=[0.15, 0.65, 0.20])[0]
               for _ in domains_iv]
        scores_iv.append(row)

    df_iv = pd.DataFrame(scores_iv, index=studies_iv, columns=[d[:30] for d in domains_iv])
    total_scores = [sum(1 for v in row if v == 1) for row in scores_iv]
    quality_labels = ["🟢 Tinggi" if s >= 9 else ("🟡 Sedang" if s >= 6 else "🔴 Rendah")
                      for s in total_scores]

    # Summary metrics
    high_q = quality_labels.count("🟢 Tinggi")
    mid_q  = quality_labels.count("🟡 Sedang")
    low_q  = quality_labels.count("🔴 Rendah")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total In Vitro", "17 studi")
    c2.metric("🟢 Kualitas Tinggi", f"{high_q}", f"{high_q/17*100:.0f}%")
    c3.metric("🟡 Kualitas Sedang", f"{mid_q}", f"{mid_q/17*100:.0f}%")
    c4.metric("🔴 Kualitas Rendah", f"{low_q}", f"{low_q/17*100:.0f}%")

    # Heatmap
    z_vals = [[color_map[v] for v in row] for row in scores_iv]
    text_vals = [[labels[v] for v in row] for row in scores_iv]

    fig = go.Figure(go.Heatmap(
        z=scores_iv,
        x=[d[:28] + "…" if len(d) > 28 else d for d in domains_iv],
        y=[f"{s} ({t})" for s, t in zip(studies_iv, quality_labels)],
        colorscale=[[0, "#dc2626"], [0.5, "#C9A227"], [1, "#16a34a"]],
        zmin=0, zmax=2,
        text=text_vals,
        texttemplate="%{text}",
        textfont=dict(size=9),
        showscale=False,
    ))
    fig.update_layout(
        title="JBI + Custom Domains — In Vitro Quality Assessment",
        height=520,
        xaxis=dict(tickangle=-35, tickfont=dict(size=9)),
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter",
        title_font_family="Playfair Display",
        title_font_color="#0F2B46",
        margin=dict(l=140, r=20, t=60, b=150),
    )
    st.plotly_chart(fig, use_container_width=True)

    # Table with totals
    df_display = pd.DataFrame({
        "Studi": studies_iv,
        "Total Skor (/ 12)": total_scores,
        "Persentase (%)": [f"{s/12*100:.0f}%" for s in total_scores],
        "Kualitas": quality_labels,
    })
    st.dataframe(df_display, use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════
# TAB 2 — IN VIVO (SYRCLE)
# ══════════════════════════════════════════════════════════════════
elif tool_sel.startswith("🐭"):
    st.markdown('<h2 class="page-title">🐭 In Vivo — SYRCLE Risk of Bias</h2>', unsafe_allow_html=True)
    st.caption("31 studi animal · 10 domain · Hooijmans et al. 2014")

    syrcle_domains = [
        "1. Sequence Generation",
        "2. Baseline Characteristics",
        "3. Allocation Concealment",
        "4. Random Housing",
        "5. Blinding (caregiver)",
        "6. Random Outcome Assessment",
        "7. Blinding (outcome)",
        "8. Incomplete Outcome Data",
        "9. Selective Outcome Reporting",
        "10. Other Sources of Bias",
    ]

    random.seed(11)
    studies_iv = [f"Study-{i+1:02d}" for i in range(31)]
    risk_labels = {0: "L", 1: "?", 2: "H"}
    risk_colors = {0: "#16a34a", 1: "#C9A227", 2: "#dc2626"}
    risk_weights = [0.45, 0.40, 0.15]

    scores_s = [[random.choices([0, 1, 2], weights=risk_weights)[0]
                 for _ in syrcle_domains] for _ in studies_iv]

    # Overall risk per study
    overall = []
    for row in scores_s:
        h = row.count(2)
        u = row.count(1)
        if h >= 2:
            overall.append("🔴 High")
        elif h == 1 or u >= 4:
            overall.append("🟡 Some Concerns")
        else:
            overall.append("🟢 Low")

    c1, c2, c3 = st.columns(3)
    c1.metric("🟢 Low Risk", overall.count("🟢 Low"))
    c2.metric("🟡 Some Concerns", overall.count("🟡 Some Concerns"))
    c3.metric("🔴 High Risk", overall.count("🔴 High"))

    # Traffic-light heatmap
    z_text = [[risk_labels[v] for v in row] for row in scores_s]
    fig = go.Figure(go.Heatmap(
        z=scores_s,
        x=syrcle_domains,
        y=[f"{s} {o}" for s, o in zip(studies_iv, overall)],
        colorscale=[[0, "#16a34a"], [0.5, "#C9A227"], [1, "#dc2626"]],
        zmin=0, zmax=2,
        text=z_text, texttemplate="%{text}",
        showscale=False,
    ))
    fig.update_layout(
        title="SYRCLE Traffic Light Plot — 31 Animal Studies",
        height=680,
        xaxis=dict(tickangle=-30, tickfont=dict(size=9)),
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter",
        title_font_family="Playfair Display",
        title_font_color="#0F2B46",
        margin=dict(l=150, r=20, t=60, b=120),
    )
    st.plotly_chart(fig, use_container_width=True)

    # Domain summary bar chart
    st.markdown("**Distribusi Risk per Domain (%)**")
    low_pct  = [sum(1 for r in scores_s if r[d] == 0) / 31 * 100 for d in range(10)]
    unc_pct  = [sum(1 for r in scores_s if r[d] == 1) / 31 * 100 for d in range(10)]
    high_pct = [sum(1 for r in scores_s if r[d] == 2) / 31 * 100 for d in range(10)]

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(name="Low Risk",        x=syrcle_domains, y=low_pct,  marker_color="#16a34a"))
    fig2.add_trace(go.Bar(name="Unclear",         x=syrcle_domains, y=unc_pct,  marker_color="#C9A227"))
    fig2.add_trace(go.Bar(name="High Risk",       x=syrcle_domains, y=high_pct, marker_color="#dc2626"))
    fig2.update_layout(
        barmode="stack",
        title="SYRCLE — Risk Distribution per Domain (%)",
        yaxis_title="% Studies",
        xaxis=dict(tickangle=-25, tickfont=dict(size=9)),
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter",
        title_font_family="Playfair Display",
        title_font_color="#0F2B46",
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.warning("⚠️ **Domain dengan Risiko Tinggi:** *Blinding (caregiver)* dan *Allocation Concealment* paling sering unclear/high — umum pada studi hewan. Dipertimbangkan dalam GRADE downgrade.")

# ══════════════════════════════════════════════════════════════════
# TAB 3 — CLINICAL RCT (RoB 2)
# ══════════════════════════════════════════════════════════════════
elif tool_sel.startswith("💊"):
    st.markdown('<h2 class="page-title">💊 Clinical RCT — RoB 2</h2>', unsafe_allow_html=True)
    st.caption("8 studi RCT · 5 domain · Cochrane RoB 2 · Sterne et al. 2019")

    rob2_domains = [
        "D1: Randomisation Process",
        "D2: Deviations from Intended Intervention",
        "D3: Missing Outcome Data",
        "D4: Measurement of the Outcome",
        "D5: Selection of Reported Results",
    ]

    random.seed(77)
    studies_rct = [
        "Goel et al. 2021", "Deng et al. 2022", "Schaer et al. 2023",
        "Heckler et al. 2021", "Lelliott et al. 2021", "Arndt et al. 2022",
        "Kumar et al. 2024", "Zhang et al. 2025",
    ]
    weights_rct = [0.6, 0.3, 0.1]
    scores_rct = [[random.choices([0, 1, 2], weights=weights_rct)[0]
                   for _ in rob2_domains] for _ in studies_rct]

    # Overall RoB per study
    def rob2_overall(row):
        if 2 in row:
            return "🔴 High"
        elif 1 in row:
            return "🟡 Some Concerns"
        return "🟢 Low"

    overall_rct = [rob2_overall(r) for r in scores_rct]

    c1, c2, c3 = st.columns(3)
    c1.metric("🟢 Low Risk", overall_rct.count("🟢 Low"))
    c2.metric("🟡 Some Concerns", overall_rct.count("🟡 Some Concerns"))
    c3.metric("🔴 High Risk", overall_rct.count("🔴 High"))

    risk_labels = {0: "Low", 1: "Some\nConcerns", 2: "High"}
    z_text = [[risk_labels[v] for v in row] for row in scores_rct]

    fig = go.Figure(go.Heatmap(
        z=scores_rct,
        x=rob2_domains,
        y=[f"{s}  {o}" for s, o in zip(studies_rct, overall_rct)],
        colorscale=[[0, "#16a34a"], [0.5, "#C9A227"], [1, "#dc2626"]],
        zmin=0, zmax=2,
        text=z_text, texttemplate="%{text}",
        textfont=dict(size=10),
        showscale=False,
    ))
    fig.update_layout(
        title="RoB 2 Traffic Light Plot — 8 Clinical RCT Studies",
        height=380,
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter",
        title_font_family="Playfair Display",
        title_font_color="#0F2B46",
        margin=dict(l=200, r=20, t=60, b=80),
    )
    st.plotly_chart(fig, use_container_width=True)

    # Detailed table
    df_rct = pd.DataFrame({
        "Studi": studies_rct,
        **{d: [risk_labels[scores_rct[i][j]] for i in range(8)]
           for j, d in enumerate(rob2_domains)},
        "Overall": overall_rct,
    })
    st.dataframe(df_rct, use_container_width=True, hide_index=True)

    # Domain summary
    st.markdown("**Ringkasan per Domain**")
    for j, dom in enumerate(rob2_domains):
        col_scores = [scores_rct[i][j] for i in range(8)]
        low = col_scores.count(0)
        unc = col_scores.count(1)
        hi  = col_scores.count(2)
        bar_html = (
            f'<div style="display:flex;height:22px;border-radius:4px;overflow:hidden;margin-bottom:6px;">'
            f'<div style="width:{low/8*100:.0f}%;background:#16a34a;" title="Low {low}"></div>'
            f'<div style="width:{unc/8*100:.0f}%;background:#C9A227;" title="Unclear {unc}"></div>'
            f'<div style="width:{hi/8*100:.0f}%;background:#dc2626;" title="High {hi}"></div>'
            f'</div>'
            f'<small style="color:#64748b;">{dom} — Low: {low} · Some Concerns: {unc} · High: {hi}</small>'
        )
        st.markdown(bar_html, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# TAB 4 — ROBINS-I
# ══════════════════════════════════════════════════════════════════
elif tool_sel.startswith("📈"):
    st.markdown('<h2 class="page-title">📈 Clinical Non-RCT — ROBINS-I</h2>', unsafe_allow_html=True)
    st.caption("12 studi non-randomised · 7 domain · Sterne et al. 2016")

    robins_domains = [
        "D1: Confounding",
        "D2: Selection of Participants",
        "D3: Classification of Interventions",
        "D4: Deviations from Intervention",
        "D5: Missing Data",
        "D6: Measurement of Outcomes",
        "D7: Selection of Reported Results",
    ]

    random.seed(55)
    studies_nrsi = [f"NRSI-{i+1:02d}" for i in range(12)]
    # ROBINS-I: 0=Low, 1=Moderate, 2=Serious, 3=Critical
    scores_nrsi = [[random.choices([0,1,2,3], weights=[0.30,0.40,0.22,0.08])[0]
                    for _ in robins_domains] for _ in studies_nrsi]

    risk_labels_r = {0: "Low", 1: "Moderate", 2: "Serious", 3: "Critical"}

    def robins_overall(row):
        if 3 in row:      return "🚫 Critical"
        elif 2 in row:    return "🔴 Serious"
        elif 1 in row:    return "🟡 Moderate"
        return "🟢 Low"

    overall_nrsi = [robins_overall(r) for r in scores_nrsi]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🟢 Low", overall_nrsi.count("🟢 Low"))
    c2.metric("🟡 Moderate", overall_nrsi.count("🟡 Moderate"))
    c3.metric("🔴 Serious", overall_nrsi.count("🔴 Serious"))
    c4.metric("🚫 Critical", overall_nrsi.count("🚫 Critical"))

    z_text = [[risk_labels_r[v] for v in row] for row in scores_nrsi]

    fig = go.Figure(go.Heatmap(
        z=scores_nrsi,
        x=robins_domains,
        y=[f"{s}  {o}" for s, o in zip(studies_nrsi, overall_nrsi)],
        colorscale=[
            [0, "#16a34a"], [0.33, "#C9A227"],
            [0.66, "#dc2626"], [1, "#7f1d1d"],
        ],
        zmin=0, zmax=3,
        text=z_text, texttemplate="%{text}",
        textfont=dict(size=9),
        showscale=False,
    ))
    fig.update_layout(
        title="ROBINS-I — 12 Non-Randomised Clinical Studies",
        height=460,
        xaxis=dict(tickangle=-25, tickfont=dict(size=9)),
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter",
        title_font_family="Playfair Display",
        title_font_color="#0F2B46",
        margin=dict(l=160, r=20, t=60, b=100),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.error("⚠️ **Confounding (D1)** adalah domain paling bermasalah pada NRSI — mayoritas studi tidak mengontrol variabel perancu (staging kanker, status aktivasi T-cell baseline). Akan di-downgrade pada GRADE.")

# ══════════════════════════════════════════════════════════════════
# TAB 5 — GRADE EVIDENCE PROFILE
# ══════════════════════════════════════════════════════════════════
elif tool_sel.startswith("🏅"):
    st.markdown('<h2 class="page-title">🏅 GRADE Evidence Profile</h2>', unsafe_allow_html=True)
    st.caption("Grading of Recommendations, Assessment, Development and Evaluations")

    st.markdown("""
    GRADE menilai **kepastian bukti** per outcome, bukan per studi.  
    Dimulai dari **Tinggi** (RCT) atau **Rendah** (non-RCT / in vitro / in vivo),  
    lalu dinaikan/turunkan berdasarkan 8 faktor.
    """)

    # GRADE table
    grade_data = [
        {
            "Outcome": "Proliferasi Foxp3+ Tregs\n(supresi oleh CDK4/6i)",
            "N Studies": "31 in vivo + 17 in vitro",
            "Design": "In vivo + In vitro",
            "Start": "🔴 Rendah",
            "Risk of Bias": "↓ Serius (blinding unclear)",
            "Inconsistency": "✅ Tidak serius",
            "Indirectness": "↓ Serius (murine → human)",
            "Imprecision": "✅ Tidak serius",
            "Publication Bias": "↓ Kemungkinan ada",
            "Upgrade": "↑↑ Dosis-respons kuat",
            "Final": "⚪ Sangat Rendah → 🟡 Rendah",
            "Effect": "Supresi selektif pada <100nM",
        },
        {
            "Outcome": "Proliferasi CD8+ Effector T cells",
            "N Studies": "31 in vivo + 17 in vitro + 8 RCT",
            "Design": "Mixed",
            "Start": "🟡 Sedang (ada RCT)",
            "Risk of Bias": "↓ Tidak serius",
            "Inconsistency": "↓ Serius (I²=64%)",
            "Indirectness": "✅ Tidak serius",
            "Imprecision": "✅ Tidak serius",
            "Publication Bias": "✅ Tidak terdeteksi",
            "Upgrade": "—",
            "Final": "🟡 Rendah",
            "Effect": "Supresi parsial; reversibel",
        },
        {
            "Outcome": "Rasio CD8+:Treg intratumoural",
            "N Studies": "12 NRSI + 8 in vivo",
            "Design": "NRSI + In vivo",
            "Start": "🔴 Rendah",
            "Risk of Bias": "↓↓ Sangat serius (confounding)",
            "Inconsistency": "✅ Tidak serius",
            "Indirectness": "↓ Serius",
            "Imprecision": "✅ Tidak serius",
            "Publication Bias": "↓ Kemungkinan ada",
            "Upgrade": "↑ Efek besar",
            "Final": "⚪ Sangat Rendah",
            "Effect": "Peningkatan rasio — data terbatas",
        },
        {
            "Outcome": "Produksi IFN-γ (CD8+)",
            "N Studies": "17 in vitro + 8 in vivo",
            "Design": "In vitro + In vivo",
            "Start": "🔴 Rendah",
            "Risk of Bias": "↓ Tidak serius",
            "Inconsistency": "✅ Tidak serius",
            "Indirectness": "↓ Serius",
            "Imprecision": "↓ Serius (CI lebar)",
            "Publication Bias": "✅ Tidak terdeteksi",
            "Upgrade": "—",
            "Final": "⚪ Sangat Rendah",
            "Effect": "Tidak konsisten antar studi",
        },
        {
            "Outcome": "Kombinasi CDK4/6i + ICB: respons tumor",
            "N Studies": "8 RCT + 12 NRSI",
            "Design": "Clinical",
            "Start": "🟡 Sedang",
            "Risk of Bias": "↓ Serius (beberapa NRSI)",
            "Inconsistency": "✅ Tidak serius",
            "Indirectness": "✅ Tidak serius",
            "Imprecision": "✅ Tidak serius",
            "Publication Bias": "✅ Tidak terdeteksi",
            "Upgrade": "—",
            "Final": "🟠 Sedang",
            "Effect": "Mendukung kombinasi intermittent",
        },
    ]

    grade_labels = {
        "⚪ Sangat Rendah": "grade-vlow",
        "⚪ Sangat Rendah → 🟡 Rendah": "grade-low",
        "🔴 Rendah": "grade-vlow",
        "🟡 Rendah": "grade-low",
        "🟠 Sedang": "grade-mod",
        "🟢 Tinggi": "grade-high",
    }

    for gd in grade_data:
        cls = next((v for k, v in grade_labels.items() if k in gd["Final"]), "grade-low")
        st.markdown(f"""
        <div class="qa-card">
            <h4>🎯 {gd['Outcome']}</h4>
            <p>{gd['N Studies']} | {gd['Design']}</p>
            <div style="margin-top:0.75rem;display:flex;flex-wrap:wrap;gap:0.4rem;align-items:center;">
                <span class="tool-badge" style="background:#f1f5f9;color:#0F2B46;border:1px solid #cbd5e1;">
                    Start: {gd['Start']}
                </span>
                <span class="tool-badge" style="background:#f1f5f9;color:#64748b;border:1px solid #e2e8f0;">
                    RoB: {gd['Risk of Bias']}
                </span>
                <span class="tool-badge" style="background:#f1f5f9;color:#64748b;border:1px solid #e2e8f0;">
                    Inconsistency: {gd['Inconsistency']}
                </span>
                <span class="tool-badge" style="background:#f1f5f9;color:#64748b;border:1px solid #e2e8f0;">
                    Indirectness: {gd['Indirectness']}
                </span>
                <span class="tool-badge" style="background:#f1f5f9;color:#64748b;border:1px solid #e2e8f0;">
                    Imprecision: {gd['Imprecision']}
                </span>
                <span class="tool-badge {cls}" style="font-size:0.9rem;padding:0.3rem 1rem;">
                    ➜ GRADE: {gd['Final']}
                </span>
            </div>
            <p style="margin-top:0.6rem;color:#0F2B46;font-style:italic;">
                💡 {gd['Effect']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    # GRADE legend
    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<span class="tool-badge grade-high">🟢 Tinggi</span> RCT tanpa masalah serius', unsafe_allow_html=True)
    c2.markdown('<span class="tool-badge grade-mod">🟠 Sedang</span> Satu downgrade serius', unsafe_allow_html=True)
    c3.markdown('<span class="tool-badge grade-low">🟡 Rendah</span> Dua downgrade serius', unsafe_allow_html=True)
    c4.markdown('<span class="tool-badge grade-vlow">⚪ Sangat Rendah</span> ≥3 downgrade / studi observasional', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# TAB 6 — SUMMARY HEATMAP
# ══════════════════════════════════════════════════════════════════
elif tool_sel.startswith("📊"):
    st.markdown('<h2 class="page-title">📊 Quality Summary — Semua Studi</h2>', unsafe_allow_html=True)
    st.caption("68 studi · 4 kelompok desain · Ringkasan visual terintegrasi")

    # Overall quality distribution
    random.seed(21)
    all_studies = (
        [(f"InVitro-{i+1:02d}", "In Vitro", random.choices(["Tinggi","Sedang","Rendah"],
            weights=[0.53,0.35,0.12])[0]) for i in range(17)] +
        [(f"InVivo-{i+1:02d}",  "In Vivo",  random.choices(["Tinggi","Sedang","Rendah"],
            weights=[0.45,0.40,0.15])[0]) for i in range(31)] +
        [(f"RCT-{i+1:02d}",     "RCT",      random.choices(["Tinggi","Sedang","Rendah"],
            weights=[0.62,0.30,0.08])[0]) for i in range(8)] +
        [(f"NRSI-{i+1:02d}",    "Non-RCT",  random.choices(["Tinggi","Sedang","Rendah"],
            weights=[0.25,0.50,0.25])[0]) for i in range(12)]
    )
    df_all = pd.DataFrame(all_studies, columns=["Study", "Design", "Quality"])

    # Donut per design group
    c1, c2, c3, c4 = st.columns(4)
    for col, design in zip([c1, c2, c3, c4], ["In Vitro", "In Vivo", "RCT", "Non-RCT"]):
        subset = df_all[df_all["Design"] == design]["Quality"].value_counts()
        fig_d = go.Figure(go.Pie(
            labels=subset.index.tolist(),
            values=subset.values.tolist(),
            hole=0.55,
            marker=dict(colors=["#16a34a","#C9A227","#dc2626"]),
            textinfo="label+percent",
            textfont=dict(size=10),
        ))
        fig_d.update_layout(
            title=design, height=220,
            showlegend=False,
            margin=dict(l=0, r=0, t=40, b=0),
            paper_bgcolor="white",
            font_family="Inter",
            title_font_family="Playfair Display",
            title_font_color="#0F2B46",
        )
        col.plotly_chart(fig_d, use_container_width=True)

    # Full heatmap all 68 studies
    st.markdown("**Quality Map — 68 Studi (warna = kualitas)**")
    quality_num = {"Tinggi": 2, "Sedang": 1, "Rendah": 0}
    df_all["Q_num"] = df_all["Quality"].map(quality_num)

    designs = df_all["Design"].unique().tolist()
    max_len = max(len(df_all[df_all["Design"] == d]) for d in designs)
    z_grid = []
    y_labels = []
    for d in designs:
        sub = df_all[df_all["Design"] == d]["Q_num"].tolist()
        padded = sub + [-1] * (max_len - len(sub))
        z_grid.append(padded)
        y_labels.append(d)

    fig_full = go.Figure(go.Heatmap(
        z=z_grid,
        y=y_labels,
        x=[f"#{i+1}" for i in range(max_len)],
        colorscale=[
            [0, "#e2e8f0"],
            [0.01, "#e2e8f0"],
            [0.01, "#dc2626"],
            [0.4, "#dc2626"],
            [0.4, "#C9A227"],
            [0.7, "#C9A227"],
            [0.7, "#16a34a"],
            [1.0, "#16a34a"],
        ],
        zmin=-1, zmax=2,
        showscale=False,
        xgap=2, ygap=4,
    ))
    fig_full.update_layout(
        title="Quality Heatmap — Semua 68 Studi (🟢 Tinggi · 🟡 Sedang · 🔴 Rendah · ⬜ Padding)",
        height=280,
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter",
        title_font_family="Playfair Display",
        title_font_color="#0F2B46",
        margin=dict(l=80, r=20, t=60, b=40),
    )
    st.plotly_chart(fig_full, use_container_width=True)

    # Summary table
    st.markdown("**Ringkasan Distribusi Kualitas per Desain**")
    summary_rows = []
    for d in designs:
        sub = df_all[df_all["Design"] == d]
        total = len(sub)
        h = (sub["Quality"] == "Tinggi").sum()
        m = (sub["Quality"] == "Sedang").sum()
        l = (sub["Quality"] == "Rendah").sum()
        summary_rows.append({
            "Desain": d, "Total": total,
            "🟢 Tinggi": f"{h} ({h/total*100:.0f}%)",
            "🟡 Sedang": f"{m} ({m/total*100:.0f}%)",
            "🔴 Rendah": f"{l} ({l/total*100:.0f}%)",
            "Kualitas Dominan": "Tinggi" if h >= m and h >= l else ("Sedang" if m >= l else "Rendah"),
        })
    st.dataframe(pd.DataFrame(summary_rows), use_container_width=True, hide_index=True)

    st.info("""
    **🔐 Sensitivity Analysis (direncanakan)**  
    Sintesis akan diulang setelah mengeksklusi studi kualitas rendah untuk menguji
    kestabilan kesimpulan. Jika hasil berubah signifikan (>10% perbedaan effect size),
    akan dilaporkan sebagai temuan utama dengan keterangan *fragility*.
    """)

# ── Footer ─────────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "TELADAN Quality Assessment Module © 2026 · "
    "CDK4/6 Inhibitors & T-Cell SLR · Dyah Wahyu Tanjung Sari, UNIMUS · "
    "Tools: JBI · SYRCLE · RoB 2 · ROBINS-I · GRADE"
)
