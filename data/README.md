# Data

The notebook uses a historical state-wise India COVID-19 time-series dataset hosted publicly by `amitvsavant/covid19-india-state-timeseries`. The source describes the dataset as state-wise reported cases from 30 January 2020 onwards, with cumulative confirmed, cured/discharged/migrated and death figures.

The project deliberately does not commit a large raw dataset. The notebook downloads the source CSV when a local copy is not present, making the repository smaller and easier to reproduce.

For offline use, save a compatible CSV as:

```text
data/covid_india.csv
```

The expected fields are:

- `Date`
- `State`
- `Total Confirmed Cases`
- `Cured/Discharged/Migrated`
- `Death`

**Source:** Public COVID-19 India state-wise historical data. See the main README for project context and limitations.
