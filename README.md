# Post-Processing Optimization for FDM 3D-Printed Parts: Surface Metrology, Mechanical Integrity, and Cost Analysis

**Principal Investigator:** Hafiz Muhammad Saad  
**Affiliation:** Department of Mechanical Engineering, University of Engineering and Technology (UET), Lahore  
**Publication Date:** August 2026  

---

## Overview

Fused Deposition Modeling (FDM) additive manufacturing is heavily constrained by inherent stair-stepping effects, surface roughness ($R_a \approx 3.2\text{--}6.3\,\mu\text{m}$), and anisotropic layer weakness[cite: 3]. This repository contains raw experimental data, automated statistical verification scripts, standard operating procedures (SOPs), and CAD assets evaluating five post-processing workflows across Acrylonitrile Butadiene Styrene (ABS) and Polylactic Acid (PLA).

The study benchmarks mechanical tensile capacity (ASTM D638 Type V), profilometric surface texture (ISO 4287), dimensional deviation, and unit manufacturing costs to establish an evidence-based selection model for industrial and functional applications.

---

## Experimental Matrix & Workflows

Specimens were fabricated on an aligned Creality Ender-3 Pro platform using a 0.4 mm nozzle, 0.2 mm layer height, and 100% solid rectilinear infill ($N=5$ per condition, 60 coupons total).

| Designation | Processing Regimen | Reagent / Tooling | Target Exposure / Cycle |
| :--- | :--- | :--- | :--- |
| **Control** | As-Printed Baseline | None | None |
| **Treatment A** | Progressive Mechanical Abrasion | 400 $\rightarrow$ 600 $\rightarrow$ 1000 Grit SiC | 10 min total (5/3/2 min split) |
| **Treatment B** | Saturated Vapor Smoothing | Acetone ($\ge 99.5\%$ ABS) / Ethyl Acetate (PLA) | 8 min (ABS) / 10 min (PLA) |
| **Treatment C** | Surface Sealant Barrier | 2-Part Epoxy Resin (5:1 stoichiometric ratio) | 150 $\mu$m target film; 24h cure @ 25°C |
| **Treatment D** | Hybrid Subtractive / Solvation | Treatment A + Treatment B | 10 min sand + 8 min solvent fuming |
| **Treatment E** | Full Tri-Stage Consolidation | Treatment A + Treatment B + Treatment C | Full sequential mechanical, vapor & epoxy |

---

## Key Experimental Findings

### 1. Surface Roughness ($R_a$) & Tensile Performance (ABS)
All post-processing methods produced statistically significant roughness reductions ($F = 48.3$, $p < 0.001$, Cohen's $d = 2.14$ for Treatment E vs. Control).

| Condition | Surface Roughness ($R_a$, $\mu\text{m}$) | Roughness Reduction (%) | Tensile Strength ($\sigma_u$, $\text{MPa}$) | Tensile Delta vs. Control (%) | Total Cost (PKR / USD) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Control** | $4.80 \pm 0.30$ | Baseline | $35.2 \pm 2.1$ | Baseline | — |
| **A (Sanding)** | $1.90 \pm 0.20$[cite: 4] | 60.4%[cite: 4] | $34.8 \pm 2.3$[cite: 4] | -1.1%[cite: 4] | 50 / $0.17 |
| **B (Vapor)** | $0.95 \pm 0.15$[cite: 4] | 80.2%[cite: 4] | $33.5 \pm 1.9$[cite: 4] | -4.8%[cite: 4] | 65 / $0.22 |
| **C (Epoxy)** | $1.20 \pm 0.20$[cite: 4] | 75.0%[cite: 4] | $38.6 \pm 2.5$[cite: 4] | +9.6%[cite: 4] | 160 / $0.55 |
| **D (Sand + Vapor)** | $0.72 \pm 0.10$[cite: 4] | 85.0%[cite: 4] | $36.2 \pm 2.2$[cite: 4] | +2.8%[cite: 4] | 115 / $0.40 |
| **E (Full Treatment)** | $0.58 \pm 0.08$[cite: 4] | 87.9%[cite: 4] | $39.1 \pm 2.4$[cite: 4] | +11.1%[cite: 4] | 255 / $0.88 |

*Currency conversion rate benchmarked at 290 PKR / 1.00 USD. PLA achieved corresponding trends: Control ($4.5\,\mu\text{m}$), B-Ethyl Acetate ($0.85\,\mu\text{m}$), and Treatment E ($0.52\,\mu\text{m}$).*

### 2. Dimensional Metrology & Tolerancing
Nominal baseline coupon: $75.0\text{ mm} \times 25.0\text{ mm} \times 3.0\text{ mm}$ (functional envelope limit: $\pm 0.30\text{ mm}$).
* **Mechanical Sanding (A):** Best dimensional precision ($\pm 0.28\text{ mm}$) via controlled, uniform material removal.
* **Vapor Smoothing (B):** Retains critical envelope ($\pm 0.32\text{ mm}$) with minimal boundary distortion[cite: 4].
* **Epoxy Systems (C, E):** Produces unilateral thickness growth (+0.42 mm max deviation) due to the nominal $+150\,\mu\text{m}$ boundary layer; CAD models must incorporate boundary offsets on mating surfaces.

---

## Critical Engineering Insights

1. **Mitigation of Solvation Degradation:** Standalone vapor smoothing degrades ultimate tensile strength by 4.8% due to localized solvent plasticization and crack-tip surface dissolution. Executing progressive abrasive sanding prior to chemical fuming eliminates primary notch asperities, preserving mechanical capacity (+2.8% over baseline).
2. **Structural Reinforcement:** Two-part stoichiometric epoxy infiltration acts as an isotropic stress-distribution barrier, sealing outer inter-bead voids and driving an 11.1% increase in tensile strength ($39.1\text{ MPa}$).
3. **Chemical Incompatibility Alert:** Acetone induces catastrophic degradation and erratic swelling on PLA matrices. PLA vapor smoothing must exclusively employ Ethyl Acetate under strictly sealed negative-pressure extraction.

---

## Industrial Decision Framework

### Case Study Implementations
* **Automotive Support Structure (Millat Tractors Engine Bracket):** Treatment E. Met tight fluid run-off roughness targets ($R_a < 0.6\,\mu\text{m}$) and maximum structural resilience at PKR 180 scaled production cost.
* **Robotic Gripper Actuator (Automated Waste Sorter):** Treatment A (PLA). Minimal production lead time, low sliding friction, and zero chemical hazard at PKR 30/unit.
* **Commercial Hardware Shell (Consumer Display):** Treatment D. High-gloss visual finish ($R_a < 0.75\,\mu\text{m}$) without extended epoxy thermal/cure cycles.




## Analytical Pipeline & Usage

### Prerequisites
```bash
pip install numpy pandas scipy statsmodels matplotlib seaborn
```

### Automated Statistical Verification
Run the evaluation script to verify one-way ANOVA, calculate confidence intervals, and render response surfaces:
```bash
python scripts/anova_statistical_analysis.py --input data/raw/surface_roughness_raw.csv --alpha 0.05
```

---

## Citation & License

If utilizing this dataset, experimental protocols, or methodology in academic research:

```bibtex
@article{saad2026fdmpostprocessing,
  author    = {Saad, Hafiz Muhammad},
  title     = {Post-Processing Techniques for FDM 3D-Printed Parts: Comparative Analysis of Surface Quality, Mechanical Properties, and Cost-Effectiveness},
  institution = {Department of Mechanical Engineering, University of Engineering and Technology (UET), Lahore},
  year      = {2026},
  month     = {August}
}
```

Distributed under the MIT License.

