#!/usr/bin/env python3
"""
install_all_dependencies.py
------------------------------------------------------
One-click installer for California Outage-Environment-Equity Digital Twin.
Installs all required packages for:
- Data ingestion (local + API)
- GIS + geospatial analysis
- ML + forecasting
- LLM / RAG + visualization
- Development utilities
"""

import subprocess
import sys
import platform
from typing import List, Tuple

def pip_install(pkgs: List[str]) -> Tuple[list, list]:
    success, failed = [], []
    for pkg in pkgs:
        print(f"🔹 Installing: {pkg}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
            success.append(pkg)
        except subprocess.CalledProcessError:
            print(f"❌ Failed: {pkg}")
            failed.append(pkg)
    return success, failed

def print_group_summary(title: str, ok: List[str], bad: List[str]):
    print(f"\n📦 {title} — summary")
    print("   ✅ Success:", len(ok))
    print("   ❌ Failed :", len(bad))
    if bad:
        print("   ↳ Retry with:\n      pip install " + " ".join(bad))

def main():
    print("\n🧭 Starting installation for all dependencies...\n")
    subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

    # ----- Minimal Core -----
    core = [
        "pandas>=2.2,<3.0",
        "numpy>=1.26,<3.0",
        "pyarrow>=17.0.0",
        "requests>=2.32",
        "tqdm>=4.66",
        "python-dateutil>=2.9",
        "urllib3>=2.2",
        "tenacity>=9.0",
    ]

    # ----- Geospatial (vector + basemap) -----
    # Wheels exist for these; if they fail, users may need system GEOS/PROJ/GDAL.
    geospatial = [
        "geopandas>=0.14,<1.0",
        "shapely>=2.0,<3.0",
        "pyproj>=3.6",
        "fiona>=1.9",
        "rtree>=1.3.0",
        "contextily>=1.6",
    ]

    # ----- Raster / Climate (optional but useful) -----
    # cfgrib requires ecCodes system lib in some environments.
    raster = [
        "xarray>=2024.7.0",
        "rioxarray>=0.15.5",
        "rasterio>=1.3.9",
        "netCDF4>=1.7",
        "cfgrib>=0.9.10.4",
    ]

    # ----- Machine Learning / Modeling -----
    ml = [
        "scikit-learn>=1.4,<2.0",
        "xgboost>=2.1,<3.0",
        "lightgbm>=4.3",
        "statsmodels>=0.14",
    ]

    # ----- Forecasting -----
    forecast = [
        "pmdarima>=2.0",
        "prophet>=1.1.5",
        "cmdstanpy>=1.2",
    ]

    # ----- Visualization + App -----
    viz = [
        "matplotlib>=3.9",
        "plotly>=5.24",
        "streamlit>=1.39",
        "pydeck>=0.9",
        "altair>=5.3",
    ]

    # ----- RAG / LLM -----
    rag = [
        "openai>=1.51",
        "tiktoken>=0.7",
        "langchain>=0.2",
        "llama-index>=0.11",
        "chromadb>=0.5",
        "faiss-cpu>=1.8",
        "unstructured>=0.15",
        "tabulate>=0.9",
    ]

    # ----- Development + Testing -----
    dev = [
        "ipykernel>=6.29",
        "black>=24.8.0",
        "ruff>=0.6",
        "pytest>=8.3",
        "colorama>=0.4.6",
    ]

    groups = [
        ("Core", core),
        ("Geospatial", geospatial),
        ("Raster/Climate", raster),
        ("ML/Modeling", ml),
        ("Forecasting", forecast),
        ("Visualization/App", viz),
        ("RAG/LLM", rag),
        ("Dev/Testing", dev),
    ]

    all_ok, all_bad = [], []

    for title, pkgs in groups:
        print(f"\n=== Installing: {title} ===")
        ok, bad = pip_install(pkgs)
        print_group_summary(title, ok, bad)
        all_ok.extend(ok); all_bad.extend(bad)

    # Final summary
    print("\n✅ Installation Summary (ALL GROUPS)")
    print("===================================")
    print(f"✅ Successful: {len(all_ok)} packages")
    print(f"❌ Failed    : {len(all_bad)} packages\n")
    if all_bad:
        print("⚠️ The following packages failed to install:")
        for pkg in all_bad:
            print(f"   - {pkg}")
        print("\nTips:")
        print(" • If geopandas/fiona/rtree fail, install system GEOS/PROJ/GDAL or use Conda:")
        print("     conda create -n ca-twin python=3.11 geopandas rtree fiona pyproj -c conda-forge")
        print(" • If cfgrib fails, install ecCodes system library or use Conda:")
        print("     conda install -c conda-forge eccodes cfgrib")
        print("\nThen retry:")
        print("     pip install " + " ".join(all_bad))

    print("\n✨ Environment setup complete. You can now run:")
    print("   python train_models.py")
    print("   streamlit run dashboard.py\n")

if __name__ == "__main__":
    main()
