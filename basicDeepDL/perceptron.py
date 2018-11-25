import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# import the data into numpy array
# Data Source: Assignment1_Q4_data.txt

data = np.loadtxt('Assignment1_Q4_data.txt')
print (data)
print (data[0][0]) 

x = data[0][0]
y = data[0][1]

plt.xlabel('Say time')
plt.ylabel('say stock price')
plt.title('Just a random points placed to see how they plot')
plt.plot(x, y)

plt.show()
