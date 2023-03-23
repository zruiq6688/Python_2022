X = pd.get_dummies(df)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)

ssd = []
# to find best K
from sklearn.cluster import KMeans
for k in range(2,10):

    model = KMeans(n_clusters=k,random_state=101)


    model.fit(scaled_X)

    #Sum of squared distances of samples to their closest cluster center.
    ssd.append(model.inertia_)

plt.plot(range(2,10),ssd,'o--')

# to get a sense of the difference
pd.Series(ssd).diff()#.plot(kind='bar')

# final model
kmeans_model = KMeans(n_clusters=5,random_state=101)
kmeans_model.fit(scaled_X)
k_label=kmeans_model.predict(scaled_X)
