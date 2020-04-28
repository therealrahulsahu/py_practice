import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

dataset = pd.read_csv('new_pages.csv')

X = dataset.iloc[:, 1:]
scalar = MinMaxScaler()
X = scalar.fit_transform(X)

cluster = 20
DM = KMeans(n_clusters=cluster, init='k-means++', random_state=0)
Y = DM.fit_predict(X)

'''
wcss = []
for i in range(1, 20):
    km = KMeans(n_clusters=i, init='k-means++')
    km.fit(X)
    wcss.append(km.inertia_)
import matplotlib.pyplot as plt
plt.plot(range(1, 20), wcss)
plt.show()
'''

result = []
for i in range(len(dataset)):
    temp = {
        'Page': dataset.iloc[i, 0],
        'PageViews': dataset.iloc[i, 1],
        'AvgTimeOnPage': dataset.iloc[i, 2],
        'Entrances': dataset.iloc[i, 3],
        'BounceRate': -dataset.iloc[i, 4],
        'Cluster': Y[i],
        'Center': sum(DM.cluster_centers_[Y[i]]),
        }
    result.append(temp)

result.sort(key=lambda x: x['Center'], reverse=True)
result = pd.DataFrame(result)

