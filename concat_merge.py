tech_finance = ['GOOG,APPL,AMZN','JPM,BAC,GS']
import pandas as pd
tickers = pd.Series(tech_finance)

############ built-in string function for DF series ##########################
tickers.str.isdigit()
tickers.str.split(',').str[0]
tickers.str.split(',',expand = True) ##becomes a DF


names = ['aa','b;b','c c  ']
names = pd.Series(names)

def cleanup(name):
    name = name.replace(';','')
    return name

names.apply(cleanup)
################### date function #######################
euro_date = '2000-10-12'
pd.to_datetime(euro_date,dayfirst = True)
