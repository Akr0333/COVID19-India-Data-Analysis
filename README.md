# COVID-19 India Data Analysis 🇮🇳

A Python data-analysis project exploring the spread and impact of COVID-19 in India using **Pandas, NumPy, Matplotlib and Requests**.

## Project Overview

This project demonstrates a practical data-analysis workflow:

1. Collect COVID-19 data from a public source.
2. Clean and transform the raw data.
3. Analyse daily and state-wise trends.
4. Calculate cumulative confirmed cases, recoveries and deaths.
5. Identify highly affected states.
6. Create clear visualisations for communicating the results.

> **Note:** Historical COVID-19 datasets and APIs can change or become unavailable. The analysis code is designed so that a local CSV can also be supplied when the online source is unavailable.

## Repository Structure

```text
COVID19-India-Data-Analysis/
│
├── data/
│   └── README.md
├── notebooks/
│   └── COVID19_India_Analysis.ipynb
├── src/
│   └── analysis.py
├── visualisations/
│   └── README.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies Used

- Python 3.9+
- Pandas
- NumPy
- Matplotlib
- Requests
- Jupyter Notebook

## Key Analysis

- Daily confirmed-case trends
- State-wise case comparison
- Cumulative confirmed cases
- Recovery and death trends when available
- Top affected states
- Basic descriptive statistics
- Time-series visualisation

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Akr0333/COVID19-India-Data-Analysis.git
cd COVID19-India-Data-Analysis
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the notebook

```bash
jupyter notebook notebooks/COVID19_India_Analysis.ipynb
```

## Learning Outcomes

This project is useful for practising:

- Data collection
- Data cleaning
- Exploratory Data Analysis (EDA)
- Pandas data manipulation
- Time-series analysis
- Data visualisation
- Reproducible Python projects
- Git and GitHub project organisation

## Disclaimer

This repository is an educational data-analysis project. It is not intended for medical, epidemiological, or policy decisions.

## Author

**Akr0333**
