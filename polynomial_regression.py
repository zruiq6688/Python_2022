X = df_ad.drop('sales',axis=1)
y = df_ad['sales']

from sklearn.preprocessing import PolynomialFeatures
polynomial_coverter=PolynomialFeatures(degree=2,include_bias=False)
poly_features = polynomial_coverter.fit_transform(X)
poly_converter.get_feature_names(X.columns) # to get the column names 

---> X.shape = (200,3)
---> poly_features.shape = (200,9)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(poly_features,y,test_size=0.3,random_state=101)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)
test_predictions = model.predict(X_test)

## performance evaluation #
from sklearn.metrics import mean_absolute_error, mean_squared_error
mae=mean_absolute_error(y_test,test_predictions)
mse=mean_squared_error(y_test,test_predictions)
rmse=np.sqrt(mse)
print("mae is",mae,"rmse is",rmse)


## save and use the model ####
from joblib import dump,load
dump(model,'model.joblib')
dump(polynomial_coverter,'polynomial_coverter.joblib')
loaded_converted =load('poly_converter.joblib')
loaded_model=load('model.joblib')

campaign=[[149,22,12]]
transformed_data=loaded_converted.fit_transform(campaign)
loaded_model.predict(transformed_data)


############################### DEGREE SELECTION WITH LOOP ########################
train_rmse_errors=[]
test_rmse_errors=[]
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

X = df_ad.drop('sales',axis=1)
y = df_ad['sales']

for d in range(1,10):
    poly_converter = PolynomialFeatures(degree=d,include_bias=False)
    poly_features=poly_converter.fit_transform(X)

    X_train,X_test,y_train,y_test=train_test_split(poly_features,y,test_size=0.3,random_state=101)

    model=LinearRegression()
    model.fit(X_train,y_train)

    train_pred=model.predict(X_train)
    test_pred=model.predict(X_test)

    train_rmse=np.sqrt(mean_squared_error(y_train,train_pred))
    test_rmse=np.sqrt(mean_squared_error(y_test,test_pred))

    train_rmse_errors.append(train_rmse)
    test_rmse_errors.append(test_rmse)

import matplotlib.pyplot as plt
import seaborn as sns

plt.plot(range(1,6),train_rmse_errors[:5],label='train')
plt.plot(range(1,6),test_rmse_errors[:5],label='test',color='red')
(we choose degree=3 in this case)
plt.legend(loc=(1,0))
