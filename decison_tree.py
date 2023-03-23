X = pd.get_dummies(df.drop('species',axis=1),drop_first=True)
y = df['species']

# no need for feature scaling in decision tree, because each feature is used seperately.

# train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

base_pre = model.predict(X_test)
# result
from sklearn.metrics import classification_report, plot_confusion_matrix
print(classification_report(y_test,base_pre))

plot_confusion_matrix(model,X_test,y_test)

pd.DataFrame(index = X.columns,data=model.feature_importances_,columns=['Feature Importance']).sort_values(by='Feature Importance')
# visualise the decision tree
from sklearn.tree import plot_tree
plt.figure(figsize=(20,10))
plot_tree(model,feature_names = X.columns,filled=True)
plt.show()

### to explore diffrence hyperparameters
def report_model(model):
    model_pre = model.predict(X_test)
    print(classification_report(y_test,model_pre))
    print('⧵n')
    plt.figure(figsize=(20,10))
    plot_tree(model,feature_names = X.columns,filled=True)
    plt.show()
# model 2
pruned_tree = DecisionTreeClassifier(max_depth=2) # to avoid overfitting
pruned_tree.fit(X_train,y_train)
report_model(pruned_tree)

# model 3
