# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import matplotlib as mat
import numpy as np
from scipy.stats import binom

# -------------------------------------------------
# Graph Parameters
# -------------------------------------------------
fontsize = 18
y = [200,751]
x_axis = [0.0, 0.19]
colors = ['green', 'blue', 'purple']

# -------------------------------------------------
# MatplotLib Parameters
# -------------------------------------------------
mat.rc('legend', fontsize=fontsize, handlelength=3)
mat.rc('axes', titlesize=fontsize)
mat.rc('axes', labelsize=30)
mat.rc('xtick', labelsize=fontsize)
mat.rc('ytick', labelsize=fontsize)
# mat.rc('text', usetex=True)
mat.rc('font', size=fontsize, family='serif', style='normal', variant='normal',stretch='normal', weight='normal')
    
# -------------------------------------------------
# top camera
# -------------------------------------------------
n_values = [750, 750, 750]
b_values = [745.0/750.0, 702.0/750.0, 663.0/750.0]
x = np.arange(200, 755)

fig, ax = plt.subplots(figsize=(5, 3.75))

graphs = []

plt.subplot(211)
for (n, b, c) in zip(n_values, b_values, colors):
    # create a binomial distribution
    dist = binom(n, b)
    rect = plt.plot(x, dist.pmf(x), 'bo', ms= 5, c = c, alpha = 0.6)
    plt.plot(x, dist.pmf(x), ls='-', c = c, alpha = 0.5, linewidth = 1.0, label=r'$b=%.1f,\ n=%i$' % (b, n), linestyle='-') 
    graphs.append(rect)

plt.title(u"Distribuição Binominal: Câmera Superior - (1, 3, 5) Hz", fontsize = 30)
plt.legend( ( graphs[0][0], graphs[1][0], graphs[2][0]), (u'1 Hz', u'3 Hz', u'5 Hz'), loc=2)
plt.xticks( np.arange(min(y), max(y), 25) )
plt.yticks( np.arange(min(x_axis), max(x_axis), 0.02) )
plt.xlabel('$x$')
plt.ylabel(r'$p(x|p, n)$')
plt.xlim(200, 755)

plt.grid(True)

# -------------------------------------------------
# bottom camera
# -------------------------------------------------

n_values = [750, 750, 750]
b_values = [733.0/750.0, 507.0/750.0, 268.0/750.0]
x = np.arange(200, 755)

plt.subplot(212)
for (n, b, c) in zip(n_values, b_values, colors):
    # create a binomial distribution
    dist = binom(n, b)
    rect = plt.plot(x, dist.pmf(x), 'bo', ms= 5, c = c, alpha = 0.6)
    plt.plot(x, dist.pmf(x), ls='-', c=c, alpha = 0.5, linewidth = 1.0, label=r'$b=%.1f,\ n=%i$' % (b, n), linestyle='-')

plt.title(u"Distribuição Binominal: Câmera Inferior - (1, 3, 5) Hz", fontsize = 30)
plt.legend( ( graphs[0][0], graphs[1][0], graphs[2][0]), (u'1 Hz', u'3 Hz', u'5 Hz'), loc=2 )
plt.xlim(200, 755)
plt.xticks( np.arange(min(y), max(y), 25) )
plt.yticks( np.arange(min(x_axis), max(x_axis), 0.02) )
plt.xlabel('$x$')
plt.ylabel(r'$p(x|p, n)$')

plt.grid(True)
plt.show()