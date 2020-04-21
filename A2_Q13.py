import numpy as np
import matplotlib.pyplot as plt

def f2(t,f,f1):
    return np.array([f1,t*np.log(t)-2*f/(t**2)+2*f1/t])

a=1
b=2
h=0.001
n=int(1+(b-a)/h)

f1=np.zeros(n)      #first derivative
f=np.zeros(n)       #function
t=np.linspace(a,b,n)#domain

f1[0]=0
f[0]=1
for i in range(n-1):
    fd=h*f2(t[i],f[i],f1[i])    #step integral of first and second derivative
    f[i+1]=f[i]+fd[0]
    f1[i+1]=f1[i]+fd[1]

ytr=7*t/4+t**3/2*np.log(t)-0.75*t**3    #true function

plt.plot(t,f,'g',label='Calculated Function')
plt.plot(t,ytr,'--r',label='True Function')
plt.legend()
plt.grid(True)
plt.minorticks_on()
plt.grid(which='minor', linewidth='0.2')
plt.show()
