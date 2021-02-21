import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time

#https://www.101computing.net/number-only/
#^^helped get user input
bnds = [-1.5,1.5,-1.5,1.5]
BELLOS = [(-.618034,0),(0,-.75),(-.382,.618034),(.69,-.69)\
        ,(.4233,.015),(.285,.01),(-.123,.685),(-.835,-.2321)\
        ,(-.8,.156),(-.7269,.1889),(-.70176,-.03842)]

delta = .00676
xs = np.arange(bnds[0],bnds[1],delta)
ys = np.arange(bnds[2],bnds[3],delta)
size = len(xs)
luck = 0
luckstr = ""
while True: #getting the values
    while luckstr != "y" and luckstr != "n" and luckstr != "t":
        luckstr = input("Feeling lucky? (y/n) ")
    if luckstr == "y" or luckstr == "t":
        luck = 1
        break
    try:
        rz = float(input("We need a complex number z. What should be Re(z)? "))
        iz = float(input("What should be Im(z)? "))
        N = int(input("To what age do turtles live? An integer is best. "))
    except ValueError:
        print("Not a good number. Try again.")
        continue
    else:
        break
if(luck):
    (rz,iz)=BELLOS[np.random.randint(0,len(BELLOS))]
    N = 11
z = complex(rz,iz)
R = .5 + np.sqrt(.25 + abs(z)) # just a definition my youtube course suggested
def f(x):
    return(x**2 + z) #change this to a 4 and it's cool, try a 3 and see why the dinosaurs went extinct
out =np.zeros((size,size))
for xi in range(size):
    for yi in range(size):
        num = complex(xs[xi], ys[yi])
        itr =0
        while abs(num) < R:
            num = f(num)
            itr = itr+1
        out[xi,yi] = itr/N
        if xi%200==0:
            print("at " + str(xi) +" out of " + str(size) + \
                  ". Using " + str(N) + " iterations. ")
plt.subplot()
plt.imshow(out, extent=bnds, interpolation='nearest', cmap=cm.hot)
plt.title(" Julia set: f(z) = z^2 + c; c = " + str(rz) + "+" + str(iz) + "i")
plt.show()