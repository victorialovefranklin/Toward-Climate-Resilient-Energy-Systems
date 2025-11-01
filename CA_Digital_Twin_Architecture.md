# Architectural Plan for Data Ingestion, Integration, and Machine Learning

**Author:** Vicky Love Franklin, Ph.D.

**Affiliation:** Meharry Medical College, School of Applied Computational Sciences

**Email:** victoria.franklin@mmc.edu

**LinkedIn:** linkedin.com/in/victorialovefranklin

**GitHub:** github.com/victorialovefranklin

**Project Focus:** Resilient Infrastructure, Environmental Intelligence, and Health Equity Modeling

**Overview:** This repository builds a GIS-enabled Digital Twin integrating power-outage, wildfire, weather, air-quality, and social-equity data for predictive resilience analytics across California.
The workflow separates data ingestion, staging, feature engineering, and machine-learning modeling for transparency and reproducibility. 


# The system supports:
- **Outage prediction** using machine-learning (RF, XGB, SVR, MLP, ARIMA, LSTM)  
- **Short- and long-term forecasting** with error/performance assessments  
- **Streamlit dashboards** for interactive GIS and trend visualization  
- **RAG-enabled LLM analysis** for natural-language interpretation of datasets
---

![System Architecture](CA_Digital_Twin_Architecture.png)
 
# Installation: Core Dependencies
| Group                    | Packages                                                  |
| ------------------------ | --------------------------------------------------------- |
| **Core Data**            | pandas • numpy • pyarrow • requests • tqdm                |
| **Geospatial**           | geopandas • shapely • pyproj • fiona • rtree • contextily |
| **Modeling**             | scikit-learn • xgboost • statsmodels • pmdarima • prophet |
| **Visualization**        | matplotlib • plotly • streamlit • pydeck                  |
| **LLM / RAG (optional)** | openai • langchain • llama-index • chromadb • faiss-cpu   |


# Pipeline Modules
| **Module**                 | **Purpose**                                       | **Key Tasks**                                                                                                                                                                                   | **Inputs (Local Only)**                          | **Output**                                                                              |
| -------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **ingest_local.py**        | Load & standardize **local CSV / shapefile data** | Read and normalize EAGLE-I, EIA-861, PRISM, NOAA StormEvents, CAL FIRE, PSPS, Real-Time/Planned Incidents, CES 4.0, HUD, CalEPA/OEHHA, AQS Ozone & PM (2014–2025), County shapefile & crosswalk | `/content/*.csv`, `/content/tl_2023_us_county.*` | `/staging/*.parquet`                                                                    |
| **staging_to_features.py** | Merge **local staging data** into feature tables  | Aggregate by `year`, `month`, and `fips`; derive lags (1, 3, 6, 12 months); handle missing values                                                                                               | `/staging/*.parquet`                             | `/features/state_monthly_features.parquet`  `/features/county_monthly_features.parquet` |
| **train_models.py**        | Train + compare machine-learning models           | Random Forest, XGBoost (if available), SVR, MLP, KNN; temporal 60/40 split; compute metrics & feature importances                                                                               | `/features/*.parquet`                            | `/models/model_results_state.csv`  `/models/model_results_county.csv`                   |
| **rag_answer.py**          | LLM + RAG over **local metadata**                 | Retrieve & cite dataset sources (local cards / READMEs); generate Markdown answers with citations                                                                                               | `/staging_meta/*.json`, local docs               | Markdown answers + citations                                                            |


**Validation & Forecasting Metrics**
| **Metric**   | **Meaning**                    |
| ------------ | ------------------------------ |
| **RMSE**     | Root Mean Squared Error        |
| **MAE**      | Mean Absolute Error            |
| **R²**       | Coefficient of Determination   |
| **MAPE (%)** | Mean Absolute Percentage Error |


**Predictive Model Design**
| **Horizon**             | **Algorithms**               | **Validation & Metrics**                   | **Description**                                                                   |
| ----------------------- | ---------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------- |
| **Short-Term (1–3 mo)** | LR, RF, SVR, KNN, MLP, ARIMA | RMSE, MAE, R², MAPE (60/40 temporal split) | Operational forecasting of near-term outage risk, intensity, and customer impact. |
| **Long-Term (6–12 mo)** | RF, XGB, MLP, ARIMA, LSTM    | RMSE, MAE, R², MAPE (rolling holdout)      | Strategic modeling of seasonal/climate and infrastructure resilience trends.      |


**Validation:**
- Time-series holdout (temporal split).
- Transferability tests across counties / time windows.
- Forecasting Error Analysis:
- Cross-model comparison.
- Feature importance & SHAP interpretation.

# Modeling Design Summary
| **Goal**                                               | **Approach**                           |
| ------------------------------------------------------ | -------------------------------------- |
| Predict outage magnitude / duration                    | Regression (Random Forest, XGBoost)    |
| Classify outage cause (weather vs policy vs equipment) | Multiclass classification              |
| Interpret key drivers                                  | SHAP + Permutation Importance          |
| Forecast resilience scenarios                          | Prophet / ARIMA time-series extensions |


# Target Variables:
**outage_count, customer_weighted_hours, event_duration**
**Feature Families** 
- Meteorological: NOAA StormEvents, PRISM Norms
- Wildfire: CAL FIRE, Post-Fire Dataset
- Air Quality: EPA AQS (Ozone & PM 2014–2025)
- Socio-Economic: CalEnviroScreen 4.0, HUD LAI
- Policy: PSPS, Planned vs Unplanned Outages
  

# Data Refresh Cadence
| **Source**                     | **Update Cycle**      | **Method**                        |
| ------------------------------ | --------------------- | --------------------------------- |
| EAGLE-I / EIA-861              | Annual                | Local CSV refresh                 |
| CAL FIRE Incidents             | Annual / Quarterly    | Local CSV (from internal archive) |
| NOAA Storm Events              | Quarterly             | FTP batch CSV (CA subset)         |
| PRISM Norms                    | Static (30-yr)        | Local CSV                         |
| EPA AQS (Ozone & PM 2014–2025) | Periodic (as updated) | Local CSV upload                  |
| CalEnviroScreen 4.0            | Static / Periodic     | Local CSV                         |
| HUD LAI v3                     | Annual                | Local CSV                         |
| CalEPA / OEHHA                 | Static                | Local CSV                         |
| County Shapefiles & Crosswalks | Static                | Local shapefile + CSV join        |



# Development Conventions
| **Aspect**          | **Standard**                                                |
| ------------------- | ----------------------------------------------------------- |
| **Language**        | Python 3.12 +                                               |
| **Core Libraries**  | `pandas`, `geopandas`, `scikit-learn`, `xgboost`, `prophet` |
| **Visualization**   | `matplotlib`, `plotly`, `streamlit`, `leafmap`              |
| **Data Formats**    | CSV ↔ Parquet ↔ GeoJSON ↔ Shapefile                         |
| **Version Control** | Git LFS for > 50 MB files                                   |
| **Environment**     | `.env` for paths only (no API keys needed in local mode)    |



# Machine-Learning Outputs
| **Artifact**                     | **Contents**                 | **Example Use**        |
| -------------------------------- | ---------------------------- | ---------------------- |
| `model_results_state.csv`        | RMSE, MAE, R² for each model | Model comparison table |
| `feature_importance_RF.csv`      | SHAP + Permutation scores    | Interpretability plots |
| `forecast_outage_trends.csv`     | 12-month forecasts           | Dashboard integration  |
| `state_monthly_features.parquet` | Unified training feature set | Reproducible ML inputs |



# Digital Twin Architecture Plan (Two Horizons: Short-Term + Long-Term)
| **Layer / Module**                | **Purpose**                           | **Key Inputs**                                      | **Core Process / Methods**                    | **Outputs & Artifacts**               | **Update Cadence** | **Metrics (QoS + Model)**      | **Owner / Role**    | **Notes**                              |
| --------------------------------- | ------------------------------------- | --------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------ | ------------------------------ | ------------------- | -------------------------------------- |
| **Data Ingestion (ETL)**          | Load & validate local files           | EAGLE-I, NOAA, PRISM, CAL FIRE, PSPS, EIA-861, SDOH | Batch load; schema enforcement; file tracking | `/data/raw/*`, logs                   | Monthly            | Pipeline success %, latency    | Data Engineering    | Use schema contracts + version hashes  |
| **Data Quality (DQ)**             | Validate and cleanse                  | Raw staging files                                   | Null / dup checks, range tests, spatial joins | `/data/clean/*`, DQ reports           | Each ingest        | % valid rows, rule pass rate   | Data Eng + QA       | Archive DQ reports for audit           |
| **Feature Store**                 | Shared feature repository             | Cleaned parquet tables                              | Monthly aggregations, lags, rolling stats     | `/features/{level}/{horizon}.parquet` | Monthly            | Feature freshness, drift (PSI) | MLOps               | Keep schema stable across horizons     |
| **Short-Term Modeling (Ops)**     | 1–30 day forecasts                    | Weather, alerts, recent outages                     | ARIMA, RF, XGB, Prophet                       | `predictions_daily.parquet`           | Daily              | RMSE, MAE, alert precision     | Data Sci (Ops)      | Core operational risk model            |
| **Long-Term Modeling (Strategy)** | 6–12 mo+ resilience projections       | Aggregates + policy covariates                      | XGB / RF scenario models, Monte Carlo         | `projections_annual.parquet`          | Quarterly          | RMSE, R², scenario spread      | Data Sci (Strategy) | Tie to planning & investment decisions |
| **Simulation & What-If**          | Test policy or infra changes          | Models + user inputs                                | Counterfactual simulation / CBA               | `sim_runs/*.parquet`                  | On demand          | Benefit-cost ratio (BCR)       | Analytics Eng       | Keep first iteration simple            |
| **Geospatial Services**           | Spatial risk mapping                  | Features + county/tract shapes                      | Hotspot / clustering maps                     | Vector tiles + GeoJSON                | With predictions   | Tile build time, map latency   | GIS Eng             | Pre-compute heavy tiles                |
| **Dashboards (Ops)**              | Real-time situational awareness       | Short-term preds + alerts                           | Streamlit UI with SHAP drivers                | Web app + PDF brief                   | Daily              | Uptime, lead time              | Prod Eng + Ops      | ≤ 3 core charts per view               |
| **Dashboards (Strategy)**         | Long-term planning view               | Scenarios + equity layers                           | Trend panels + scenario toggles               | Web app + quarterly brief             | Quarterly          | ROI of actions, decision use   | Prod Eng + Planning | Connect to budget planner              |
| **Alerting & Workflow**           | Turn predictions into actions         | Short-term alerts / thresholds                      | Rules engine + ticketing                      | Alerts + logs                         | Near-real-time     | False alarm rate, ack time     | Ops                 | Start simple; iterate                  |
| **MLOps & Governance**            | Ensure reproducibility & traceability | Code + data + models                                | Registry + CI/CD + lineage tracking           | Versioned artifacts + audit logs      | Continuous         | Drift (PSI), rollback time     | MLOps               | Enforce review / approval gates        |
| **Security & Compliance**         | Protect data access                   | All components                                      | IAM, encryption, audit logs                   | Access policies + KMS keys            | Continuous         | Violations, key rotation       | SecOps              | Apply least privilege                  |
| **Documentation & RACI**          | Shared understanding                  | All teams                                           | READMEs, runbooks, RACI matrix                | `/docs/*`, wiki                       | Continuous         | Doc freshness, handoff rate    | PMO                 | Update each release                    |

 
# Deployment Vision
| **Component**            | **Description**                                             |
| ------------------------ | ----------------------------------------------------------- |
| **Streamlit Dashboard**  | Interactive GIS maps + ML trend summaries                   |
| **GitHub Actions CI/CD** | Automate model training + artifact publishing               |
| **Data Exports**         | County / State GeoJSON for public dashboards                |
| **LLM Integration**      | Local RAG assistant for interpreting outputs with citations |


