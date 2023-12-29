import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,5]
plt.plot(x,y,'r')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill_between(x[1:3],y[1:3],alpha=0.5) #alpha는 투명도
plt.show()