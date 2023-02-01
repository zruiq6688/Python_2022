from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_X = scaler.fit_transform(df)

from sklearn.decomposition import PCA
pca_model = PCA(n_components = 2)
pca_results = pca_model.fit_transform(scaled_X)

# the explaination power
pca_model.explained_variance_ratio_

# to further explore the 2 PC
df_comp = pd.DataFrame(pca_model.components_,index=['PC1','PC2'],columns=df.columns)

# to find the optimal n value
sum_power = []

for n in range(1,30):
    pca = PCA(n_components = n)
    pca.fit(scaled_X)
    sum_= np.sum(pca.explained_variance_ratio_)

    sum_power.append(sum_)

plt.plot(range(1,30),sum_power,'o--')
