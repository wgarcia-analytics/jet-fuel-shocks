import pandas as pd

def load(name):
    df = pd.read_csv(f"data/raw/{name}.csv", na_values=".")
    df.columns = ["date", name]
    df["date"] = pd.to_datetime(df["date"])
    return df

jet = load("jet")
diesel = load("diesel")

prices = jet.merge(diesel, on="date")
print("Rows after lining up by date:", len(prices))

prices = prices.dropna()
print("Rows with both prices:", len(prices))

prices["gap"] = ((prices["jet"] - prices["diesel"]) * 100).round(1)
prices.to_csv("data/clean/jet_vs_diesel.csv", index=False)

print(prices.tail())
print(prices["gap"].describe().round(1))