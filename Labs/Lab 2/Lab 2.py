import pandas as pd
from sklearn.cluster import OPTICS, DBSCAN
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


# colnames = ['a', 'b', 'GazeEventDuration', 'c', 'GazePointX', 'GazePointY' ]
df = pd.read_csv('Lab 2 Data.tsv', sep='\t')
#del df['Unnamed: 6']
# print(df)

my_data = np.genfromtxt('Lab 2 Data.tsv', delimiter='\t')

test = df.filter(items=['GazePointX(px)', 'GazePointY(px)']).values

# data = np.array([df['GazeEventDuration(mS)'][1:], df['GazePointX(px)'][1:], df['GazePointY(px)'][1:]])

# clustering = OPTICS(min_samples=10, xi = 0.10).fit(test)

clustering = DBSCAN(eps=62, min_samples=13).fit(test)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# x = np.array(df['GazeEventDuration(mS)'])
# y = np.array(df['GazePointX(px)'])
# z = np.array(df['GazePointY(px)'])

# ax.scatter(x,y,z, marker="o", c=clustering.labels_, s=40, cmap="RdBu")
# plt.xlabel('TIME')
# plt.ylabel('X')

# plt.show()


df['Cluster'] = clustering.labels_
df.plot.scatter(x='GazePointX(px)', y='GazePointY(px)', s=0.05*df['GazeEventDuration(mS)'],
    c='Cluster', cmap=plt.cm.get_cmap("Dark2", 7), alpha=0.6, edgecolors='none')

# df.plot(x='GazePointX(px)', y='GazePointY(px)', c='RdBu', alpha=0.8)

# df.plot(x='RecordingTimestamp', y='Cluster')
# plt.grid(True, axis='y')

plt.show()