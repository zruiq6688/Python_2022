X = df_ad.drop('sales',axis=1)
y = df_ad['sales']

from sklearn.preprocessing import PolynomialFeatures
poly_converter = PolynomialFeatures(degree =3, include_bias = False)
poly_features = poly_converter.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(poly_features,y,test_size=0.3,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
sca_X_train = scaler.transform(X_train)
sca_X_test = scaler.transform(X_test)
