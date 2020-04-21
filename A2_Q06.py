import numpy as np
import matplotlib.pyplot as plt


h=0.01
t1=10

n=int(1+(t1/h))

def f2(x,f1,t):
    return np.array([f1,-g])    #array of function of 1st and 2nd derivative

def x_true(t):
    return g*(-t*t/2+t1*t/2)        #true function


t=np.linspace(0,t1,n)   
x=np.zeros(n)
f1=np.zeros(n)
g=np.zeros(8)


x[0]=0

for j in range(np.size(g)):              #calculating overshoot/undershoot for 8 different initial values of f1
    
    f1[0]=(g[j]*(0.9+h*0.5)*t1)/2
    for i in range(n-1):
        k=h*f2(x[i],f1[i],t[i])
        x[i+1]=x[i]+k[0]
        f1[i+1]=f1[i]+k[1]

    plt.plot(t,x,'--')

xtr=x_true(t)
plt.plot(t,xtr,'y',label='True Function')

plt.legend()
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.show()
