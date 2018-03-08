# -*- coding: utf-8 -*-
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 

mat.rcParams.update({'font.size': 18})

N = 750
p = 748/750.0

binominal = stats.binom(N,p)  

data = [(x,binominal.pmf(x)) for x in np.arange(N+1)]
important_data = [pair for pair in data if pair[1] > 0.0001]

x = [pair[0] for pair in important_data]
y = [pair[1] for pair in important_data]

plt.bar(x,y,align='center',color='red', alpha = 0.6)

plt.title(u"Distribuição Binominal: Câmera Superior e Inferior - 1 Hz")
plt.ylabel('Probabilidade')
plt.xlabel('Quantidade de imagens capturadas com sucesso')

plt.grid(True)
plt.show()