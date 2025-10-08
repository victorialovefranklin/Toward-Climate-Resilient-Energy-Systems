 ## Cal OES — Statewide Power Outages Dataset 

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

 
