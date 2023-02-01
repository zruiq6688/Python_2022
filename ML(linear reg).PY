## split train and test
from sklearn.model_selection import train_test_split
X = df_ad.drop(['sales'],axis=1)
y = df_ad['sales']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)

## modelling
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)
test_predictions = model.predict(X_test)
model.coef_

## performance evaluation
from sklearn.metrics import mean_absolute_error, mean_squared_error

mae=mean_absolute_error(y_test,test_predictions)
mse=mean_squared_error(y_test,test_predictions)
rmse=np.sqrt(mse)

print("mae is",mae,", rmse is", rmse)

df_ad['sales'].mean() ##to compare your MAE and RMSE


####################### TO VALUATE IS LINEAR REG. IS A GOOD CHOICE OR NOT ############
test_residuals=y_test - test_predictions
sns.scatterplot(x=y_test,y=test_residuals)
plt.xlabel('y_test')
plt.ylabel('test_residuals')
plt.axhline(y=0, color='red',ls='--')
#(test-residual graph, it should look very random along the red line)

# you can also look at the dist. of test_res, it should be normally distributed if linear is valid
sns.displot(test_residuals,kde=True,bins=20)
# normality check
import scipy as sp
fig,ax=plt.subplots()
_=sp.stats.probplot(test_residuals,plot=ax)
