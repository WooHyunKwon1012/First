import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,5,0.5)
print(x)
plt.plot(x,x,'ro')
plt.plot(x,x**2,color='#FFFF00',marker='*',linewidth=1)
plt.plot(x,x**3,color='forestgreen',marker='^',markersize=5)
plt.xticks([0,5])
plt.yticks(np.arange(0,100,10))
plt.show()