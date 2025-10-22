# Comparative Analysis between EAGLE-I Outage Data (2014–2023) and EIA-861 Sales to Ultimate Customers and Service Territory (2014–2023)

---

## **Analytical Approach — EAGLE-I**

### **a) Cross-Sectional Comparison (per Year)**
For each year **2014–2023**:
- Aggregate **EAGLE-I outage data** by **county** and **year**.  
- Merge aggregated outage records with **EIA-861 total customer counts** (Residential, Commercial, Industrial, and Transportation).  
- Compute the **percentage of customers affected** and analyze **sectoral outage exposure** using proportional allocation methods.

---

### **b) Temporal Trend Analysis**
- Plot **annual totals** for both datasets to visualize the relationship between:  
  - Total **customer base** (*EIA-861*)  
  - Total **outage customers** (*EAGLE-I*)  
- Examine **correlation patterns** between **growth in customer populations** and **frequency/severity of outages** across California counties.  
- Assess **year-over-year variability** to identify operational or environmental trends.

---

### **c) Data Completeness & Quality Assessment**
- Compute **coverage gaps** by identifying **counties or utilities** present in **EIA-861** but **absent in EAGLE-I** reporting for the same period.  
- Quantify **data completeness** as:  
  \[
  \text{Coverage Ratio} = \frac{\text{Counties with EAGLE-I outages}}{\text{Counties in EIA-861}}
  \]
- Evaluate potential **reporting lags**, **underrepresentation**, or **inconsistencies** between operational (EAGLE-I) and regulatory (EIA-861) data sources.

---

### **d) Forecasting / Extrapolation for 2024**
- Use **2014–2023 historical outage trends** from EAGLE-I to **forecast expected 2024 outage counts and customer impacts** using regression or time-series models.  
- Compare projected outage patterns with **EIA-861 2024 customer growth rates** to assess:
  - Whether **customer expansion** aligns with **outage vulnerability**.  
  - Anticipated **grid resilience trends** under continued load growth.

---

## **Expected Outputs**
- County-level **outage and customer alignment table (2014–2023)**  
- **Trend visualization plots** (customers vs. outages)  
- **Coverage completeness matrix** comparing EAGLE-I and EIA-861 utilities  
- **2024 forecast report** estimating outage coverage based on customer growth projections  

---

## **Interpretation & Insights**

| **Analysis Focus** | **Expected Outcome** |
|--------------------|----------------------|
| **Spatial Coverage** | Identifies under-reported regions or utilities in EAGLE-I. |
| **Customer Base Consistency** | Confirms whether outage reporting aligns with customer population density. |
| **Sectoral Exposure** | Quantifies vulnerability of each customer type to outages. |
| **Temporal Trends** | Reveals whether outages scale with customer growth or operational constraints. |

---

## **Expected Deliverables**

1. **Comparative Coverage Table** — Year-by-year alignment of utilities, customers, and outages.  
2. **Sectoral Allocation Matrix** — Residential, Commercial, Industrial, and Transportation shares.  
3. **County-Level Correlation Map** — Outage rate vs. customer density.  
4. **2024 Projection Summary** — Estimated outage exposure based on 2024 customer counts.  

---

## **Purpose**
This analysis compares **utility-reported outage data** from the **EAGLE-I system** with the official **EIA-861 Annual Electric Power Industry Report** for **2014–2023**.  
The goal is to evaluate the relationship between **outage impacts** and **customer distribution by type** across California counties, ensuring proper alignment between customer populations and service territories.

---

## **Analytical Focus**

- **Research Question:** Which customer type experiences the largest outage share across California counties in 2014?  
- **Objective:** Analyze current outage impacts across customer types and counties by merging **EAGLE-I outage data** with **EIA-861 customer distribution data**, thereby assessing the correlation between **total customers affected** and **customer composition** (Residential, Commercial, Industrial, Transportation).

---

## **Relevance of Comparative Framework**

The authors’ methodology supports aligning **utility-level customer data (EIA-861)** with **real-time outage reports (EAGLE-I)** to establish baseline accuracy in outage severity calculations.  
Such comparative validation enhances interpretability and ensures that outage magnitudes are analyzed **proportionally to total customer counts**, **utility service territories**, and **county coverage**.

---

## **Data Sources**

| **Dataset** | **Description** | **Source** |
|--------------|----------------|-------------|
| **EAGLE-I Outage Data (2014)** | Contains real-time outage events and total customers affected at 15-minute intervals. | U.S. Department of Energy – EAGLE-I Portal |
| **CA Sales to Ultimate Customers (2014)** | Provides electricity customer counts by type (Residential, Commercial, Industrial, Transportation) and utility, as reported to the EIA. | Form EIA-861 Annual Electric Power Industry Report |
| **CA Service Territory (2014)** | Defines geographic boundaries and county-level coverage for each utility. | EIA-861 Service Territory Dataset |
| **Merged CA EAGLE-I × EIA-861 Dataset (2014)** | Integrates outage data with customer type distributions and service territories for county-level comparative analysis. | Prepared by the author for this study |

---

## **About the EIA-861 Annual Report**

- **Form EIA-861 (Annual Electric Power Industry Report)** and **Form EIA-861S (Short Form)** collect data from electric distribution utilities and power marketers across the U.S.  
- The survey captures information on **generation, transmission, and distribution** activities and serves as a **census of all U.S. electric utilities**.  
- Data include **revenues**, **sales (MWh)**, and **customer counts** by state, sector, and balancing authority.  
- **Historical coverage:** 1990–present  
- **Release date:** October 7, 2025 (final 2024 data)  
- **Next release:** October 2026  
- **URL:** [EIA-861 Annual Data and Documentation](https://www.eia.gov/electricity/data/eia861/)  
- **FAQ:** [Form EIA-861 Frequently Asked Questions](https://www.eia.gov/electricity/data/eia861/faq.php)  

---

### **Historical Note**
In **2003**, the EIA reclassified customer categories, introducing the **Transportation** sector and removing the **Other** category.  
Activities such as **street and highway lighting** were reassigned to the **Commercial** sector, improving **granularity** in usage and customer segmentation data.
