# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat

fontsize = 20

mat.rc('legend', fontsize=fontsize, handlelength=3)
mat.rc('axes',   titlesize=fontsize)
mat.rc('axes',   labelsize=fontsize)
mat.rc('xtick',  labelsize=fontsize)
mat.rc('ytick',  labelsize=fontsize)

mat.rc('font', size=fontsize, family='serif', style='normal', variant='normal',stretch='normal', weight='normal')

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.28       # the width of the bars

frequency = ('     1 Hz', '    3 Hz', '    5 Hz')

fig = plt.figure()
ax = fig.add_subplot(111)

top = [5,48,87]
rects1 = ax.bar(ind, top, width, color='blue', alpha = 0.5)
bottom = [17,243,482]
rects2 = ax.bar(ind+width, bottom, width, color='g', alpha = 0.5)
both = [2,5,2]
rects3 = ax.bar(ind+width*2, both, width, color='red', alpha = 0.5)

ax.set_ylabel(u'Nº de falhas')
ax.set_xlabel(u'Frequência')
ax.set_xticks(ind+width)
ax.set_xticklabels(frequency)
ax.legend( (rects1[0], rects2[0], rects3[0]), (u'Câmera superior', u'Câmera inferior', u'Duas câmeras'), loc=2 )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.grid(True)
plt.show()