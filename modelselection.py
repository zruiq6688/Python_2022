from sklearn.metrics import mean_squared_error,mean_absolute_error

def run_model(model,X_train,y_train,X_test,y_test):
    # GOT MODEL TRAINING
    model.fit(X_train,y_train)
    # GET METRICS
    pre = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test,pre))
    mae = mean_absolute_error(y_test,pre)
    print(f'mae:{mae}')
    print(f'rmse:{rmse}')
    # PLOT
    signal_pre = model.predict(df['Signal'].values.reshape(-1,1))
    sns.scatterplot(x='Signal',y='Density',data=df)
    sns.scatterplot(x=df['Signal'],y=signal_pre,color = 'red')
