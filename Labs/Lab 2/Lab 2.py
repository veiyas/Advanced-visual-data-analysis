import pandas as pd
from sklearn.cluster import OPTICS
import numpy as np

colnames = ['a', 'b', 'GazeEventDuration', 'c', 'GazePointX', 'GazePointY' ]
df = pd.read_csv('Lab 2 Data.tsv', sep='\t', names=colnames)
#del df['Unnamed: 6']
print(df)

my_data = np.genfromtxt('my_file.csv', delimiter='\t')

test = [df.GazeEventDuration.tolist(), df.GazePointX.tolist(), df.GazePointY.tolist()]
print(test)

clustering = OPTICS(min_samples=2).fit(test)
print("a")

