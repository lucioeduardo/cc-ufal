import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import pandas as pd
  

# Plotando gráfico para teste visual
# Item A
x = np.array([128, 256, 384, 512, 640, 768, 896, 1024])

ob1 = np.array([386,850,1544,3035,6650,13887,28059,50916])
ob2 = np.array([375,805,1644,3123,6839,14567,27439,52129])
ob3 = np.array([393,824,1553,3235,6768,13456,27659,51360])

plt.scatter(x,ob1,15)
plt.scatter(x,ob2,15)
plt.scatter(x,ob3,15)

plt.xlabel('Tamanho do registro')
plt.ylabel('Tempo')

plt.show()

# Criando o modelo de regressão linear e plotando gráfico
# Item B

x = np.array([128, 256, 384, 512, 640, 768, 896, 1024])

x_c = sm.add_constant(x)
model = sm.OLS(ob1,x_c)
results = model.fit()

b0,b1 = results.params
print("b1: %.4f\nb0:%.4f\n"%(b1,b0))

plt.scatter(x,ob1)
plt.plot(x, b0 + x*b1, color='black')
plt.show()

# Item C
print("Porcentagem de variação explicada: %.4f\n"%results.rsquared)

# Item D
ic_b0,ic_b1 = results.conf_int(alpha=0.10)

print("IC-b1: (%.4f, %.4f)"%(ic_b1[0], ic_b1[1]))
print("IC-b0: (%.4f, %.4f)\n"%(ic_b0[0], ic_b0[1]))

# Item E
print("Valor para um registro de 2^20 kbits: %.4f"%(b1*(2**17) + b0))

v = pd.DataFrame([[2**17, 0]])

prediction = results.get_prediction(v)
                  
print("IC para a média com x=2^20:", prediction.conf_int(0.1))