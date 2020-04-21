import numpy as np
import matplotlib.pyplot as plt

def f(t,u1,u2,u3): #array of functions
    return np.array([u1+2*u2-2*u3+np.exp(-t),u2+u3-2*np.exp(-t),u1+2*u2+np.exp(-t)])

a=0
b=1
h=0.01
n=int(1+(b-a)/h)

u1=np.zeros(n)  
u2=np.zeros(n)
u3=np.zeros(n)
t=np.linspace(a,b,n)

u1[0]=3
u2[0]=-1
u3[0]=1
for i in range(n-1):
	k1=h*f(t[i],u1[i],u2[i],u3[i])
	k2=h*f(t[i]+h/2,u1[i]+k1[0]/2,u2[i]+k1[1]/2,u3[i]+k1[2]/2)
	k3=h*f(t[i]+h/2,u1[i]+k2[0]/2,u2[i]+k2[1]/2,u3[i]+k2[2]/2)
	k4=h*f(t[i]+h,u1[i]+k3[0],u2[i]+k3[1],u3[i]+k3[2])
	u1[i+1]=u1[i]+(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
	u2[i+1]=u2[i]+(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
	u3[i+1]=u2[i]+(k1[2]+2*k2[2]+2*k3[2]+k4[2])/6

plt.plot(t,u1,'--g')
plt.plot(t,u2,'--r')
plt.plot(t,u3,'--b')
plt.grid(True)
plt.minorticks_on()
plt.grid(which='minor', linewidth='0.2')

plt.show()
