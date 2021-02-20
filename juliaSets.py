import numpy as np
import matplotlib.pyplot as plt
bnds = [-6.0,6.0,-6.0,6.0]
delta = .05
xs = np.arange(bnds[0],bnds[1],delta)
ys = np.arange(bnds[2],bnds[3],delta)
size = len(xs)
 = int(input("We need a complex number z. What should be Re(z)? "))
