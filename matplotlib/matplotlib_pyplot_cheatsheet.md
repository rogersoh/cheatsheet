# Matplotlib 

Matplotlib is a Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms.

## Prepare the Data  
1D Data 
```
import numpy as np
x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x)
```
2D Data or image
```
data = 2 * np.random.random((10, 10))
data2 = 3 * np.random.random((10, 10))
Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = 1 X** 2 + Y
V = 1 + X Y**2
from matplotlib.cbook import get_sample_data
img = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))
```

## Create Plot
```
import matplotlib.pyplot as plt
```

Figure 
```
fig = plt.figure()
fig2 = plt.figure(figsize=plt.figaspect(2.0))
```
Axes 
```
fig.add_axes()
ax1 = fig.add_subplot(221) #row-col-num
ax3 = fig.add_subplot(212)
fig3, axes = plt.subplots(nrows=2,ncols=2)
fig4, axes2 = plt.subplots(ncols=3)
```
Save Plot 
```
plt.savefig('foo.png') #Save figures
plt.savefig('foo.png',  transparent=True) #Save transparent figures
```
Show Plot
```
plt.show()
```

## figure, axes label
y label only on the left
x label on the bottom of the axes

metadata is a dataframe with "Nice name" as column
```
plt.figure(figsize=(8,30))
for i,test in enumerate(ref_tests):
  ax  = plt.subplot(int(np.ceil(len(tests)/4)),4,i+1)
  .....
  remove_top_right_frame([ax]) # remove the top and right side border
  ax.set_title(metadata.loc[test]['Nice name'])
  ax.set_xlabel('Fold change\n(Clalit)')
  ax.set_ylabel('Fold change\n(Reference)')

  if i<len(ref_tests)-4:
    ax.set_xlabel('')
  if np.mod(i,4) != 0:
    ax.set_ylabel('')
```

initial plot setting
```
init_printing()
plt.rc('axes', labelsize= 5.0)
plt.rc('legend', title_fontsize = 8)
plt.rc('legend', fontsize =6)
plt.rc('font', size=8) 
plt.rc('xtick', labelsize=6) 
plt.rc('ytick', labelsize=6) 
plt.rc('axes', titlesize=8) 
matplotlib.rcParams["figure.dpi"] = 100
```

list all rcParams dict
```
matplotlib.rcParams
```