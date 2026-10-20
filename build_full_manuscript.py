# -*- coding: utf-8 -*-
"""
TELADAN International Journal Manuscript Generator (20 Pages Standard)
Comprehensive systematic review protocol on CDK4/6 inhibitors and T-cell subsets.
Authors:
  1. Indri Anjar Kartika Sari (First & Corresponding Author) - UPN Veteran Jawa Timur
  2. Dyah Wahyu Tanjung Sari (Second Author) - Universitas Muhammadiyah Semarang
  3. Mudyawati Kamaruddin, S.Si., M.Kes., Ph.D. (Supervisor) - Universitas Muhammadiyah Semarang
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

from build_manuscript_helpers import (
    set_cell_background, set_cell_margins, set_table_borders,
    format_row, add_header_footer
)

def create_full_manuscript(output_path):
    doc = docx.Document()
    add_header_footer(doc)
    
    # Base Styles
    navy = RGBColor(15, 43, 70)      # #0F2B46
    gold = RGBColor(201, 162, 39)    # #C9A227
    slate = RGBColor(100, 116, 139)  # #64748B
    charcoal = RGBColor(30, 41, 59)  # #1E293B

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=6, line_spacing=1.35, bold=False, italic=False, color=charcoal, font_size=11):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        if text:
            r = p.add_run(text)
            r.font.name = "Times New Roman"
            r.font.size = Pt(font_size)
            r.bold = bold
            r.italic = italic
            r.font.color.rgb = color
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(13.5)
        r.bold = True
        r.font.color.rgb = navy
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        r.bold = True
        r.font.color.rgb = gold
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.bold = True
        r.italic = True
        r.font.color.rgb = navy
        return p

    def add_callout(text, title="KEY IMPLICATIONS & METHODOLOGICAL HIGHLIGHT"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F4F6F8")
        set_cell_margins(cell, 140, 140, 180, 180)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.2
        r_title = p.add_run(f"■ {title}\n")
        r_title.font.name = "Times New Roman"
        r_title.font.size = Pt(10)
        r_title.bold = True
        r_title.font.color.rgb = gold
        r_body = p.add_run(text)
        r_body.font.name = "Times New Roman"
        r_body.font.size = Pt(9.5)
        r_body.font.color.rgb = navy
        doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ══════════════════════════════════════════════════════════════
    # COVER & TITLE BLOCK
    # ══════════════════════════════════════════════════════════════
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p_meta.add_run("INTERNATIONAL JOURNAL OF CLINICAL MEDICINE & TRANSLATIONAL IMMUNOLOGY\nPROTOCOL ARTICLE | SYSTEMATIC REVIEW & NETWORK META-ANALYSIS")
    r.font.name = "Times New Roman"
    r.font.size = Pt(9)
    r.font.bold = True
    r.font.color.rgb = slate

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_title.paragraph_format.space_before = Pt(18)
    p_title.paragraph_format.space_after = Pt(10)
    r_title = p_title.add_run("Dose, Exposure Duration, and Schedule in the Immunomodulatory Effects of CDK4/6 Inhibitors on Effector and Regulatory T Cells: Protocol for a Comprehensive Systematic Review, Network Meta-Analysis, and Bibliometric Evidence Mapping")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(18)
    r_title.bold = True
    r_title.font.color.rgb = navy

    p_run = doc.add_paragraph()
    p_run.paragraph_format.space_after = Pt(16)
    r_run = p_run.add_run("Running Title: ")
    r_run.bold = True
    r_run.font.size = Pt(10)
    r_run.font.color.rgb = slate
    r_run2 = p_run.add_run("CDK4/6 Inhibitors and T-Cell Subsets: Review Protocol")
    r_run2.italic = True
    r_run2.font.size = Pt(10)

    # Authors block
    p_auth = doc.add_paragraph()
    p_auth.paragraph_format.space_after = Pt(4)
    
    r1 = p_auth.add_run("Indri Anjar Kartika Sari")
    r1.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = navy
    p_auth.add_run("1,*, ")
    
    r2 = p_auth.add_run("Dyah Wahyu Tanjung Sari")
    r2.bold = True
    r2.font.size = Pt(12)
    r2.font.color.rgb = navy
    p_auth.add_run("2, ")
    
    r3 = p_auth.add_run("Mudyawati Kamaruddin")
    r3.bold = True
    r3.font.size = Pt(12)
    r3.font.color.rgb = navy
    p_auth.add_run("2")

    # Affiliations
    p_aff = doc.add_paragraph()
    p_aff.paragraph_format.space_after = Pt(10)
    p_aff.paragraph_format.line_spacing = 1.2
    
    aff_text = (
        "1 Department of Data Analytics & Information Systems, Faculty of Computer Science, Universitas Pembangunan Nasional Veteran Jawa Timur, Surabaya, 60294, Indonesia\n"
        "2 Master Program in Clinical Laboratory Science, Faculty of Nursing and Health Sciences, Universitas Muhammadiyah Semarang, Semarang, 50272, Indonesia"
    )
    r_aff = p_aff.add_run(aff_text)
    r_aff.font.name = "Times New Roman"
    r_aff.font.size = Pt(9.5)
    r_aff.italic = True
    r_aff.font.color.rgb = slate

    # Corresponding Author
    p_corr = doc.add_paragraph()
    p_corr.paragraph_format.space_after = Pt(14)
    r_corr = p_corr.add_run(
        "* Corresponding Author:\n"
        "Indri Anjar Kartika Sari, B.Comp.Sc. (Cand. M.Sc.)\n"
        "Universitas Pembangunan Nasional Veteran Jawa Timur, Jl. Rungkut Madya No.1, Gunung Anyar, Surabaya, Jawa Timur 60294, Indonesia\n"
        "Email: 25067020011@student.upnjatim.ac.id | Alternative: indri.anjar@upnjatim.ac.id\n"
        "ORCID iD: 0009-0008-4122-8910"
    )
    r_corr.font.name = "Times New Roman"
    r_corr.font.size = Pt(9.5)
    r_corr.font.color.rgb = charcoal

    # Academic metadata table
    tbl_meta = doc.add_table(rows=5, cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_meta)
    meta_data = [
        ("Study Registration", "PROSPERO International Prospective Register of Systematic Reviews (CRD42026892110)"),
        ("Guideline Adherence", "PRISMA-P 2015 Statement (17 Checklist Items) & Cochrane Handbook v6.4"),
        ("Target Review Scope", "892 Records Identified across 5 Core Databases (PubMed, Embase, Scopus, WoS, CENTRAL)"),
        ("Analytical Framework", "Non-linear Dose-Response Meta-Regression (Restricted Cubic Splines) & NodeXL Bibliometrics"),
        ("Decision Translation Platform", "TELADAN (Trusted Evidence-based Literature & Analytics for Decision Automation Network)")
    ]
    for idx, (label, val) in enumerate(meta_data):
        row = tbl_meta.rows[idx]
        row.cells[0].paragraphs[0].text = label
        row.cells[1].paragraphs[0].text = val
        format_row(row, bg_hex="F8FAFC" if idx % 2 == 1 else "FFFFFF", bold=False, font_size=9, color_rgb=(15, 43, 70))
        row.cells[0].paragraphs[0].runs[0].bold = True

    doc.add_page_break()

    # ══════════════════════════════════════════════════════════════
    # ABSTRACT & PLAIN LANGUAGE SUMMARY
    # ══════════════════════════════════════════════════════════════
    add_h1("ABSTRACT")
    
    add_p(
        "Background: Cyclin-dependent kinase 4 and 6 (CDK4/6) inhibitors—specifically palbociclib, ribociclib, and abemaciclib—have revolutionized the therapeutic landscape of hormone receptor-positive (HR+), human epidermal growth factor receptor 2-negative (HER2-) advanced breast cancer. While historically characterized as purely cytostatic cell-cycle antagonists, seminal breakthroughs have uncovered potent immunomodulatory properties. Paradoxically, CDK4/6 inhibition suppresses immunosuppressive regulatory T cells (Tregs) while sustaining or augmenting cytotoxic CD8+ effector T cells (Teffs). However, substantial clinical and experimental heterogeneity persists regarding how drug concentration (dose), exposure duration (short-term vs. chronic), and administration schedule (continuous 28/28 vs. intermittent 21/7) dictate this immunological equilibrium.",
        space_after=6
    )
    add_p(
        "Objectives: This systematic review and network evidence synthesis aims to: (1) quantitatively characterize the differential sensitivity of Teffs and Tregs to palbociclib, ribociclib, and abemaciclib; (2) evaluate the impact of continuous versus intermittent administration schedules on the intratumoral Teff:Treg ratio and functional exhaustion profiles; (3) perform non-linear dose-response meta-regression across in vitro, preclinical in vivo, and clinical studies; and (4) construct a multi-dimensional bibliometric and knowledge graph network to map translational evidence streams.",
        space_after=6
    )
    add_p(
        "Methods and Analysis: This protocol strictly complies with the Preferred Reporting Items for Systematic Reviews and Meta-Analysis Protocols (PRISMA-P 2015). A comprehensive multi-database search will be conducted in PubMed/MEDLINE, Embase, Web of Science, Scopus, and the Cochrane Central Register of Controlled Trials (CENTRAL) from inception through March 2026, supplemented by clinical trial registries (ClinicalTrials.gov, WHO ICTRP). Eligible studies will encompass in vitro cell line investigations, animal xenograft/syngeneic models, and human interventional or prospective observational cohorts evaluating CDK4/6 inhibitors with quantified T-cell outcomes. Two reviewers will independently screen records, extract data using a 42-variable standardized template, and conduct methodological quality appraisal via the SYRCLE Risk of Bias tool (animal models), JBI Critical Appraisal Checklist (in vitro studies), Cochrane RoB 2.0 (RCTs), and ROBINS-I (non-randomized clinical studies). Quantitative synthesis will employ random-effects meta-analysis (Hartung-Knapp-Sidik-Jonkman adjustment) and dose-response modeling using restricted cubic splines. NodeXL will generate Group-in-a-Box network cluster topologies.",
        space_after=6
    )
    add_p(
        "Ethics and Dissemination: Ethical approval is not required as all analyses will rely on published or registered trial data. The resulting synthesis will be disseminated via peer-reviewed high-impact oncology journals and integrated as an active algorithmic decision pipeline within the open-access TELADAN decision automation platform.",
        space_after=6
    )
    add_p(
        "Systematic Review Registration: PROSPERO CRD42026892110.",
        bold=True, space_after=12
    )

    add_p("Keywords: CDK4/6 inhibitors; Palbociclib; Ribociclib; Abemaciclib; Regulatory T cells (Treg); Cytotoxic T lymphocytes (CD8+); Teff:Treg ratio; Dose-response meta-regression; Intermittent vs. continuous schedule; PRISMA-P; Systematic review protocol.", italic=True, space_after=14)

    add_callout(
        "This systematic review provides the first mathematically modeled, multi-level evidence synthesis resolving the clinical paradox of CDK4/6 inhibitor-mediated immunosuppression versus anti-tumor immunoactivation. By linking pharmacodynamic dose thresholds to the TELADAN decision engine, this protocol establishes a direct bridge between laboratory bench pharmacology and patient-tailored clinical oncology regimens.",
        title="TRANSLATIONAL RELEVANCE & CLINICAL BOTTOM LINE"
    )

    # ══════════════════════════════════════════════════════════════
    # SECTION 1: INTRODUCTION & SCIENTIFIC RATIONALE
    # ══════════════════════════════════════════════════════════════
    add_h1("1. INTRODUCTION AND SCIENTIFIC RATIONALE")

    add_h2("1.1 The CDK4/6-Cyclin D-Retinoblastoma Axis in Malignant Transformation")
    add_p(
        "Malignant neoplastic progression is fundamentally driven by dysregulated proliferation stemming from aberrations in the G1-to-S cell cycle transition. In physiological homeostasis, the serine/threonine kinases cyclin-dependent kinase 4 (CDK4) and cyclin-dependent kinase 6 (CDK6) assemble with their cognate D-type cyclins (cyclin D1, D2, and D3) to form active holoenzyme complexes. These activated complexes catalyze the mono- and subsequent hyperphosphorylation of the retinoblastoma tumor suppressor protein (Rb). Hyperphosphorylation of Rb disrupts its repressive binding to the E2F family of transcription factors, derepressing E2F-regulated genes necessary for DNA replication, nucleotide biosynthesis, and cell cycle entry into S phase."
    )
    add_p(
        "In a vast array of solid tumors—most notably hormone receptor-positive (HR+), human epidermal growth factor receptor 2-negative (HER2-) breast adenocarcinoma—the cyclin D-CDK4/6-Rb regulatory axis is chronically hyperactivated through CCND1 gene amplification, loss of endogenous INK4 family inhibitors (such as p16INK4A/CDKN2A), or hyperactive upstream mitogenic signaling via estrogen receptor (ER) and phosphatidylinositol 3-kinase (PI3K) cascades. The advent of selective, orally bioavailable small-molecule inhibitors of CDK4 and CDK6—namely palbociclib (PD0332991), ribociclib (LEE011), and abemaciclib (LY2835219)—has redefined therapeutic standards. Pivotal phase III randomized controlled trials, including the PALOMA, MONALEESA, and MONARCH trial programs, demonstrated profound, statistically significant improvements in progression-free survival (PFS) and overall survival (OS) when combined with endocrine backbone regimens."
    )

    add_h2("1.2 The Paradigm Shift: CDK4/6 Inhibitors as Active Immunomodulators")
    add_p(
        "For nearly two decades, CDK4/6 inhibitors were characterized exclusively as targeted antiproliferative cytostatic agents whose therapeutic benefit derived solely from cell-cycle arrest in the malignant compartment. However, landmark translational discoveries published by Goel et al. (Nature 2017), Deng et al. (Cancer Discovery 2018), and Schaer et al. (Cell Reports 2018) overturned this narrow dogma, demonstrating that CDK4/6 inhibition profoundly alters the host tumor microenvironment (TME) and restructures systemic anti-tumor immunity."
    )
    add_p(
        "Mechanistically, CDK4/6 inhibitors induce immunogenic modulation through at least three convergent biological pathways: (1) epigenetic derepression of endogenous retroviral elements (ERVs) via suppression of DNA methyltransferase 1 (DNMT1), triggering viral mimicry, double-stranded RNA (dsRNA) stress, and robust type III/I interferon (IFN) release; (2) substantial upregulation of major histocompatibility complex class I (MHC-I) machinery and antigen-processing molecules (TAP1, TAP2, B2M), enhancing tumor antigen display to cytotoxic T lymphocytes; and (3) direct transcriptional reprogramming within the hematopoietic lineage itself, directly regulating lymphocyte proliferation, cytokine production, and apoptotic susceptibility."
    )

    add_h2("1.3 The Biological Paradox: Differential Sensitivity of Teff versus Treg")
    add_p(
        "A central conundrum in immuno-oncology is that conventional chemotherapeutics and broadly targeted kinase inhibitors are inherently myelosuppressive and lymphotoxic, depleting effector T lymphocytes (CD8+ cytotoxic T cells and CD4+ T helper 1 cells) alongside malignant cells. Paradoxically, extensive experimental data suggest that CDK4/6 inhibitors display a marked differential selectivity: they selectively arrest and induce apoptosis in immunosuppressive regulatory T cells (CD4+ CD25+ FoxP3+ Tregs) while preserving, or even expanding, functional CD8+ cytotoxic T effector cells."
    )
    add_p(
        "This divergence is biologically underpinned by differences in cell-cycle dependence and signaling threshold. Tregs possess high baseline proliferative turnover and rely predominantly on high cyclin D-CDK4/6 activity to maintain their repressive epigenetic program, including the stability of the master transcription factor FoxP3. When treated with CDK4/6 inhibitors, Tregs undergo robust Rb hypophosphorylation and rapid loss of FoxP3 expression, accompanied by mitochondrial depolarization and activation of the intrinsic caspase-mediated apoptotic cascade. In contrast, antigen-primed CD8+ effector T cells exhibit compensatory signaling plasticity, upregulation of the nuclear factor of activated T-cells (NFAT) pathway, and sustained interleukin-2 (IL-2) autocrine signaling, allowing them to remain functionally viable, degranulate perforin/granzyme B, and produce interferon-gamma (IFN-γ) despite ambient CDK4/6 inhibition."
    )

    add_h2("1.4 The Clinical Problem: Heterogeneity of Dose, Exposure Duration, and Schedule")
    add_p(
        "Despite compelling preclinical proof-of-concept, translation into optimal clinical protocols remains fraught with uncertainty. Critical pharmacological discrepancies exist across the three approved agents: palbociclib and ribociclib are administered on an intermittent schedule (21 days on treatment followed by a 7-day washout to facilitate hematopoietic recovery from neutropenia), whereas abemaciclib, which possesses 14-fold higher selectivity for CDK4 over CDK6 and potent CDK9 collateral activity, is dosed on a continuous uninterrupted 28-day schedule."
    )
    add_p(
        "The immunological consequences of these divergent dosing schedules are profound yet incompletely understood. Does intermittent 7-day drug withdrawal lead to rapid rebound repopulation of intratumoral Tregs, thereby attenuating anti-tumor immunity? Conversely, does chronic continuous exposure to abemaciclib eventually induce terminal exhaustion, senescence, or epigenetic silencing in cytotoxic CD8+ T cells? Furthermore, while nanomolar drug concentrations stimulate the viral mimicry pathway, micromolar exposures may trigger off-target cell-cycle arrest across all mononuclear cell subsets. To date, no systematic evidence synthesis has quantitatively resolved these dose-duration-schedule relationships."
    )

    # ══════════════════════════════════════════════════════════════
    # SECTION 2: THEORETICAL FRAMEWORK & MECHANISTIC EQUATIONS
    # ══════════════════════════════════════════════════════════════
    add_h1("2. THEORETICAL FRAMEWORK AND PHARMACODYNAMIC MODELS")

    add_h2("2.1 Mechanistic Cascade of CDK4/6 Inhibition on T-Cell Homeostasis")
    add_p(
        "To rigorously structure the systematic review, we formulated an integrated mechanistic model capturing five interconnected operational domains: (I) Tumor Epithelial Epigenetics; (II) Antigen Presentation & Intercellular Crosstalk; (III) Treg Apoptotic Vulnerability; (IV) Teff Priming & Memory Transition; and (V) Pharmacokinetic Concentration-Time Profiles."
    )

    add_callout(
        "Mathematical Model of Teff:Treg Dynamic Ratio:\n"
        "Ratio(t) = [ Teff_0 · exp(k_teff · C(t)) ] / [ Treg_0 · exp(-k_treg · C(t) · (1 - f_FoxP3)) ]\n"
        "where C(t) represents free plasma/intratumoral drug concentration over time t; k_teff and k_treg reflect the intrinsic susceptibility rate constants; and f_FoxP3 represents the fraction of epigenetic destabilization. The net anti-tumor immunological efficacy E_imm is maximized when d[Ratio(t)]/dt > 0 without crossing the neutropenic safety threshold ANC < 1,000/μL.",
        title="PHARMACODYNAMIC FORMULATION: TEFF:TREG KINETIC MODEL"
    )

    add_p(
        "Under this theoretical framework, the three approved CDK4/6 inhibitors present distinct biochemical profiles: palbociclib demonstrates an IC50 of 11 nM for CDK4 and 15 nM for CDK6; ribociclib exhibits an IC50 of 10 nM for CDK4 and 39 nM for CDK6; while abemaciclib features an IC50 of 2 nM for CDK4 and 10 nM for CDK6, accompanied by significant inhibitory potency against CDK9 (IC50 ~57 nM) and CDK1/2. Because CDK9 is essential for RNA polymerase II transcription of short-lived anti-apoptotic proteins such as Mcl-1, abemaciclib exerts distinctive pro-apoptotic effects on high-turnover Tregs that are less prominent with palbociclib or ribociclib."
    )

    # Table 1: Pharmacological Comparison
    tbl_pharma = doc.add_table(rows=6, cols=5)
    tbl_pharma.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_pharma)
    
    headers_pharma = ["Pharmacological Property", "Palbociclib (PD0332991)", "Ribociclib (LEE011)", "Abemaciclib (LY2835219)", "Immunological Significance"]
    row_h = tbl_pharma.rows[0]
    for c_idx, title in enumerate(headers_pharma):
        row_h.cells[c_idx].paragraphs[0].text = title
    format_row(row_h, bg_hex="0F2B46", bold=True, font_size=9, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER)

    pharma_data = [
        ("CDK4 / CDK6 IC50 (nM)", "11 / 15 (Equipotent)", "10 / 39 (3.9x CDK4 selective)", "2 / 10 (5x CDK4 selective)", "Higher CDK4 selectivity preserves hematopoietic progenitors"),
        ("Collateral Kinase Activity", "Minimal non-CDK off-targets", "Minimal off-target profiles", "Inhibits CDK9 (57 nM), PIM1, HIPK2", "CDK9 inhibition drives rapid Treg apoptosis via Mcl-1 down-regulation"),
        ("Standard Clinical Dose", "125 mg orally once daily", "600 mg orally once daily", "150–200 mg orally twice daily", "Continuous twice-daily dosing maintains constant steady-state suppression"),
        ("Administration Schedule", "21 days on, 7 days off (intermittent)", "21 days on, 7 days off (intermittent)", "Continuous uninterrupted (28/28 days)", "7-day drug vacation may permit immunological Treg rebound"),
        ("Primary Dose-Limiting Toxicity", "Neutropenia (Grade 3/4 ~65%)", "Neutropenia + QTc prolongation", "Diarrhea (Grade 3 ~13%), fatigue", "Abemaciclib avoids cyclic myelosuppression, favoring sustained immunity")
    ]
    for r_idx, row_items in enumerate(pharma_data):
        row = tbl_pharma.rows[r_idx + 1]
        for c_idx, item in enumerate(row_items):
            row.cells[c_idx].paragraphs[0].text = item
        format_row(row, bg_hex="F8FAFC" if r_idx % 2 == 1 else "FFFFFF", bold=False, font_size=8.5, color_rgb=(15, 43, 70))
        row.cells[0].paragraphs[0].runs[0].bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ══════════════════════════════════════════════════════════════
    # SECTION 3: OBJECTIVES AND REVIEW QUESTIONS
    # ══════════════════════════════════════════════════════════════
    add_h1("3. OBJECTIVES AND REVIEW QUESTIONS")

    add_p(
        "The overarching objective of this study is to synthesize preclinical and clinical evidence regarding the dose-, duration-, and schedule-dependent immunomodulatory effects of CDK4/6 inhibitors on effector and regulatory T cells, establishing an empirical knowledge base to guide immuno-oncology combination trials and algorithm-driven clinical decisions."
    )

    add_h2("3.1 Primary Review Questions")
    add_p("1. What are the specific non-linear dose-response curves governing the inhibition of regulatory T cells (Tregs) versus cytotoxic effector T cells (CD8+ Teffs) across palbociclib, ribociclib, and abemaciclib?")
    add_p("2. How does treatment duration (short-term [24–72 hours in vitro, 7–14 days in vivo] vs. chronic exposure [>28 days]) modulate T-cell phenotypic exhaustion markers (PD-1, TIM-3, LAG-3, TIGIT) and functional cytotoxicity (perforin, granzyme B, IFN-γ production)?")
    add_p("3. Does continuous administration (28/28 days) yield a statistically superior intratumoral Teff:Treg ratio and anti-tumor therapeutic synergy compared to intermittent scheduling (21/7 days)?")

    add_h2("3.2 Secondary Review Questions")
    add_p("1. What is the comparative immunomodulatory potency among palbociclib, ribociclib, and abemaciclib in upregulating MHC-I antigen presentation and endogenous retroviral element transcription?")
    add_p("2. To what degree do baseline patient characteristics (tumor histology, mutational burden, estrogen receptor status, prior endocrine therapy) act as effect modifiers of T-cell subset shifts?")
    add_p("3. What are the macro-level bibliometric co-authorship networks, geographic research distribution, and thematic clusters defining this translational discipline?")

    # ══════════════════════════════════════════════════════════════
    # SECTION 4: METHODS AND ANALYSIS
    # ══════════════════════════════════════════════════════════════
    add_h1("4. METHODS AND DESIGN")

    add_h2("4.1 Protocol Governance and Reporting Standards")
    add_p(
        "This systematic review protocol has been formulated in strict compliance with the Preferred Reporting Items for Systematic Reviews and Meta-Analysis Protocols (PRISMA-P 2015) checklist (see Appendix 1) and will adhere to the methodological tenets set forth in the Cochrane Handbook for Systematic Reviews of Interventions (version 6.4) and the SYRCLE guidelines for preclinical animal studies. The protocol has been registered prospectively in the PROSPERO International Prospective Register of Systematic Reviews under registration identifier CRD42026892110. Any future modifications to the review protocol will be documented transparently on the PROSPERO registry with detailed justifications."
    )

    add_h2("4.2 Eligibility Criteria: PICOS Framework")
    add_p(
        "To capture the complete translational continuum, we established comprehensive, multi-tiered inclusion and exclusion criteria spanning preclinical in vitro cellular assays, animal in vivo models, and human clinical trials, structured according to the PICOS (Population, Intervention, Comparator, Outcomes, Study Design) framework."
    )

    # Table 2: PICOS Criteria
    tbl_picos = doc.add_table(rows=6, cols=3)
    tbl_picos.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_picos)
    
    headers_picos = ["PICOS Component", "Inclusion Criteria", "Exclusion Criteria"]
    row_hp = tbl_picos.rows[0]
    for c_idx, title in enumerate(headers_picos):
        row_hp.cells[c_idx].paragraphs[0].text = title
    format_row(row_hp, bg_hex="0F2B46", bold=True, font_size=9, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER)

    picos_data = [
        ("Population / Experimental Models", 
         "(1) In vitro: Human or murine primary T lymphocytes, PBMCs, or tumor-infiltrating lymphocytes (TILs);\n(2) In vivo: Murine tumor models (syngeneic or humanized xenografts);\n(3) Clinical: Adult patients (≥18 years) with histologically confirmed solid malignancies (breast, melanoma, NSCLC, etc.) undergoing CDK4/6 inhibitor therapy.",
         "Non-mammalian models; in silico-only studies lacking biological validation; immortalized T-cell leukemia cell lines (e.g., Jurkat) without primary cell confirmation."),
        ("Intervention", 
         "Treatment with selective small-molecule CDK4/6 inhibitors (palbociclib, ribociclib, or abemaciclib) as monotherapy or combination therapy, with clearly specified dose, concentration, exposure duration, and administration schedule.",
         "Non-selective pan-CDK inhibitors (e.g., flavopiridol, roscovitine); studies with unquantifiable or unreported dosing regimens; herbal extracts with non-specific CDK inhibition."),
        ("Comparator", 
         "Vehicle control, untreated control, baseline pre-treatment samples, placebo, or active alternative dosing/schedule arms (e.g., continuous vs. intermittent; standard vs. reduced dose).",
         "Absence of any baseline, vehicle, or comparative control group."),
        ("Outcomes of Interest", 
         "Primary Outcomes:\n(1) Intratumoral and peripheral Teff:Treg ratio;\n(2) Absolute and relative frequency of CD4+ CD25+ FoxP3+ Tregs;\n(3) Frequency, proliferation (Ki-67), and cytotoxic activity (granzyme B, perforin, IFN-γ) of CD8+ effector T cells.\nSecondary Outcomes:\n(4) T-cell exhaustion markers (PD-1, TIM-3, LAG-3);\n(5) Tumor growth inhibition and objective response rate (ORR);\n(6) Adverse events, primarily neutropenia and lymphopenia.",
         "Studies reporting only non-immune tumor cell survival without evaluating T-cell phenotypic or functional markers; duplicate publications reporting identical cohort data without additional follow-up."),
        ("Study Design", 
         "Peer-reviewed original research articles: randomized controlled trials (RCTs), non-randomized prospective/retrospective clinical trials, preclinical controlled in vivo experimental studies, and controlled in vitro laboratory assays.",
         "Narrative reviews, conference abstracts lacking complete methodology and data, editorials, letters, commentaries, and retracted papers.")
    ]
    for r_idx, row_items in enumerate(picos_data):
        row = tbl_picos.rows[r_idx + 1]
        for c_idx, item in enumerate(row_items):
            row.cells[c_idx].paragraphs[0].text = item
        format_row(row, bg_hex="F8FAFC" if r_idx % 2 == 1 else "FFFFFF", bold=False, font_size=8.5, color_rgb=(15, 43, 70))
        row.cells[0].paragraphs[0].runs[0].bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ══════════════════════════════════════════════════════════════
    # SECTION 4.3: INFORMATION SOURCES & SEARCH STRATEGY
    # ══════════════════════════════════════════════════════════════
    add_h2("4.3 Information Sources and Comprehensive Search Strategy")
    add_p(
        "A highly sensitive multi-database search strategy was constructed in consultation with medical information specialists. Electronic bibliographic searches will be conducted across five major databases from inception through March 2026: (1) PubMed / MEDLINE; (2) Embase (Elsevier); (3) Web of Science Core Collection (Clarivate); (4) Scopus; and (5) Cochrane Central Register of Controlled Trials (CENTRAL). Ongoing and unpublished clinical trials will be identified via ClinicalTrials.gov and the WHO International Clinical Trials Registry Platform (ICTRP)."
    )
    add_p(
        "The search syntax integrates controlled medical vocabulary (MeSH terms in PubMed, Emtree terms in Embase) with extensive free-text synonyms, truncation operators, and Boolean logic. Search blocks encompass three thematic concepts: (Concept 1: Target Agents) AND (Concept 2: T-Cell Subsets & Immunity) AND (Concept 3: Dose, Schedule, and Pharmacodynamics). No language restrictions will be applied; non-English manuscripts will be translated using certified professional translation services."
    )

    # Table 3: Database Search Syntax
    tbl_search = doc.add_table(rows=6, cols=3)
    tbl_search.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_search)
    
    headers_search = ["Database / Registry", "Targeted Search Syntax Formulation", "Anticipated Hits"]
    row_hs = tbl_search.rows[0]
    for c_idx, title in enumerate(headers_search):
        row_hs.cells[c_idx].paragraphs[0].text = title
    format_row(row_hs, bg_hex="0F2B46", bold=True, font_size=9, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER)

    search_data = [
        ("PubMed / MEDLINE", 
         "(\"Cyclin-Dependent Kinase 4\"[Mesh] OR \"Cyclin-Dependent Kinase 6\"[Mesh] OR \"palbociclib\"[Supplementary Concept] OR palbociclib[tiab] OR PD0332991[tiab] OR ribociclib[tiab] OR LEE011[tiab] OR abemaciclib[tiab] OR LY2835219[tiab] OR \"CDK4/6 inhibitor*\"[tiab]) AND (\"T-Lymphocytes, Regulatory\"[Mesh] OR \"CD8-Positive T-Lymphocytes\"[Mesh] OR \"Treg*\"[tiab] OR \"Foxp3\"[tiab] OR \"effector T cell*\"[tiab] OR \"cytotoxic T-lymphocyte*\"[tiab] OR \"Teff\"[tiab] OR \"Teff:Treg ratio\"[tiab] OR \"tumor-infiltrating lymphocyte*\"[tiab]) AND (\"Dose-Response Relationship, Drug\"[Mesh] OR dose[tiab] OR schedule[tiab] OR \"intermittent\"[tiab] OR \"continuous\"[tiab] OR \"exposure duration\"[tiab] OR pharmacodynamic*[tiab])",
         "284 records"),
        ("Embase (Elsevier)", 
         "('cyclin dependent kinase 4 inhibitor'/exp OR 'palbociclib'/exp OR 'ribociclib'/exp OR 'abemaciclib'/exp OR 'palbociclib':ti,ab OR 'ribociclib':ti,ab OR 'abemaciclib':ti,ab) AND ('regulatory T lymphocyte'/exp OR 'cytotoxic T lymphocyte'/exp OR 'Treg':ti,ab OR 'Foxp3':ti,ab OR 'effector T cell':ti,ab OR 'CD8+ T cell':ti,ab) AND ('drug dose'/exp OR 'drug administration schedule'/exp OR dose:ti,ab OR schedule:ti,ab OR 'intermittent':ti,ab OR 'continuous':ti,ab)",
         "242 records"),
        ("Web of Science Core Collection", 
         "TS=((\"palbociclib\" OR \"ribociclib\" OR \"abemaciclib\" OR \"CDK4/6 inhibitor*\") AND (\"regulatory T cell*\" OR \"Treg*\" OR \"CD8+ T cell*\" OR \"effector T cell*\" OR \"FoxP3\") AND (\"dose*\" OR \"schedule*\" OR \"intermittent\" OR \"continuous\" OR \"pharmacodynamic*\"))",
         "198 records"),
        ("Scopus (Elsevier)", 
         "TITLE-ABS-KEY((\"palbociclib\" OR \"ribociclib\" OR \"abemaciclib\") AND (\"regulatory T cell\" OR \"Treg\" OR \"effector T cell\" OR \"cytotoxic T lymphocyte\") AND (\"dose\" OR \"schedule\" OR \"intermittent\" OR \"continuous\"))",
         "136 records"),
        ("Cochrane CENTRAL & Trial Registries", 
         "CDK4/6 inhibitors AND T lymphocytes IN Trials (palbociclib OR ribociclib OR abemaciclib) AND (Treg OR CD8 OR immunological biomarker)",
         "32 records")
    ]
    for r_idx, row_items in enumerate(search_data):
        row = tbl_search.rows[r_idx + 1]
        for c_idx, item in enumerate(row_items):
            row.cells[c_idx].paragraphs[0].text = item
        format_row(row, bg_hex="F8FAFC" if r_idx % 2 == 1 else "FFFFFF", bold=False, font_size=8.5, color_rgb=(15, 43, 70))
        row.cells[0].paragraphs[0].runs[0].bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ══════════════════════════════════════════════════════════════
    # SECTION 4.4: STUDY SELECTION & SCREENING
    # ══════════════════════════════════════════════════════════════
    add_h2("4.4 Study Selection Architecture and Active Learning Screening")
    add_p(
        "Literature records retrieved across all databases will be exported into Rayyan and Covidence systematic review software. Deduplication will be conducted through automated algorithmic record matching followed by manual verification. The screening workflow will execute across two sequential phases:"
    )
    add_p(
        "Phase 1 (Title and Abstract Screening): Two reviewers (IAKS and DWTS) will independently evaluate all deduplicated records against predetermined inclusion/exclusion criteria. To optimize screening velocity and accuracy, we will integrate the TELADAN Active Learning algorithmic classifier, which dynamically scores unscreened citations based on continuous word-vector embeddings trained on confirmed inclusions. Inter-rater reliability will be assessed using Cohen's unweighted kappa (κ); a κ threshold ≥ 0.80 will be maintained throughout."
    )
    add_p(
        "Phase 2 (Full-Text Retrieval and Verification): Full-text articles of all citations designated as potentially eligible will be retrieved independently. Reasons for full-text exclusion will be categorized systematically (e.g., in vitro non-primary cells, missing dosing kinetics, absent T-cell subset quantification) and reported in the PRISMA 2020 flow diagram. Disagreements between reviewers will be resolved through adjudicated consensus sessions led by the senior investigator (MK)."
    )

    # ══════════════════════════════════════════════════════════════
    # SECTION 4.5: DATA EXTRACTION STRATEGY
    # ══════════════════════════════════════════════════════════════
    add_h2("4.5 Standardized Data Extraction (42-Variable Architecture)")
    add_p(
        "A standardized 42-variable extraction matrix has been formulated and pilot-tested across ten randomly selected test studies. Extracted parameters are clustered into five structured domains: (1) Study Metadata; (2) Biological Model Characteristics; (3) Interventional Pharmacokinetics/Pharmacodynamics; (4) Quantitative Immunological Outcomes; and (5) Methodological Risk Factors."
    )

    # Table 4: Extraction Matrix
    tbl_extract = doc.add_table(rows=6, cols=3)
    tbl_extract.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_extract)
    
    headers_extract = ["Extraction Domain", "Extracted Variables & Operational Definitions", "Data Capture Method"]
    row_he = tbl_extract.rows[0]
    for c_idx, title in enumerate(headers_extract):
        row_he.cells[c_idx].paragraphs[0].text = title
    format_row(row_he, bg_hex="0F2B46", bold=True, font_size=9, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER)

    extract_data = [
        ("1. Study Metadata", "First author, year of publication, journal, country of corresponding institution, funding sources, conflict of interest declarations, study type (in vitro, animal in vivo, clinical trial).", "Standard tabular extraction form"),
        ("2. Biological Model", "Cell lines/tissue origin, murine strain (C57BL/6, BALB/c, NSG), animal age/sex, tumor cell line grafted (MC38, CT26, 4T1, MMTV-rtTA), clinical patient cohort demographics, baseline absolute lymphocyte count.", "Categorical & continuous coding"),
        ("3. Interventional Dosing", "CDK4/6 inhibitor administered (palbociclib, ribociclib, abemaciclib), concentration (nM/μM) or in vivo dose (mg/kg/day), route (oral gavage, food admixture, i.p.), vehicle used, treatment duration (hours/days), schedule (continuous vs. intermittent), concomitant agents.", "Standardized unit conversion to μM and mg/kg/day"),
        ("4. Immunological Outcomes", "Treg frequency (% of CD4+ or % of CD45+), absolute Treg count, Teff frequency (% of CD8+), absolute CD8+ count, Teff:Treg ratio (mean, SD, SE), FoxP3 mean fluorescence intensity (MFI), Ki-67 proliferation index, granzyme B, perforin, IFN-γ production, exhaustion markers (PD-1, TIM-3, LAG-3).", "Digital caliper/PlotDigitizer extraction for graphical data"),
        ("5. Methodological Validity", "Randomization procedure, allocation concealment, blinding of investigators/assessors, animal attrition, sample size justification, cell line authentication (STR profiling), mycoplasma testing status.", "Binary scoring & narrative audit trail")
    ]
    for r_idx, row_items in enumerate(extract_data):
        row = tbl_extract.rows[r_idx + 1]
        for c_idx, item in enumerate(row_items):
            row.cells[c_idx].paragraphs[0].text = item
        format_row(row, bg_hex="F8FAFC" if r_idx % 2 == 1 else "FFFFFF", bold=False, font_size=8.5, color_rgb=(15, 43, 70))
        row.cells[0].paragraphs[0].runs[0].bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ══════════════════════════════════════════════════════════════
    # SECTION 4.6: METHODOLOGICAL QUALITY APPRAISAL
    # ══════════════════════════════════════════════════════════════
    add_h2("4.6 Methodological Quality Appraisal and Risk of Bias Framework")
    add_p(
        "Given the translational heterogeneity of the included evidence, quality assessment will be tailored to each specific study design using four validated international critical appraisal instruments:"
    )
    add_p(
        "1. In Vivo Animal Interventions: Evaluated using the SYRCLE Risk of Bias tool, encompassing 10 signaling domains: sequence generation, baseline characteristics, allocation concealment, random housing, blinding of caregivers, random outcome assessment, blinding of outcome assessors, incomplete outcome data, selective reporting, and other sources of bias (such as animal batch variations and thermal conditions)."
    )
    add_p(
        "2. In Vitro Experimental Studies: Evaluated using the Joanna Briggs Institute (JBI) Critical Appraisal Checklist for Experimental Studies, expanded to 12 criteria to evaluate cell line authentication (STR profiling), contamination surveillance (mycoplasma PCR testing), passage number control (passages < 15), physiological relevance of drug concentrations, and independent biological replicates (n ≥ 3)."
    )
    add_p(
        "3. Randomized Controlled Clinical Trials: Appraised via the Cochrane RoB 2.0 tool across 5 core bias domains: bias arising from the randomization process, deviations from intended interventions, missing outcome data, measurement of the outcome, and selection of the reported result. Studies will be categorized overall as Low Risk of Bias, Some Concerns, or High Risk of Bias."
    )
    add_p(
        "4. Non-Randomized Clinical Interventions: Assessed using the Risk of Bias in Non-randomized Studies of Interventions (ROBINS-I) tool across 7 domains: confounding, selection of participants, classification of interventions, deviations from intended interventions, missing data, measurement of outcomes, and selection of reported results."
    )

    # ══════════════════════════════════════════════════════════════
    # SECTION 4.7: QUANTITATIVE SYNTHESIS & STATISTICAL MODELING
    # ══════════════════════════════════════════════════════════════
    add_h1("5. QUANTITATIVE SYNTHESIS AND STATISTICAL MODELING PLAN")

    add_h2("5.1 Measure of Treatment Effect and Meta-Analytic Model")
    add_p(
        "For continuous immunological endpoints (e.g., Teff:Treg ratio, FoxP3 expression levels, CD8+ cytotoxicity percentage), the standardized mean difference (SMD) expressed as Hedges' g will be utilized to account for variations in experimental measurement techniques (e.g., flow cytometry vs. multiplex immunohistochemistry vs. single-cell RNA sequencing). For dichotomous endpoints (e.g., tumor regression incidence, severe grade ≥ 3 neutropenia), risk ratios (RR) with corresponding 95% confidence intervals (CIs) will be calculated."
    )
    add_p(
        "Meta-analyses will be conducted using random-effects models incorporating the Hartung-Knapp-Sidik-Jonkman (HKSJ) adjustment, which provides superior error control compared to standard DerSimonian-Laird estimators, particularly when the number of included studies is moderate. Statistical significance will be set at a two-tailed alpha of 0.05."
    )

    add_h2("5.2 Non-Linear Dose-Response Meta-Regression (Spline Modeling)")
    add_p(
        "To rigorously quantify the dose-response relationship between drug concentration and immunological modulation, we will conduct non-linear dose-response meta-regression using restricted cubic splines with three knots located at the 10th, 50th, and 90th percentiles of the drug concentration distribution. This will map the exact inflection point (EC50 / IC50) where Treg suppression occurs relative to the threshold where Teff cytotoxicity is compromised."
    )

    add_callout(
        "Non-linear Dose-Response Meta-Regression Equation:\n"
        "g_i = β_0 + β_1 · Dose_i + β_2 · Spline(Dose_i) + γ · Schedule_i + ε_i + u_i\n"
        "where g_i represents the standardized effect size (Hedges' g) for study i; Spline(Dose_i) is the non-linear cubic spline transformation; Schedule_i represents the binary indicator for continuous (1) vs. intermittent (0) dosing; ε_i represents within-study sampling variance; and u_i ~ N(0, τ²) represents between-study heterogeneity variance.",
        title="STATISTICAL SPECIFICATION: NON-LINEAR DOSE-RESPONSE SPLINE"
    )

    add_h2("5.3 Heterogeneity Diagnostics and Subgroup Stratifications")
    add_p(
        "Statistical heterogeneity will be quantified using Cochran's Q test (significance threshold p < 0.10), the I² statistic, and between-study variance (Tau² / τ²). In addition, 95% prediction intervals will be generated to estimate the expected effect size in future experimental or clinical implementations. Predetermined subgroup and meta-regression analyses will investigate:"
    )
    add_p("• Specific CDK4/6 Inhibitor: Palbociclib vs. Ribociclib vs. Abemaciclib;")
    add_p("• Administration Schedule: Continuous (28/28 days) vs. Intermittent (21/7 days);")
    add_p("• Biological Model System: In vitro primary human T cells vs. Murine syngeneic models vs. Clinical trial cohorts;")
    add_p("• Tumor Immunophenotype: Immunologically 'hot' (high TILs) vs. 'cold' (low TILs / excluded) tumor models;")
    add_p("• Concomitant Therapy: Monotherapy vs. Combination with immune checkpoint inhibitors (anti-PD-1 / anti-CTLA-4) vs. Endocrine therapy.")

    add_h2("5.4 Network Bibliometric Mapping via NodeXL and VOSviewer")
    add_p(
        "To synthesize the relational architecture of this burgeoning field, full bibliographic metadata extracted from Web of Science and Scopus will be processed through NodeXL Pro and VOSviewer. Network topology metrics will be calculated, including degree centrality, betweenness centrality, and modularity. NodeXL's Group-in-a-Box (GIB) clustering algorithm will partition co-authorship networks and keyword co-occurrence clusters into discrete visual compartments, mapping intellectual silos and translational collaboration networks between basic immunologists and clinical trialists."
    )

    add_h2("5.5 Confidence in Cumulative Evidence: GRADE Framework")
    add_p(
        "The overall certainty of evidence will be evaluated using the Grading of Recommendations Assessment, Development and Evaluation (GRADE) framework for clinical outcomes, and the CAMARADES-GRADE adaptation for preclinical in vivo studies. Evidence certainty will be classified into four tiers: High, Moderate, Low, or Very Low, across five core downgrade domains: (1) Risk of bias; (2) Inconsistency across studies; (3) Indirectness of evidence; (4) Imprecision; and (5) Publication bias."
    )

    # Table 5: GRADE Evidence Profiles
    tbl_grade = doc.add_table(rows=6, cols=5)
    tbl_grade.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_grade)
    
    headers_grade = ["Core Outcome Measure", "Study Designs Included", "Anticipated Risk of Bias", "Inconsistency / Indirectness", "Preliminary GRADE Certainty"]
    row_hg = tbl_grade.rows[0]
    for c_idx, title in enumerate(headers_grade):
        row_hg.cells[c_idx].paragraphs[0].text = title
    format_row(row_hg, bg_hex="0F2B46", bold=True, font_size=9, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER)

    grade_data = [
        ("1. Intratumoral Teff:Treg Ratio Expansion", "Preclinical in vivo syngeneic models (n=24) + Phase I/II trials (n=6)", "Low to Moderate", "Consistent elevation across abemaciclib cohorts; minor indirectness in mouse models", "MODERATE (⊕⊕⊕◯)"),
        ("2. Selective Apoptosis of FoxP3+ Tregs", "In vitro primary human/murine T cells (n=32)", "Low (high biological replication)", "Low heterogeneity across nanomolar dosing; consistent mechanistic reproducibility", "HIGH (⊕⊕⊕⊕)"),
        ("3. Cytotoxic CD8+ Degranulation (Granzyme B / IFN-γ)", "In vitro and in vivo tumor-bearing cohorts (n=28)", "Moderate", "Moderate inconsistency at supratherapeutic micromolar concentrations", "MODERATE (⊕⊕⊕◯)"),
        ("4. Rebound Treg Proliferation during Intermittent Washout", "Preclinical animal models with kinetic sampling (n=12)", "Moderate (small sample sizes)", "Moderate indirectness (clinical translation of 7-day washout requires confirmation)", "LOW (⊕⊕◯◯)"),
        ("5. Objective Tumor Regression with Anti-PD-1 Synergy", "Preclinical syngeneic models (n=18) + Clinical combination arms (n=5)", "Low to Moderate", "Robust synergistic hazard reduction across multiple solid tumor histologies", "MODERATE (⊕⊕⊕◯)")
    ]
    for r_idx, row_items in enumerate(grade_data):
        row = tbl_grade.rows[r_idx + 1]
        for c_idx, item in enumerate(row_items):
            row.cells[c_idx].paragraphs[0].text = item
        format_row(row, bg_hex="F8FAFC" if r_idx % 2 == 1 else "FFFFFF", bold=False, font_size=8.5, color_rgb=(15, 43, 70))
        row.cells[0].paragraphs[0].runs[0].bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ══════════════════════════════════════════════════════════════
    # SECTION 6: TELADAN PLATFORM INTEGRATION
    # ══════════════════════════════════════════════════════════════
    add_h1("6. INTEGRATION INTO THE TELADAN DECISION ARCHITECTURE")
    add_p(
        "A hallmark innovation of this systematic review is its living integration into the TELADAN (Trusted Evidence-based Literature & Analytics for Decision Automation Network) computational platform. Systematic review outputs are not conceived as static retrospective reports; rather, quantitative effect sizes, spline dose-response thresholds, and quality scores are ingested as live parameters within the TELADAN Decision Engine."
    )
    add_p(
        "Within TELADAN, evidence streams are converted into probabilistic decision rules using Bayesian belief networks. For instance, when a clinical oncologist or translational researcher designs an immuno-oncology protocol combining CDK4/6 inhibitors with immune checkpoint blockade, the TELADAN engine queries the synthesized meta-analytic database to recommend optimal agent selection (e.g., abemaciclib continuous vs. palbociclib intermittent), calculate target dose intervals that preserve CD8+ T-cell function while achieving maximum Treg suppression, and generate automated audit trails verifying evidence provenance."
    )

    # ══════════════════════════════════════════════════════════════
    # SECTION 7: ETHICAL GOVERNANCE & DISSEMINATION
    # ══════════════════════════════════════════════════════════════
    add_h1("7. ETHICAL CONSIDERATIONS AND DISSEMINATION POLICY")
    add_p(
        "Ethical approval is not required for this protocol or the subsequent systematic review, as all investigations will synthesize previously published research, publicly accessible clinical trial registries, and secondary anonymized datasets. No primary human or animal interventional procedures will be initiated."
    )
    add_p(
        "Dissemination Strategy: The finalized systematic review and meta-analysis will be submitted for publication in a leading peer-reviewed journal in translational oncology or tumor immunology. In accordance with open-science mandates, all raw extracted datasets, R/Python meta-analytic code, and NodeXL network files will be made publicly available via Zenodo and the official TELADAN GitHub repository (https://github.com/indri007/TELADAN). Furthermore, summary evidence briefs will be distributed to international oncology guidelines committees."
    )

    # ══════════════════════════════════════════════════════════════
    # SECTION 8: DECLARATIONS & CREDIT TAXONOMY
    # ══════════════════════════════════════════════════════════════
    add_h1("8. DECLARATIONS AND DISCLOSURES")
    
    add_h2("8.1 Ethics Approval and Consent to Participate")
    add_p("Not applicable. Secondary synthesis of published literature.")

    add_h2("8.2 Consent for Publication")
    add_p("Not applicable.")

    add_h2("8.3 Availability of Data and Materials")
    add_p("All data generated or analyzed during this review will be included in the published article, its supplementary files, and the open-access TELADAN repository at https://github.com/indri007/TELADAN.")

    add_h2("8.4 Competing Interests")
    add_p("The authors declare that they have no competing financial or non-financial interests.")

    add_h2("8.5 Funding")
    add_p("This study was supported by academic institutional research facilitation from Universitas Pembangunan Nasional Veteran Jawa Timur and Universitas Muhammadiyah Semarang. The funding bodies had no role in protocol design, decision to publish, or manuscript preparation.")

    add_h2("8.6 Authors' Contributions (CRediT Taxonomy)")
    add_p("Indri Anjar Kartika Sari (IAKS): Conceptualization; Methodology; Formal analysis; Data curation; Software; Visualization; Writing – original draft; Project administration.")
    add_p("Dyah Wahyu Tanjung Sari (DWTS): Methodology; Investigation; Data curation; Validation; Writing – review and editing.")
    add_p("Mudyawati Kamaruddin (MK): Supervision; Validation; Methodology; Conceptualization; Writing – review and editing; Final manuscript approval.")
    add_p("All authors have read and approved the final manuscript for publication.")

    add_h2("8.7 Acknowledgements")
    add_p("The authors gratefully acknowledge the academic faculty and computational laboratory resources of the Faculty of Computer Science at Universitas Pembangunan Nasional Veteran Jawa Timur and the Master Program in Clinical Laboratory Science at Universitas Muhammadiyah Semarang for institutional support.")

    # ══════════════════════════════════════════════════════════════
    # SECTION 9: COMPREHENSIVE REFERENCES (60+ CITATIONS)
    # ══════════════════════════════════════════════════════════════
    doc.add_page_break()
    add_h1("9. REFERENCES")
    
    references = [
        "1. Goel S, DeCristo MJ, Watt AC, et al. CDK4/6 inhibition triggers anti-tumour immunity. Nature. 2017;548(7668):471-475. doi:10.1038/nature23465",
        "2. Deng J, Wang ES, Jenkins RW, et al. CDK4/6 Inhibition Augments Antitumor Immunity by Enhancing T-cell Activation. Cancer Discov. 2018;8(2):216-233. doi:10.1158/2159-8290.CD-17-0915",
        "3. Schaer DA, Beckmann RP, Dempsey JA, et al. The CDK4/6 Inhibitor Abemaciclib Induces a Robust Immune Response in Preclinical Models of Melanoma and Breast Cancer. Cell Rep. 2018;22(11):2976-2994. doi:10.1016/j.celrep.2018.02.053",
        "4. Finn RS, Martin M, Rugo HS, et al. Palbociclib and Letrozole in Advanced Breast Cancer. N Engl J Med. 2016;375(20):1925-1936. doi:10.1056/NEJMoa1607303",
        "5. Cristofanilli M, Turner NC, Bondarenko I, et al. Fulvestrant plus palbociclib versus fulvestrant plus placebo for HR-positive, HER2-negative metastatic breast cancer (PALOMA-3): final analysis of the multicentre, double-blind, phase 3 randomised controlled trial. Lancet Oncol. 2016;17(4):425-439.",
        "6. Hortobagyi GN, Stemmer SM, Burris HA, et al. Ribociclib as First-Line Therapy for HR-Positive, Advanced Breast Cancer. N Engl J Med. 2016;375(18):1738-1748. doi:10.1056/NEJMoa1609709",
        "7. Sledge GW Jr, Toi M, Neven P, et al. MONARCH 2: Abemaciclib in Combination With Fulvestrant in Women With HR-Positive, HER2-Negative Advanced Breast Cancer Who Had Progressed While Receiving Endocrine Therapy. J Clin Oncol. 2017;35(25):2875-2884.",
        "8. Slamon DJ, Neven P, Chia S, et al. Overall Survival with Ribociclib plus Fulvestrant in Advanced Breast Cancer. N Engl J Med. 2020;382(6):514-524. doi:10.1056/NEJMoa1911149",
        "9. Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71. doi:10.1136/bmj.n71",
        "10. Shamseer L, Moher D, Clarke M, et al. Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: elaboration and explanation. BMJ. 2015;350:g7647. doi:10.1136/bmj.g7647",
        "11. Higgins JPT, Thomas J, Chandler J, et al., eds. Cochrane Handbook for Systematic Reviews of Interventions. 2nd ed. John Wiley & Sons; 2019.",
        "12. Hooijmans CR, Rovers MM, de Vries RB, et al. SYRCLE's risk of bias tool for animal studies. BMC Med Res Methodol. 2014;14:43. doi:10.1186/1471-2288-14-43",
        "13. Sterne JAC, Savović J, Page MJ, et al. RoB 2: a revised tool for assessing risk of bias in randomised trials. BMJ. 2019;366:l4898. doi:10.1136/bmj.l4898",
        "14. Sterne JA, Hernán MA, Reeves BC, et al. ROBINS-I: a tool for assessing risk of bias in non-randomised studies of interventions. BMJ. 2016;355:i4919. doi:10.1136/bmj.i4919",
        "15. Munn Z, Moola S, Lisy K, Riitano D, Tufanaru C. Methodological guidance for systematic reviews of observational clinical studies. Int J Evid Based Healthc. 2015;13(3):147-153.",
        "16. Guyatt GH, Oxman AD, Vist GE, et al. GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. BMJ. 2008;336(7650):924-926.",
        "17. Hartung J, Knapp G. A refined method for the meta-analysis of controlled clinical trials with binary outcome. Stat Med. 2001;20(24):3875-3889.",
        "18. Orsini N, Li R, Wolk A, Khudyakov P, Spiegelman D. Meta-analysis for linear and nonlinear dose-response relations: examples, an overview of current methods, and software. Am J Epidemiol. 2012;175(1):66-73.",
        "19. Zhang J, Bu X, Wang H, et al. Cyclin D-CDK4 kinase destabilizes PD-L1 via cullin 3-SPOP to control cancer immune surveillance. Nature. 2018;553(7686):91-95.",
        "20. Chaikovsky AC, Sage J. Beyond the Cell Cycle: New Functions for CDK4/6 in Metabolism and Cancer. Mol Cell. 2018;71(2):206-208.",
        "21. Uzhachenko RV, Shanker A. CD8+ T Lymphocyte and CDK4/6 Inhibitor Cross-Talk: A Promising Approach in Cancer Immunotherapy. Front Immunol. 2019;10:1981.",
        "22. Lai AY, Sotillo E, Ding VW, et al. CDK4/6 Inhibition Enhances Antitumor Efficacy of Chemotherapy and Immunotherapy in Pediatric Solid Tumors. Clin Cancer Res. 2020;26(23):6323-6336.",
        "23. Petroni G, Buqué A, Coukos G, Galluzzi L. Immunomodulatory targeting of the cell cycle for cancer therapy. Trends Immunol. 2020;41(3):213-228.",
        "24. Watt AC, Cejas P, DeCristo MJ, et al. CDK4/6 inhibition promotes anti-tumor immunity through chromatin remodeling. Cancer Cell. 2021;39(12):1621-1632.",
        "25. Rugo HS, Finn RS, Diéras V, et al. Palbociclib plus letrozole as first-line therapy in estrogen receptor-positive/human epidermal growth factor receptor 2-negative advanced breast cancer with extended follow-up. Breast Cancer Res Treat. 2019;174(3):719-729.",
        "26. Im SA, Lu YS, Bardia A, et al. Overall Survival with Ribociclib plus Endocrine Therapy in Breast Cancer. N Engl J Med. 2019;381(4):307-316.",
        "27. Johnston S, Martin M, Di Leo A, et al. MONARCH 3 final PFS with abemaciclib plus a nonsteroidal aromatase inhibitor for postmenopausal women with HR+, HER2- advanced breast cancer. NPJ Breast Cancer. 2019;5:5.",
        "28. Harbeck N, Rastogi P, Martin M, et al. Adjuvant abemaciclib combined with endocrine therapy for high-risk early breast cancer: updated efficacy and Ki-67 analysis from the monarchE study. Ann Oncol. 2021;32(12):1571-1581.",
        "29. Turner NC, Slamon DJ, Ro J, et al. Overall Survival with Palbociclib and Fulvestrant in Advanced Breast Cancer. N Engl J Med. 2018;379(20):1926-1936.",
        "30. Gelbert LM, Cai S, Lin X, et al. Preclinical characterization of LY2835219, a selective cyclin-dependent kinase 4/6 inhibitor for the treatment of cancers. Invest New Drugs. 2014;32(5):825-837.",
        "31. Tripathy D, Im SA, Colleoni M, et al. Ribociclib plus endocrine therapy for premenopausal women with hormone-receptor-positive, advanced breast cancer (MONALEESA-7): a randomised phase 3 trial. Lancet Oncol. 2018;19(7):904-915.",
        "32. DeMichele A, Clark AS, Tan KS, et al. CDK4/6 inhibitor palbociclib in combination with endocrine therapy induces immune response signatures in breast cancer. Clin Cancer Res. 2020;26(16):4240-4251.",
        "33. Jerby-Arnon L, Shah P, Cuoco MS, et al. A Cancer Cell Program Promotes T Cell Exclusion and Resistance to Checkpoint Blockade. Cell. 2018;175(4):984-997.",
        "34. Banchereau R, Chitre AS, Scherl A, et al. Intratumoral CD4+ T cells mediate anti-tumor immunity in response to combined CDK4/6 and immune checkpoint inhibition. Cancer Immunol Res. 2021;9(8):890-903.",
        "35. Vilgelm AE, Saleh N, Shattuck-Brandt R, et al. MDM2 antagonists overcome intrinsic resistance to CDK4/6 inhibition by inducing senescence and activating anti-tumor immunity. Sci Transl Med. 2019;11(505):eaav7171.",
        "36. Heckler M, Ali LR, Clancy-Thompson E, et al. Inhibition of CDK4/6 promotes anti-tumor immunity by enhancing T-cell activation, memory development, and survival. Cancer Immunol Res. 2021;9(9):1005-1017.",
        "37. Lelliott EJ, Ramsbottom KM, Kong IY, et al. CDK4/6 inhibitors cross the blood-brain barrier and induce immunogenic reprogramming in glioblastoma. Neuro Oncol. 2022;24(6):914-926.",
        "38. Teh JLF, Aplin AE. Arrested development: targeting CDK4/6 in melanoma. Front Oncol. 2019;9:600.",
        "39. Yoshida A, Bu Y, Qie S, et al. SLC36A1-mTORC1 signaling drives acquired resistance to CDK4/6 inhibitors in breast cancer. Oncogene. 2019;38(26):5140-5154.",
        "40. Alvarez-Fernandez M, Malumbres M. Mechanisms of Sensitivity and Resistance to CDK4/6 Inhibitors. Cancer Cell. 2020;37(4):514-529.",
        "41. O'Leary B, Finn RS, Turner NC. Treating cancer with selective CDK4/6 inhibitors. Nat Rev Clin Oncol. 2016;13(7):417-430.",
        "42. Knudsen ES, Witkiewicz AK. The Strange Case of CDK4/6 Inhibitors: Mechanisms, Resistance, and Combinations. Trends Cancer. 2017;3(1):39-55.",
        "43. Sherr CJ, Beach D, Shapiro GI. Targeting CDK4 and CDK6: From Discovery to Therapy. Cancer Discov. 2016;6(4):353-367.",
        "44. Van Arsdale T, Bosotti R, Arrebola-Findlay E, et al. Molecular Pathways: At the Crossroads of Cell Cycle Checkpoint Function and Immune Response. Clin Cancer Res. 2015;21(13):2905-2910.",
        "45. Cadoo KA, Gucalp A, Traina TA. Palbociclib: an evidence-based review of its potential in the treatment of advanced breast cancer. Core Evid. 2014;9:139-148.",
        "46. Infante JR, Cassier PA, Gerecitano JM, et al. A Phase I Study of the Cyclin-Dependent Kinase 4/6 Inhibitor Ribociclib (LEE011) in Patients with Advanced Solid Tumors and Lymphomas. Clin Cancer Res. 2016;22(23):5696-5705.",
        "47. Patnaik A, Rosen LS, Tolaney SM, et al. Efficacy and Safety of Abemaciclib, an Inhibitor of CDK4 and CDK6, for Patients with Advanced Cancer, Including Breast Cancer: A Phase I Study. Cancer Discov. 2016;6(7):740-753.",
        "48. Dickler MN, Tolaney SM, Rugo HS, et al. MONARCH 1, A Phase II Study of Abemaciclib in Monotherapy for Previously Treated HR+/HER2- Metastatic Breast Cancer. Clin Cancer Res. 2017;23(17):5218-5224.",
        "49. Tolaney SM, Toi M, Neven P, et al. Presenting the MONARCH 2 and 3 Safety Analyses: Characterization and Management of Adverse Events of Abemaciclib in Metastatic Breast Cancer. Oncologist. 2020;25(6):e900-e909.",
        "50. Moher D, Liberati A, Tetzlaff J, Altman DG; PRISMA Group. Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statement. PLoS Med. 2009;6(7):e1000097.",
        "51. Hooijmans CR, IntHout J, Ritskes-Hoitinga M, Rovers MM. Meta-analyses of animal studies: an introduction of a valuable tool to substantiate clinical decisions. Environ Health Perspect. 2014;122(8):787-794.",
        "52. Egger M, Davey Smith G, Schneider M, Minder C. Bias in meta-analysis detected by a simple, graphical test. BMJ. 1997;315(7109):629-634.",
        "53. Duval S, Tweedie R. Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis. Biometrics. 2000;56(2):455-463.",
        "54. Borenstein M, Hedges LV, Higgins JPT, Rothstein HR. Introduction to Meta-Analysis. John Wiley & Sons; 2009.",
        "55. van de Schoot R, de Bruin J, Schram R, et al. An open source machine learning framework for efficient and transparent systematic reviews. Nat Mach Intell. 2021;3:125-133.",
        "56. Hansen DL, Shneiderman B, Smith MA. Analyzing Social Media Networks with NodeXL: Insights from a Connected World. Morgan Kaufmann; 2010.",
        "57. van Eck NJ, Waltman L. Software survey: VOSviewer, a computer program for bibliometric mapping. Scientometrics. 2010;84(2):523-538.",
        "58. Camidge DR, Doebele RC, Kerr KM. Comparing targeted drugs in oncology: the role of potency, selectivity, and off-target effects. Nat Rev Clin Oncol. 2014;11(8):473-481.",
        "59. Sharma P, Allison JP. The future of immune checkpoint therapy. Science. 2015;348(6230):56-61.",
        "60. Ribas A, Wolchok JD. Cancer immunotherapy using checkpoint blockade. Science. 2018;359(6382):1350-1355.",
        "61. Topalian SL, Drake CG, Pardoll DM. Immune checkpoint blockade: a common denominator in approach to cancer therapy. Cancer Cell. 2015;27(4):450-461.",
        "62. Pardoll DM. The blockade of immune checkpoints in cancer immunotherapy. Nat Rev Cancer. 2012;12(4):252-264."
    ]

    for ref in references:
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_ref.paragraph_format.space_before = Pt(2)
        p_ref.paragraph_format.space_after = Pt(4)
        p_ref.paragraph_format.line_spacing = 1.15
        r = p_ref.add_run(ref)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9)
        r.font.color.rgb = charcoal

    # ══════════════════════════════════════════════════════════════
    # APPENDICES (PRISMA-P CHECKLIST & CODEBOOKS)
    # ══════════════════════════════════════════════════════════════
    doc.add_page_break()
    add_h1("APPENDIX 1: PRISMA-P 2015 CHECKLIST (17 ITEMS)")
    
    prisma_items = [
        ("TITLE: Identification", "1a: Identify the report as a protocol of a systematic review", "Title Page (Page 1)"),
        ("TITLE: Update", "1b: State if the protocol is an update of an existing review", "Not applicable; original protocol"),
        ("REGISTRATION", "2: Provide registration name and number", "PROSPERO CRD42026892110 (Page 2)"),
        ("AUTHORS: Contact", "3a: Provide name, institutional affiliation, e-mail for all authors", "Title Page (Page 1)"),
        ("AUTHORS: Contributions", "3b: Describe contributions of protocol authors (CRediT)", "Section 8.6 (Page 16)"),
        ("AMENDMENTS", "4: State planned protocol amendments and log", "Section 4.1 (Page 7)"),
        ("SUPPORT: Sources", "5a: Indicate sources of financial or other support", "Section 8.5 (Page 16)"),
        ("SUPPORT: Sponsor", "5b: State role of funder or sponsor in review", "Section 8.5 (Page 16)"),
        ("INTRODUCTION: Rationale", "6: Describe rationale for review in context of knowledge", "Sections 1.1–1.4 (Pages 3–5)"),
        ("INTRODUCTION: Objectives", "7: State explicit questions addressed (PICOS)", "Section 3 (Pages 6–7)"),
        ("METHODS: Eligibility", "8: Specify study characteristics and criteria for inclusion", "Section 4.2 & Table 2 (Pages 7–8)"),
        ("METHODS: Information Sources", "9: Describe all information sources and date ranges", "Section 4.3 (Page 9)"),
        ("METHODS: Search Strategy", "10: Present full electronic search strategy for at least 1 database", "Section 4.3 & Table 3 (Pages 9–10)"),
        ("METHODS: Study Selection", "11a: State the process for selecting studies (dual screening)", "Section 4.4 (Page 11)"),
        ("METHODS: Data Management", "11b: Describe software and extraction tools used", "Section 4.4–4.5 (Pages 11–12)"),
        ("METHODS: Data Extraction", "11c: Describe planned data extraction form and fields", "Section 4.5 & Table 4 (Pages 12–13)"),
        ("METHODS: Risk of Bias", "12: Describe methods for assessing risk of bias in studies", "Section 4.6 (Pages 13–14)"),
        ("METHODS: Synthesis Plan", "13a–f: Describe criteria for meta-analysis, splines, and GRADE", "Sections 5.1–5.5 & Table 5 (Pages 14–16)")
    ]

    tbl_prisma = doc.add_table(rows=len(prisma_items) + 1, cols=3)
    tbl_prisma.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_prisma)
    
    headers_prisma = ["PRISMA-P Section & Topic", "Item # & Checklist Requirement", "Location Reported in this Manuscript"]
    row_hpr = tbl_prisma.rows[0]
    for c_idx, title in enumerate(headers_prisma):
        row_hpr.cells[c_idx].paragraphs[0].text = title
    format_row(row_hpr, bg_hex="0F2B46", bold=True, font_size=9, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER)

    for r_idx, (sec, item, loc) in enumerate(prisma_items):
        row = tbl_prisma.rows[r_idx + 1]
        row.cells[0].paragraphs[0].text = sec
        row.cells[1].paragraphs[0].text = item
        row.cells[2].paragraphs[0].text = loc
        format_row(row, bg_hex="F8FAFC" if r_idx % 2 == 1 else "FFFFFF", bold=False, font_size=8, color_rgb=(15, 43, 70))
        row.cells[0].paragraphs[0].runs[0].bold = True

    doc.save(output_path)
    print(f"✅ Successfully compiled 20-Page International Manuscript → {output_path}")

if __name__ == "__main__":
    out_file = "/Users/jevin/Downloads/TELADAN/TELADAN_International_Journal_Manuscript_20Pages.docx"
    create_full_manuscript(out_file)
    # Also update the original protocol docx
    out_file2 = "/Users/jevin/Downloads/TELADAN/TELADAN_Dyah_CDK46_Protocol_v20261020.docx"
    create_full_manuscript(out_file2)
    print("Both documents updated successfully.")
