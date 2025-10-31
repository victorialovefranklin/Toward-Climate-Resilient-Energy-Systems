# Installation Guide — California Outage–Environment–Equity Digital Twin

**Author:** Vicky Love Franklin  
**Institution:** Meharry Medical College — School of Applied Computational Sciences  
**Project:** California Outage–Environment–Equity Digital Twin  
**Focus:** GIS • Smart Grid • Machine Learning • Climate & Equity Modeling  

---
**File:** install_all_dependencies.py 
## Purpose

This installation guide provides everything needed to set up the environment for the  
**California Outage–Environment–Equity Digital Twin** project — a geospatial and predictive modeling system integrating outage, climate, and socio-environmental data across California.

The setup script installs all dependencies required for:
- Data ingestion (local and API)
- Geospatial and raster analysis
- Machine learning and forecasting
- LLM / RAG natural language querying
- Visualization and dashboarding
- Development, testing, and quality assurance

---

### What the Script Does

1. Upgrades `pip` to the latest version  
2. Installs all grouped dependencies (Core, GIS, ML, RAG, etc.)  
3. Displays progress for each package  
4. Prints a summary of successes and failures  
5. Suggests retry commands for any failed installs  

---

# Step-by-Step Setup

# Dependency Groups 
| Group                           | Description                           | Example Packages                                                          |
| ------------------------------- | ------------------------------------- | ------------------------------------------------------------------------- |
| **Minimal Core**                | Core data handling, I/O, utils        | `pandas`, `numpy`, `pyarrow`, `requests`, `tqdm`                          |
| **Geospatial**                  | Mapping & vector processing           | `geopandas`, `shapely`, `pyproj`, `fiona`, `rtree`, `contextily`          |
| **Raster / Climate (Optional)** | PRISM, ERA5, or NetCDF file support   | `xarray`, `rioxarray`, `rasterio`, `cfgrib`, `netCDF4`                    |
| **Machine Learning**            | Predictive & regression models        | `scikit-learn`, `xgboost`, `lightgbm`, `statsmodels`                      |
| **Forecasting**                 | Short-term / long-term forecasting    | `pmdarima`, `prophet`, `cmdstanpy`                                        |
| **Visualization / App**         | Charts, dashboards, GIS visualization | `matplotlib`, `plotly`, `streamlit`, `pydeck`, `altair`                   |
| **API Helpers**                 | REST, retry logic, AQS API            | `pyaqsapi`, `urllib3`, `tenacity`                                         |
| **RAG / LLM**                   | Natural-language & AI augmentation    | `openai`, `langchain`, `llama-index`, `chromadb`, `faiss-cpu`, `tiktoken` |
| **Development / Testing**       | Dev utilities & code formatting       | `ipykernel`, `black`, `ruff`, `pytest`, `colorama`                        |


----

pandas>=2.2,<3.0
numpy>=1.26,<3.0
pyarrow>=17.0.0
requests>=2.32
tqdm>=4.66
python-dateutil>=2.9
xarray>=2024.7.0
rioxarray>=0.15.5
rasterio>=1.3.9
netCDF4>=1.7
cfgrib>=0.9.10.4
geopandas>=0.14,<1.0
shapely>=2.0,<3.0
pyproj>=3.6
fiona>=1.9
rtree>=1.3.0
contextily>=1.6
scikit-learn>=1.4,<2.0
xgboost>=2.1,<3.0
lightgbm>=4.3
statsmodels>=0.14
pmdarima>=2.0
prophet>=1.1.5
cmdstanpy>=1.2
matplotlib>=3.9
plotly>=5.24
streamlit>=1.39
pydeck>=0.9
altair>=5.3
pyaqsapi>=0.0.9
urllib3>=2.2
tenacity>=9.0
openai>=1.51
tiktoken>=0.7
langchain>=0.2
llama-index>=0.11
chromadb>=0.5
faiss-cpu>=1.8
unstructured>=0.15
tabulate>=0.9
ipykernel>=6.29
black>=24.8.0
ruff>=0.6
pytest>=8.3
colorama>=0.4.6
