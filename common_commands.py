df.dtypes
df.info()
df.describe()
df.corr()
df.isnull().sum()
df['col1'].value_counts()
df.replace('NA',np.nan) # to change all NA to nan
df.at[df[df['sex'] == '.'].index,'sex'] = 'FEMALE' # to change a single copy

df.groupby('level of education').agg({'salary':[np.mean,np.std],'sales':np.mean})



## apply & transform ###
df = pd.DataFrame({
    'key': ['a','b','c'] * 3,
    'A': np.arange(9),
    'B': [1,2,3] * 3,
})

def group_sum(x):
    return x.sum()

gr_data_ap = df.groupby('key')['A'].apply(group_sum)

gr_data_tr = df.groupby('key')['A'].transform(group_sum)
# transform returns the same length as input

####################################### correlation visulisation ##########################
corr=X.corr()['clusters'].sort_values()

plt.figure(figsize=(20,5))
sns.barplot(x=corr.index,y=corr)
plt.xticks(rotation=90)
plt.show()
# or
corr.plot(kind='bar')

#################################### aggeregate duplicated values into a column ###############
lst = df.groupby('Courses')['Fee'].apply(list)
dd = pd.DataFrame(lst).reset_index()
dd['lenth'] = dd['Fee'].apply(lambda x:len(x))

#################################### to get % within a group #############################
dd = pd.DataFrame(df[df['gender_code'].isin(['1','2'])].groupby(['label','gender_code'])['gender_code'].count())
dd/dd.groupby('label').transform(np.sum)
# all index and columns need to match to perform operation on DFs

################################### fillna with grouped values ###########################
df_housing.groupby('Street')['Lot Frontage'].transform(lambda value:value.fillna(value.mean()))
#or
fill_values=df_housing.groupby('Street')['Lot Frontage'].tranform(np.mean)
df_housing['Lot Frontage'].fillna(fill_values)
# if a dataframe then index and columns need to match
