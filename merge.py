import pandas as pd
import glob, os

results = pd.DataFrame([])

for counter, file in enumerate(glob.glob("csv/*")):
    namedf = pd.read_csv(file, sep='\t', skiprows=0)
    results = results.append(namedf)

results.to_csv('combined.csv')