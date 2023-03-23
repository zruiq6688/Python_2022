dd = df_union.groupby(['receipt_id','prod_name']).sum()

dd.loc[['receipt_id1','receipt_id2']] ## only takes in the outer index

dd.xs(key='pants',level='prod_name') ## cross section - only takes in 1 argument

################################## flatten index and columns #######################
dd = df.groupby(['model_year','origin','cylinders']).agg({'mpg':['mean','max'],'horsepower':['mean','max']})

col = []
for i in dd.reset_index().columns:
    col.append(i[0])

dd = dd.reset_index()
dd.columns = ['model_year', 'origin', 'cylinders', 'mpg_mean', 'mpg_max', 'horsepower_mean', 'horsepower_max']

## if you have duplicated col names 
dd = pd.DataFrame(df_pd.groupby(['profit_omni_value_segment','product_type_name'])['product_type_name'].count())
dd.columns = ['cnt']
dd = dd.reset_index()
