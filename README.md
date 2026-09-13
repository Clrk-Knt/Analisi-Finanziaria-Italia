# Italian Financial Market Quantitative Analysis

A Python-based data pipeline and quantitative analysis script designed to compare the performance and statistical correlation of the **FTSE MIB index** and **Intesa Sanpaolo (`ISP.MI`)** stock from January 2020 to the present.

## Overview
This project automates the extraction, cleaning, normalization, and statistical analysis of historical stock market data. By aligning daily closing prices and scaling them to a common baseline (Base 100 = 2020), it enables both visual trend comparison and rigorous statistical evaluation through correlation matrices.

## Key Features
* **Automated Data Ingestion:** Downloads historical closing price series directly via the Yahoo Finance API (`yfinance`).
* **Data Wrangling & Alignment:** Cleans structures, handles missing values, and synchronizes temporal timelines using `pandas`.
* **Base 100 Normalization:** Rescales assets with different nominal values onto a unified percentage scale for direct comparative visualization.
* **Statistical Modeling:** Computes Pearson's correlation matrix and renders an intuitive heat map via `seaborn`.

## Tech Stack
* **Python**
* **`yfinance`** — Financial data retrieval
* **`pandas`** — Data manipulation and cleaning
* **`matplotlib` & `seaborn`** — Data visualization

## Installation & Setup

Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/Clrk-Knt/Analisi-Finanziaria-Italia.git](https://github.com/Clrk-Knt/Analisi-Finanziaria-Italia.git)
cd Analisi-Finanziaria-Italia
pip install pandas yfinance matplotlib seaborn
