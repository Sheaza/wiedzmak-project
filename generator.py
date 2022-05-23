import numpy as np
import pandas as pd

results = []
row = []

for i in range(200):
    for j in range(7):
        row.append(np.random.randint(0,2))
    while row in results:
        row = []
        for j in range(7):
            row.append(np.random.randint(0, 2))
    row.append(np.random.random())
    results.append(row)
    row = []
index = ['pazury', 'skrzydla', 'ogon', 'siersc', 'dwie nogi', 'kly', 'rogi', 'humanoidalnosc']
results = pd.DataFrame(data=np.array(results), columns=index)

results.loc[results['humanoidalnosc'] <= 0.25, 'humanoidalnosc'] = 0
results.loc[(results['humanoidalnosc'] > 0.25) & (results['humanoidalnosc'] <= 0.5), 'humanoidalnosc'] = 1
results.loc[(results['humanoidalnosc'] > 0.5) & (results['humanoidalnosc'] <= 0.75), 'humanoidalnosc'] = 2
results.loc[(results['humanoidalnosc'] > 0.75) & (results['humanoidalnosc'] <= 1), 'humanoidalnosc'] = 3
print(results)

results.to_excel('dataset.xlsx')