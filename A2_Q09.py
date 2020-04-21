import numpy as np
import matplotlib.pyplot as plt

a=1
b=3
h=0.01
n=int(1+(b-a)/h)

def f(y,t):     
    return y*(y+1)/t

def f_true(t):           #true function
    return 2*t/(1-2*t)

t=np.linspace(a,b,n)
ytr=np.zeros(n) #array of true function

y=np.zeros(n)   #array of calculated function

for i in range(np.size(t)):
    ytr[i]=f_true(t[i])

y[0]=-2
for i in range(n-1):
    k1=h*f(y[i],t[i])
    k2=h*f(y[i]+k1/2,t[i]+h/2)
    k3=h*f(y[i]+k2/2,t[i]+h/2)
    k4=h*f(y[i]+k3,t[i]+h)
    y[i+1]=y[i]+(k1+2*k2+2*k3+k4)/6
    if np.abs((y[i+1]-y[i])/(y[i+1]))< 1e-4 :  #condition for adaptation
        y[i+1+1]=2*y[i+1]-y[i]                  
        i=i+1
print(ytr)

plt.plot(t,ytr,'r',label='True Function')
plt.plot(t,y,'--b',label='Calculated Function')
plt.legend()
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.show()

