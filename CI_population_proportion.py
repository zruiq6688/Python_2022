dx = da[["SMQ020x", "RIAGENDRx"]]#.dropna()
dx.isna().sum()
dx = da[["SMQ020x", "RIAGENDRx"]].dropna()
pd.crosstab(dx["RIAGENDRx"],dx["SMQ020x"])


dx["SMQ020x"] = dx.SMQ020x.replace({"Yes": 1, "No": 0})
dz = dx.groupby("RIAGENDRx").agg({"SMQ020x": [np.mean, np.size]})
dz.columns = ["Proportion", "Total n"]


import statsmodels.api as sm
sm.stats.ztest(x1, value = 100) ##two-sided by default
sm.stats.ztest(x1,x2,alternative = 'two-sided')
