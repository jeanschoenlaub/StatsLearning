import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

rng= np.random.default_rng(12)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
x = rng.standard_normal(10) 
y = rng.standard_normal(10) 

# First plot  -- scater
axes[0,0].plot(x, y, 'o') 
axes[0,0].set_xlabel("this is the x-axis")
axes[0,0].set_ylabel("this is the y-axis")
axes[0,0].set_title("Scatter Plot of X vs Y")


# Second plot  -- contour
x = np.linspace(-np.pi, np.pi, 50)
y= np.linspace(-np.pi, np.pi, 50)
f = np.multiply.outer(np.cos(y), 1 / (1 + x**2)) 
axes[0,1].set_xlabel("this is the x-axis")
axes[0,1].set_ylabel("this is the y-axis")
axes[0,1].set_title("Contour Plot")
axes[0,1].contour(x,y, f, levels=45)


#3rd plot -- contour filled
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 40)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
axes[1,0].contourf(X, Y, Z, 20)  # 'RdGy' is short for Red-Gray colormap
axes[1,0].set_title("Filled Contour plot")

# 4th plot
x = rng.standard_normal(10) 
y = rng.standard_normal(10) 

axes[1,1].scatter(x, y, marker='+')
axes[1,1].set_xlabel("this is the x-axis")
axes[1,1].set_ylabel("this is the y-axis")
axes[1,1].set_title("Plot of X vs Y")

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()