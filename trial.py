
import numpy as np
import matplotlib.pyplot as plt
x = np.array([3,4,5,6,10])
y =np.array([1,0,2,-4,4])
plt.subplot(1,2,1)
plt.plot(x,2*y)
#ok now I can plot functions, but to work with Julia sets and the mandelbrot
#I will need to plot functions with two dimension domains( X+iY) outputting
#one dimensional outputs (velocity of divergence or binary value
#denoting convergence)
bnds = [-6.0, 6.0, -6.0, 6.0]
detail =.05
xs = np.arange(bnds[0],bnds[1],detail)
ys = np.arange(bnds[2],bnds[3],detail)
pixWidth =len(xs)
out = np.zeros((pixWidth,pixWidth))
for xi in range(pixWidth):
    for yi in range(pixWidth):
        if abs((xs[xi])**2 - (ys[yi])**2 -4)<.3:
            out[xi,yi]= 1
fig =plt.subplot(1,2,2)
plt.imshow(out, extent=bnds )
plt.show()

