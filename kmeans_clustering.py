import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("driver_data.csv")
print("******** data ***********")
print(df.head())

f1 = df['Distance_Feature'].values
f2 = df['Speeding_Feature'].values
# X = [[i, j] for i in f1 for j in f2]
X = [list(a) for a in zip(f1, f2)]

plt.scatter(f1, f2)
# plt.show()

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
print("labels  : ",kmeans.labels_)

centers = kmeans.cluster_centers_
print("centers : ",centers)
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()