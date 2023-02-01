############################# outlier by iqr ###############################
ser.describe()
# or
q75, q25 = np.percentile(ser,[75,25])
iqr = q75 - q25 - 25th

lower_limit = 25th - 1.5*iqr
upper_limit = 75th + 1.5*iqr


############################ outlier #######################################
ids = df_housing[(df_housing['Gr Liv Area'] > 4000) & (df_housing['SalePrice'] < 300000)].index
df_clean = df_housing.drop(ids,axis=0)


##########################  missing values ####################################
def percent_missing(df):
    percent_null = 100*df.isnull().sum()/len(df)
    percent_null = percent_null[percent_null>0].sort_values()

    return percent_null ## better to create function, so you can reuse it

#visulisation
plt.figure(figsize=(20,3))
plt.xticks(rotation=90)
sns.barplot(x=percent_null.index,y=percent_null)

# drop rows
df = df_housing_clean.dropna(axis=0, subset=['Electrical','Garage Cars'])

# fill missing data
bsmt_num_cols = ['BsmtFin SF 1', 'BsmtFin SF 2', 'Bsmt Unf SF','Total Bsmt SF', 'Bsmt Full Bath', 'Bsmt Half Bath']
df[bsmt_num_cols] = df[bsmt_num_cols].fillna(0)

bsmt_str_cols =  ['Bsmt Qual', 'Bsmt Cond', 'Bsmt Exposure', 'BsmtFin Type 1', 'BsmtFin Type 2']
df[bsmt_str_cols] = df[bsmt_str_cols].fillna('None')

df_housing.groupby('Street')['Lot Frontage'].transform(lambda value:value.fillna(value.mean()))
#or
fill_values=df_housing.groupby('Street')['Lot Frontage'].tranform(np.mean)
df_housing['Lot Frontage'].fillna(fill_values)


######################################### dummy variable ################################
df_object=df.select_dtypes(include='object')
df_numeric=df.select_dtypes(exclude ='object')
df_object_dummies = pd.get_dummies(df_object,drop_first=True)
final_df = pd.concat([df_numeric,df_object],axis=1)
