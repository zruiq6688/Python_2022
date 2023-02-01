df.dtypes
df.info()
df.describe()
df.corr()
df.isnull().sum()
df['col1'].value_counts()

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
