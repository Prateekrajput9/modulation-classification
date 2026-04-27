import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("final_dataset.csv")

# Separate labels
modulations = df["modulation"]
db_values = df["db"]
data = df.drop(columns=["modulation", "db"]).values

num_samples = len(data)

print(f"Total samples: {num_samples}")
print("Available modulations:", set(modulations))
print("Available dB values:", sorted(set(db_values)))

# -------- Frequency Table --------
print("\n📊 Modulation vs dB Distribution:\n")
freq_table = pd.crosstab(df["modulation"], df["db"])
print(freq_table)

# Optional: normalized (percentage)
print("\n📊 Percentage Distribution:\n")
print(pd.crosstab(df["modulation"], df["db"], normalize="index") * 100)

# -------- Interactive Viewer --------
while True:
    try:
        idx = int(input(f"\nEnter sample index (0 to {num_samples-1}, -1 to exit): "))
        
        if idx == -1:
            break
        
        if idx < 0 or idx >= num_samples:
            print("❌ Invalid index")
            continue
        
        sample = data[idx]
        modulation = modulations.iloc[idx]
        db = db_values.iloc[idx]
        
        # Split into I and Q
        I = sample[0::2]
        Q = sample[1::2]
        
        print(f"📌 Modulation: {modulation} | dB: {db}")
        
        # -------- Time Domain --------
        plt.figure(figsize=(10,4))
        plt.plot(I, label="I")
        plt.plot(Q, label="Q")
        plt.title(f"Time Domain - Sample {idx} ({modulation}, {db} dB)")
        plt.legend()
        plt.grid()
        plt.show()
        
        # -------- Constellation --------
        plt.figure(figsize=(5,5))
        plt.scatter(I, Q, s=5)
        plt.title(f"Constellation - Sample {idx} ({modulation}, {db} dB)")
        plt.grid()
        plt.axis('equal')
        plt.show()

    except ValueError:
        print("❌ Enter a valid number")