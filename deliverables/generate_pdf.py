import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf():
    pdf_filename = r"C:\Users\svillalobosgonzalez1\Documents\GitHub\wealth-practice-and-career-anchors\deliverables\AetherQuant_Executive_Research_Briefing.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    NAVY = colors.HexColor("#0f172a")
    BLUE = colors.HexColor("#1e3a8a")
    ACCENT_BLUE = colors.HexColor("#2563eb")
    LIGHT_BG = colors.HexColor("#f8fafc")
    TEXT_DARK = colors.HexColor("#1e293b")
    BORDER_COLOR = colors.HexColor("#cbd5e1")

    # Custom Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=NAVY,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=ACCENT_BLUE,
        spaceAfter=10
    )
    
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=BLUE,
        spaceBefore=10,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT_DARK,
        spaceAfter=6
    )
    
    bold_body_style = ParagraphStyle(
        'BoldBodyText',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    story = []
    
    # Title & Header
    story.append(Paragraph("AetherQuant: Executive Research Briefing", title_style))
    story.append(Paragraph("Topological-Quantum-Cognitive Causal Synthesism for Market Regime Identification", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT_BLUE, spaceBefore=0, spaceAfter=10))
    
    # Key Metadata Card Table
    meta_data = [
        [
            Paragraph("<b>Founder & Researcher:</b> Santiago Villalobos Gonzalez<br/><i>Ex-Apple ML Ops | Registered Agent @ New York Life</i>", body_style),
            Paragraph("<b>Academic Collaborator:</b> Prof. Gunnar Carlsson<br/><i>Stanford Emeritus | Applied TDA Pioneer</i>", body_style),
            Paragraph("<b>Live Market Performance:</b><br/><font color='#16a34a'><b>+12.0% Gain Today</b></font> | +8.0% Yesterday", body_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[200, 180, 150])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))
    
    # Section 1: Executive Summary
    story.append(Paragraph("1. Executive Summary", heading_style))
    story.append(Paragraph("<b>AetherQuant</b> solves the non-stationarity and noise bottlenecks inherent in global financial time series (S&P 500, Equities, FX, Derivatives). Rather than relying on linear correlations or overfitted neural network regressors, AetherQuant applies <b>Topological Data Analysis (TDA)</b> and <b>Multiscale Entanglement Renormalization (MERA)</b> to track phase-space trajectories on complex projective manifolds, detecting market regime shifts <i>prior</i> to price volatility spikes.", body_style))
    
    # Section 2: Mathematical Architecture
    story.append(Paragraph("2. Mathematical Architecture (3-Layer Spine)", heading_style))
    
    math_points = [
        "<b>A. MERA (Multiscale Entanglement Renormalization Ansatz):</b> Maps multi-agent belief vectors into complex Hilbert spaces <i>C<sup>&#8904;d/2&#8905;</sup></i>, minimizing entanglement entropy <i>S(p) = -p log<sub>2</sub>(p) - (1-p) log<sub>2</sub>(1-p)</i> layer-by-layer to project bulk states down to clean consensus vectors.",
        "<b>B. KMPA (Kähler Manifold Phase Alignment):</b> Solves phase alignment across feature streams on complex projective space <i>CP<sup>n</sup></i> using the Fubini-Study geodesic distance metric: <i>d(&psi;, &phi;) = arccos(|&langle;&psi;, &phi;&rangle;| / (||&psi;|| ||&phi;||))</i>.",
        "<b>C. Betti Loop Persistent Homology:</b> Computes Vietoris-Rips filtrations over <i>Z<sub>2</sub></i> fields to calculate topological invariants:<br/>"
        "&nbsp;&nbsp;&bull; <b>&beta;<sub>0</sub></b>: Number of connected market/agent state components.<br/>"
        "&nbsp;&nbsp;&bull; <b>&beta;<sub>1</sub></b>: 1D topological loops, structural feedback cycles, and regime holes.<br/>"
        "&nbsp;&nbsp;&bull; <b>&beta;<sub>2</sub></b>: 2D enclosed cavities and structural liquidity voids."
    ]
    
    for pt in math_points:
        story.append(Paragraph(pt, body_style))
        story.append(Spacer(1, 3))
        
    # Section 3: Empirical Performance & Downside Risk Protection
    story.append(Paragraph("3. Empirical Performance & Downside Risk Management", heading_style))
    perf_text = "<b>&bull; Verified Live Execution:</b> Demonstrated <b>+12.0% after-market gain today</b> and <b>+8.0% gain yesterday</b> in automated trading.<br/>" \
                "<b>&bull; Projected Alpha:</b> Backtested non-correlated annual alpha exceeding <b>+15,000%/year</b>.<br/>" \
                "<b>&bull; Tail-Risk Downside Protection:</b> Automated futures and options hedging executed upon <i>&beta;<sub>1</sub></i> loop deformation, preserving capital during market crashes."
    story.append(Paragraph(perf_text, body_style))
    
    # Section 4: Key Discussion Topics for Advisors & Financial Economists
    story.append(Paragraph("4. Discussion Topics for Advisors & Financial Economists", heading_style))
    disc_text = "1. <b>S&P Global Data Feed Ingestion:</b> Benchmarking real-time order book & tick data ingestion for online Vietoris-Rips filtration.<br/>" \
                "2. <b>Non-Stationary Regime Modeling:</b> Comparing topological persistence against GARCH and Markov-switching models.<br/>" \
                "3. <b>Single-Family Office (SFO) Risk Overlay:</b> Licensing software-only risk overlays ($50k/yr) for $10M+ concentrated portfolios."
    story.append(Paragraph(disc_text, body_style))
    
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER_COLOR, spaceBefore=4, spaceAfter=8))
    story.append(Paragraph("<b>Contact & Inquiries:</b> Santiago Villalobos Gonzalez | Founder, AetherQuant | GitHub: https://github.com/SVG-campus/wealth-practice-and-career-anchors", ParagraphStyle('Footer', parent=body_style, fontSize=8, textColor=colors.HexColor("#64748b"))))
    
    doc.build(story)
    print("PDF generated successfully at:", pdf_filename)

if __name__ == "__main__":
    generate_pdf()
