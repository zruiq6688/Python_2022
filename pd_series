##Pandas series as a one_dimensional laebled array
import numpy as np
import pandas as pd
myindex= ['USA','CAD','MXC']
mydata = ['1988','1887','1888']
myser = pd.Series(data=mydata, index=myindex)

ages = {'Sam':5,'Doris':6,'Peter':7}
age_pd = pd.Series(ages)
age_pd
age_pd.keys()
age_pd.['Sam']

############
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}
sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)

sales_q1+sales_q2 ##gives nah to keys that are not present in both series
sales_q1.add(sales_q2,fiil_value=0)
