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

##statistical analysis
df.describe()
df.describe().transpose()

##retrive certain columns
mycols = ['total_bill','tip','size','price_per_person']
df[mycols]
##OR
df[['total_bill','tip','size','price_per_person']]


##create new columns
df['tip_percentage'] =100*df['tip'] / df['total_bill']
df['tip_percentage'] = np.round(df['tip_percentage'],2)

#drop columns
df.drop('tip_percentage',axis = 1) ##not permenant
df = df.drop('tip_percentage',axis = 1) ##permenant drop
