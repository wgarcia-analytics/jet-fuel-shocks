import requests

series = {
    "jet": "DJFUELUSGULF",
    "diesel": "DDFUELUSGULF",
    "heating_oil": "DHOILNYH",
}

for name, series_id in series.items():
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code == 200:
        with open(f"data/raw/{name}.csv", "wb") as f:
            f.write(response.content)
        print("Saved:", name)
    else:
        print("FAILED:", name, response.status_code)