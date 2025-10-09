# The Environment for Analysis of Geo-Located Energy Information (EAGLE-I)  
### Recorded Electricity Outages (2014–2024)

---

## About the Dataset

The **EAGLE-I (Environment for Analysis of Geo-Located Energy Information)** dataset provides **county-level U.S. electricity outage data** from **2014 to 2024**, collected at **15-minute intervals** from public utility outage maps by the EAGLE-I program at **Oak Ridge National Laboratory (ORNL)** under the **U.S. Department of Energy’s Office of Cybersecurity, Energy Security, and Emergency Response (DOE CESER)**.

This dataset represents one of the most comprehensive outage monitoring archives available, supporting **energy resilience**, **climate-disaster response**, and **grid reliability analysis**.

---

## Supplementary Files

| File | Description |
|------|--------------|
| `coverage_history.csv` | State-level customer coverage (2018–2022) |
| `MCC.csv` | Modeled customer counts per county (2022 baseline) |
| `DQI.csv` | Data Quality Index (DQI) and subcomponents by FEMA Region (2018–2022) |

**Recent Updates**
- **Feb 16 2023:** Added 2023 outage data + visualization scripts (`Uri_Map.R`, `DQI_processing.R`)  
- **Apr 10 2025:** Added 2024 outage data  

**Funding:** DOE CESER, U.S. Department of Energy  
**Keywords:** electricity outage, resilience, energy infrastructure, extreme weather, grid monitoring  

**Citation:**  
> Brelsford, C., Tennille, S., Myers, A., Chinthavali, S., Tansakul, V., Denman, M., *et al.* (2024).  
> *The Environment for Analysis of Geo-Located Energy Information’s Recorded Electricity Outages, 2014–2024.*  
> *Scientific Data (Nature Portfolio).* DOI: [10.1038/s41597-024-03095-5](https://doi.org/10.1038/s41597-024-03095-5)

---

## California Focus (2014–2024)

**Primary Source:** EAGLE-I (DOE-CESER / ORNL)  
**Frequency:** 15-minute intervals  
**Coverage:** About 92 % of U.S. electric customers (2022)  
**Purpose:** The EAGLE-I (2014–2024) dataset provides historical, validated, county-level power outage records across the U.S., including California, at 15-minute resolution.

---

## Dataset Files Overview

| File | Size | Rows | Notes |
|------|------:|------:|------|
| `eaglei_outages_2014.csv` | 78 MB | 1,689,461 | County outages (15-min) |
| `eaglei_outages_2015.csv` | 599 MB | 12,939,158 |  |
| `eaglei_outages_2016.csv` | 620 MB | 13,306,025 |  |
| `eaglei_outages_2017.csv` | 699 MB | 15,078,365 |  |
| `eaglei_outages_2018.csv` | 999 MB | 21,776,807 |  |
| `eaglei_outages_2019.csv` | 1.1 GB | 24,074,123 |  |
| `eaglei_outages_2020.csv` | 1.17 GB | 25,545,518 |  |
| `eaglei_outages_2021.csv` | 1.14 GB | 24,826,103 |  |
| `eaglei_outages_2022.csv` | 1.20 GB | 25,796,466 |  |

---

## Column Dictionary

| Column | Type | Definition | Example |
|---------|------|------------|----------|
| `fips_code` | string(5) | County FIPS code (zero-padded) | 06073 |
| `county` | string | County name | San Diego |
| `state` | string | Two-letter state abbreviation | CA |
| `customers_out` | numeric | Customers without power at timestamp | 1243 |
| `run_start_time` | datetime | Snapshot timestamp (UTC or local) | 2023-10-05 14:15:00 |

---

## Methods

### Data Collection
EAGLE-I automatically scrapes public utility outage maps every 15 minutes, collecting the number of customers without power by county.  
The platform does not distinguish **why** outages occur—it captures all visible interruptions regardless of cause.

**Process Workflow**
1. Retrieve outage data (HTML, JSON, GIS feeds)  
2. Parse and extract fields (`county`, `fips_code`, `customers_out`, `timestamp`)  
3. Store structured results in ORNL’s relational database  
4. Log parsing errors (`PARSER_ERROR`, `CONNECTION_ERROR`, `TIMEOUT`) for review  

---

## Calculation & Derived Metrics

| Metric | Formula / Description |
|---------|----------------------|
| **Raw Outages** | `customers_out` — direct value reported by utilities |
| **Percent Customers Out** | `PercentOut_i = (customers_out_i / c_i) × 100` where `c_i` = modeled customers in county *i* |
| **Modeled Customers per County** | `c_i = (p_i / P) × C` using LandScan population (*pᵢ*), EIA-861 totals (*C*), and service-territory populations (*P*) |
| **Temporal Aggregations** | Hourly, daily, or event-based roll-ups |
| **Data Quality Index (DQI)** | `DQI = (0.4 S + 0.3 E + 0.2 C + 0.1 P)` where *S* = Success Rate, *E* = Enabled Share, *C* = Coverage, *P* = Spatial Precision |

---

## Interpretation Guidelines

Because the dataset lacks an **“outage cause”** field, analysts must cross-reference **external datasets** to distinguish between:  
- **PSPS (Planned Public Safety Power Shutoffs)**  
- **Unplanned Outages** (storms, equipment failures, grid overloads)

| Scenario | Likely Event | Recommended Cross-Reference |
|-----------|--------------|-----------------------------|
| Continuous zeros or missing data during PSPS period | Planned PSPS | CAL FIRE / CPUC PSPS logs |
| Sudden spike/quick restoration | Storm or grid fault | NOAA / CAISO event data |
| Extended feed drop | Reporting suspension or maintenance | DOE CESER summaries |

---

## Data Quality Index (2018–2022)

| Component | Meaning | Weight |
|------------|----------|--------|
| S | Parser success rate | 40 % |
| E | Percent enabled (active collection share) | 30 % |
| C | Customer coverage | 20 % |
| P | Spatial precision (county = 100, ZIP = 50, polygon = 25) | 10 % |

Region IX (California) improved steadily, achieving > 90 % coverage and reliability by 2022.

---

## Gaps, Errors, and Limitations

| Category | Description / Findings | Impact |
|-----------|------------------------|---------|
| Temporal Coverage | ≈ 2,100 counties (2014) → > 3,000 (2022) | Early years incomplete |
| County Coverage (CA) | Full by 2018; minor rural gaps | < 1 % unmonitored |
| Parser & Connection Errors | ≈ 1 M total (2017–2022) | Most auto-resolved < 15 min |
| Short-Duration Outages | < 15 min outages under-sampled | May appear missing |
| Spatial Discrepancies | County boundaries by area, not population | Minor misallocations |
| Temporal Gaps | During storms (e.g., Winter Storm Uri 2021) | Typically 15–60 min |
| Metadata Missingness | < 1 % missing state or county | Minimal impact |
| Zero vs Missing | Cannot distinguish true 0 vs data void | Requires contextual filtering |
| Manual Corrections | Unflagged FEMA/DOE edits possible | Limited effect |
| Validation Limitations | DQI available only after 2018 | Use caution pre-2017 |

---

## Parsing Notes

**Parsing** means reading and structuring raw data from unstandardized sources.  
EAGLE-I’s parser converts HTML, JSON, or GIS feeds into clean tabular records.

**Common Parser Errors**
- Utility format/API changes  
- Feed downtime or malformed JSON/XML  
- Mid-update data pulls are causing incomplete tags  

**Result:** parser retries automatically; temporary data voids (≤ 15 min).

---

## Additional Context

- **Unmonitored Utilities:** about 8 % of U.S. customers (mostly rural/municipal)  
- **Baseline Sources:** EIA-861, HIFLD, LandScan USA  
- **Operational Interruptions:** Utility website outages = missing data periods  
- **Correction Protocol:** Logged, reviewed, and patched via ETL updates  
- **Regional Reliability:** FEMA Region IX (CA) > 90 % DQI by 2022  

---

## Summary Assessment

| Period | Data Quality Summary |
|---------|----------------------|
| 2014–2016 | Pilot phase; partial national coverage |
| 2017–2020 | Expansion + stabilization |
| 2021–2022 | High completeness; minimal short gaps |
| 2023–2024 | Ongoing ingestion; minor trailing gaps |

**EAGLE-I** is a robust, validated, and continuously improving dataset for national-scale energy resilience analysis.

---

## Data Sources for California Integration

- Utility outage maps: 15-min feeds (scraped formats vary)  
- EIA Form 861: Utility customer totals  
- LandScan USA: Day/night population estimates  
- HIFLD: Utility service territories  
- FEMA Regions: Basis for DQI aggregation (Region IX = California)  

---

## Access & Citation

**Public Archive:** [Figshare — DOI 10.6084/m9.figshare.24237376](https://doi.org/10.6084/m9.figshare.24237376)  

**Reference Publication:**  
> Brelsford C., Tennille S., Myers A., *et al.* (2024).  
> *A dataset of recorded electricity outages by United States county, 2014–2022.* *Scientific Data*, 11, 271.  
> DOI: [10.1038/s41597-024-03095-5](https://doi.org/10.1038/s41597-024-03095-5)

**Note:** The live EAGLE-I GIS Dashboard is restricted to government and emergency partners.  
The Figshare archive provides the complete, public historical dataset used for analysis.
