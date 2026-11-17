import pandas as pd

prices = pd.read_csv("data/clean/jet_vs_diesel.csv", parse_dates=["date"])

events = {
    "COVID": "2020-03-11",
    "FAA outage": "2023-01-11",
    "CrowdStrike": "2024-07-19",
    # "Ground stop": "2026-11-16",
}

rows = []

for name, day in events.items():
    day = pd.Timestamp(day)
    history = prices[prices["date"] < day].tail(250)
    after = prices[prices["date"] >= day]
    before = history["gap"].iloc[-1]

    for n in [1, 5, 20]:
        move = after["gap"].iloc[n - 1] - before
        normal = history["gap"].diff(n).std()
        rows.append([name, n, round(move, 1), round(normal, 1), round(move / normal, 1)])

table = pd.DataFrame(rows, columns=["event", "days_after", "move", "normal_move", "times_normal"])
print(table)
table.to_csv("data/clean/event_moves.csv", index=False)