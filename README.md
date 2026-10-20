<p align="center">
  <img src="assets/teladan_logo_3d.svg" alt="TELADAN Material Design 3 3D Logo" width="650" />
</p>

<p align="center">
  <a href="https://teladan.streamlit.app"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit App" /></a>
  <img src="https://img.shields.io/badge/Material%20Design-3%20Expressive-1E3A5F.svg?style=flat-square&logo=google" alt="Material Design 3" />
  <img src="https://img.shields.io/badge/PRISMA--P-2015%20Verified-C9A227.svg?style=flat-square" alt="PRISMA-P" />
  <img src="https://img.shields.io/badge/GRADE-Evidence%20Certainty-0F2B46.svg?style=flat-square" alt="GRADE" />
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue.svg?style=flat-square&logo=python" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/License-MIT-gold.svg?style=flat-square" alt="MIT License" />
</p>

<h2 align="center">
  <strong>Trusted Evidence-based Literature &amp; Analytics for Decision Automation Network</strong>
</h2>

<p align="center">
  <em>"Jaringan Analitik &amp; Literatur Berbasis Bukti untuk Otomasi Keputusan"</em><br />
  <strong>Where Evidence Meets Decision.</strong>
</p>

---

## 🏛️ Tentang TELADAN

**TELADAN** adalah platform analitik dan sintesis literatur berbasis bukti (*evidence-based decision platform*) berstandar internasional yang dirancang untuk mengintegrasikan telaah sistematis ilmiah (**Systematic Literature Review - SLR**), pemodelan farmakodinamik/dosis-respons, dan visualisasi jaringan relasional ke dalam pipeline otomasi keputusan klinis dan manajerial.

Nama **TELADAN** merepresentasikan komitmen kami untuk menetapkan baku emas (*gold standard*) dalam tata kelola bukti ilmiah yang dapat diverifikasi, dapat direproduksi, dan siap diimplementasikan.

---

## 🔬 Publikasi & Protokol Tinjauan Sistematis Internasional (20 Lembar)

TELADAN mendayagunakan metodologi mutakhir yang telah dituangkan dalam protokol naskah jurnal internasional berstandar **PRISMA-P 2015 / PRISMA 2020** dan **Cochrane Handbook for Systematic Reviews**:

> **Judul Naskah:**  
> *"Dose, exposure duration and schedule in the effects of CDK4/6 inhibitors on effector and regulatory T cells: comprehensive protocol and evidence synthesis framework for a systematic review and network meta-analysis"*

### 👥 Tim Penulis (*Authorship & Affiliations*):
1. **Indri Anjar Kartika Sari¹ (IAKS)** — *Penulis Pertama & Corresponding Author*  
   *Afiliasi:* Universitas Pembangunan Nasional Veteran Jawa Timur (UPNVJT), Surabaya, Indonesia  
   *Email:* [25067020011@student.upnjatim.ac.id](mailto:25067020011@student.upnjatim.ac.id) · *NIM:* 25067020011  
   *Kontribusi CRediT:* Konseptualisasi, Investigasi, Kurasi Data, Analisis Formal, Visualisasi, Penulisan Draf Asli.
2. **Dyah Wahyu Tanjung Sari² (DWTS)** — *Penulis Kedua*  
   *Afiliasi:* Program Studi Magister Ilmu Laboratorium Klinik, Universitas Muhammadiyah Semarang (UNIMUS), Semarang, Indonesia  
   *NIM:* 16112630009  
   *Kontribusi CRediT:* Metodologi, Investigasi, Kurasi Data, Penulisan – Reviu dan Penyuntingan.
3. **Mudyawati Kamaruddin, S.Si., M.Kes., Ph.D.² (MK)** — *Dosen Pembimbing & Penelaah Senior*  
   *Afiliasi:* Universitas Muhammadiyah Semarang (UNIMUS), Semarang, Indonesia  
   *NIDN:* 0906037402 · *Email:* [mudyawati@unimus.ac.id](mailto:mudyawati@unimus.ac.id)  
   *Kontribusi CRediT:* Supervisi, Validasi, Metodologi, Penelaahan Kritis Naskah Akhir.

📄 **Dokumen Lengkap 20 Lembar:**  
Tersedia dalam repositori ini: [`TELADAN_International_Journal_Manuscript_20Pages.docx`](./TELADAN_International_Journal_Manuscript_20Pages.docx) dan [`TELADAN_Dyah_CDK46_Protocol_v20261020.docx`](./TELADAN_Dyah_CDK46_Protocol_v20261020.docx).

---

## 🚀 Fitur Utama & Modul Interaktif

Aplikasi TELADAN dibangun dengan arsitektur multipage Streamlit berdesain **Material Design 3**:

```
TELADAN/
├── app.py                            # 🏛️ Landing Page Utama & Showcase Studi Kasus
├── pages/
│   ├── 01_SLR_Demo.py                # 🔬 Demo Interaktif Systematic Review (6 Modul)
│   └── 02_Quality_Assessment.py      # ⚖️ Quality Assessment Suite (6 Critical Appraisal Tools)
├── assets/
│   ├── teladan_logo_3d.svg           # 🎨 3D Material Design 3 Animated Logo
│   └── logo.svg                      # 🛡️ Official Flat SVG Emblem
├── TELADAN_International_Journal_Manuscript_20Pages.docx # 📑 Naskah Jurnal 20 Halaman
└── requirements.txt                  # 📦 Dependensi Python
```

### 1. 🔬 SLR Interactive Suite (`pages/01_SLR_Demo.py`)
- **Modul 1: Literature Hub** — Akses 892 rekaman lintas basis data (PubMed, Scopus, Web of Science, Cochrane, Embase).
- **Modul 2: AI Screening Assist** — Active learning dual-reviewer dengan prioritisasi probabilitas relevansi.
- **Modul 3: Evidence Synthesis** — Pemodelan dosis-respons, kurva Hill non-linear, dan kontribusi faktor fitur via SHAP values.
- **Modul 4: PRISMA Flow Interactive** — Diagram Sankey alir seleksi interaktif & audit kepatuhan checklist PRISMA 2020.
- **Modul 5: Risk of Bias Engine** — Traffic light plot & summary diagram untuk Cochrane RoB 2 dan SYRCLE.
- **Modul 6: Decision Dashboard** — Harvest plot integratif untuk rekomendasi regulasi dosis dan jadwal kontinu vs. intermiten.

### 2. ⚖️ Quality Assessment Suite (`pages/02_Quality_Assessment.py`)
Mencakup instrumen penelaahan kualitas metodologis untuk setiap desain studi:
1. **In Vitro Studies** — JBI Critical Appraisal Tool (12 domain termasuk validasi lini sel & konsentrasi sitotoksik).
2. **In Vivo Preclinical Studies** — SYRCLE Risk of Bias Tool (10 domain bias seleksi, performa, deteksi, atrisi, dan pelaporan).
3. **Clinical RCTs** — Cochrane RoB 2.0 (5 domain bias proses randomisasi hingga seleksi hasil yang dilaporkan).
4. **Non-Randomized Clinical Studies** — ROBINS-I (7 domain kerancuan, seleksi partisipan, dan klasifikasi intervensi).
5. **GRADE Evidence Profiles** — Penilaian kepastian bukti untuk 5 luaran kunci imunologi & onkologi.
6. **Summary Heatmap Matrix** — Pemetaan komprehensif seluruh 68 studi inklusi dengan rencana uji sensitivitas.

---

## 🎨 Identitas Desain (Material Design 3)

| Token Desain | Nilai | Implementasi |
|--------------|-------|--------------|
| **Primary Color** | `#0F2B46` (Deep Navy) | Otoritas akademik, ketegasan bukti |
| **Accent / Secondary** | `#C9A227` (Imperial Gold) | Standar baku emas, transparansi |
| **Surface Base** | `#071927` / `#F4F6F8` | Material 3 surface elevation & depth |
| **Typography Display** | *Playfair Display* (Serif) | Judul institusional berwibawa |
| **Typography Body** | *Inter* (Sans-serif) | Keterbacaan data numerik & analitik |
| **Motion Physics** | `cubic-bezier(0.2, 0.8, 0.2, 1)` | Transisi fluida, elevasi 3D dan gyro orbital |

---

## ⚙️ Menjalankan Secara Lokal

```bash
# 1. Klon repositori
git clone https://github.com/indri007/TELADAN.git
cd TELADAN

# 2. Siapkan virtual environment
python3 -m venv venv
source venv/bin/activate  # Di Windows: venv\Scripts\activate

# 3. Pasang dependensi
pip install -r requirements.txt

# 4. Jalankan aplikasi Streamlit
streamlit run app.py
```

---

## 📑 Sitasi Naskah (*Citation*)

Jika Anda merujuk pada protokol atau kerangka kerja TELADAN dalam penelitian Anda, mohon sitasi sebagai berikut:

```bibtex
@article{sari2026dose,
  title={Dose, exposure duration and schedule in the effects of CDK4/6 inhibitors on effector and regulatory T cells: comprehensive protocol and evidence synthesis framework for a systematic review and network meta-analysis},
  author={Sari, Indri Anjar Kartika and Sari, Dyah Wahyu Tanjung and Kamaruddin, Mudyawati},
  journal={TELADAN Evidence-Based Decision Suite},
  volume={1},
  pages={1--20},
  year={2026},
  publisher={TELADAN Platform}
}
```

---

*© 2026 Tim Peneliti TELADAN · Indri Anjar Kartika Sari, Dyah Wahyu Tanjung Sari, & Mudyawati Kamaruddin.*
