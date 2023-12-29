import numpy as np
import matplotlib.pyplot as plt

x=np.arange(3)
years=['2020','2023','2022']
values=[450,230,700]
plt.bar(x,values)
plt.xticks(x,years)
plt.show()