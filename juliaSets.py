import numpy as np
import matplotlib.pyplot as plt

#https://www.101computing.net/number-only/
#^^helped get user input
bnds = [-6.0,6.0,-6.0,6.0]
delta = .05
xs = np.arange(bnds[0],bnds[1],delta)
ys = np.arange(bnds[2],bnds[3],delta)
size = len(xs)

while True:
    try:
        rz = float(input("We need a complex number z. What should be Re(z)? "))
        iz = float(input("What should be Im(z)? "))
    except ValueError:
        print("Not an float! Try again.")
        continue
    else:
        break


print(rz+iz)
