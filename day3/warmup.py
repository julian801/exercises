

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon.csv')
df.set_index('#',inplace=True)

short = df[['Name','HP','Attack']]
short.info()
short.describe()
short[short['HP']>=140]
df.groupby('Type 1')['Defense'].mean()         
df.groupby('Type 1')['Attack','Defense'].mean()         
atdef = df.groupby('Type 1')['Attack','Defense'].mean() 

atdef.plot.scatter('Attack','Defense')
atdef.plot.hist()
plt.savefig


piv = df.groupby(['Type 1','Type 2'])[['HP']].count().unstack()
piv.head(3)
piv.fillna(0.0, inplace=True)
piv_to_csv('pokemon_pivot.csv')
#%hist

import random

x = list(range(20))
y = [3 * xx + 2 + 10*random.random() for xx in x]
X = np.array(x).reshape(-1,1)
y = np.array(y)
X.shape
y.shape


plt.plot(x, y, 'bo')
plt.show()

from sklearn.linear_model import LinearRegression
m = LinearRegression()
m.fit(X,y)

ypred = m.predict(X)

plt.figure()
plt.plot(X,y,'bo')
plt.plot(X,ypred,'rx')
plt.show()
m.score(X,y)







