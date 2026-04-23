import random
import math
import copy
import numpy as np
import pandas as pd
def create_data():
    data = []
    for i in range(15):
        d = {
            "zone": i,
            "metrics": {
                "traffic": random.randint(50, 150),
                "pollution": random.randint(30, 120),
                "energy": random.randint(40, 130)
            },
            "history": [random.randint(10, 50) for j in range(5)]
        }
        data.append(d)
    return data
def custom_risk_score(t, p, e):
    return math.log(t + p + e)
def mutate(data):
    for d in data:
        d["metrics"]["traffic"] += 5
        d["history"].append(random.randint(10, 50))
        t = d["metrics"]["traffic"]
        p = d["metrics"]["pollution"]
        e = d["metrics"]["energy"]
        d["risk"] = custom_risk_score(t, p, e)
def to_dataframe(data):
    rows = []
    for d in data:
        rows.append([
            d["zone"],
            d["metrics"]["traffic"],
            d["metrics"]["pollution"],
            d["metrics"]["energy"],
            d.get("risk", 0)
        ])
    return pd.DataFrame(rows, columns=["zone","traffic","pollution","energy","risk"])
def find_anomalies(df):
    mean = df["risk"].mean()
    std = df["risk"].std()
    res = []
    for i in range(len(df)):
        if df["risk"][i] > mean + std:
            res.append(df["zone"][i])
    return res
def manual_corr(x, y):
    xm = np.mean(x)
    ym = np.mean(y)

    num = np.sum((x - xm) * (y - ym))
    den = math.sqrt(np.sum((x - xm)**2) * np.sum((y - ym)**2))

    return num / den
def clusters(zones):
    zones = sorted(zones)
    res = []
    temp = []
    for z in zones:
        if not temp:
            temp.append(z)
        elif z == temp[-1] + 1:
            temp.append(z)
        else:
            res.append(temp)
            temp = [z]
    if temp:
        res.append(temp)

    return res
roll = 11646

data = create_data()
if roll % 2 == 0:
    data = data[::-1]
else:
    data = data[3:] + data[:3]
print("\n--- BEFORE MUTATION ---")
print(data)
assign_copy = data
shallow = copy.copy(data)
deep = copy.deepcopy(data)
mutate(shallow)
print("\n--- AFTER SHALLOW COPY MUTATION ---")
print(shallow)
print("\n--- ORIGINAL AFTER SHALLOW CHANGE (CORRUPTION PROOF) ---")
print(data)
df = to_dataframe(shallow)
print("\n--- DATAFRAME ---")
print(df)
an = find_anomalies(df)
print("\nANOMALY ZONES:", an)
corr = manual_corr(df["traffic"].values, df["pollution"].values)
print("CORRELATION (manual):", corr)
var = df["risk"].var()
stability = 1 / var if var != 0 else 0
mx = df["risk"].max()
mn = df["risk"].min()
result_tuple = (mx, mn, stability)
print("\nFINAL TUPLE (max, min, stability):")
print(result_tuple)
cl = clusters(an)
print("\nCLUSTERS:", cl)
# decision
if len(an) == 0:
    print("\nFINAL DECISION: System Stable")
elif len(an) < 3:
    print("\nFINAL DECISION: Moderate Risk")
elif len(an) < 6:
    print("\nFINAL DECISION: High Corruption Risk")
else:
    print("\nFINAL DECISION: Critical Failure")