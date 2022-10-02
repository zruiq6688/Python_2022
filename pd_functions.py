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
## or you can use numpy vectorize, which should be much faster
import numpy as np
df['quality'] = np.vectorize(quality)(df['total_bill'],df['tip'])
