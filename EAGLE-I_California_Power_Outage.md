# The Environment for Analysis of Geo-Located Energy Information’s Recorded Electricity Outages 2014-2024

The core of the provided dataset includes eight years of power outage information at the county level from 2014 to 2024 at 15-minute intervals collected from utility’s public outage maps on their websites by the EAGLE-I program at ORNL. Three supplementary files are included to augment the power outage data files. The first file includes the customer coverage rate of each state from 2018-2022. The second file provides the modeled number of electric customers per county as of 2022. The third presents our Data Quality Index and the four sub-components by year by FEMA Region for 2018-2022. UPDATE 2/16/2023: Added 2023 outage data and Uri_Map.R and DQI_processing.R files have been added. They were used to create graphics in associated works.
UPDATE 4/10/2025: Added 2024 outage data.

## Funding
Department of Energy Office of Cybersecurity, Energy Security, and Emergency Response (DOE CESER)
- Keywords
- electricity outage
- energy resilience
- extreme weather

Citation: Brelsford, Christa; Tennille, Sarah; Myers, Aaron; Chinthavali, Supriya; Tansakul, Varisara; Denman, Matthew; et al. (2023). The Environment for Analysis of Geo-Located Energy Information’s Recorded Electricity Outages 2014-2024. figshare. Dataset. https://doi.org/10.6084/m9.figshare.24237376.v3 

## County-Level Power Outage Dataset — **California Focus (2014–2022)**

**Based on:** Brelsford et al., *Scientific Data* (2024), DOI: 10.1038/s41597-024-03095-5  
**Primary Source:** EAGLE-I (DOE-CESER / ORNL) — county-level outage counts every **15 min** (2014–2022); ~**92%** of U.S. customers represented by 2022.

---

## What this repo provides
- How to use the **public historical** EAGLE-I outage files for **California counties** (2014–2022).
- Exact **column names** (all outage years), core **indicators**, and the **customer-estimation** formula with a worked example.
- **Known gaps/limitations** to avoid misinterpretation.
- Where to obtain the dataset and the reference publication.

---

## Files in the public dataset (excerpt)
*(Each year is a separate CSV at 15-minute cadence; auxiliaries cover coverage, modeled customers, and quality.)*

| File                      | Size   | Rows       | Notes                                        |
|---------------------------|:------:|-----------:|----------------------------------------------|
| `eaglei_outages_2014.csv` | 78.1 MB|  1,689,461 | County outages (15-min)                      |
| `eaglei_outages_2015.csv` | 599 MB | 12,939,158 |                                              |
| `eaglei_outages_2016.csv` | 619.8 MB| 13,306,025 |                                              |
| `eaglei_outages_2017.csv` | 698.8 MB| 15,078,365 |                                              |
| `eaglei_outages_2018.csv` | 999.2 MB| 21,776,807 |                                              |
| `eaglei_outages_2019.csv` | 1.1 GB | 24,074,123 |                                              |
| `eaglei_outages_2020.csv` | 1.17 GB| 25,545,518 |                                              |
| `eaglei_outages_2021.csv` | 1.14 GB| 24,826,103 |                                              |
| `eaglei_outages_2022.csv` | 1.20 GB| 25,796,466 |                                              |
| `MCC.csv`                 | 41 KB  |      3,235 | Modeled customers per county (2022)          |
| `coverage_history.csv`    | 12 KB  |        280 | State coverage (2018–2022)                   |
| `DQI.csv`                 | 6 KB   |         50 | Data Quality Index by FEMA region (2018–2022)|

---

## Column names (all outage years)
**Outage files (`eaglei_outages_YYYY.csv`):**
- `fips_code` — county FIPS  
- `county` — county name  
- `state` — state name  
- `customers_out` — customers without power (integer; **0s are not included**)  
- `run_start_time` — UTC timestamp (`MM/DD/YY HH:MM`)


 EAGLE-I California poeOutage 



**Auxiliaries:**
- `MCC.csv`: `County_FIPS`, `Customers`  
- `coverage_history.csv`: `year`, `state`, `total_customers`, `min_covered`, `max_covered`, `min_pct_covered`, `max_pct_covered`  
- `DQI.csv`: `fema`, `year`, `success_rate`, `percent_enabled`, `spatial_precision`, `cust_coverage`, `max_covered`, `total_customers`, `DQI`

---

## Producer & purpose (California relevance)
- **Producer:** Oak Ridge National Laboratory (ORNL) for **DOE-CESER** via **EAGLE-I**.  
- **Scope:** County-level outage estimates every 15 min (2014–2022).  
- **Why California:** Enables real-time situational awareness, resilience analysis, and longitudinal modeling across **58 CA counties**.

---

## Background (concise)
- The **2003 Northeast Blackout** exposed gaps in **situational awareness**, leading DOE to build wide-area monitoring that evolved into **EAGLE-I**.  
- EAGLE-I has supported response/assessment during **Winter Storm Uri (2021)**, **Hurricane Ian (2022)**, and the **Camp Fire (2018)**.  
- Methods include parsing ~**400** utility web maps (JSON/eBill/IFactor/XML/HTML), normalizing point/ZIP/polygon reports to **county level**, and expanding coverage from **1,072 counties without data (2014)** to **182 (2022)**.

---

## Data sources (for California analysis)
- **Utility outage maps** (15-min parsing; heterogeneous formats).  
- **EIA Form 861** (utility customer totals).  
- **LandScan USA** (day/night population).  
- **HIFLD** (service territories).  
- **FEMA regions** for quality aggregation (**Region IX** includes California).

---

## Indicators (compute directly)
- **Raw outages:** `customers_out`  
- **Percent customers out:**  
  \[
  \text{PercentOut}=\frac{\text{customers\_out}}{c_i}\times 100
  \]
  where \(c_i\) is modeled customers for county \(i\) (from `MCC.csv` or computed below).  
- **Temporal rollups:** hourly/daily maxima per county.  
- **Quality/coverage context:** join `DQI.csv` (Region IX) and `coverage_history.csv`.

**External predictors (not included in EAGLE-I; join separately):** CAL FIRE wildfire perimeters, NOAA/NCEI wind/temperature/heat, drought indices, CAISO load/curtailment, ACS socio-demographics.

---

## Estimating **total customers per county** (when not provided)
Utilities often don’t publish county totals; EAGLE-I models them using **LandScan** (population), **EIA-861** (utility totals), and **HIFLD** (territories).

Let:
- \(C\) = total customers in a utility’s service area  
- \(P\) = total population in that service area  
- \(p_i\) = population in county \(i\) within the service area  
- \(c_i\) = modeled customers in county \(i\)

---

## Data Quality Index (**DQI**, 2018–2022)
Components and weights:
- \(S\) = **Success Rate** (parser runs without error)  
- \(E\) = **Percent Enabled** (active collection share)  
- \(C\) = **Customer Coverage**  
- \(P\) = **Spatial Precision** (county = 100, point = 75, ZIP = 50, polygon = 25)

Computed by **FEMA region × year**; **Region IX** (includes CA) improves over **2018–2022**.

---

## Known gaps & cautions
- **Sub-15-minute outages** can be missed (sampling cadence).  
- **Under-coverage** of some small/municipal/rural utilities (~**8%** of customers not represented by 2022).  
- **Parser/website changes** may introduce temporary gaps or inconsistencies.  
- **Modeled customers** assume proportionality with population (may misstate areas with atypical commercial/industrial load).  
- **DQI available only for 2018–2022** (earlier years lack this metric).

---

## Access & citation (provide)
- **Historic dataset (public):** Figshare — DOI: **10.6084/m9.figshare.24237376** https://figshare.com/articles/dataset/The_Environment_for_Analysis_of_Geo-Located_Energy_Information_s_Recorded_Electricity_Outages_2014-2022/24237376  
- **Reference publication:** Brelsford, C., Tennille, S., Myers, A., *et al.* (2024). *A dataset of recorded electricity outages by United States county, 2014–2022.* **Scientific Data**, 11, 271. https://doi.org/10.1038/s41597-024-03095-5

> **Note:** The live EAGLE-I GIS dashboard is **restricted** to government and approved emergency-management partners; the Figshare archive provides the **historical** data used here.
