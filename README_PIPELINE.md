# Reproducible Data Pipeline — Documentation

**Generated:** 2025-11-01T18:20:55.738151Z

## Overview
This pipeline standardizes, imputes, and validates environmental, outage, and SDOH datasets.
It also derives normalized metrics for air quality and outages, and exports quality diagnostics.

## Imputation Rules
- Numeric: median
- Categorical: mode
- High-missingness flagged at > 70%

## Derived Features
- `ozone_ratio_to_std`  = Daily Max 8-hr Ozone (ppb) / 70.0
- `pm25_ratio_to_std`   = Daily Mean PM2.5 (µg/m³) / 35.0
- `outage_hours_per_customer` = customer_weighted_hours / total_customers_impacted
- `avg_duration_per_outage`   = customer_weighted_hours / outage_count
- `peak_to_avg_duration_ratio` = max_outage_duration / avg_duration_per_outage

## Column Dictionary

### ozone_YYYY

| Column | Description |
|---|---|
| `Date` | Observation date (YYYY-MM-DD) |
| `Daily Max 8-hour Ozone Concentration` | Max 8-hr ozone, ppb |
| `ozone_ratio_to_std` | Ozone / NAAQS 8-hr standard (70 ppb) |


### pm_YYYY

| Column | Description |
|---|---|
| `Date` | Observation date (YYYY-MM-DD) |
| `Daily Mean PM2.5 Concentration` | Daily average PM2.5 (µg/m³) |
| `pm25_ratio_to_std` | PM2.5 / NAAQS 24-hr standard (35 µg/m³) |


### eaglei_ca_outages_agg

| Column | Description |
|---|---|
| `customer_weighted_hours` | Sum(customers * hours) |
| `total_customers_impacted` | Total customers impacted |
| `outage_count` | Number of outage events |
| `outage_hours_per_customer` | CWH / total_customers_impacted |
| `avg_duration_per_outage` | CWH / outage_count |

