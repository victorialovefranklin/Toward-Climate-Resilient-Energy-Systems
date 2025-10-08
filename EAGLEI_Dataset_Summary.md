# ⚡ The Environment for Analysis of Geo-Located Energy Information (EAGLE-I)
### Recorded Electricity Outages (2014–2024)

## 📘 Overview
EAGLE-I provides county-level U.S. power outage data (2014–2024) at 15-minute intervals from public utility outage maps.
It supports energy resilience, climate impact, and grid monitoring research.

## ⚙️ Methods
- Automated scraping from utility outage maps every 15 minutes.
- Core fields: `fips_code`, `county`, `state`, `customers_out`, `run_start_time`.
- Outage cause (planned/unplanned) is **not specified** in feeds.

## 🧮 Calculation / Formula
**Percent Customers Out**
```
PercentOut = (customers_out / c_i) × 100
```
**Modeled Customers per County**
```
c_i = (p_i / P) × C
```
Where:
- C = total customers in utility’s service area
- P = total population in service area
- p_i = population in county i

**Data Quality Index (DQI)**
```
DQI = (0.4 * S) + (0.3 * E) + (0.2 * C) + (0.1 * P)
```

## ⚠️ Gaps & Limitations
- Partial coverage 2014–2016 (~2,100 counties).
- Expanded to >3,000 by 2022 with >90% coverage in FEMA Region IX (CA).
- Parser/connection errors ≈ 1M (mostly corrected automatically).
- Outages <15 min may be underrepresented.
- DQI only available post-2018.
- Missing or zero values may reflect PSPS reporting pauses or downtime.

## ✅ Summary
Robust and validated dataset improving over time:
- 2014–2016: pilot coverage  
- 2017–2020: expansion and stabilization  
- 2021–2022: high completeness  
- 2023–2024: ongoing ingestion  

## 🔗 Access & Citation
**Public Dataset:** [Figshare — DOI 10.6084/m9.figshare.24237376](https://doi.org/10.6084/m9.figshare.24237376)

**Reference Publication:**  
Brelsford, C., Tennille, S., Myers, A., Chinthavali, S., Tansakul, V., Denman, M., *et al.* (2024).  
*A dataset of recorded electricity outages by United States county, 2014–2022.* *Scientific Data*, 11, 271.  
DOI: [10.1038/s41597-024-03095-5](https://doi.org/10.1038/s41597-024-03095-5)
