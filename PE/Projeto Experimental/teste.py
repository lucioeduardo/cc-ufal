from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import numpy as np

x = np.array([128, 256, 384, 512, 640, 768, 896, 1024]).reshape((-1, 1))
ob1 = np.array([386,850,1544,3035,6650,13887,28059,50916])
# x = x.reshape(1,-1)
# ob1 = ob1.reshape(1,-1)


linear_regressor = linear_model.LinearRegression()  
linear_regressor.fit(x,ob1)  # Função que faz a regressão linear
Y_pred = linear_regressor.predict(x) 

plt.plot(x,Y_pred,color='black')
plt.scatter(x,ob1)


plt.show()
