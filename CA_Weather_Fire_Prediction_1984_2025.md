# California Weather and Fire Prediction Dataset (1984–2025) with Engineered Features  

---

## About the Dataset  

This dataset is a comprehensive compilation of **daily weather observations and wildfire ignition data** across California over the period **1984–2025**, enriched with **engineered features** designed to support predictive modeling of fire occurrence. :contentReference[oaicite:0]{index=0}  

It integrates meteorological data (e.g. precipitation, temperature, wind) from NOAA with **CAL FIRE wildfire incident records**, producing derived features such as temperature range, wind–temperature ratios, and lagged cumulative precipitation. :contentReference[oaicite:1]{index=1}  

This dataset is released under a **Creative Commons Attribution 4.0 International (CC-BY 4.0)** license. :contentReference[oaicite:2]{index=2}  

---

## Purpose  

The dataset is intended to facilitate:

- **Wildfire ignition prediction** based on weather and climate signals  
- **Climate–fire relationship studies** over multidecadal timescales  
- **Benchmarking predictive models** (e.g. Random Forest, XGBoost, neural nets)  
- **Operational early-warning tools** for fire management agencies  
- **Feature engineering experiments** using lagged and derived meteorological indicators  

---

## Citation & Provenance  

**Produced by:**  
Cemil Emre Yavas (Contact), Christopher Kadlec, Jongyeop Kim, Lei Chen :contentReference[oaicite:3]{index=3}  

**Published:** January 21, 2025 (version v1) :contentReference[oaicite:4]{index=4}  
**DOI / Link:** [10.5281/zenodo.14712845](https://doi.org/10.5281/zenodo.14712845) :contentReference[oaicite:5]{index=5}  
**File:** `CA_Weather_Fire_Dataset_1984-2025.csv` (≈ 1.5 MB) :contentReference[oaicite:6]{index=6}  

---

## Dataset Summary  

- **Temporal range:** 1984 to 2025 (daily resolution) :contentReference[oaicite:7]{index=7}  
- **Coverage:** entire state of California  
- **Feature types:** raw meteorological observations + engineered predictors + fire-ignition indicator  

---

## Data Columns  

The dataset includes the following columns:

| Field | Type | Description |
|---|---|-------------|
| `DATE` | date | Observation date |
| `PRECIPITATION` | numeric | Daily precipitation (inches) |
| `MAX_TEMP` | numeric | Daily maximum temperature (°F) |
| `MIN_TEMP` | numeric | Daily minimum temperature (°F) |
| `AVG_WIND_SPEED` | numeric | Daily average wind speed (mph) |
| `FIRE_START_DAY` | binary / logical | Whether a wildfire ignition occurred that day |
| `YEAR` | integer | Year component of the date |
| `TEMP_RANGE` | numeric | `MAX_TEMP – MIN_TEMP` (daily temperature variation) |
| `WIND_TEMP_RATIO` | numeric | `AVG_WIND_SPEED / MAX_TEMP` |
| `MONTH` | integer | Month number (1–12) |
| `SEASON` | categorical | Season label (Spring, Summer, Fall, Winter) |
| `LAGGED_PRECIPITATION` | numeric | Sum of precipitation over preceding 7 days |
| `LAGGED_AVG_WIND_SPEED` | numeric | Mean wind speed over preceding 7 days |
| `DAY_OF_YEAR` | integer | Day index within year (1–365/366) |

These engineered fields help capture temporal context, seasonal cycles, and cumulative conditions relevant to fire risk. :contentReference[oaicite:8]{index=8}  

---

## Data Dictionary  

| Field | Units / Format | Example | Role in Modeling |
|---|----------------|---------|-------------------|
| DATE | YYYY-MM-DD | 2005-08-14 | Index / time axis |
| PRECIPITATION | inches | 0.12 | Moisture predictor |
| MAX_TEMP | °F | 96.5 | Heat stress predictor |
| MIN_TEMP | °F | 60.2 | Baseline temperature |
| AVG_WIND_SPEED | mph | 5.7 | Wind-driven desiccation |
| FIRE_START_DAY | 0 / 1 boolean | 1 | Target variable (ignition event) |
| YEAR | integer | 2005 | Trend / drift control |
| TEMP_RANGE | °F | 36.3 | Diurnal variation indicator |
| WIND_TEMP_RATIO | unitless | 0.059 | Combined wind–heat stress metric |
| MONTH | 1–12 | 8 | Seasonal feature |
| SEASON | string | “Summer” | Categorical seasonal label |
| LAGGED_PRECIPITATION | inches | 0.35 | Recent moisture memory |
| LAGGED_AVG_WIND_SPEED | mph | 4.2 | Recent wind trends |
| DAY_OF_YEAR | 1–365 | 226 | Ordinal time within year |

---

## Summary of Indicators & Predictors  

### Indicator / Target  
- `FIRE_START_DAY` — binary indicator whether a wildfire ignition occurred on that date (1 = yes, 0 = no)  

### Predictors / Features  
Meteorological and engineered features used to predict ignition risk:

- **Raw predictors:**  
  - `PRECIPITATION`  
  - `MAX_TEMP`, `MIN_TEMP`  
  - `AVG_WIND_SPEED`  

- **Engineered features:**  
  - `TEMP_RANGE` (heat variability)  
  - `WIND_TEMP_RATIO` (wind relative to heat)  
  - `LAGGED_PRECIPITATION` (preceding moisture)  
  - `LAGGED_AVG_WIND_SPEED` (prevailing wind)  
  - `MONTH`, `SEASON`, `DAY_OF_YEAR` (temporal cycles)  
  - `YEAR` (trend / secular drift)

These predictors aim to capture both immediate and memory (lagged) influences on fire ignition probability.

---
