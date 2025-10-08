 # Cal OES Statewide Power Outages (Real-Time) Dataset 

**Source:** [California Governor’s Office of Emergency Services (Cal OES) GIS Division](https://www.arcgis.com/home/item.html?id=439afad071eb4754903906aff1946719)  
**Metadata:** [FGDC-Compliant XML Metadata](https://www.arcgis.com/sharing/rest/content/items/439afad071eb4754903906aff1946719/info/metadata/metadata.xml?format=default&output=html)  
**Service Endpoint:** [ArcGIS REST Feature Service](https://services.arcgis.com/BLN4oKB0N1YSgvY8/arcgis/rest/services/Power_Outages_(View)/FeatureServer)  
**Maintained By:** Cal OES GIS Division (gis@caloes.ca.gov)  
**Update Frequency:** Automatically updated every 15 minutes (“as needed”)  
**Last Update:** August 19 2025 (4:57 PM CDT)  
**Access Level:** Public  
**License:** Custom — For situational awareness and emergency management use  

**Tags:** CalOES | Power Outage | ESF12 | PG&E | SCE | SDG&E | SMUD | PSPS | CAOpenData | Statewide Dataset  
---

### Overview
The **Cal OES Statewide Power Outages (View)** layer aggregates real-time outage information directly from California’s major utility public outage maps.  
It provides **current, not historical**, statewide outage visibility and supports emergency-operations dashboards.

#### Included Utilities
- **Pacific Gas and Electric (PG&E)**  
- **Southern California Edison (SCE)**  
- **San Diego Gas and Electric (SDG&E)**  
- **Sacramento Municipal Utility District (SMUD)**  

---

### Layers
| **Layer Name** | **Geometry Type** | **Description / Use** |
|----------------|------------------|------------------------|
| **Power Outage Incidents** | Point | Individual outage points from all utilities — shows approximate outage locations and drives dashboard totals. |
| **Power Outage Areas** | Polygon | Rough outage polygons from **PG&E only** — visually indicates affected zones; limited positional accuracy. |
| **Power Outages by County** | Polygon (summarized) | County-level aggregation of impacted customers; ideal for statewide visualization and analytics. |

---

### Purpose
Developed by Cal OES as part of the Emergency Support Function 12 (ESF-12) program, this dataset delivers real-time situational awareness of power disruptions across California to support emergency-management and response coordination.
The Cal OES — Statewide Power Outages (Real-Time) dataset captures live, event-based outage incidents updated hourly or more frequently, providing details such as Public Safety Power Shutoff (PSPS) events, start and end times, affected areas, and reported outage causes.
---

## Dataset Summary

| Metric | Description |
|--------|-------------|
| **File Name** | `CA_Power_Outages_Real_Time.csv` |
| **Rows** | 130 |
| **Columns** | 15 |
| **Numeric Columns** | 5 |
| **Categorical Columns** | 10 |
| **Datetime Columns** | 0 |
| **Update Frequency** | Hourly or more frequent |
| **Geographic Coverage** | California counties |
| **Temporal Range** | Current (real-time feed) |
| **Data Source** | Cal OES Power Outages Dashboard |

---

## Table Columns Overview

| Column Name | Data Type | Missing Values | Unique Values | Description |
|--------------|------------|----------------|----------------|--------------|
| OBJECTID | int64 | 0 | 130 | Unique record identifier for each outage event. |
| UtilityCompany | object | 0 | 3 | Name of the utility provider (e.g., PG&E, SCE, SDG&E). |
| Start Date/Time | object | 0 | 108 | Outage start timestamp (event initiation time). |
| Estimated Restoration Date/Time | object | 12 | 40 | Estimated time when service will be restored. |
| Cause | object | 36 | 19 | Outage cause such as **Weather**, **PSPS**, **Equipment Failure**, or **Maintenance**. |
| Impacted Customers | int64 | 0 | 41 | Number of customers affected during the outage. |
| County | object | 0 | 35 | California county where the outage occurred. |
| Outage Status | object | 0 | 1 | Indicates active or resolved outage status (most are Active). |
| Outage Type | object | 0 | 2 | Outage classification (e.g., **PSPS**, **Unplanned**). |
| GlobalID | object | 0 | 130 | Global unique identifier assigned to the record. |
| OutageTypeColor | object | 0 | 2 | Color code used for map visualization by outage type. |
| OutageStatusColor | float64 | 130 | 0 | Color code for outage status (unused or missing). |
| Indicent ID | object | 0 | 130 | Unique incident identifier (same as event ID in mapping interface). |
| x | float64 | 0 | 126 | Longitude coordinate for mapping. |
| y | float64 | 0 | 126 | Latitude coordinate for mapping. |

---

## Data Dictionary

| Field | Definition | Example | Analytical Role |
|--------|-------------|----------|-----------------|
| **OBJECTID** | Unique row identifier for each outage record. | 123 | Primary Key |
| **UtilityCompany** | Electric utility responsible for the service area. | “Pacific Gas & Electric” | Predictor (categorical) |
| **Start Date/Time** | Outage start timestamp (local time). | “2025-10-08 14:30” | Temporal feature |
| **Estimated Restoration Date/Time** | Predicted restoration time, if available. | “2025-10-08 20:00” | Used to calculate outage duration |
| **Cause** | Cause or trigger of outage. | “Weather – High Winds” | Predictor |
| **Impacted Customers** | Number of customers affected. | 2,150 | Indicator (dependent variable) |
| **County** | County where event occurred. | “Los Angeles” | Spatial variable |
| **Outage Status** | Indicates if outage is active/resolved. | “Active” | Categorical flag |
| **Outage Type** | Classification such as “PSPS” or “Unplanned.” | “PSPS” | Predictor |
| **GlobalID** | Global unique identifier for record traceability. | “b7ef3a…fa34” | Metadata |
| **OutageTypeColor** | Color code used for map visualization. | “#E6194B” | Visualization |
| **OutageStatusColor** | Color code for outage status (may be null). | — | Visualization |
| **Indicent ID** | Incident identifier associated with outage. | “CAOES-202510081430” | Linking variable |
| **x** | Longitude (EPSG:4326). | −121.23 | GIS spatial coordinate |
| **y** | Latitude (EPSG:4326). | 38.95 | GIS spatial coordinate |

---

## Summary of Indicators and Predictors

### Indicators (Dependent Variables)
These measure the **outcome or impact** of outage events and are targets for prediction:
- `Impacted Customers` — magnitude of outage impact  
- Outage duration — calculated as *(Estimated Restoration − Start Date/Time)*  
- Outage frequency per county or utility  
- Outage Type distribution (PSPS vs. unplanned)

### Predictors (Independent Variables)
Features that can explain or forecast outage behavior:
- `UtilityCompany` — organizational or operational driver  
- `County` — geographic risk exposure  
- `Cause` — type of initiating factor (weather, PSPS, maintenance)  
- `Start Date/Time` — time-based pattern (seasonal, diurnal)  
- `x`, `y` — geospatial position for mapping and clustering  
- `Estimated Restoration Date/Time` — proxy for outage duration  
- **External joins:** Weather data (temperature, wind, precipitation), wildfire incidents, and EAGLE-I historical outage trends

---

## Data Access and Citation

**Source:** [Cal OES Power Outages Dashboard](https://www.caloes.ca.gov/)  
**Public Dataset:** `CA_Power_Outages_Real_Time.csv`  
**Integration Reference:** EAGLE-I Dataset (DOE CESER / ORNL) — [DOI:10.6084/m9.figshare.24237376](https://doi.org/10.6084/m9.figshare.24237376)  
**Reference Publication:** Brelsford, C. *et al.* (2024). *Scientific Data*, 11, 271. DOI: [10.1038/s41597-024-03095-5](https://doi.org/10.1038/s41597-024-03095-5)


### Limitations
- **No historical archive.** Represents *only* the most recent outage snapshot at any given time.  
- **Accuracy varies by utility.** PG&E polygon data is approximate; other utilities report only point data.  
- **Operational use only.** Intended for awareness, not for certified counts of affected customers.  
- **Continuous updates.** Each refresh overwrites the previous feed; researchers must log or cache data for time-series analysis.

---

### Spatial Domain
- **Extent:** California statewide (≈ 31.69° N – 42.61° N, –125.18° W – –113.63° W)  
- **Coordinate System:** WGS 84  
- **Bounding Counties:** All 58 California counties  

---

### Citation
Brelsford, C., et al. (2025). *Statewide Power Outages (Public View)* [Data set].  
California Governor’s Office of Emergency Services (Cal OES).  
Available at: [https://www.arcgis.com/home/item.html?id=439afad071eb4754903906aff1946719](https://www.arcgis.com/home/item.html?id=439afad071eb4754903906aff1946719)

 
