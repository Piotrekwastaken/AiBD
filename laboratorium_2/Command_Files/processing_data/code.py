import pandas as pd
import numpy as np
file = pd.read_csv("../../original_data/drinks.csv", sep=',')

new_file = file.copy()
new_file = new_file.sort_values(by=['country'])

x, y = new_file.shape
for k in ["beer_servings", "spirit_servings", "wine_servings", "total_litres_of_pure_alcohol"]:
    new_file[k] = np.float64(new_file[k])
    for r in range(x):
        if new_file[k][r] < 0:
            new_file[k][r] *= -1

for c in range(x):
    if new_file["total_litres_of_pure_alcohol"][c] == 0:
        new_file = new_file.drop([c])

new_file.to_csv('../../Analysis_Data/gotowe_dane.csv', index=False)