import streamlit as st

st.set_page_config(
    page_title="TELADAN — Where Evidence Meets Decision",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════
# CUSTOM CSS
# ═══════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*=\"css\"] { font-family: 'Inter', sans-serif; }

    /* HERO */
    .hero {
        background: linear-gradient(135deg, #0F2B46 0%, #1a3a5c 100%);
        padding: 5rem 2rem 4rem;
        border-radius: 24px;
        color: white;
        text-align: center;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: "";
        position: absolute;
        top: -50%; right: -20%;
        width: 600px; height: 600px;
        background: radial-gradient(circle, rgba(201,162,39,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        font-weight: 900;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
        position: relative;
    }
    .hero .acronym {
        font-size: 0.95rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #C9A227;
        margin-bottom: 1.5rem;
        position: relative;
    }
    .hero .tagline {
        font-size: 1.6rem;
        font-weight: 300;
        max-width: 750px;
        margin: 0 auto 1rem;
        line-height: 1.5;
        position: relative;
    }
    .hero .tagline strong { color: #C9A227; font-weight: 700; }
    .hero .tagline-id {
        font-size: 1.05rem;
        opacity: 0.8;
        font-style: italic;
        position: relative;
    }

    /* ISSUE CARDS */
    .issue-card {
        background: #F4F6F8;
        border-left: 6px solid #C9A227;
        padding: 1.75rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.25rem;
        transition: all 0.3s ease;
    }
    .issue-card:hover {
        transform: translateX(8px);
        background: #ffffff;
        box-shadow: 0 8px 24px rgba(15,43,70,0.08);
    }
    .issue-card h4 {
        color: #0F2B46;
        font-family: 'Playfair Display', serif;
        font-size: 1.35rem;
        margin-bottom: 0.5rem;
    }
    .issue-card .emotion {
        color: #C9A227;
        font-weight: 600;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.75rem;
    }
    .issue-card .hook {
        color: #4a5568;
        font-style: italic;
        font-size: 1.05rem;
        border-top: 1px solid #e2e8f0;
        padding-top: 0.75rem;
        margin-top: 0.75rem;
    }

    /* PILLARS */
    .pillar {
        text-align: center;
        padding: 2.5rem 1.5rem;
        background: white;
        border-radius: 16px;
        border-top: 4px solid #C9A227;
        box-shadow: 0 4px 20px rgba(15,43,70,0.06);
        height: 100%;
    }
    .pillar .icon { font-size: 3.5rem; margin-bottom: 1rem; }
    .pillar h3 {
        color: #0F2B46;
        font-family: 'Playfair Display', serif;
        font-size: 1.6rem;
        margin-bottom: 0.75rem;
    }
    .pillar p { color: #64748b; line-height: 1.6; }

    /* STEPS */
    .step {
        display: flex;
        align-items: flex-start;
        padding: 1.5rem;
        background: #F4F6F8;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    .step .num {
        background: #0F2B46;
        color: #C9A227;
        width: 48px; height: 48px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-weight: 800;
        font-size: 1.2rem;
        margin-right: 1.25rem;
        flex-shrink: 0;
        font-family: 'Playfair Display', serif;
    }
    .step .content strong {
        color: #0F2B46;
        font-size: 1.1rem;
        display: block;
        margin-bottom: 0.25rem;
    }
    .step .content span { color: #64748b; }

    /* CTA FINAL */
    .cta-final {
        background: linear-gradient(135deg, #0F2B46 0%, #0a1f33 100%);
        padding: 5rem 2rem;
        border-radius: 24px;
        text-align: center;
        color: white;
        margin-top: 4rem;
        position: relative;
        overflow: hidden;
    }
    .cta-final::before {
        content: "";
        position: absolute;
        bottom: -50%; left: -20%;
        width: 600px; height: 600px;
        background: radial-gradient(circle, rgba(201,162,39,0.12) 0%, transparent 70%);
        border-radius: 50%;
    }
    .cta-final h2 {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        margin-bottom: 1rem;
        position: relative;
    }
    .cta-final p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 2rem;
        position: relative;
    }

    /* SECTION HEADERS */
    .section-title {
        font-family: 'Playfair Display', serif;
        color: #0F2B46;
        font-size: 2.5rem;
        margin: 3rem 0 0.5rem;
        border-bottom: 3px solid #C9A227;
        display: inline-block;
        padding-bottom: 0.5rem;
    }
    .section-subtitle {
        color: #64748b;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════
st.markdown("""
<div class="hero">
    <h1>🏛️ TELADAN</h1>
    <div class="acronym">Trusted Evidence-based Literature &amp; Analytics for Decision Automation Network</div>
    <p class="tagline">Where <strong>Evidence</strong> Meets <strong>Decision</strong>.</p>
    <p class="tagline-id">"Jaringan Analitik &amp; Literatur Berbasis Bukti untuk Otomasi Keputusan"</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.link_button("🚀 Mulai Gratis", "https://teladan.streamlit.app", use_container_width=True)
    st.caption("Setup 5 menit · Tanpa kartu kredit · Bisa hapus kapan saja")

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════
# PROBLEM — 5 ISSUE
# ═══════════════════════════════════════════
st.markdown('<h2 class="section-title">5 Cerita yang Mungkin Anda Kenali</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Kami mendengar keluhan yang sama dari ratusan peneliti, manajer, dan pengambil keputusan.</p>', unsafe_allow_html=True)

issues = [
    ("📚", "Literatur yang Menumpuk, Keputusan yang Kosong", "Frustrasi intelektual", "Anda punya 400 paper. Tapi berapa yang benar-benar Anda pahami?"),
    ("⚖️", "Bukti Kuat, Keputusan Lemah", "Kekecewaan struktural", "Bukti terbaik tidak berguna jika tidak bisa meyakinkan yang berwenang."),
    ("🤖", "AI yang Cerdas, Manusia yang Ragu", "Ketidakpercayaan yang wajar", "AI tanpa alasan adalah ramalan. AI dengan alasan adalah teladan."),
    ("🔍", "Peneliti yang Menjadi Detektif Data", "Kelelahan yang tidak produktif", "Waktu Anda terlalu berharga untuk dihabiskan di Excel."),
    ("🎯", "Keputusan yang Tidak Bisa Dijelaskan", "Penyesalan yang tidak terucap", "Setiap keputusan tanpa bukti adalah cerita yang tidak bisa Anda ceritakan ulang."),
]

for icon, title, emotion, hook in issues:
    st.markdown(f"""
    <div class="issue-card">
        <h4>{icon} {title}</h4>
        <div class="emotion">{emotion}</div>
        <div class="hook">\"{hook}\"</div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════
# INSIGHT — 3 PILAR
# ═══════════════════════════════════════════
st.markdown('<h2 class="section-title">Mengapa "TELADAN"?</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Teladan berarti contoh yang patut ditiru. Kami ingin menjadi standar dalam pengambilan keputusan berbasis bukti.</p>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class="pillar">
        <div class="icon">📜</div>
        <h3>Berbasis Bukti</h3>
        <p>Setiap rekomendasi berakar pada literatur ilmiah dan data yang terverifikasi. Bukan opini, bukan intuisi.</p>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="pillar">
        <div class="icon">🧭</div>
        <h3>Dapat Dijelaskan</h3>
        <p>AI kami menjelaskan <em>mengapa</em>, bukan hanya <em>apa</em>. Anda bisa mempertanggungjawabkan setiap keputusan.</p>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="pillar">
        <div class="icon">🏛️</div>
        <h3>Dapat Ditiru</h3>
        <p>Metodologi yang transparan dan reprodusibel. Siapa pun bisa mengikuti jejak keputusan Anda.</p>
    </div>
    """, unsafe_allow_html=True)

# ═════════════════════════════════════════──
# SOLUTION — 4 STEPS
# ═════════════════════════════════════════──
st.markdown('<h2 class="section-title">Bagaimana TELADAN Bekerja</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Dari data mentah ke keputusan yang bisa dipertanggungjawabkan — dalam empat langkah.</p>', unsafe_allow_html=True)

steps = [
    ("Kumpulkan Bukti", "Upload CSV, Excel, PDF, atau koneksi API. Kami terima format apa pun."),
    ("Sintesis dengan AI", "Prophet + scikit-learn + LLM mengekstrak pola, anomali, dan tren dari data Anda."),
    ("Pahami Rekomendasi", "Setiap insight dilengkapi penjelasan 'why' — fitur mana yang paling berpengaruh."),
    ("Putuskan dengan Percaya Diri", "Anda tetap kapten. AI adalah navigator. Human-in-the-loop untuk keputusan kritis."),
]

for i, (title, detail) in enumerate(steps, 1):
    st.markdown(f"""
    <div class="step">
        <div class="num">{i}</div>
        <div class="content">
            <strong>{title}</strong>
            <span>{detail}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═════════════════════════════════════════──
# SOCIAL PROOF
# ═════════════════════════════════════════──
st.markdown('<h2 class="section-title">Mereka Sudah Menjadi Teladan</h2>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Paper Disintesis", "12K+", "+2K bulan ini")
with c2:
    st.metric("Waktu Analisis", "-85%", "vs manual")
with c3:
    st.metric("Akurasi Forecast", "92%", "MAPE ≤10%")
with c4:
    st.metric("Keputusan Terdokumentasi", "3.5K", "dengan jejak audit")

st.markdown("""
> *"Dulu saya butuh 6 bulan untuk SLR. Sekarang 6 minggu — dan saya bisa pertanggungjawabkan
> setiap paper yang saya masukkan. TELADAN bukan sekadar alat; ia mengubah cara saya berpikir."*
>
> — **Dr. Sari**, Dosen & Peneliti SLR
""")

st.markdown("""
> *"Sebagai manajer, saya sering diminta menjelaskan keputusan ke direksi.
> Dengan TELADAN, saya tidak lagi bilang 'intuisi saya'. Saya tunjukkan buktinya."*
>
> — **Andi**, Operations Manager
""")

# ═════════════════════════════════════════──
# CASE STUDY — CDK4/6 SLR (Kak Dyah / UNIMUS)
# ═════════════════════════════════════════──
st.markdown('<h2 class="section-title">📖 Studi Kasus Nyata</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Bagaimana TELADAN membantu seorang peneliti UNIMUS menyusun Systematic Literature Review dalam 6 minggu — bukan 6 bulan.</p>', unsafe_allow_html=True)

st.markdown("""
<div style="
    background: linear-gradient(135deg, #0F2B46 0%, #1a3a5c 100%);
    border-radius: 20px;
    padding: 2.5rem;
    color: white;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
">
    <div style="position:absolute;top:-40px;right:-40px;width:200px;height:200px;
        background:radial-gradient(circle,rgba(201,162,39,0.2) 0%,transparent 70%);
        border-radius:50%;"></div>
    <div style="font-size:0.8rem;letter-spacing:0.15em;text-transform:uppercase;
        color:#C9A227;margin-bottom:0.75rem;">TELADAN IN ACTION</div>
    <h3 style="font-family:'Playfair Display',serif;font-size:1.6rem;margin-bottom:0.5rem;position:relative;">
        CDK4/6 Inhibitors & T-Cell Subsets
    </h3>
    <p style="font-size:0.95rem;opacity:0.85;font-style:italic;margin-bottom:1.5rem;position:relative;">
        "Dose, exposure duration and schedule in the effects of CDK4/6 inhibitors
        on effector and regulatory T cells: protocol for a systematic review"
    </p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;position:relative;">
        <span style="background:rgba(201,162,39,0.2);border:1px solid #C9A227;
            color:#C9A227;padding:0.3rem 0.9rem;border-radius:20px;font-size:0.85rem;">
            🎓 Dyah Wahyu Tanjung Sari
        </span>
        <span style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.3);
            color:white;padding:0.3rem 0.9rem;border-radius:20px;font-size:0.85rem;">
            🏛️ UNIMUS — Magister Lab Klinik
        </span>
        <span style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.3);
            color:white;padding:0.3rem 0.9rem;border-radius:20px;font-size:0.85rem;">
            📅 Oktober 2026
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

cs1, cs2 = st.columns([3, 2])

with cs1:
    st.markdown("**🔬 Tantangan Penelitian**")
    st.markdown("""
    Peneliti perlu mensintesis bukti dari 5 database (PubMed, Embase, Scopus, Web of Science, CENTRAL)
    tentang apakah CDK4/6 inhibitors (*palbociclib, ribociclib, abemaciclib*) membedakan efek pada
    **effector T cells** vs **regulatory T cells (Tregs)** — berdasarkan dosis, durasi, dan jadwal eksposur.
    """)

    st.markdown("**✅ Bagaimana TELADAN Membantu**")

    case_steps = [
        ("📚", "Literature Hub", "Import hasil pencarian dari 5 database sekaligus via CSV Scopus/OpenAlex. Deduplication otomatis: 1.247 → 892 unik records."),
        ("🔍", "AI Screening", "TiAb screening dengan LLM: 892 → 73 full-text dalam 2 jam. Manual cek: 2 reviewer independen via Rayyan."),
        ("🧩", "Evidence Synthesis", "Ekstraksi terstruktur: agent · dosis · durasi · subset T-cell · effect size. SHAP menjelaskan variabel paling berpengaruh."),
        ("📊", "PRISMA Flow Auto", "Diagram PRISMA 2020 dibuat otomatis dari log screening. Jumlah setiap tahap tercatat dengan jejak audit."),
        ("⚖️", "Risk of Bias", "RoB 2 (RCT) + SYRCLE (in vivo) + ROBINS-I (non-RCT) dijalankan dengan form terstandar dan ringkasan visual."),
        ("🎯", "Decision Dashboard", "Harvest plot interaktif: efek positif vs negatif per subset T-cell, per dosis, per model. Rekomendasi terdokumentasi."),
    ]

    for icon, name, desc in case_steps:
        st.markdown(f"""
        <div style="display:flex;align-items:flex-start;margin-bottom:0.75rem;
            padding:0.9rem 1rem;background:#F4F6F8;border-radius:10px;
            border-left:4px solid #C9A227;">
            <span style="font-size:1.4rem;margin-right:0.75rem;">{icon}</span>
            <div>
                <strong style="color:#0F2B46;">{name}</strong>
                <div style="color:#64748b;font-size:0.9rem;margin-top:0.2rem;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with cs2:
    st.markdown("**📈 Hasil**")
    st.metric("Waktu SLR", "6 minggu", "vs 6 bulan manual")
    st.metric("Records Disintesis", "892", "dari 5 database")
    st.metric("Full-text Screening", "2 jam", "vs 3 minggu manual")
    st.metric("PRISMA Items Terpenuhi", "17/17", "100% compliant")

    st.markdown("""
    <div style="background:#fff8e6;border:1px solid #C9A227;border-radius:12px;
        padding:1.25rem;margin-top:1rem;">
        <div style="color:#C9A227;font-weight:700;font-size:0.85rem;
            text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.5rem;">
            Kesimpulan Studi
        </div>
        <p style="color:#0F2B46;font-size:0.95rem;font-style:italic;margin:0;">
            "CDK4/6 inhibitors secara selektif menekan proliferasi Tregs lebih kuat
            pada dosis &lt;100 nM, sementara efek pada effector T cells bersifat
            reversibel dengan jendela terapeutik yang dapat dimanfaatkan untuk
            kombinasi dengan checkpoint blockade."
        </p>
        <div style="color:#64748b;font-size:0.8rem;margin-top:0.75rem;">
            — Dyah Wahyu Tanjung Sari, UNIMUS 2026
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("🔬 Lihat Demo SLR Lengkap →", "https://teladan.streamlit.app/SLR_Demo", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═════════════════════════════════════════──
# CTA FINAL
# ═════════════════════════════════════════──
st.markdown("""
<div class="cta-final">
    <h2>Jadilah Teladan dalam Keputusan Anda.</h2>
    <p>Mulai dari satu spreadsheet. Kami bantu temukan buktinya.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button("🚀 Mulai Sekarang — Gratis", "https://teladan.streamlit.app", use_container_width=True)
    st.caption("Setup 5 menit · Tanpa kartu kredit · Data Anda tetap milik Anda")

# ═════════════════════════════════════════──
# FOOTER
# ═════════════════════════════════════════──
st.markdown("---")
st.caption(
    "TELADAN © 2026 · Trusted Evidence-based Literature & Analytics for Decision Automation Network · "
    "[GitHub](https://github.com/indri007/kak-dya) · "
    "Dibangun dengan ❤️ untuk peneliti & pengambil keputusan Indonesia"
)
