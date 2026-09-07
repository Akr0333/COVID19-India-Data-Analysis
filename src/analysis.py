"""Reusable helpers for the COVID-19 India analysis project."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV dataset and return a copy of the dataframe."""
    return pd.read_csv(path).copy()


def standardise_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalise column names for easier analysis."""
    result = df.copy()
    result.columns = (
        result.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return result


def find_first_column(df: pd.DataFrame, candidates: Iterable[str]) -> str | None:
    """Return the first candidate column that exists."""
    for column in candidates:
        if column in df.columns:
            return column
    return None


def prepare_dates(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """Convert a date column to datetime and sort chronologically."""
    result = df.copy()
    result[date_column] = pd.to_datetime(result[date_column], errors="coerce")
    return result.dropna(subset=[date_column]).sort_values(date_column)


def daily_totals(df: pd.DataFrame, date_column: str, value_column: str) -> pd.DataFrame:
    """Aggregate a numeric metric by date."""
    result = df.copy()
    result[value_column] = pd.to_numeric(result[value_column], errors="coerce").fillna(0)
    return (
        result.groupby(date_column, as_index=False)[value_column]
        .sum()
        .sort_values(date_column)
    )


def top_regions(df: pd.DataFrame, region_column: str, value_column: str, n: int = 10) -> pd.DataFrame:
    """Return the top regions by total value."""
    result = df.copy()
    result[value_column] = pd.to_numeric(result[value_column], errors="coerce").fillna(0)
    return (
        result.groupby(region_column, as_index=False)[value_column]
        .sum()
        .sort_values(value_column, ascending=False)
        .head(n)
    )


if __name__ == "__main__":
    print("COVID-19 India Analysis helpers loaded successfully.")
