# Architectural Plan for Data Ingestion, Integration, and Machine Learning

**Author:** Vicky Love Franklin, Ph.D.

**Affiliation:** Meharry Medical College, School of Applied Computational Sciences

**Email:** victoria.franklin@mmc.edu

**LinkedIn:** linkedin.com/in/victorialovefranklin

**GitHub:** github.com/victorialovefranklin

**Project Focus:** Resilient Infrastructure, Environmental Intelligence, and Health Equity Modeling

**Overview:** This repository builds a GIS-enabled Digital Twin integrating power-outage, wildfire, weather, air-quality, and social-equity data for predictive resilience analytics across California.
The workflow separates data ingestion, staging, feature engineering, and machine-learning modeling for transparency and reproducibility.

 


                     +--------------------------+
                     |      API Connectors      |
                     |  (ODIN, FIRMS, WFIGS,   |
                     |   AQS, CalEnviroScreen)  |
                     +------------+-------------+
                                  |
                                  v
                     +--------------------------+
                     |   Local File Ingestion    |
                     | (EAGLE-I, EIA-861, PRISM,|
                     |  CES 4.0, HUD, Shapefiles)|
                     +------------+-------------+
                                  |
                                  v
                     +--------------------------+
                     |     Staging Layer         |
                     | Cleaned + normalized data |
                     +------------+-------------+
                                  |
                                  v
                     +--------------------------+
                     |  Feature Engineering      |
                     | Join API + local by       |
                     | county, month, sector     |
                     +------------+-------------+
                                  |
                                  v
                     +--------------------------+
                     | Machine-Learning Models   |
                     |  RF, XGB, SVR, MLP etc.  |
                     |  with metrics + SHAP      |
                     +------------+-------------+
                                  |
                                  v
                     +--------------------------+
                     | Visualization / Dashboards|
                     | Streamlit + GIS mapping   |
                     +--------------------------+

![System Architecture](docs/CA_Digital_Twin_Architecture.png)
 

/content/
├── data_local/              # static CSV & shapefile datasets
│   ├── core/                # EAGLE-I, PSPS, EIA-861
│   ├── weather_fire/        # PRISM, CAL FIRE, POST-FIRE
│   ├── equity/              # CES 4.0, 21 Indicators, HUD
│   └── reference/           # shapefiles, county crosswalk
│
├── data_api_raw/            # timestamped raw API pulls
├── staging/                 # normalized parquet/csv
├── features/                # modeling-ready feature tables
├── models/                  # metrics + artifacts
└── pipelines/
    ├── ingest_local.py
    ├── ingest_api.py
    ├── staging_to_features.py
    └── train_models.py

# Pipeline Modules

| **Module**               | **Purpose**                                                           | **Key Tasks**                                     | **Outputs**                                |
| ------------------------ | --------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------ |
| `ingest_local.py`        | Load and standardize static CSV/shapefile data                        | Read EAGLE-I, EIA, PRISM, CES 4.0 etc.            | `/staging/*.parquet`                       |
| `ingest_api.py`          | Fetch live data from ODIN, FIRMS, WFIGS, AQS and CalEnviroScreen APIs | Timestamped pulls → normalized format             | `/data_api_raw/` + `/staging/*.parquet`    |
| `staging_to_features.py` | Merge API + local data into monthly state/county feature tables       | Derive `year`, `month`, `fips`; aggregate metrics | `/features/state_monthly_features.parquet` |
| `train_models.py`        | Compare ML algorithms for outage prediction                           | Train RF, XGB, SVR, MLP with cross-validation     | `/models/model_results_state.csv`          |


# Modeling Design
| **Goal**                                               | **Approach**                          |
| ------------------------------------------------------ | ------------------------------------- |
| Predict outage magnitude / duration                    | Regression (RandomForest, XGBoost)    |
| Classify outage cause (weather vs policy vs equipment) | Multiclass classification             |
| Interpret feature importance                           | SHAP + Permutation Importance         |
| Forecast resilience scenarios                          | Prophet / ARIMA time-series extension |


# Target Variables:
outage_count, customer_weighted_hours, event_duration
**Feature Families:**
- Meteorological (NOAA, PRISM)
- Wildfire (CAL FIRE, FIRMS, POST-FIRE)
- Air Quality (EPA AQS)
- Socio-economic (CES 4.0, HUD)
- Policy (PSPS, Planned vs Unplanned)

# Data Refresh Cadence
| **Source**          | **Update Cycle**  | **Method**           |
| ------------------- | ----------------- | -------------------- |
| ODIN Outages        | Daily             | API pull             |
| WFIGS Incidents     | Daily             | ArcGIS REST → CSV    |
| NASA FIRMS          | Daily             | Area API (BBOX CA)   |
| EPA AQS             | Weekly            | API (batch state=06) |
| NOAA Storm Events   | Quarterly         | FTP download         |
| EAGLE-I / EIA-861   | Annual            | Local CSV refresh    |
| CalEnviroScreen 4.0 | Static / Periodic | CSV + ArcGIS API     |


# Development Conventions
- Language: Python 3.12+
- Core Libraries: pandas, geopandas, requests, scikit-learn, xgboost, prophet
- Visualization: matplotlib, plotly, streamlit, leafmap
- Data Formats: CSV ↔ Parquet ↔ GeoJSON ↔ Shapefile
- Version Control: Git LFS for large data assets (>50 MB)
- Environment: .env with API keys (AQS_API_KEY, AQS_EMAIL, FIRMS_MAP_KEY)

# Machine-Learning Outputs
| **Output Artifact**              | **Contents**                 | **Example Use**             |
| -------------------------------- | ---------------------------- | --------------------------- |
| `model_results_state.csv`        | RMSE, MAE, R² for each model | Model comparison table      |
| `feature_importance_RF.csv`      | SHAP values + ranking        | Interpretability plots      |
| `forecast_outage_trends.csv`     | 12-month forecasts           | Dashboard integration       |
| `state_monthly_features.parquet` | Unified feature set          | Reproducible training input |


# Deployment Vision
- Streamlit Dashboard: interactive maps + ML summaries
- GitHub Actions: automated daily API refresh and model retrain
- Data Export: County / State GeoJSON for public web visualizations
