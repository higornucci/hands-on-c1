import urllib.request
from pathlib import Path
import pandas as pd

datapath = Path() / "data" / "lifesat"
datapath.mkdir(parents=True, exist_ok=True)

# data_root = "data/"
# for filename in ("BLI_02042024030302099.csv", "gdp_per_capita-worldbank.csv"):
#     if not (datapath / filename).is_file():
#         url = data_root + "lifesat/" + filename
#         urllib.request.urlretrieve(url, datapath / filename)

oecd_bli = pd.read_csv(datapath / "BLI_02042024030302099.csv")
gdp_per_capita = pd.read_csv(datapath / "gdp-per-capita-worldbank.csv")
gdp_year = 2021
gdppc_col = "GDP per capita (USD)"
lifesat_col = "Life satisfaction"

gdp_per_capita = gdp_per_capita[gdp_per_capita["Year"] == gdp_year]
gdp_per_capita = gdp_per_capita.drop(["Code", "Year"], axis=1)
gdp_per_capita.columns = ["Country", gdppc_col]
gdp_per_capita.set_index("Country", inplace=True)

print(gdp_per_capita.head(10))
