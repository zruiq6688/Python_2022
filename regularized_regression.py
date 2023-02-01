############## ridge model ###################
from sklearn.linear_model import RidgeCV
from sklearn.metrics import SCORERS
SCORERS.keys() ### to get the scoring you want

ridge_cv_model=RidgeCV(alphas=(0.1,1.0,5.0,10.0),scoring='neg_mean_absolute_error')
ridge_cv_model.fit(sca_X_train,y_train) ## from feature scaling

ridge_cv_model.alpha_

from sklearn.metrics import mean_absolute_error, mean_squared_error
test_predictions = ridge_cv_model.predict(sca_X_test)
mae = mean_absolute_error(y_test,test_predictions)
rmse = np.sqrt(mean_squared_error(y_test,test_predictions))
print(mae,rmse)


################ lasso model ###########
# it can shrink coef. all the way to 0
from sklearn.linear_model import Lasso, LassoCV
lasso_cv_model = LassoCV(eps=0.001,n_alphas=100,cv=5)
lasso_cv_model.fit(sca_X_train,y_train)


################## elastic net ###############
from sklearn.linear_model import ElasticNetCV
ela_model = ElasticNetCV(l1_ratio=[.1,.5,.7,.9,.95,.99,1],eps=0.001,n_alphas=100,max_iter=1000000)
ela_model.fit(X_train,y_train)
ela_model.l1_ratio_   --> this gives 1, meaning it's 100% Lasso 
