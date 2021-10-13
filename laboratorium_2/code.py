import pandas as pd

file = pd.read_csv("original_data/drinks.csv", sep = ',')
#print(file)
new_file = file.copy()


#for line in new_file:
#    for i in range(1, 5):
#        if line[i] < 0:
#            line[i] *= -1
    
#print(new_file)
print(new_file.shape)