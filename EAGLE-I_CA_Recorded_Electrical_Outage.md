# The Environment for Analysis of Geo-Located Energy Information (EAGLE-I) — Recorded Electricity Outages (2014–2024)

### Overview
The **EAGLE-I dataset** (Environment for Analysis of Geo-Located Energy Information) provides **county-level U.S. power outage data** from **2014 to 2024**, collected at **15-minute intervals** from utility public outage maps by the **EAGLE-I program at Oak Ridge National Laboratory (ORNL)**.

Three supplementary files support interpretation and validation:

1. **State Coverage (2018–2022):** Customer coverage rates by state.  
2. **Modeled County Customers (2022):** Estimated number of electric customers per county.  
3. **Data Quality Index (DQI, 2018–2022):** Overall quality and four subcomponents by FEMA Region.

**Updates:**
- **02/16/2023:** Added 2023 outage data, plus `Uri_Map.R` and `DQI_processing.R` scripts for visualization.  
- **04/10/2025:** Added 2024 outage data.

**Funding:** U.S. Department of Energy — Office of Cybersecurity, Energy Security, and Emergency Response (DOE CESER)

**Keywords:** `electricity outage`, `energy resilience`, `extreme weather`, `grid monitoring`

**Citation:**  
Brelsford, C., Tennille, S., Myers, A., Chinthavali, S., Tansakul, V., Denman, M., *et al.* (2024).  
*The Environment for Analysis of Geo-Located Energy Information’s Recorded Electricity Outages, 2014–2024.*  
**Scientific Data** (Nature Portfolio). DOI: [10.1038/s41597-024-03095-5](https://doi.org/10.1038/s41597-024-03095-5)

---
## Focus Study:*California Focus (2014–2024)*
**Primary Source:** EAGLE-I (DOE-CESER / ORNL)  
**Frequency:** 15-minute intervals  
**Coverage:** ~92% of U.S. electric customers represented by 2022  
**Purpose:** Enables real-time situational awareness, resilience analysis, and longitudinal modeling across 58 California counties.

---

## Public Dataset Files  

| **File** | **Size** | **Rows** | **Notes** |
|-----------|-----------|-----------|-----------|
| `eaglei_outages_2014.csv` | 78.1 MB | 1,689,461 | County outages (15-min) |
| `eaglei_outages_2015.csv` | 599 MB | 12,939,158 |  |
| `eaglei_outages_2016.csv` | 619.8 MB | 13,306,025 |  |
| `eaglei_outages_2017.csv` | 698.8 MB | 15,078,365 |  |
| `eaglei_outages_2018.csv` | 999.2 MB | 21,776,807 |  |
| `eaglei_outages_2019.csv` | 1.1 GB | 24,074,123 |  |
| `eaglei_outages_2020.csv` | 1.17 GB | 25,545,518 |  |
| `eaglei_outages_2021.csv` | 1.14 GB | 24,826,103 |  |
| `eaglei_outages_2022.csv` | 1.20 GB | 25,796,466 |  |
| `MCC.csv` | 41 KB | 3,235 | Modeled customers per county (2022) |
| `coverage_history.csv` | 12 KB | 280 | State coverage (2018–2022) |
| `DQI.csv` | 6 KB | 50 | Data Quality Index by FEMA Region (2018–2022) |

---

## Column Names (All Outage Years)

| **Column** | **Type** | **Definition** | **Example** |
|-------------|-----------|----------------|--------------|
| `fips_code` | string(5) | 5-digit county FIPS code (zero-padded). | `06073` |
| `county` | string | County name associated with the FIPS code. | `San Diego` |
| `state` | string | Two-letter state abbreviation. | `CA` |
| `customers_out` | numeric | Number of customers reported without power at the recorded timestamp. | `1243` |
| `run_start_time` | datetime | Timestamp when the outage snapshot was generated (local or UTC). | `2023-10-05 14:15:00` |

---
Methods: 

Data collection
### How EAGLE-I Collects the Data

- **Collection method:** EAGLE-I automatically scrapes outage data from public utility web maps at **15-minute intervals**.  
- **Feed content:** These maps display **active customer outages only** — they do **not** include metadata describing *why* an outage occurred.  
- **System behavior:** As a result, **all service interruptions** visible on the utilities’ feeds are recorded as *customers without power*, regardless of whether they were **preventive (PSPS)** or **unexpected (incident outages)**.
- 
### The EAGLE-I dataset does not explicitly distinguish between:**
1. **Planned Public Safety Power Shutoff (PSPS) events**, and  
2. **Unplanned or emergency outage incidents** (e.g., storms, equipment failure, grid overload).

All interruptions are recorded uniformly as `customers_out` based on utilities’ public outage maps, without a field specifying the cause or intent of the outage.
---

## Indicators and Derived Metrics

| **Indicator** | **Formula / Description** |
|----------------|---------------------------|
| **Raw outages** | `customers_out` |
| **Percent customers out** | `PercentOut = (customers_out / c_i) × 100`, where `c_i` = modeled customers in county *i*. |
| **Temporal rollups** | Hourly/daily maxima per county. |
| **Quality context** | Join `DQI.csv` (Region IX) and `coverage_history.csv`. |
| **External predictors** | (Not included in EAGLE-I) Join with CAL FIRE, NOAA/NCEI, CAISO, ACS. |

---

## Estimating Modeled Customers per County
EAGLE-I models customer counts where utilities don’t publish them, using:
- **LandScan** population data  
- **EIA-861** utility totals  
- **HIFLD** service territory boundaries  

**Formula:**  
`c_i = (p_i / P) × C`  
where:  
- `C` = total customers in utility’s service area  
- `P` = total population in service area  
- `p_i` = population in county *i*

---

## Data Quality Index (DQI, 2018–2022)
Components & weights:
- **S** = Success Rate (parser runs without error)  
- **E** = Percent Enabled (active collection share)  
- **C** = Customer Coverage  
- **P** = Spatial Precision (county=100, point=75, ZIP=50, polygon=25)

**Region IX (California):** Continuous improvement from 2018 → 2022.

---


---



---

### What the ORNL Report States
According to the official report (Brelsford et al., *Scientific Data*, 2024, DOI: [10.1038/s41597-024-03095-5]):

- Outages represent **“utility-reported customer interruptions”** aggregated by county and time.  
- The EAGLE-I platform’s scope **does not include classification or root-cause tagging**.  
- During major PSPS or wildfire prevention events, **utilities may pause reporting**, causing the feed to drop to zero or go missing temporarily.  
  These appear as **NaN or zero-customer intervals**, not as a labeled PSPS event.

---

### Interpretation Guidance (for California Analysts)

Analysts using EAGLE-I should interpret PSPS and unplanned outages by cross-referencing with additional datasets:

| **Scenario** | **Recommended Interpretation** | **External Cross-Reference** |
|---------------|--------------------------------|-------------------------------|
| **Continuous zero or missing intervals** during known PSPS periods | Likely *planned Public Safety Power Shutoffs* | CAL FIRE PSPS logs, CPUC PSPS dataset |
| **Sudden spikes** in `customers_out` followed by restoration | Likely *unplanned outage incidents* | NOAA storm reports, CAISO curtailment or grid event logs |
| **Extended missing feeds** | May indicate intentional reporting suspension or website downtime | Utility maintenance logs, DOE CESER incident summaries |

**Best practice:**  
Combine EAGLE-I’s continuous outage records with **CAL FIRE**, **CAISO**, and **NOAA/NCEI** event data to classify outage types and improve resilience modeling accuracy.

---

### Summary
| **Aspect** | **EAGLE-I Representation** | **Clarification** |
|-------------|-----------------------------|-------------------|
| Outage type field | ❌ Not provided | No field indicating PSPS vs. unplanned outage. |
| Data source | Utility public outage maps | Cause metadata unavailable. |
| PSPS periods | Often appear as data gaps or zero-customer intervals. | Requires external matching. |
| True outage incidents | Reflected as non-zero `customers_out` values with timestamped restoration. | Represent emergency or equipment-related outages. |

---

**In short:**  
> EAGLE-I captures **all visible service interruptions** but does **not specify** whether they are *planned* PSPS events or *unplanned* outages.  
> To distinguish them, analysts must **cross-reference external California PSPS and weather datasets.**



---
## EAGLE-I Dataset Gaps, Errors, and Missing Data (2014–2024)

| **Category** | **Details / Findings (Based on ORNL EAGLE-I Report, 2024)** | **Impact / Notes** |
|---------------|-------------------------------------------------------------|--------------------|
| **Temporal Coverage (2014–2024)** | Coverage expands from about 2,100 U.S. counties in 2014 → > 3,000 by 2022. | 2014–2016 partial data; stable by 2018 for most states, including CA. |
| **County Coverage (CA)** | By 2018, all CA counties represented; minor rural utilities may remain unmapped. | < 1% of customers unmonitored. |
| **Parser & Connection Errors (2017–2022)** | about 1M total parser events (`PARSER_ERROR`, `CONNECTION_ERROR`, `TIMEOUT`, etc.). | Caused by network issues or format changes; most fixed within 15 min. |
| **Short-Duration Outages** | Outages <15 min are under-represented due to sampling frequency. | Short outages may appear missing. |
| **Spatial Discrepancies** | County boundaries split by area rather than population. | Minor misallocations are possible. |
| **Temporal Gaps** | Gaps during severe weather (e.g., Winter Storm Uri 2021). | Typically 15–60 min; collection resumes automatically. |
| **Data Quality Index (DQI)** | Implemented 2018–2022; measures success rate, coverage, and uptime. | Region IX (CA) > 90% coverage by 2022. |
| **Spatial Precision** | Decline in 2019 from coarser polygon feeds. | Minimal county-level impact. |
| **Metadata Missingness** | Occasional missing `state` or `county` fields (<1%). | Filtered via FIPS prefix “06”. |
| **FIPS Code Missingness** | Early years lacked standardized mapping. | <0.5% missing post-2018. |
| **Customers_Out Missingness** | 2–5% missing during feed disruptions or wildfires. | Common during PSPS events. |
| **Run_Start_Time Missingness** | <0.5% unparseable timestamps (DST or delays). | Treated as NaN; not imputed. |
| **Zero vs Missing** | The Dataset doesn’t distinguish true zero vs missing feeds. | Contextual interpretation needed. |
| **Manual Corrections** | FEMA/DOE may apply unflagged manual edits. | Minor impact. |
| **Validation Limitations** | No DQI before 2018. | Pre-2017 data requires caution. |

---
### Notes: 
- What Does “Parse” Mean? To **parse** means to **read, interpret, and convert raw data into a structured format** that a computer program can process efficiently. In the Context of EAGLE-I, EAGLE-I parses data every 15 minutes from public utility outage maps and feeds.
**Process:**
1. **Download** raw data (HTML, JSON, GIS).  
2. **Extract** values: county name, FIPS, customers out, timestamp.  
3. **Convert & store** these in structured database tables.

### What a “Parser Error” Means
A **parser error** occurs when data cannot be read or interpreted correctly.
**Causes include:**
- Utility changes data format or API endpoint.  
- Feed or web page is temporarily down.  
- Incomplete or malformed JSON/XML.  
- Data arrives mid-update → inconsistent tags.

**In summary:**
- **Parsing:** Translating messy raw feeds into structured records.  
- **Parser errors:** Failures in that translation due to data or connection issues.
---

## Additional Notes
- **Unmonitored Utilities:** About 8% of U.S. customers (mostly rural/municipal) are not represented.  
- **Geographic Baseline:** Based on *EIA-861* and *HIFLD* boundaries (*customers ≠ population*).  
- **Operational Interruptions:** Any utility website outage = synchronized data void.  
- **Correction Protocol:** Errors auto-logged; ORNL resolves persistent issues in ETL updates.  
- **Data Quality Improvements:** Continuous improvement 2018 → 2022 across FEMA Region IX (CA).

---

## Summary Assessment
- **Robust, validated, and improving dataset.**  
- **2014–2016:** Incomplete pilot coverage.  
- **2017–2020:** Expansion and stabilization.  
- **2021–2022:** High completeness, minor short gaps.  
- **2023–2024:** Ongoing ingestion; trailing incompleteness under review.  

---
## 🏗️ Data Sources for California Analysis

- **Utility outage maps:** 15-min parsing (heterogeneous formats).  
- **EIA Form 861:** Utility customer totals.  
- **LandScan USA:** Day/night population estimates.  
- **HIFLD:** Service territories.  
- **FEMA Regions:** Used for DQI aggregation (Region IX includes CA).

---



## 🔗 Access & Citation
**Historic Dataset (Public):**  
[Figshare — DOI: 10.6084/m9.figshare.24237376](https://figshare.com/articles/dataset/The_Environment_for_Analysis_of_Geo-Located_Energy_Information_s_Recorded_Electricity_Outages_2014-2022/24237376)

**Reference Publication:**  
Brelsford, C., Tennille, S., Myers, A., *et al.* (2024).  
*A dataset of recorded electricity outages by United States county, 2014–2022.*  
*Scientific Data*, 11, 271. [DOI: 10.1038/s41597-024-03095-5](https://doi.org/10.1038/s41597-024-03095-5)

**Note:**  
The live EAGLE-I GIS dashboard is restricted to government and emergency partners.  
The **Figshare archive** provides the complete historical dataset used in this repository.
