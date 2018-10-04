
import pandas as pd

spices = ['chili', 'salt', 'basil', 'thyme', 'juniper']
n = [2, 0, 6, 11, 0]
cohort = [True, False, True, True, False]

df = pd.DataFrame({'name': spices, 'participants': n, 'cohort': cohort})

at_spiced = df[df['cohort']]
print(at_spiced.sort_values(by='participants'))

print("\ntotal participants:", df['participants'].sum())

