# California Power Outage Classification Dictionary
_Developed for PSPS and Power Outage Incident Analysis_

---

## Overview
This classification system standardizes **power outage events** across California for modeling and analysis.  
It distinguishes between **planned (preventative)** outages, such as Public Safety Power Shutoffs (PSPS), and **unplanned (reactive)** incidents due to natural or technical hazards.

---

## Coding Dictionary

| **Label / Code** | **Type** | **Definition / Criteria** | **Example Triggers** | **Primary Sources** |
|------------------|-----------|---------------------------|----------------------|---------------------|
| `planned_psps` | Planned | Public Safety Power Shutoff — proactive de-energization by a utility to reduce wildfire ignition risk during high wind, low humidity, or dry fuel conditions. | Red Flag warnings, high-wind events | [CPUC PSPS Portal](https://www.cpuc.ca.gov/consumer-support/psps/utility-company-psps-reports-post-event-and-post-season); PSE Healthy Energy (2023) |
| `planned_maintenance` | Planned | Scheduled maintenance or system upgrade outages not related to wildfire risk. | Infrastructure upgrades, vegetation management | Utility outage dashboards (PG&E, SCE, SDG&E) |
| `unplanned_weather` | Unplanned | Weather-driven outages caused by natural events such as storms, flooding, wind, lightning, or heat. | Santa Ana winds, lightning strikes, flooding | [DOE OE-417](https://www.energy.gov/ceser/oe-417-electric-emergency-incident-and-disturbance-reports); [Cal OES Power Outage Incidents](https://gis.data.ca.gov/datasets/Caloes::power-outage-incidents/about) |
| `unplanned_equipment` | Unplanned | Equipment or infrastructure failure unrelated to external hazards. | Transformer or cable failure | DOE OE-417; utility reliability filings |
| `unplanned_vegetation` | Unplanned | Vegetation or debris contacting energized equipment causing short circuits or damage. | Fallen trees, branches, vegetation intrusion | CPUC Vegetation Management Rules; NERC cause codes |
| `unplanned_public` | Unplanned | Third-party interference or damage to equipment. | Vehicle crashes, construction dig-ins, vandalism | Utility safety and reliability reports |
| `unplanned_upstream` | Unplanned | Grid supply or transmission disturbances propagating downstream. | Transmission line faults, generation loss | DOE OE-417 / NERC EOP-004 |
| `unknown` | N/A | Outages without sufficient information to assign a classification. | Missing metadata, unverified event | Default category |

---

## Dataset Alignment

This schema aligns with:
- **CPUC PSPS Event Rollup (2013–Present)**  
- **PSE Healthy Energy (2023) Public Safety Power Shutoff Map – Methodology & Data Sources**  
- **DOE OE-417 Electric Emergency Incident Reports**  
- **EAGLE-I (ORNL, DOE CESER) Electricity Outage Dataset, 2014–2024**  
- **Cal OES Power Outage Incidents (real-time feed)**  

---

## Reference Citations

1. **California Public Utilities Commission (CPUC).** (2025). *Utility Company PSPS Reports: Post-Event and Post-Season Portal.*  
   [https://www.cpuc.ca.gov/consumer-support/psps/utility-company-psps-reports-post-event-and-post-season](https://www.cpuc.ca.gov/consumer-support/psps/utility-company-psps-reports-post-event-and-post-season)

2. **PSE Healthy Energy.** (2023, April). *Public Safety Power Shutoff Maps: Methodology & Data Sources.*  
   [https://www.psehealthyenergy.org/wp-content/uploads/2023/04/Public-Safety-Power-Shutoff-Maps_Methodology-Data-Sources.pdf](https://www.psehealthyenergy.org/wp-content/uploads/2023/04/Public-Safety-Power-Shutoff-Maps_Methodology-Data-Sources.pdf)

3. **U.S. Department of Energy, CESER.** (2024). *OE-417 Electric Emergency Incident and Disturbance Reports.*  
   [https://www.energy.gov/ceser/oe-417-electric-emergency-incident-and-disturbance-reports](https://www.energy.gov/ceser/oe-417-electric-emergency-incident-and-disturbance-reports)

4. **California Governor’s Office of Emergency Services (Cal OES).** (2024). *Power Outage Incidents Dataset.*  
   [https://gis.data.ca.gov/datasets/Caloes::power-outage-incidents/about](https://gis.data.ca.gov/datasets/Caloes::power-outage-incidents/about)

5. **Oak Ridge National Laboratory (ORNL).** (2024). *EAGLE-I Electricity Outages Dataset (2014–2024).*  
   [https://data.osti.gov/details/EAGLE-I](https://data.osti.gov/details/EAGLE-I)

6. **California Public Utilities Commission (CPUC).** (2022). *Fire-Threat Maps and Fire Safety Rulemaking.*  
   [https://www.cpuc.ca.gov/industries-and-topics/wildfires/fire-threat-maps-and-fire-safety-rulemaking](https://www.cpuc.ca.gov/industries-and-topics/wildfires/fire-threat-maps-and-fire-safety-rulemaking)

   **Created By:** 
   Victoria Love Franklin 
   Ph.D. Student & Researcher
   School of Applied Computational Sciences 
   Meharry Medical College 
