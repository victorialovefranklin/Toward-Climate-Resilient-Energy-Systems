# California Power Outage GIS Digital Twin & Smart Grid Prediction Study

**Author:** Victoria Love Franklin
**Institution:** Meharry Medical College, School of Applied Computational Sciences  
**Focus Area:** Data Science • GIS • Smart Grid • Climate Resilience • AI Modeling

---

## Overview
This project integrates **NOAA Storm Events**, **DOE EAGLE-I outage data**, and **smart grid / digital twin datasets** to model **power outage probability, duration, and resilience** across California (2010–2024).
We apply **machine learning**, **GIS spatial analysis**, and **digital twin modeling** to understand how weather events, infrastructure age, and smart grid technologies influence **outage frequency**, **restoration time**, and **community vulnerability**.

---

## Research Objectives

- Build predictive models for **outage frequency and duration** using meteorological and infrastructure data.  
- Develop a **Digital Twin framework** to simulate and optimize grid resilience.  
- Perform **spatial hotspot and vulnerability analysis** using GIS and SDOH indicators.  
- Evaluate how **smart grid and AMI technologies** reduce outage severity and restoration time.  
- Assess **environmental equity** by linking outage exposure with socioeconomic and health vulnerability indices.

---

## Datasets

| **Dataset Name**                                         | **Description**                                          | **Years**  | **Source**                 |
|----------------------------------------------------------|----------------------------------------------------------|-----------:|----------------------------|
| `ca_stormevents_county_month_eventtype_2010_2024.csv`    | Monthly storm events by county and event type            | 2010–2024 | NOAA NCEI Storm Events     |
| `ca_stormevents_eventtype_summary_2010_2024.csv`         | Summary of storm event types and severity                | 2010–2024 | NOAA NCEI                  |
| `EAGLE-I Power Outage Dataset`                           | Real-time outage events (customers, duration, cause)     | 2014–2024 | DOE CESER                  |
| `EIA-861 Service Territory Data`                         | Utility customer bases and sectoral load data            | 2010–2024 | U.S. EIA                   |
| `FEMA Disaster Declarations`                             | Economic & infrastructure losses from declared disasters | 2010–2024 | FEMA Open Data             |
| `EPA AQS PM2.5 & O₃`                                     | Ambient air quality measurements                        | 2010–2024 | U.S. EPA AQS               |
| `CalEnviroScreen` & `CDC SVI`                            | Community-level vulnerability indices (SDOH)             | 2010–2024 | CalEPA, CDC                |
| `CalFire Incident Archive`                               | Wildfire ignition and containment records                | 2010–2024 | CalFire                    |
| `USDA CropScape`                                         | Crop distribution and agricultural losses                | 2010–2024 | USDA NASS                  |

---

## Data Dictionary

### Storm & Weather Variables

| **Variable**                              | **Purpose / Description**                               | **Possible Correlative Datasets**     | **Potential Analysis / Use Case**                               | **Data Source**  |
|-------------------------------------------|----------------------------------------------------------|----------------------------------------|------------------------------------------------------------------|------------------|
| `year`                                    | Annual trends in severe weather                          | NOAA NCEI, CalFire, DOE CESER          | Temporal trend analysis; YoY comparisons                         | NOAA NCEI        |
| `month`                                   | Seasonal variability of storm events                     | EIA-861, EPA AQS                       | Monthly climatology; weather–energy interactions                 | NOAA NCEI        |
| `county`                                  | County-level geographic linkage                          | FIPS shapefiles, SVI, CalEnviroScreen  | Spatial mapping; equity-based vulnerability assessment           | NOAA + US Census |
| `event_type`                              | Storm type (flood, wildfire, high wind, etc.)            | CalFire, PSPS, EAGLE-I                 | Correlate event types with outages or wildfire ignition          | NOAA Storm Events|
| `event_count`                             | Frequency of events by month/county                      | DOE-417, EIA-861                       | Frequency comparison; reliability stress testing                 | NOAA NCEI        |
| `fatalities_direct`, `fatalities_indirect`| Human impact (mortality)                                 | CDC WONDER, NCHS                       | Public health correlation; disaster mortality risk               | NOAA + CDC       |
| `injuries_direct`, `injuries_indirect`    | Morbidity impact                                         | HCUP CA                                 | Injury prevalence & severity assessment                          | NOAA + HHS       |
| `damage_property`                         | Economic loss from property damage (USD)                 | FEMA, EAGLE-I, CalOES                  | Cost modeling; loss forecasting; insurance risk analytics        | NOAA + FEMA      |
| `damage_crops`                            | Agricultural impact (USD)                                | USDA CropScape                         | Climate–agriculture impact modeling                              | NOAA + USDA      |
| `fips`                                    | County-level identifier for joins                        | EIA-861, DOE CESER                      | Geospatial joins; weather–grid resilience correlation            | US Census        |
| `lat`, `lon`                              | Event geolocation                                        | MODIS/VIIRS, NLDAS, PRISM              | Spatial clustering; regression kriging; Moran’s I; Getis-Ord Gi* | NOAA + NASA      |
| `event_duration_hours`                    | Duration of storm event                                  | EAGLE-I time series                    | Duration–impact correlation; outage duration vs. event type      | NOAA + DOE       |
| `storm_magnitude_index` *(derived)*       | Composite severity (freq × duration × loss)              | EPA AQS, DOE-417                       | Climate resilience severity index                                | Derived          |

---

### Power Outage & Smart Grid Variables

| **Variable**                         | **Purpose / Description**                                      | **Correlative Dataset(s)**      | **Potential Analysis / Use Case**                                         |
|-------------------------------------|-----------------------------------------------------------------|----------------------------------|----------------------------------------------------------------------------|
| `county_fips`                       | County identifier for spatial analysis                          | Census, SVI                      | Outage hotspot mapping; vulnerability overlay                             |
| `event_datetime`                    | Timestamp of outage/grid event                                  | NOAA Weather Data                | Time alignment & lag correlation with storms                              |
| `outage_duration_hours`             | Length of outage event                                          | OMS, Asset Records               | Regression to predict duration given causes & infrastructure status       |
| `number_customers_affected`         | Scale of population affected                                     | EIA-861, ACS                     | Risk & exposure modeling; population-weighted metrics                      |
| `cause_code`                        | Outage cause (vegetation, weather, equipment)                   | Vegetation GIS, CalFire          | Classification of causes driving severe/long outages                      |
| `asset_age_years`                   | Age of grid asset (pole, transformer, feeder)                   | Utility GIS                      | Predictive maintenance; failure risk vs. age                               |
| `feeder_load_mw`                    | Load on feeder at event time                                    | Smart meter / AMI                | Load-stress modeling; capacity constraints                                 |
| `gis_lat`, `gis_lon`                | Outage geolocation                                              | Terrain & vegetation layers      | Geospatial clustering; risk-zone mapping                                   |
| `weather_wind_mph`, `weather_precip_mm` | Weather metrics at outage time                                | NOAA stations/satellite          | Multivariate features for outage probability & duration forecasting        |
| `smart_grid_feature_count`          | Count of smart devices (sensors/switches)                       | Utility tech deployment logs     | Evaluate digital readiness & impact on outage mitigation                   |
| `digital_twin_status`               | Digital twin active for asset/region (0/1)                      | IT/OT Registry                   | A/B comparisons: twin vs. non-twin regions                                 |
| `restoration_time_hours`            | Time from detection to restoration completion                   | Crew dispatch logs, OMS          | Workflow optimization; factors delaying restoration                        |
| `socioeconomic_vulnerability_index` | Composite SDOH vulnerability score                              | ACS, CalEnviroScreen             | Equity analysis: disproportionate burden detection                          |
| `smart_meter_density_per_km2`       | Smart meter deployment density                                  | AMI data                         | Detection speed & restoration improvements                                 |
| `renewable_generation_mw`           | Local renewable generation capacity                              | DER interconnections             | Relationship between DER penetration and resilience                         |

---

## Dataset Correlations

| **Storm Dataset Variable**           | **Correlate With**            | **Expected Insight**                                        |
|-------------------------------------|-------------------------------|-------------------------------------------------------------|
| `event_type`, `event_count`         | DOE EAGLE-I Power Outages     | Impact of specific storm types on grid reliability          |
| `damage_property`                   | FEMA Disaster Cost Data       | Relationship between storm magnitude and disaster costs     |
| `fatalities_*`, `injuries_*`        | CDC WONDER / Hospitalizations | Health burden of climate hazards                            |
| `month`, `event_type`               | EPA AQS PM2.5 & O₃            | Air quality deterioration during/after storm events         |
| `county`, `damage_crops`            | USDA Crop Loss Reports        | Agricultural vulnerability by climate region                |
| `lat`, `lon`                        | MODIS Fire Radiative Power    | Weather–wildfire interaction mapping                        |

---

## Planned Analyses
1. **GIS Hotspot Mapping** — Identify outage clusters using Moran’s I and Getis-Ord Gi*.  
2. **Time-Series Forecasting** — ARIMA/Prophet/XGBoost to forecast outage probability & duration.  
3. **Predictive Maintenance** — Failure-risk models using asset age, load, vegetation, weather.  
4. **Digital Twin Impact** — Compare metrics (detection, duration, restoration) for twin vs. non-twin areas.  
5. **Equity & Vulnerability** — Link outage burden to CalEnviroScreen and CDC SVI indices.  
6. **Smart Grid Effectiveness** — Assess how AMI density & switching reduce outage duration.  
7. **Multivariate Modeling** — Classification (major/minor outage) and regression (restoration time).

---

## Citations
1. **NOAA NCEI** — Storm Events Database (2010–2024): https://www.ncei.noaa.gov/pub/data/swdi/stormevents  
2. **DOE CESER** — EAGLE-I Power Outage Data (2014–2024).  
3. **U.S. EIA** — Form EIA-861: Annual Electric Power Industry Report.  
4. **FEMA** — Disaster Declarations Summaries.  
5. **EPA AQS** — Ambient Monitoring Data (PM2.5, O₃).  
6. **CDC WONDER & NCHS** — Mortality and Population Data.  
7. **USDA NASS** — CropScape & Quick Stats Database.  
8. **CalEPA** — CalEnviroScreen 4.0.  
9. **U.S. Census Bureau** — ACS & FIPS Codes.  
10. **Gridworks (2024)** — PG&E Grid Modernization & Digital Twin Integration Report.

---

**Contact**
Vicky Love Franklin, Ph.D. Pre-Candidate 
Meharry Medical College — Nashville, TN
**LinkedIn:** https://www.linkedin.com/in/victorialovefranklin
