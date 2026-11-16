import pandas as pd
import matplotlib.pyplot as plt

prices = pd.read_csv("data/clean/jet_vs_diesel.csv", parse_dates=["date"])

print("Lowest gap:")
print(prices.loc[prices["gap"].idxmin()])
print()
print("Highest gap:")
print(prices.loc[prices["gap"].idxmax()])

events = {
    "COVID": "2020-03-11",
    "FAA outage": "2023-01-11",
    "CrowdStrike": "2024-07-19",
    "Ground stop": "2026-11-13",
}

plt.figure(figsize=(12, 5))
plt.plot(prices["date"], prices["gap"], color="#2a78d6", linewidth=1)
plt.axhline(0, color="gray", linewidth=1)

top = prices["gap"].max()
for name, day in events.items():
    plt.axvline(pd.Timestamp(day), color="#e34948", linestyle="--", linewidth=1)
    plt.text(pd.Timestamp(day), top, name, rotation=90, va="top", ha="right", color="#e34948")

plt.title("Jet fuel minus diesel, U.S. Gulf Coast, 2006 to 2026")
plt.ylabel("Cents per gallon (below 0 = jet is cheaper)")
plt.tight_layout()
plt.savefig("charts/jet_vs_diesel_gap.png", dpi=200)
print("Saved chart")

prices["daily_change"] = prices["gap"].diff()
prices["year"] = prices["date"].dt.year
print(prices.groupby("year")["daily_change"].std().round(1))

recent = prices[prices["date"] >= "2026-01-01"]

plt.figure(figsize=(12, 5))
plt.plot(recent["date"], recent["jet"], label="Jet fuel", color="#2a78d6", linewidth=1.5)
plt.plot(recent["date"], recent["diesel"], label="Diesel", color="#eb6834", linewidth=1.5)
plt.legend()
plt.title("Jet fuel and diesel, U.S. Gulf Coast, 2026")
plt.ylabel("Dollars per gallon")
plt.tight_layout()
plt.savefig("charts/jet_and_diesel_2026.png", dpi=200)
print("Saved 2026 chart,", len(recent), "days")