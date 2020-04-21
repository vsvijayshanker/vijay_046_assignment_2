#
#I do not have mathematica so i did calculation in python only
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

h=0.01   #common step size for all calculation is used

a=1
b=2
n=int(1+(b-a)/h)
def f(x, y):        #first and second order derivatives of 1st equation
    return np.vstack((y[1], -np.exp(-2*y[0])))
def bc(ya, yb):     #boundary conditions of 1st equation
    return np.array([ya[0], yb[0]-np.log(2)])
x = np.linspace(a,b,n)
y = np.ones((2, x.size))
ytr = np.log(x)
sol1 = solve_bvp(f, bc, x, y)
print(sol1)
plt.plot(x,sol1.sol(x)[0],'-g',label='Calculated Solution')
plt.plot(x,ytr,'--y', label='Analytic Solution')
plt.minorticks_on()
plt.legend()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.grid(True)
#first part ends
#
#second part starts
a=0
b=np.pi/2
n=int(1+(b-a)/h)
def f(x, y):        #first and second order derivative of 2nd equation
    return np.vstack((y[1], y[1]*np.cos(x)-y[0]*np.log(y[0]) ))
def bc(ya, yb):     #boundary conditions of 2nd equation
    return np.array([ya[0]-1, yb[0]-np.exp(1)])
x = np.linspace(a,b,n)
y = np.zeros((2, x.size))
y[0]=1
ytr = np.exp(np.sin(x))
sol1 = solve_bvp(f, bc, x, y)
print(sol1)
plt.subplots()
plt.plot(x,sol1.sol(x)[0],'-g',label='Calculated Solution')
plt.plot(x,ytr,'--y', label='Analytic Solution')
plt.legend()
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.grid(True)

#second part ends
#
#third part starts
a=np.pi/4
b=np.pi/3
n=int(1+(b-a)/h)
def f(x, y):    #first and second derivative of 3rd equation
    return np.vstack((y[1], -(2*y[1]**3+y[0]**2*y[1])/np.cos(x)))
def bc(ya, yb):#boundary conditions of 3rd equation 
    return np.array([ya[0]-2**(-1/4), yb[0]-np.sqrt(np.sqrt(3)/2)])
x = np.linspace(a,b,n)
y = np.ones((2, x.size))
y[0]=2**(-1/4)
ytr = np.sqrt(np.sin(x))
sol1 = solve_bvp(f, bc, x, y)
print(sol1)
plt.subplots()
plt.plot(x,sol1.sol(x)[0],'-g',label='Calculated Solution')
plt.plot(x,ytr,'--y', label='Analytic Solution')
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.grid(True)
#third part ends
#
#fourth part stars
a=0
b=np.pi
n=int(1+(b-a)/h)
def f(x, y):        #first and second order derivative of 4th equation
    return np.vstack((y[1],0.5*(1-y[1]**2-y[0]*np.sin(x))))
def bc(ya, yb):     #boundary condtions of 4th equation
    return np.array([ya[0]-2, yb[0]-2 ])
x = np.linspace(a,b,n)
y = np.ones((2, x.size))
y[1]=1
ytr = 2+np.sin(x)
sol1 = solve_bvp(f, bc, x, y)
print(sol1)
plt.subplots()
plt.plot(x,sol1.sol(x)[0],'-g',label='Calculated Solution')
plt.plot(x,ytr,'--y', label='Analytic Solution')
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.grid(True)

plt.show()
