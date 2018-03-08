# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
 
frequency = ('1 Hz', '3 Hz', '5 Hz')
y_pos = np.arange(len(frequency))


# Top bar chart
top = [5,48,87]
y = [0,100]
plt.figure(1)
plt.subplot(221)
plt.bar(y_pos, top, align='center', color='#580f41', alpha=0.5)
plt.xticks(y_pos, frequency)
plt.yticks( np.arange(min(y), max(y), 5) )
plt.ylabel(u'Nº de falhas')
plt.title(u'Testes de exaustão câmera Top')
plt.grid(True)


# Bottom bar graph
bottom = [17,243,482]
y = [0,501]
plt.figure(1)
plt.subplot(223)
plt.bar(y_pos, bottom, align='center', color='green', alpha=0.5)
plt.xticks(y_pos, frequency)
plt.yticks( np.arange(min(y), max(y), 25) )
plt.ylabel(u'Nº de falhas')
plt.title(u'Testes de exaustão câmera Bottom')
plt.grid(True)

# Both bar graph
both = [2,5,2]
y = [0,10]
plt.figure(1)
plt.subplot(122)
plt.bar(y_pos, both, align='center', color='red', alpha=0.5)
plt.xticks(y_pos, frequency)
plt.yticks( np.arange(min(y), max(y), 1) )
plt.ylabel(u'Nº de falhas')
plt.title(u'Testes de exaustão das duas câmeras')
 
plt.grid(True)
plt.show()