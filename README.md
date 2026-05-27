# SPE Africa Geothermal Datathon 2026 — Team GeoLogic Analytics

## Project Title

**Integrated Medium-Temperature Geothermal District Energy System — Transmissivity-Aware Reservoir Targeting with Uncertainty-Aware Optimisation**

## Team Name

**GeoLogic Analytics**

## Problem Statement

This project develops an integrated geothermal district energy system for the Utrecht region (Netherlands) using medium-temperature resources from the Upper Rotliegend formation. The system targets:

- **10 MW district heating** capacity
- **5 MW district cooling** capacity

through transmissivity-aware reservoir selection, ATES (Aquifer Thermal Energy Storage) integration, heat-pump-assisted operation, and hybrid backup systems — with uncertainty-aware economic evaluation.

## Methodology Summary

### Stage 0 — Data Engineering and QC
- LAS file ingestion for 4 official wells (BLT-01, EVD-01, JUT-01, PKP-01)
- Missing-data assessment and visualisation
- TVD validation using directional survey data
- Lithostratigraphic integration for Rotliegend target zone identification
- Feature engineering from well log properties

### Stage 1 — Reservoir Intelligence
- ThermoGIS P90/P50/P10 property analysis
- ThermoGIS external scouting (4 supplementary candidates + 1 optimised corridor)
- Multi-criteria geothermal screening and ranking
- Transmissivity-driven viability assessment
- Final doublet selection: BLT-01 + GLA-01

### Stage 2 — Thermodynamic Modelling
- Thermal extraction calculations (Q = ṁ × Cp × ΔT)
- Seasonal demand modelling (heating and cooling profiles)
- Heat-pump integration analysis
- Cascade thermal utilisation

### Stage 3 — Integrated System Design
- Geothermal doublet production architecture
- ATES warm/cold well integration
- District heating/cooling loop design
- Hybrid backup strategy

### Stage 4 — Economic Analysis
- LCoE modelling using adapted TNO framework
- CAPEX/OPEX breakdown
- Sensitivity analysis (drilling costs, flow rate, temperature)

### Stage 5 — Uncertainty Analysis
- P10/P50/P90 scenario propagation
- Monte Carlo workflow for economic uncertainty

## Repository Structure

```
africa-geothermal-datathon-2026/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                    # Original competition data + LCOE template
│   ├── processed/              # Cleaned outputs from Notebook 01
│   └── thermogis_exports/      # ThermoGIS screenshots and maps
├── notebooks/
│   ├── 01_geothermal_resource_assessment.ipynb
│   ├── 02_integrated_energy_system_design.ipynb
│   └── 03_economic_and_ai_workflow.ipynb
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── exports/
├── presentation_assets/
└── docs/
```

## Instructions to Reproduce Results

### Environment Setup

```bash
pip install -r requirements.txt
```

### Execute Notebooks (in order)

```
01_geothermal_resource_assessment.ipynb    → Data engineering + reservoir screening
02_integrated_energy_system_design.ipynb   → System design + demand modelling
03_economic_and_ai_workflow.ipynb          → Economics + uncertainty + automation
```

Each notebook reads from `data/raw/` or outputs of the previous notebook, and writes results to `data/processed/`, `outputs/figures/`, and `outputs/tables/`.

## Key Engineering Findings

1. **Transmissivity > Temperature:** Hydraulic reservoir quality exerts stronger control on geothermal viability than temperature alone (PKP-01 counter-example: 88°C but 0.1 Dm transmissivity → non-viable)
2. **BLT-01 + GLA-01 doublet** provides ~10.8 MW combined thermal output — meeting the 10 MW heating requirement
3. **ATES integration** enables seasonal thermal balancing for the 5 MW cooling demand
4. **Integrated system architecture** reduces peak-load dependency and minimises heat-pump electricity consumption

## External Data Sources

- **ThermoGIS** (thermogis.nl): Used for supplementary well scouting and corridor optimisation. All extracted properties are documented in Notebook 01.
- **TNO LCOE Framework**: Adapted for integrated geothermal district energy economics.

## Dependencies

- Python 3.10+
- pandas, numpy, matplotlib, seaborn, scipy, lasio, openpyxl
- See `requirements.txt` for complete list
