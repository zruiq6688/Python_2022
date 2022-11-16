## A group of pandas series objects that share the same index
df=spark.read.csv('/FileStore/tables/tips.csv')
df=df.toPandas()
import pandas as pd
headers = df.iloc[0]
df  = pd.DataFrame(df.values[1:], columns=headers)


##quick check
df.columns
df.index
df.head(5)
df.tail()
df.info()
df.duplicated()
df.drop_duplicates()

##statistical analysis
df.describe()
df.describe().transpose()

##################retrive certain columns################################
mycols = ['total_bill','tip','size','price_per_person']
df[mycols]
##OR
df[['total_bill','tip','size','price_per_person']]
##OR
df.iloc[:,[1,3,5,7]]

##################retrive certain rows#################################
df.iloc[2]
##OR
df[2:3]
##OR
df.loc["Sun2929"] ##with labelled index


##################create new columns##########################
df['tip_percentage'] =100*df['tip'] / df['total_bill']
df['tip_percentage'] = np.round(df['tip_percentage'],2)


##################create new rows##########################
one_row = df.iloc[0]
df = df.append(one_row) ##permenant


######################drop & select ###############################
df.drop('tip_percentage',axis = 1) ##drop column, not permenant
df = df.drop('tip_percentage',axis = 1) ##drop column, permenant drop
df.drop('Sum2929', axis = 0) #drop row with labelled index, not permenant
df.drop(0, axis = 0) #drop first row without labelled index, not permenant
df = df.iloc[1:] #drop first row without labelled index, permenant

##index
df.set_index("Payment ID") ##not permenant
df = df.set_index("Payment ID") ##permenant
df = df.reset_index() ##revert the change

##location
df.iloc[2]
df.loc["Sun2929"]
==== ##above 2 gives the same
df.iloc[:,2] ##take column 2


##############################conditional filtering########################################
df[(df['total_bill'] > 30) & (df['sex'] == 'Male')] ##and/or is only used to compare 2 single boolean values, not used for series of boolean values
df[df['day'].isin(['Sat','Sun'])]


##############################categoritical columns########################################
df['sex'].value_counts()
df['sex'].unique()
df['sex'].nunique() == len(df['sex'].unique())

df['sex'].replace(['Female','Male'],['F','M']) ##easy to use when replacing null values
##or
mymap = {'Female':'F','Male':'M'}
df['sex'].map(mymap)


######################################################################
df.nlargest(2,'tip')
df.nsmallest(2,'tip')
df.sample(5)
df.sample(frac = 0.1)
