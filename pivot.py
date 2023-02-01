pd.pivot_table(data=df_mpg,index='model_year',columns='origin',values=['weight','cylinders'],aggfunc = ['mean','sum'],fill_value = 0)
