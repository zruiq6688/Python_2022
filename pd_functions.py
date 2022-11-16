def last_two(num):
    return num[-2,:]

##apply a function to a series
df['last_two'] = df['CC Number'].apply(last_two)

##THE SAME WITH LAMBDA
df['total_bill'].apply(lambda num: num*2) ##good with quick anounymous experrions you only use once
#OR
def simple(num):
    return num*2
df['total_bill'].apply(simple)


#################################### How to use lambda to apply 2 arguments in df ##############################
def quality(total_bill, tip):
    if tip/total_bill > 0.25:
        return 'big'
    else:
        return 'other'
## you can either use apply
df['quality'] = df[['total_bill','tip']].apply(lambda df: quality(df['total_bill'],df['tip']),axis = 1)
## or you can use numpy vectorize, which makes the code numpy-aware --> better performance
import numpy as np
df['quality'] = np.vectorize(quality)(df['total_bill'],df['tip'])


####################################
df['total_bill'].idxmax()
df.corr() ## only works with numeric value
df['sex'].value_counts()
df['day'].unique()
df['day'].nunique() == len(df['day'].unique())

df['sex'].replace(['Female','Male'],['F','M'])
==
mymap = {'Female':'F','Male':'M'} ## eaier to work with if multiple values
df['sex'].map(mymap)

df.duplicated()
df.drop_duplicates()
df['total_bill'].between(10,20,inclusive = True)
df.nlargest(5,'tip')
df.nsmallest(5,'tip')
df.sample(frac = 0.05)
