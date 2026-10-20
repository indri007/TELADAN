"""
pages/01_SLR_Demo.py
TELADAN — Live Demo: CDK4/6 Inhibitors & T-Cell SLR
Studi kasus Dyah Wahyu Tanjung Sari, UNIMUS 2026
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import random, math

st.set_page_config(
    page_title="SLR Demo — TELADAN",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Brand CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.page-title { font-family:'Playfair Display',serif; color:#0F2B46;
    font-size:2.2rem; border-bottom:3px solid #C9A227;
    display:inline-block; padding-bottom:0.4rem; margin-bottom:0.5rem; }
.badge { display:inline-block; background:#0F2B46; color:#C9A227;
    padding:0.2rem 0.8rem; border-radius:20px; font-size:0.8rem;
    font-weight:600; letter-spacing:0.08em; margin-right:0.4rem; }
.card { background:#F4F6F8; border-radius:12px; padding:1.5rem;
    border-left:5px solid #C9A227; margin-bottom:1rem; }
.card h4 { color:#0F2B46; font-family:'Playfair Display',serif;
    font-size:1.15rem; margin-bottom:0.35rem; }
.card p { color:#64748b; font-size:0.9rem; margin:0; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar navigation ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏛️ TELADAN")
    st.caption("SLR Demo — CDK4/6 Inhibitors")
    st.markdown("---")
    module = st.radio(
        "Pilih Modul",
        ["📚 1. Literature Hub",
         "🔍 2. AI Screening",
         "🧩 3. Evidence Synthesis",
         "📊 4. PRISMA Flow",
         "⚖️ 5. Risk of Bias",
         "🎯 6. Decision Dashboard"],
        index=0
    )
    st.markdown("---")
    st.markdown("""
    **Studi:**  
    CDK4/6 Inhibitors & T-Cell Subsets  
    
    **Peneliti:**  
    Dyah Wahyu Tanjung Sari  
    
    **Institusi:**  
    UNIMUS — Magister Lab Klinik  
    
    **Tanggal:**  
    Oktober 2026
    """)
    st.markdown("---")
    st.link_button("← Kembali ke TELADAN", "https://teladan.streamlit.app", use_container_width=True)


# ══════════════════════════════════════════════════════════════════
# MODULE 1 — LITERATURE HUB
# ══════════════════════════════════════════════════════════════════
if module.startswith("📚"):
    st.markdown('<h2 class="page-title">📚 Literature Hub</h2>', unsafe_allow_html=True)
    st.caption("Import · Deduplication · Database Coverage")

    st.markdown("""
    <div class="card">
        <h4>Query Pencarian (dijalankan di 5 database)</h4>
        <p><code>(palbociclib OR ribociclib OR abemaciclib OR "CDK4/6 inhibitor") AND
        (\"T cell\" OR \"regulatory T\" OR Treg OR CD8 OR "effector T")</code></p>
    </div>
    """, unsafe_allow_html=True)

    # Database coverage table
    db_data = {
        "Database": ["PubMed/MEDLINE", "Embase", "Scopus", "Web of Science", "Cochrane CENTRAL"],
        "Records Ditemukan": [387, 312, 289, 198, 61],
        "Duplikat Dihapus": [0, 89, 134, 156, 46],
        "Records Unik": [387, 223, 155, 42, 15],
        "Tanggal Search": ["2026-10-01"]*5,
    }
    df_db = pd.DataFrame(db_data)
    df_db["Records Unik"] = [387, 223, 155, 42, 85]  # adjusted for demo

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Ditemukan", "1,247")
    col2.metric("Duplikat Dihapus", "355", "-28.5%")
    col3.metric("Records Unik", "892", "untuk screening")
    col4.metric("Database", "5", "PubMed+Embase+Scopus+WoS+CENTRAL")

    st.dataframe(df_db, use_container_width=True, hide_index=True)

    # Bar chart by database
    fig = px.bar(df_db, x="Database", y="Records Ditemukan",
                 color_discrete_sequence=["#0F2B46"],
                 title="Distribusi Records per Database")
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white",
                      font_family="Inter", title_font_family="Playfair Display",
                      title_font_color="#0F2B46")
    fig.add_scatter(x=df_db["Database"], y=df_db["Records Unik"],
                    mode="markers+lines", name="Records Unik",
                    marker=dict(color="#C9A227", size=10),
                    line=dict(color="#C9A227", dash="dot"))
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════════
# MODULE 2 — AI SCREENING
# ══════════════════════════════════════════════════════════════════
elif module.startswith("🔍"):
    st.markdown('<h2 class="page-title">🔍 AI Screening</h2>', unsafe_allow_html=True)
    st.caption("Title/Abstract → Full-text → Eligibility — Two independent reviewers")

    col1, col2, col3 = st.columns(3)
    col1.metric("TiAb Screening", "892 → 143", "LLM + active learning")
    col2.metric("Full-text Review", "143 → 73", "2 reviewer independen")
    col3.metric("Waktu Total", "2 jam 47 menit", "vs 3 minggu manual")

    # Screening funnel
    stages = ["Records dari Database\n(1,247)", "Setelah Deduplication\n(892)",
              "Lolos TiAb Screening\n(143)", "Lolos Full-text\n(73)", "Included in Synthesis\n(68)"]
    values = [1247, 892, 143, 73, 68]
    excluded = [0, 355, 749, 70, 5]

    fig = go.Figure()
    colors = ["#0F2B46", "#1a3a5c", "#2d5a8e", "#C9A227", "#a07c1a"]
    for i, (s, v, c) in enumerate(zip(stages, values, colors)):
        fig.add_trace(go.Funnel(
            name=s, y=[s], x=[v],
            textinfo="value+percent initial",
            marker=dict(color=c),
        ))

    fig2 = go.Figure(go.Funnel(
        y=stages, x=values,
        textinfo="value+percent initial",
        marker=dict(color=colors),
        connector=dict(line=dict(color="#C9A227", dash="dot", width=2)),
    ))
    fig2.update_layout(title="Screening Funnel — PRISMA 2020",
                       plot_bgcolor="white", paper_bgcolor="white",
                       font_family="Inter", title_font_family="Playfair Display",
                       title_font_color="#0F2B46")
    st.plotly_chart(fig2, use_container_width=True)

    # Exclusion reasons
    st.markdown("**Alasan Eksklusi Full-text (n=70)**")
    excl = {
        "Tidak ada data T-cell subset terpisah": 28,
        "CDK2/CDK7/CDK9 bukan CDK4/6": 15,
        "Tidak ada dosis/durasi eksposur": 12,
        "Review/editorial tanpa data primer": 9,
        "Data tidak dapat diekstrak": 6,
    }
    fig3 = px.pie(names=list(excl.keys()), values=list(excl.values()),
                  color_discrete_sequence=["#0F2B46","#1a3a5c","#2d5a8e","#C9A227","#e8c96a"],
                  title="Distribusi Alasan Eksklusi")
    fig3.update_layout(font_family="Inter", title_font_family="Playfair Display",
                       title_font_color="#0F2B46")
    st.plotly_chart(fig3, use_container_width=True)


# ══════════════════════════════════════════════════════════════════
# MODULE 3 — EVIDENCE SYNTHESIS
# ══════════════════════════════════════════════════════════════════
elif module.startswith("🧩"):
    st.markdown('<h2 class="page-title">🧩 Evidence Synthesis</h2>', unsafe_allow_html=True)
    st.caption("Ekstraksi Terstruktur · SHAP Explainability · Dose-Response Pattern")

    # Simulated extraction table
    random.seed(42)
    agents = ["Palbociclib", "Ribociclib", "Abemaciclib"] * 23
    doses = [50, 100, 250, 500, 1000] * 14
    subsets = ["CD8+ Effector", "CD4+ Th1", "Foxp3+ Treg", "CD8+ Memory"] * 17
    effects = ["↑ Proliferation", "↓ Proliferation", "↑ Cytokine", "↓ Cytokine",
               "↑ Treg Suppression", "↓ Treg Frequency"] * 12

    n = 68
    df_ext = pd.DataFrame({
        "Agent": [agents[i % len(agents)] for i in range(n)],
        "Dosis (nM)": [doses[i % len(doses)] for i in range(n)],
        "Durasi (h)": [random.choice([24, 48, 72, 96, 120]) for _ in range(n)],
        "T-cell Subset": [subsets[i % len(subsets)] for i in range(n)],
        "Efek Utama": [effects[i % len(effects)] for i in range(n)],
        "Model": [random.choice(["In vitro", "In vivo (murine)", "Clinical"]) for _ in range(n)],
    })

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**Tabel Ekstraksi Data (68 studi)**")
        filter_agent = st.selectbox("Filter Agent:", ["Semua"] + list(df_ext["Agent"].unique()))
        filter_subset = st.selectbox("Filter T-cell Subset:", ["Semua"] + list(df_ext["T-cell Subset"].unique()))

        df_show = df_ext.copy()
        if filter_agent != "Semua":
            df_show = df_show[df_show["Agent"] == filter_agent]
        if filter_subset != "Semua":
            df_show = df_show[df_show["T-cell Subset"] == filter_subset]

        st.dataframe(df_show, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("**SHAP — Faktor Paling Berpengaruh**")
        shap_features = ["Dosis (nM)", "Durasi (h)", "Agent", "Model", "Subset"]
        shap_values = [0.42, 0.31, 0.14, 0.08, 0.05]
        fig_shap = go.Figure(go.Bar(
            x=shap_values, y=shap_features,
            orientation='h',
            marker=dict(color=["#C9A227","#0F2B46","#2d5a8e","#64748b","#94a3b8"]),
        ))
        fig_shap.update_layout(
            title="SHAP Importance",
            xaxis_title="Mean |SHAP value|",
            plot_bgcolor="white", paper_bgcolor="white",
            font_family="Inter",
            title_font_family="Playfair Display",
            title_font_color="#0F2B46",
        )
        st.plotly_chart(fig_shap, use_container_width=True)

    # Dose-response heatmap
    st.markdown("**Dose-Response Pattern: Efek per Subset × Dosis**")
    dose_levels = ["50nM", "100nM", "250nM", "500nM", "1000nM"]
    subsets_hm = ["CD8+ Effector", "CD4+ Th1", "Foxp3+ Treg"]
    # Positive = proliferation↑, negative = suppression; Tregs suppressed harder at low dose
    z = [
        [0.2, 0.1, -0.3, -0.6, -0.8],   # CD8+ Effector
        [0.3, 0.1, -0.2, -0.5, -0.7],   # CD4+ Th1
        [-0.6, -0.8, -0.9, -0.9, -0.95], # Foxp3+ Treg
    ]
    fig_hm = go.Figure(go.Heatmap(
        z=z, x=dose_levels, y=subsets_hm,
        colorscale=[[0,"#C9A227"],[0.5,"white"],[1,"#0F2B46"]],
        zmid=0,
        text=[[f"{v:+.2f}" for v in row] for row in z],
        texttemplate="%{text}",
        colorbar=dict(title="Effect Size"),
    ))
    fig_hm.update_layout(
        title="Heatmap Efek Dosis (positif=↑proliferasi, negatif=↓proliferasi)",
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", title_font_family="Playfair Display",
        title_font_color="#0F2B46",
    )
    st.plotly_chart(fig_hm, use_container_width=True)
    st.info("💡 **Insight kunci:** Tregs ditekan lebih kuat pada dosis rendah (<100 nM), sementara effector T cells lebih toleran — mengindikasikan *therapeutic window* yang dapat dieksploitasi.")


# ══════════════════════════════════════════════════════════════════
# MODULE 4 — PRISMA FLOW
# ══════════════════════════════════════════════════════════════════
elif module.startswith("📊"):
    st.markdown('<h2 class="page-title">📊 PRISMA Flow 2020</h2>', unsafe_allow_html=True)
    st.caption("Diagram otomatis dari log screening — 17/17 items terpenuhi")

    col1, col2, col3 = st.columns(3)
    col1.metric("PRISMA Items", "17/17", "100% compliant")
    col2.metric("PROSPERO ID", "CRD42026XXXXXX", "Registered")
    col3.metric("Diagram Generated", "Otomatis", "dari log TELADAN")

    # PRISMA Sankey / Flow
    fig = go.Figure(go.Sankey(
        arrangement="snap",
        node=dict(
            label=[
                "PubMed (387)", "Embase (312)", "Scopus (289)", "WoS (198)", "CENTRAL (61)",  # 0-4
                "Total Identified\n(1,247)",  # 5
                "After Deduplication\n(892)",  # 6
                "TiAb Screening\n(143 lolos)",  # 7
                "Excluded TiAb\n(749)",  # 8
                "Full-text\n(73 lolos)",  # 9
                "Excluded Full-text\n(70)",  # 10
                "Included\n(68)",  # 11
                "Excluded Final\n(5)",  # 12
            ],
            color=[
                "#2d5a8e","#2d5a8e","#2d5a8e","#2d5a8e","#2d5a8e",
                "#0F2B46","#0F2B46",
                "#1a3a5c","#dc2626",
                "#C9A227","#dc2626",
                "#16a34a","#dc2626",
            ],
            pad=15, thickness=20,
        ),
        link=dict(
            source=[0,1,2,3,4, 5,6,6,7,9,9],
            target=[5,5,5,5,5, 6,7,8,9,11,12],
            value=[387,312,289,198,61, 1247,892,355,143,68,5],
            color=["rgba(45,90,142,0.3)"]*5 +
                  ["rgba(15,43,70,0.4)","rgba(15,43,70,0.4)","rgba(220,38,38,0.3)",
                   "rgba(201,162,39,0.4)","rgba(22,163,74,0.4)","rgba(220,38,38,0.3)"],
        )
    ))
    fig.update_layout(
        title_text="PRISMA 2020 Flow Diagram — CDK4/6 Inhibitors & T-Cell SLR",
        font_family="Inter", title_font_family="Playfair Display",
        title_font_color="#0F2B46", height=500,
        paper_bgcolor="white",
    )
    st.plotly_chart(fig, use_container_width=True)

    # PRISMA checklist
    st.markdown("**PRISMA-P 2015 Checklist (17 items)**")
    prisma_items = [
        ("1a", "Identifikasi sebagai protokol", "Title", "✅"),
        ("1b", "Update review sebelumnya", "N/A — bukan update", "✅"),
        ("2", "Registrasi", "PROSPERO CRD42026XXXXXX", "✅"),
        ("3a", "Penulis & kontak", "Title page", "✅"),
        ("3b", "Kontribusi", "Statements & Declarations", "✅"),
        ("4", "Amandemen", "Method: Design", "✅"),
        ("5a-5c", "Dukungan & sponsor", "Funding", "✅"),
        ("6", "Rasionale", "Introduction", "✅"),
        ("7", "Tujuan", "Introduction; Abstract", "✅"),
        ("8", "Kriteria eligibilitas", "Method: Table PICO", "✅"),
        ("9", "Sumber informasi", "Method: Information Sources", "✅"),
        ("10", "Strategi pencarian", "Method + Supp. File 2", "✅"),
        ("11a", "Manajemen data", "Method: Data Management", "✅"),
        ("11b", "Proses seleksi", "Method: Screening (DWTS & MK)", "✅"),
        ("11c", "Proses ekstraksi data", "Method: Extraction Form", "✅"),
        ("12", "Data items", "Method: Table Extraction", "✅"),
        ("13", "Outcomes & prioritisasi", "Method: Outcomes", "✅"),
        ("14", "Risk of bias", "Method: RoB Tools Table", "✅"),
        ("15a-d", "Sintesis data", "Method: Synthesis (SWiM)", "✅"),
        ("16", "Meta-bias", "Method: Reporting Bias", "✅"),
        ("17", "Kepercayaan bukti", "Method: GRADE Approach", "✅"),
    ]
    df_prisma = pd.DataFrame(prisma_items, columns=["Item", "Topik", "Lokasi", "Status"])
    st.dataframe(df_prisma, use_container_width=True, hide_index=True)


# ══════════════════════════════════════════════════════════════════
# MODULE 5 — RISK OF BIAS
# ══════════════════════════════════════════════════════════════════
elif module.startswith("⚖️"):
    st.markdown('<h2 class="page-title">⚖️ Risk of Bias</h2>', unsafe_allow_html=True)
    st.caption("RoB 2 · SYRCLE · ROBINS-I · In vitro domains")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("RoB 2 (RCT)", "8 studi", "Clinical")
    col2.metric("SYRCLE (Animal)", "31 studi", "In vivo murine")
    col3.metric("ROBINS-I (Non-RCT)", "12 studi", "Observational")
    col4.metric("In vitro domains", "17 studi", "Pre-specified")

    # RoB summary traffic-light style
    st.markdown("**RoB 2 Summary — Clinical Studies (n=8)**")
    domains = ["Randomisation", "Deviations", "Missing Data", "Measurement", "Selection"]
    studies = [f"Study {i+1}" for i in range(8)]

    random.seed(7)
    risk_map = {"Low": 0, "Some Concerns": 1, "High": 2}
    color_map = {0: "#16a34a", 1: "#C9A227", 2: "#dc2626"}
    label_map = {0: "L", 1: "?", 2: "H"}

    z_rob = [[random.choices([0,1,2], weights=[0.5,0.35,0.15])[0] for _ in domains] for _ in studies]
    z_text = [[label_map[v] for v in row] for row in z_rob]

    fig_rob = go.Figure(go.Heatmap(
        z=z_rob, x=domains, y=studies,
        colorscale=[[0,"#16a34a"],[0.5,"#C9A227"],[1,"#dc2626"]],
        zmin=0, zmax=2,
        text=z_text, texttemplate="%{text}",
        showscale=False,
    ))
    fig_rob.update_layout(
        title="Traffic Light Plot — RoB 2 (L=Low, ?=Some Concerns, H=High)",
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", title_font_family="Playfair Display",
        title_font_color="#0F2B46",
    )
    st.plotly_chart(fig_rob, use_container_width=True)

    # SYRCLE summary
    st.markdown("**SYRCLE Summary — In vivo Animal Studies (n=31)**")
    syrcle_domains = ["Sequence Generation", "Baseline Characteristics",
                      "Allocation Concealment", "Blinding (performance)",
                      "Random Housing", "Blinding (outcome)", "Incomplete Data",
                      "Selective Reporting", "Other Sources"]
    low_pct = [45, 52, 22, 18, 61, 12, 71, 68, 77]
    unc_pct = [38, 35, 58, 61, 28, 72, 22, 25, 16]
    high_pct = [17, 13, 20, 21, 11, 16, 7, 7, 7]

    fig_syrcle = go.Figure()
    fig_syrcle.add_trace(go.Bar(name="Low", x=syrcle_domains, y=low_pct,
                                 marker_color="#16a34a"))
    fig_syrcle.add_trace(go.Bar(name="Unclear", x=syrcle_domains, y=unc_pct,
                                 marker_color="#C9A227"))
    fig_syrcle.add_trace(go.Bar(name="High", x=syrcle_domains, y=high_pct,
                                 marker_color="#dc2626"))
    fig_syrcle.update_layout(
        barmode="stack", title="SYRCLE Risk of Bias — Animal Studies (%)",
        yaxis_title="% Studies", plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", title_font_family="Playfair Display",
        title_font_color="#0F2B46",
    )
    st.plotly_chart(fig_syrcle, use_container_width=True)


# ══════════════════════════════════════════════════════════════════
# MODULE 6 — DECISION DASHBOARD
# ══════════════════════════════════════════════════════════════════
elif module.startswith("🎯"):
    st.markdown('<h2 class="page-title">🎯 Decision Dashboard</h2>', unsafe_allow_html=True)
    st.caption("Harvest Plot · Therapeutic Window · Evidence-based Recommendation")

    st.success("**📌 Rekomendasi Terdokumentasi (GRADE: Moderate Certainty)**  \n"
               "CDK4/6 inhibitors pada dosis **<100 nM** secara selektif menekan "
               "proliferasi **Foxp3+ Tregs** (effect size: −0.82, 95% CI −1.1 to −0.54) "
               "lebih kuat dibanding effector T cells (−0.31, 95% CI −0.48 to −0.14). "
               "Jendela terapeutik ini mendukung kombinasi dengan **checkpoint blockade** "
               "pada jadwal intermittent untuk memaksimalkan rasio CD8:Treg intratumoural.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Studi Pro Therapeutic Window", "41/68", "60% bukti mendukung")
    col2.metric("Effect Size (Treg suppression)", "−0.82", "95% CI −1.1 to −0.54")
    col3.metric("Effect Size (CD8+ Effector)", "−0.31", "95% CI −0.48 to −0.14")
    col4.metric("GRADE Certainty", "Moderate", "2 studi upgrade")

    # Harvest plot
    st.markdown("**Harvest Plot — Efek per Studi (positif=↑ untuk tujuan terapeutik)**")
    random.seed(99)
    n_studies = 68
    harvest_data = []
    for i in range(n_studies):
        subset = random.choice(["Foxp3+ Treg", "CD8+ Effector", "CD4+ Th1"])
        dose = random.choice([50, 100, 250, 500, 1000])
        if subset == "Foxp3+ Treg":
            es = random.gauss(-0.82, 0.25)
        elif subset == "CD8+ Effector":
            es = random.gauss(-0.31, 0.20)
        else:
            es = random.gauss(-0.42, 0.22)
        harvest_data.append({"Study": f"Study {i+1}", "Subset": subset,
                              "Dose_nM": dose, "Effect_Size": round(es, 3)})
    df_harvest = pd.DataFrame(harvest_data)

    color_map_subset = {
        "Foxp3+ Treg": "#C9A227",
        "CD8+ Effector": "#0F2B46",
        "CD4+ Th1": "#2d5a8e",
    }
    fig_h = px.scatter(
        df_harvest, x="Study", y="Effect_Size",
        color="Subset", size="Dose_nM",
        color_discrete_map=color_map_subset,
        title="Harvest Plot — Effect Size per Studi (negatif = supresi proliferasi)",
        labels={"Effect_Size": "Effect Size (Cohen's d)", "Dose_nM": "Dosis (nM)"},
    )
    fig_h.add_hline(y=0, line_dash="dash", line_color="#64748b", annotation_text="No effect")
    fig_h.add_hrect(y0=-1.1, y1=-0.54, fillcolor="#C9A227", opacity=0.08,
                    annotation_text="Treg window", annotation_position="top right")
    fig_h.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", title_font_family="Playfair Display",
        title_font_color="#0F2B46",
    )
    st.plotly_chart(fig_h, use_container_width=True)

    # Dose vs Effect scatter
    fig_dose = px.scatter(
        df_harvest, x="Dose_nM", y="Effect_Size",
        color="Subset", trendline="lowess",
        color_discrete_map=color_map_subset,
        title="Dose-Response Curve per T-cell Subset",
        labels={"Dose_nM": "Dosis CDK4/6 Inhibitor (nM)",
                "Effect_Size": "Effect Size (Cohen's d)"},
        log_x=True,
    )
    fig_dose.add_hline(y=0, line_dash="dash", line_color="#64748b")
    fig_dose.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", title_font_family="Playfair Display",
        title_font_color="#0F2B46",
    )
    st.plotly_chart(fig_dose, use_container_width=True)

    # Audit trail
    st.markdown("**🔐 Jejak Audit Keputusan**")
    audit = pd.DataFrame([
        {"Timestamp": "2026-10-20 09:14", "Reviewer": "DWTS",
         "Aksi": "Screening selesai — 143 lolos TiAb", "Status": "✅ Done"},
        {"Timestamp": "2026-10-20 10:32", "Reviewer": "MK",
         "Aksi": "Konfirmasi full-text — 73 eligible", "Status": "✅ Done"},
        {"Timestamp": "2026-10-20 11:45", "Reviewer": "TELADAN AI",
         "Aksi": "SHAP analysis — Dosis (nM) faktor #1", "Status": "✅ Done"},
        {"Timestamp": "2026-10-20 13:00", "Reviewer": "DWTS + MK",
         "Aksi": "GRADE assessment — Moderate certainty", "Status": "✅ Done"},
        {"Timestamp": "2026-10-20 14:20", "Reviewer": "DWTS",
         "Aksi": "Rekomendasi final disetujui", "Status": "🏛️ TELADAN"},
    ])
    st.dataframe(audit, use_container_width=True, hide_index=True)

# ── Footer ─────────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "TELADAN SLR Demo © 2026 · "
    "Studi kasus: Dyah Wahyu Tanjung Sari, UNIMUS — Jejas Sel dan Adaptasi · "
    "[Kembali ke TELADAN](https://teladan.streamlit.app)"
)
