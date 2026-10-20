# TELADAN — Trusted Evidence-based Literature & Analytics for Decision Automation Network

> **"Jaringan Analitik & Literatur Berbasis Bukti untuk Otomasi Keputusan"**  
> *Where Evidence Meets Decision.*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://teladan.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)

---

## 🏛️ Apa itu TELADAN?

**TELADAN** adalah platform analitik berbasis bukti yang menghubungkan literatur ilmiah dengan pengambilan keputusan bisnis dalam satu jaringan transparan.

Nama **TELADAN** dipilih karena dalam Bahasa Indonesia berarti *contoh yang patut ditiru* — mencerminkan komitmen kami untuk menjadi standar pengambilan keputusan berbasis bukti di Indonesia.

---

## 🎨 Brand Identity

| Elemen | Nilai |
|--------|-------|
| **Nama** | TELADAN |
| **Akronim** | Trusted Evidence-based Literature & Analytics for Decision Automation Network |
| **Tagline EN** | *Where Evidence Meets Decision.* |
| **Tagline ID** | *"Jaringan Analitik & Literatur Berbasis Bukti untuk Otomasi Keputusan"* |
| **Warna Primer** | Deep Navy `#0F2B46` |
| **Warna Aksen** | Gold `#C9A227` |
| **Warna Netral** | Slate `#F4F6F8` |
| **Font Heading** | Playfair Display (Serif) |
| **Font Body** | Inter (Sans-serif) |

---

## 🚦 5 Problem yang Diselesaikan TELADAN

| # | Masalah | Hook |
|---|---------|------|
| 1 | **Literatur Menumpuk, Keputusan Kosong** | "Anda punya 400 paper. Tapi berapa yang benar-benar Anda pahami?" |
| 2 | **Bukti Kuat, Keputusan Lemah** | "Bukti terbaik tidak berguna jika tidak bisa meyakinkan yang berwenang." |
| 3 | **AI Cerdas, Manusia Ragu** | "AI tanpa alasan adalah ramalan. AI dengan alasan adalah teladan." |
| 4 | **Peneliti Jadi Detektif Data** | "Waktu Anda terlalu berharga untuk dihabiskan di Excel." |
| 5 | **Keputusan Tidak Bisa Dijelaskan** | "Setiap keputusan tanpa bukti adalah cerita yang tidak bisa Anda ceritakan ulang." |

---

## ⚙️ Getting Started

```bash
# Clone
git clone https://github.com/indri007/TELADAN.git
cd TELADAN

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

---

## 📁 Struktur Project

```
TELADAN/
├── app.py                     # Landing page & main Streamlit app
├── requirements.txt           # Python dependencies
├── .streamlit/
│   └── config.toml            # Theme config (Navy + Gold)
├── assets/                    # Logo, images, NodeXL exports
├── docs/
│   ├── PRD.md                 # Product Requirements Document
│   ├── erd.md                 # Entity Relationship Diagram
│   └── business-rules.md      # Business rules & AI guardrails
├── tech/
│   └── schema.sql             # PostgreSQL DDL with RLS
├── oalex/                     # OpenAlex async client
└── README.md
```

---

## 🧠 Tech Stack

| Layer | Teknologi |
|-------|-----------|
| **Frontend** | Streamlit + Custom CSS (Material Design 3) |
| **Forecasting** | Prophet + LSTM |
| **Anomaly Detection** | Isolation Forest + SHAP |
| **Clustering** | K-Means RFM |
| **Literature** | OpenAlex API (`oalex` client) |
| **Database** | PostgreSQL (Row-Level Security) |
| **Vector Store** | Qdrant |
| **Cache** | Redis |
| **Storage** | MinIO |

---

## 📊 NodeXL Visualizations

Enam visualisasi jaringan untuk analisis literatur TELADAN:

1. **Network Graph** — Peta aktor keseluruhan (betweenness centrality + community clusters)
2. **Group-in-a-Box** — Klaster dalam kotak terpisah
3. **Top Items & Word Cloud** — Kata teratas per klaster
4. **Time-Series Evolution** — Evolusi jaringan antar periode
5. **Sentiment Network** — Peta sentimen pada node/edge
6. **Motif Simplification** — Penyederhanaan pola berulang untuk audiens non-teknis

---

## 📞 Kontak

- **GitHub Issues**: [github.com/indri007/TELADAN/issues](https://github.com/indri007/TELADAN/issues)
- **Streamlit App**: [teladan.streamlit.app](https://teladan.streamlit.app)

---

*© 2026 TELADAN · Dibangun dengan ❤️ untuk peneliti & pengambil keputusan Indonesia*
