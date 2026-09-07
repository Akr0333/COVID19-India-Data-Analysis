# COVID-19 India Data Analysis 🇮🇳

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualisation-orange)
![License](https://img.shields.io/badge/Project-Educational-lightgrey)

A portfolio-ready **exploratory data analysis (EDA)** project studying the spread of COVID-19 across India using Python.

## 🎯 Project Goals

- Analyse the growth of COVID-19 cases over time.
- Compare the reported burden across Indian states/regions.
- Examine cumulative confirmed, recovered and deceased cases.
- Estimate daily changes from cumulative totals.
- Calculate simple recovery and fatality rates.
- Communicate findings through clean Matplotlib visualisations.

## 📊 What the Notebook Produces

### India-wide analysis
- Cumulative confirmed, recovered and deceased case curves
- Estimated daily increase in confirmed cases
- Identification of the highest reported daily increase

### State-wise analysis
- Latest available state/region totals
- Top 10 regions by confirmed cases
- Recovery and fatality-rate calculations

### Data-quality awareness
The notebook also demonstrates date conversion, numeric coercion, missing-value handling and sorting. COVID reporting involved revisions, delays and changes in definitions, so historical figures should be interpreted as reported data.

## 🗂️ Project Structure

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
├── requirements.txt
├── .gitignore
└── README.md
```

## 🛠️ Tech Stack

- **Python** — programming and analysis
- **Pandas** — data cleaning and aggregation
- **NumPy** — numerical calculations
- **Matplotlib** — visualisation
- **Requests** — downloading the historical dataset
- **Jupyter Notebook** — interactive analysis
- **Git/GitHub** — version control and portfolio presentation

## 🚀 Run the Project

### 1. Clone

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

### 4. Launch Jupyter

```bash
jupyter notebook
```

Open:

```text
notebooks/COVID19_India_Analysis.ipynb
```

The notebook first looks for `data/covid_india.csv`. If it is not present, it downloads the historical CSV from the public source configured in the notebook.

## 📁 Dataset

The project uses a historical state-wise COVID-19 India time series. The public source describes data from **30 January 2020 onwards**, with cumulative confirmed, cured/discharged/migrated and death figures.

The repository keeps the large raw dataset out of Git history and documents the expected schema in `data/README.md`.

## 🔍 Example Questions

This project can be extended to answer questions such as:

- Which states had the highest reported case burden?
- When were the strongest periods of growth?
- How did recovery and fatality rates vary?
- Which states experienced different growth patterns?
- How can the same workflow be adapted to other public-health datasets?

## 📌 Future Improvements

- Add an interactive Plotly dashboard.
- Add a state-level animated bar chart.
- Add wave/period comparison.
- Add testing and positivity-rate analysis where reliable testing data is available.
- Add automated data validation tests.
- Add GitHub Actions for notebook/code checks.

## ⚠️ Disclaimer

This is an **educational data-analysis project**. Historical COVID-19 data may contain revisions, reporting delays, missing values and differences in definitions. The results should not be used for medical, epidemiological or policy decisions.

## 👨‍💻 Author

**Akr0333**

If you find this project useful, feel free to ⭐ the repository.
