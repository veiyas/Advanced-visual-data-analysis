import pandas as pd
from sklearn.cluster import OPTICS, DBSCAN
import matplotlib.pyplot as plt
import numpy as np

# colnames = ['a', 'b', 'GazeEventDuration', 'c', 'GazePointX', 'GazePointY' ]
df = pd.read_csv('Lab 2 Data.tsv', sep='\t')
#del df['Unnamed: 6']
# print(df)

my_data = np.genfromtxt('Lab 2 Data.tsv', delimiter='\t')

test = df.filter(items=['GazePointX(px)', 'GazePointY(px)', 'GazeEventDuration(mS)']).values

data = np.array([df['GazeEventDuration(mS)'][1:], df['GazePointX(px)'][1:], df['GazePointY(px)'][1:]])

clustering = OPTICS(min_samples=2).fit(test)
# cluster = DBSCAN(eps=3, min_samples=10).fit(test)
print(clustering.labels_)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.array(df['GazeEventDuration(mS)'])
y = np.array(df['GazePointX(px)'])
z = np.array(df['GazePointY(px)'])

ax.scatter(x,y,z, marker="s", c=clustering.labels_, s=40, cmap="RdBu")
plt.xlabel('TIME')

plt.show()