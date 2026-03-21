import requests
import pandas as pd

url = "https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Functinal_HSPs_Dynamic_Map/FeatureServer/5/query"

params = {
    "where": "1=1",
    "outFields": "*",
    "returnGeometry": "true",
    "outSR": "4326",
    "f": "json"
}

r = requests.get(url, params=params)
data = r.json()

rows = []

for feature in data["features"]:
    attrs = feature["attributes"]
    rows.append(attrs)

df = pd.DataFrame(rows)

df.to_excel("gaza_governorates.xlsx", index=False)

print("Governorates exported")