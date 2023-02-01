import matplotlib.plot as plt

import numpy as np
x = np.arange(0,10)
y = 2*x

plt.plot(x,y)
plt.title('test')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.xlim(0,9)
plt.ylim(0,18)
plt.show() ## needed if the chart is not showing up
plt.savefig('test.jpg') ##can specify the full path if needed. otherwise saved in the same file as your code

### figure method ####
fig=plt.figure()
axes=fig.add_axes([0,0,1,1])
axes.plot(x,y)

####################### plot within a plot ##############################
fig=plt.figure(figsize=(3,3),dpi=200)
##LARGE AXES
axes1 = fig.add_axes([0,0,1,1])
axes1.plot(a,b)

axes1.set_xlim(0,8)
axes1.set_ylim(0,6000)
axes1.set_xlabel('X ALRGE')
axes1.set_ylabel('Y LARGE')
axes1.set_title('LARGE')

##SMALL AXES
axes2 = fig.add_axes([0.2,0.2,0.4,0.4])
axes2.plot(x,y)

axes2.set_xlim(0,8)
axes2.set_ylim(0,15)
axes2.set_xlabel('X SMALL')
axes2.set_ylabel('Y SMALL')
axes2.set_title('ZOOMED IN')

plt.show()

############### SUBPLOT #####################
fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(3,3))

axes_small = axes[0,1]
axes_small.plot(x,y)

axes[1,1].plot(a,b)

plt.tight_layout() ## automatic adjustment
fig.subplots_adjust(wspace=0.3,hspace=1) ## manuel adjustment. based on the scale of the cavas, 1 = 100%

fig.suptitle('TITLE FIG')

####################### LEGENDS #########################################################
fig = plt.figure()
axes=fig.add_axes([0,0,1,1])

axes.plot(x,x,label='liner',color='#f55d42',linewidth=10,linestyle='--',marker='o',markersize=20) # HEX color code
########## for short
axes.plot(x,x,lw=10,ls='--') 
axes.plot(x,x*2,label='liner*2')

axes.legend(loc = (1,0.5)) == plt.legend(loc = (1,0.5))
## OR
axes.legend(loc='upper right') == plt.legend(loc='upper right')


###################### COLORS ###############################
