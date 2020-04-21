import numpy as np
from matplotlib.pyplot import plot, show
import matplotlib.pyplot as plt

a = 1
b = 2
h = 0.1
n = int(1+(b-a)/h)

def y_true(t):
    return t/(1+np.log(t))

def y1(y,t):
    return y/t-(y/t)**2
t = np.linspace(a,b,n)

ytr = np.zeros(n)
yf = np.zeros(n)
ydiff = np.zeros(n)


for i in range(np.size(t)):
    ytr[i]=y_true(t[i])

for i in range(np.size(t)-1):
    yf[0]=1
    yf[i+1]=yf[i]+h*y1(yf[i],t[i])

error_abs=(ytr-yf)
error_rel=error_abs/ytr*100

print('\ntrue value of function is\n',ytr,'\n absolute error is\n',error_abs,'\n relative error\n',error_rel)
plt.xlabel('t')
plt.ylabel('y')
plot(t,ytr,'--r',label='True Function')
plot(t,yf,'--b',label='Calculated Function')
#plot(t,error_rel,'--y')
#plot(t,error_abs,'--g')
plt.legend()
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.show()
