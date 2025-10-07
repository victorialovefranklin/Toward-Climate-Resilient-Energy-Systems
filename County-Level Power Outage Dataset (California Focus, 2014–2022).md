# County-Level Power Outage Dataset (California Focus, 2014–2022)

**Based on:** Brelsford et al., *Scientific Data* (2024) — DOI: 10.1038/s41597-024-03095-5  
**Primary Source:** EAGLE-I (DOE-CESER / ORNL)

> This repository provides a California-focused orientation to the EAGLE-I 15-minute county-level outage dataset (2014–2022), plus example Python snippets to explore, validate, and model the data.

---

## Producer & Purpose

- **Produced by:** Oak Ridge National Laboratory (ORNL) for **DOE-CESER** via the **EAGLE-I** platform.  
- **Cadence & scope:** 15-minute county-level outage estimates (2014–2022). By 2022 the platform represents **~92% of U.S. customers**.

**Why it matters for California:** Enables real-time situational awareness, resilience analysis, and longitudinal modeling across **California’s 58 counties**.

---

## Background

The **2003 Northeast Blackout** exposed the nation’s vulnerability to widespread power failures and underscored the lack of **real-time situational awareness** across the energy grid. In response, the **U.S. Department of Energy (DOE)** developed wide-area monitoring capabilities that evolved into the **Environment for Analysis of Geo-Located Energy Information (EAGLE-I)** system.

EAGLE-I provides a **federated, geospatially enabled infrastructure** for monitoring the status of energy assets and supporting cross-sector decision-making. The platform has been instrumental during major national emergencies such as **Winter Storm Uri (2021)**, **Hurricane Ian (2022)**, and the **Camp Fire (2018)**—enabling agencies including **DOE**, **FEMA**, **DHS**, **NSC**, and **NERC** to assess outage conditions, coordinate response, and manage recovery operations.

---

## EAGLE-I™ GIS Platform Access

**EAGLE-I™** is an **interactive Geographic Information System (GIS)** developed by the DOE’s **Office of Cybersecurity, Energy Security, and Emergency Response (CESER)** and operated by **Oak Ridge National Laboratory (ORNL)**. The system allows authorized users to **visualize and analyze the nation’s energy infrastructure**—including **electric, petroleum, and natural gas networks**—within a single geospatial platform.

Through EAGLE-I™, users can:

- View and map **critical energy assets** across multiple sectors.  
- Access **near real-time situational updates** on power outages and infrastructure disruptions.  
- Integrate data from **utility reports, weather systems, and emergency response feeds**.  
- Perform **advanced GIS mapping** with customizable overlays for resilience analysis.

🔗 **Platform Access:** [DOE CESER EAGLE-I™ GIS Portal](https://eagle-i.doe.gov/)

> ⚠️ **Access Notice:**  
> EAGLE-I is a restricted system available only to **government employees** and **approved emergency management partners**.  
> Academic or public researchers currently **cannot obtain direct access** to the live dashboard.

However, the **historic EAGLE-I dataset (2014–2022)** is **publicly available** and suitable for academic and research use:

- 📦 **Dataset Download:** [Figshare Repository (DOI: 10.6084/m9.figshare.24237376)](https://doi.org/10.6084/m9.figshare.24237376)  
- 📘 **Reference Publication:** Brelsford, C., Tennille, S., Myers, A., *et al.* (2024). *A dataset of recorded electricity outages by United States county, 2014–2022.* *Scientific Data*, 11, 271. [https://doi.org/10.1038/s41597-024-03095-5](https://doi.org/10.1038/s41597-024-03095-5)

These resources provide full access to **historic outage data** and detailed documentation of **EAGLE-I’s design, methodology, and quality assurance framework**, allowing researchers to reproduce analyses or build derivative models using open data.

---

## Data Sources (California Applications)

- **Utility outage maps** parsed every 15 minutes (hundreds of utilities / multiple formats: JSON, eBill, IFactor, XML, HTML, etc.).  
- **EIA Form 861** (utility customer totals).  
- **LandScan USA** (day/night population).  
- **HIFLD** (service territories).  
- **FEMA regions** used for quality aggregation (**California in Region IX**).

---

## Methods & Data Processing

### Data Collection & Aggregation
- **Parsers** ingest ~400 sites per 15 minutes; formats include JSON/eBill/IFactor/XML/HTML (see paper Table 1).
- **Geographic normalization:** points/ZIP/polygons → **county** level.
- **Coverage growth:** counties without data fell from **1,072 (2014)** to **182 (2022)**.

### Error Monitoring
Common collection issues (parser/connection/timeout) are tracked and corrected; **privileged users can flag/patch** gaps in near real-time (cf. paper Table 3).

---

## Estimating Total Customers per County

Utilities often don’t publish county-level customer totals, so EAGLE-I models them using **population and service-area overlays** (LandScan, EIA-861, HIFLD).

Let:

- C = total customers in a utility’s service area  
- P = total population in that service area  
- pᵢ = population in county i **within** the service area  
- cᵢ = **modeled** customers in county i

**Proportional allocation formula**  
cᵢ = (pᵢ / P) × C

**Worked example — Los Angeles County (illustrative numbers)**  
If a utility has C = 10,000,000 customers, its service-area population is P = 40,000,000, and LA County’s share is pᵢ = 9,800,000, then:  
cᵢ = (9,800,000 / 40,000,000) × 10,000,000 = 2,450,000

If at a timestamp the dataset reports **Customers_Out = 61,250** for LA County:  
Percent Customers Out = (61,250 / 2,450,000) × 100 = **2.5%**

---

## Data Quality Index (DQI)

**Components & weights:**

- **Success Rate** (S)  
- **Percent Enabled** (E)  
- **Customer Coverage** (C)  
- **Spatial Precision** (P)

**Formula:**  
DQI = 0.4S + 0.3E + 0.2C + 0.1P

Computed by **FEMA region/year**; **Region IX** (includes CA) improves through 2018–2022.

---

## Python Quickstart

### Load and Merge Data

```python
import pandas as pd

outages = pd.read_csv("eaglei_outages_2022.csv")
mcc = pd.read_csv("MCC.csv")

df = outages.merge(mcc, on="county_fips", how="left")
df["pct_out"] = (df["customers_out"] / df["modeled_customers"]) * 100
print(df.head())
```

### Compute Data Quality Index (DQI)

```python
def compute_dqi(S, E, C, P):
    return 0.4*S + 0.3*E + 0.2*C + 0.1*P

example = {"S": 95, "E": 92, "C": 90, "P": 100}
print(compute_dqi(**example))
```

---

## Citation

Brelsford, C., Tennille, S., Myers, A., et al. (2024). *A dataset of recorded electricity outages by United States county, 2014–2022.* **Scientific Data**, 11, 271. https://doi.org/10.1038/s41597-024-03095-5

---
