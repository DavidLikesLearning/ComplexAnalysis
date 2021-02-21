import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#https://www.101computing.net/number-only/
#^^helped get user input
bnds = [-1.5,1.5,-1.5,1.5]
delta = .00176
xs = np.arange(bnds[0],bnds[1],delta)
ys = np.arange(bnds[2],bnds[3],delta)
size = len(xs)

while True: #getting the values
    try:
        rz = float(input("We need a complex number z. What should be Re(z)? "))
        iz = float(input("What should be Im(z)? "))
        N = int(input("To what age do turtles live? An integer is best. "))
    except ValueError:
        print("Not a good number. Try again.")
        continue
    else:
        break

z = complex(rz,iz)
R = .5 + np.sqrt(.25 + abs(z)) # just a definition my youtube course suggested
def f(x):
    return(x**2 + z)
out =np.zeros((size,size))
for xi in range(size):
    for yi in range(size):
        num = complex(xs[xi], ys[yi])
        itr =0
        while abs(num) < R:
            num = f(num)
            itr = itr+1
        out[xi,yi] = itr/N

plt.subplot()
plt.imshow(out, extent=bnds, cmap=cm.hot)

plt.show()

