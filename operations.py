df.groupby('model_year').describe().transpose()
df.groupby('model_year').mean['msg']
df.groupby('model_year').agg({'msg':"mean","count"})

###################### Multiindex DF ##########################
year_cyl = df_mpg.groupby(['model_year','cylinders']).mean()
year_cyl.index
year_cyl.index.names
year_cyl.index.levels
year_cyl.columns

year_cyl.loc[70].loc[4]
## OR ##
year_cyl.loc[(70,4)]

year_cyl.xs(key = 4, level='cylinders') ## to grab data based on level 2,key can only take in 2 value.

year_cyl.swaplevel()

year_cyl.sort_index(level = 'model_year',ascending = False)

################## USE MAP for aggregation #############################
df_mpg.agg({'mpg':['mean','size'],'weight':['sum']}).transpose()
## or a more ugly way
df_mpg.agg(['std','mean'])['mpg']
