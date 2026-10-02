# 🍕 Zomato Business Intelligence & Machine Learning Dashboard

An end-to-end data analytics and machine learning capstone project evaluating Zomato's operational efficiency, customer behavior, and delivery logistics across multiple Indian cities.

## 🎥 Dashboard Demo

![Zomato Dashboard Demo](02-38-59.mp4)

---

## 🚀 Project Overview
This project bridges the gap between raw relational databases and predictive intelligence. By ingesting data from MySQL across 10+ operational tables, cleaning it through Python, training machine learning models, and visualizing insights in Power BI, this portfolio piece addresses key business questions around **revenue drivers, customer churn, traffic congestion, and delivery time forecasting**.

---

## 🛠️ Tech Stack & Architecture
* **Database / SQL**: MySQL (Relational schema normalization across 10 tables)
* **Data Processing & ML**: Python (`pandas`, `numpy`, `scikit-learn` for regression and classification)
* **Data Visualization**: Power BI Desktop (6-page interactive BI report)

---

## 📊 6-Page Power BI Dashboard Structure
1. **Executive Dashboard**: High-level KPI cards (`Total Revenue`), city slicers, and regional revenue breakdown.
2. **Customer Analytics**: Membership tier distributions (Basic vs. Pro/Gold) and order frequency metrics.
3. **Restaurant Analytics**: Top/bottom performing restaurant rankings and cuisine popularity analysis.
4. **Delivery Analytics**: Operational friction analysis mapping traffic congestion levels and weather/rainfall impacts.
5. **Sales Dashboard**: Monthly revenue trends and preferred checkout/payment method distributions.
6. **ML Dashboard**: Model evaluation scatter plots (Predicted vs. Actual Delivery Time) and feature importance drivers (Traffic Score, Rain Impact, Distance).

---

## 📂 Repository Structure
```text
├── dashboard/
│   └── zomato_project.pbix       # Power BI multi-page report file
├── notebooks/
│   ├── 01_eda_cleaning.ipynb     # Data exploration & preprocessing
│   └── 04_delivery_model.ipynb   # Delivery time regression & feature importance
├── data/
│   ├── ml_delivery_predictions.csv
│   └── ml_feature_importance.csv
└── sql/
    └── schema_setup.sql          # Database relational setup scripts
