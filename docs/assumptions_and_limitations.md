# Assumptions and Limitations

## Key Assumptions

### Reservoir Properties
- P50 ThermoGIS values used as base case for all screening and design calculations
- Brine density: 1040 kg/m³ (per Surface Facilities Design Report)
- Brine specific heat: 4.0 kJ/kg·K (per Surface Facilities Design Report)
- Rock density: 2700 kg/m³
- Rock specific heat: 1000 J/kg·K

### Operational Parameters
- Reinjection temperature: 35–40°C (post heat-extraction and heat-pump support)
- District heating supply temperature: 70°C
- District heating return temperature: 40°C
- ATES warm well temperature: 15–35°C
- ATES cold well temperature: 8–15°C
- Heat pump COP: 2.25 (thermal/electric for 68→70°C upgrade, per surface report). Note: the LCOE template figure of 27 is a system-level thermal:electric ratio, not the heat pump COP.

### Economic Parameters
- Economic lifetime: 15 years (from LCOE template)
- Well cost scaling factor: 1.5
- Pump investment: 0.3 Mln EUR/pump with workover every 5 years

### Demand Assumptions
- District heating demand: 10 MW (minimum competition requirement)
- District cooling demand: 5 MW (minimum competition requirement)
- Simplified seasonal demand model (no hourly consumption data available)

## Known Limitations

1. **No coupled reservoir simulation** — Thermal extraction assumes steady-state flow; no thermal drawdown modelling over time
2. **GLA-01 is hypothetical** — Not an existing well; requires new drilling with associated uncertainty
3. **Simplified demand profiles** — No real hourly district consumption data available within challenge framework
4. **ThermoGIS uncertainty** — P50 values used as deterministic inputs; full probabilistic coupling not implemented
5. **No detailed ATES modelling** — ATES integration is conceptual; no groundwater flow simulation
6. **Single-formation target** — Only Rotliegend considered; no multi-formation stacking assessment
