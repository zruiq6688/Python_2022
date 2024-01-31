pd.pivot_table(data=df_mpg,index='model_year',columns='origin',values=['weight','cylinders'],aggfunc = ['mean','sum'],fill_value = 0)

pivot.columns = pivot.columns.droplevel() # to drop multi index

pivot.reset_index(inpace = True) # to change index back 
