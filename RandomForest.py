X = df.drop('Class',axis = 1)
y = df['Class']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=101)

from sklearn.model_selection import GridSearchCV # use gridsearch to find the best hyperparameters
from sklearn.ensemble import RandomForestClassifier
n_estimators = [64,100,128,200]
max_features = [2,3,4]
bootstrap = [True,False]
oob_score = [True,False] #only possible where bootstrap = True
param_grid = {'n_estimators':n_estimators,
             'max_features':max_features,
             'bootstrap':bootstrap,
             'oob_score':oob_score}

rfc =  RandomForestClassifier()
grid = GridSearchCV(rfc,param_grid)
grid.fit(X_train,y_train)
grid.best_params_ --> gives you the best hyperparams

############################ DO WE NEED LOTS OF ESTIMATORS? #####################################
errors = []
misclassifications = []

for n in range (1,201):
    rfc = RandomForestClassifier(bootstrap=True, max_features=2, n_estimators= n, random_state = 101)
    rfc.fit(X_train,y_train)
    pre = rfc.predict(X_test)
    err = 1-accuracy_score(y_test,pre)
    n_missed = np.sum(pre != y_test) # pre != y_test gives a boolean series, which you can sum 

    errors.append(err)
    misclassifications.append(n_missed)
