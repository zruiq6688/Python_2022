fig,ax=plt.subplots(ncols=3, nrows=1,figsize=(10,5))

ax1=ax[0]
ax1.plot(df_ad['TV'],df_ad['sales'],marker='o',linestyle='')
ax1.set_xlabel('tv')
ax1.set_ylabel('sales')
ax1.set_title('tv vs sales')

ax2=ax[1]
ax2.plot(df_ad['radio'],df_ad['sales'],marker='o',linestyle='')
ax2.set_xlabel('radio')
ax2.set_ylabel('sales')
ax2.set_title('radio vs sales')

ax3=ax[2]
ax3.plot(df_ad['newspaper'],df_ad['sales'],marker='o',linestyle='')
ax3.set_xlabel('newspaper')
ax3.set_ylabel('sales')
ax3.set_title('newspaper vs sales')

plt.tight_layout()

### THE SAME AS
sns.pairplot(data=df_ad)

################################################
np.polyfit(X,y,deg=1)

################## PERFORMANCE OF MODEL ###############################
MEAN ABSOLUTE ERROR (do not punish large error)
MEAN SQUARED ERURR (large error is punished)
ROOT MEAN SQUARED ERROR
