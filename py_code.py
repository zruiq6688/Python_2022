##change format for describe
import pandas as pd
df_pd.describe().applymap('{:,.2f}'.format)


##matplotlib
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10)) ##increase graph size
plt.hist(df_pd,density = True, bins = 1000)
plt.xlim(1, 5)

##groupby, order
from pyspark.sql.functions import countDistinct
from pyspark.sql.functions import date_format
df.groupBy(date_format("sales_date_id", "yyyy-MM")).agg(countDistinct('receipt_id')).sort(countDistinct('receipt_id').desc()).show()

##join
df = df_join.withColumn("amount_sek",col("sales_net_fcc") * col("rate_value"))


##distinct value
df.select("department").distinct().show()
==
df.select("department").dropDuplicates().show()


##lead over
from pyspark.sql.window import Window
from pyspark.sql.functions import lag, lead, first, last, col
agg_output = dff.withColumn("next_receipt_begin_time", lead('begin_date_time').over(
    Window.partitionBy("location_id","till_no").orderBy(col("begin_date_time").asc())
    ))


##describe table without scientific notation
df.describe().apply(lambda s: s.apply('{0:.5f}'.format))

print("hello")
