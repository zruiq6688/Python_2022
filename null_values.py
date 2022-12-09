######################NULL DATA#############################
help(df.dropna)

df.isnull()
df.notnull()

df.dropna() ### axis = 0 by default (drop rows)
df.dropna(subset = ['last_name']) ## drop null based on last_name col
df.dropna(thresh = 1) ## required the rows that have less than 1 non null values

df.fillna('NON')
df['pre_movie_score'].fillna(0)  ## do this on numeric col
df.fillna(df.mean())

ser.interpolate() ## linear value insert 
