import seaborn as sns
sns.set_theme(styele='darkgrid')
plt.figure(figsize=('10,10'),dpi=200)
sns.scatterplot(x='salary',y='sales',data=df
                ,hue='level of education',palette='Dark2'
                ,s=10,alpha=0.3,style='level of education')
        ## palette on matplotlib color mapping
        ## alpha is useful in scatterplot for density

###################### plot types #############################
sns.scatterplot(x='salary',y='sales',data=df)
sns.displot(data=df,x='salary',kde=True,rug=True) ##can fit 3 kinds of plots in 1
sns.histplot(data=df,x='salary')
sns.boxplot()
sns.violinplot()
sns.lmplot()
sns.swarmplot()
sns.countplot(data=df,x='division')
## the same as value_counts

sns.catplot(data=df, x='division',y='salary',kind='box',row='level of education',height=5,aspect=2)
## a mgenralised categritical plot. you can row/col in catplot

########### comparison plots ###############
sns.pairplot(data=df,corner=True) ## good to keep only cols you are interested in
sns.jointplot()

########### MATRIX PLOT #################
sns.heatmap(df,cmap='viridis') ## need to pivot the original DF first
sns.clustermap(df,col_cluster=False)

######################## adjust for figure size ###########################
plt.figure(figsize=(3,3)) ## used for axes_based charts
sns.lmplot(x=,y=,data=, height=6, aspect=1) ## used for all types of charts

####################### all plt kethods can be used too ###################
plt.xlim()
plt.ylim()
plt.title()
plt.suptitle()
plt.legend()

####################### to add annot ##############################
ax = sns.countplot(data=df,x='sex',hue='species')

for p in ax.patches:
    ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x(), p.get_height()))
plt.show()

######################## to have the x lable ordered ########################
sns.countplot(data=df_city[df_city['label']==2],x='city',order=df_city['city'].value_counts().index,hue='label')
plt.xticks(rotation = 90)
