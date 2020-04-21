import numpy as np
import matplotlib.pyplot as plt

a=0
b=1
h=0.01
n=int(1+(b-a)/h)

def f2(f,f1,t):     #second derivative function
    return np.array([f1,2*f1-f+t*np.exp(t)-t])

def f_true(t):           #true function
    return (2-t)*(np.exp(t))+((np.exp(t))*t**3/6)-t-2

t=np.linspace(a,b,n)
ytr=np.zeros(n) #array of true function
f1=np.zeros(n)  #array of first derivative
y=np.zeros(n)   #array of calculated function

for i in range(np.size(t)):
    ytr[i]=f_true(t[i])

f1[0]=0
y[0]=0
for i in range(np.size(t)-1):
    k1=h*f2(y[i],f1[i],t[i])
    k2=h*f2(y[i]+k1[0]/2,f1[i]+k1[1]/2,t[i]+h/2)
    k3=h*f2(y[i]+k2[0]/2,f1[i]+k2[1]/2,t[i]+h/2)
    k4=h*f2(y[i]+k3[0],f1[i]+k3[1],t[i]+h)
    y[i+1]=y[i]+(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
    f1[i+1]=f1[i]+(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
    
print(ytr)

plt.plot(t,ytr,'r',label='True Function')
plt.plot(t,y,'--b',label='Calculated Function')
plt.legend()
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.show()

