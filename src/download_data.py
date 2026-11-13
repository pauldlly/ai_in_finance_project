
from pathlib import Path

import requests

# FRED Treasury yield series
series = {
    "3M": "DGS3MO",
    "6M": "DGS6MO",
    "1Y": "DGS1",
    "2Y": "DGS2",
    "3Y": "DGS3",
    "5Y": "DGS5",
    "7Y": "DGS7",
    "10Y": "DGS10",
    "20Y": "DGS20",
    "30Y": "DGS30"
}

# Study period
start_date = "2005-01-01"
end_date = "2026-11-08"

ROOT = Path.cwd()

if not (ROOT / "data").is_dir() and ROOT.name == "src":
    ROOT = ROOT.parent

# Create the destination folder
data_dir = ROOT / "data"
data_dir.mkdir(parents=True, exist_ok=True)

# Download FRED data
for maturity, code in series.items():
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={code}&cosd={start_date}&coed={end_date}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    (data_dir / f"{code}.csv").write_bytes(response.content)
    print(f"{maturity} ({code}) downloaded")
