import requests
import pandas as pd

base_url = "https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Functinal_HSPs_Dynamic_Map/FeatureServer"

layers = {
    0: "Hospitals",
    1: "Field_Hospitals",
    2: "Health_Centers",
    3: "Medical_Points"
}

all_rows = []

for layer_id, layer_name in layers.items():

    print(f"Downloading Layer {layer_id} - {layer_name}")

    params = {
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "outSR": "4326",
        "f": "json"
    }

    url = f"{base_url}/{layer_id}/query"

    r = requests.get(url, params=params)
    data = r.json()

    features = data.get("features", [])

    for f in features:
        attrs = f.get("attributes", {}).copy()
        geom = f.get("geometry", {})

        attrs["longitude"] = geom.get("x")
        attrs["latitude"] = geom.get("y")

        attrs["facility_category"] = layer_name

        all_rows.append(attrs)

print("Total records:", len(all_rows))

df = pd.DataFrame(all_rows)

df.to_excel("gaza_health_facilities.xlsx", index=False)

print("Exported to gaza_health_facilities.xlsx")