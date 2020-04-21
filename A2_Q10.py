#due to the computation limit and asymptotic behaviour of solution
#i am calculating for 1e5 points and
#extrem point has same value fo other values of t
#due to computation limits i am modifying the equation as t=u/(1-u)
#range of u(0,1)spans the range of t(o,inf)
import numpy as np
import matplotlib.pyplot as plt

a=0
b=1
h=1e-5
n=int(1+(b-a)/h)

def f(u,x):     #modified equation
    return 1/(u**2+(x*(1-u))**2)

u1=np.linspace(a,b,n)
u=np.zeros(n-1)     #a reduced size is taken to avoid devision by zero
x=np.zeros(n-1)     #a reduced size is taken to avoid devision by zero
x[0]=1
for i in range(n-2):#a reduced range is taken to avoid devision by zero
    u[0]=u1[0]
    k1=h*f(u[i],x[i])
    k2=h*f(u[i]+h/2,x[i]+k1/2)
    k3=h*f(u[i]+h/2,x[i]+k2/2)
    k4=h*f(u[i]+h,x[i]+k3)
    x[i+1]=x[i]+(k1+2*k2+2*k3+k4)/6
    u[i+1]=u[0]+h*(i)
    if np.abs((x[i+1]-x[i])/x[i+1])<1e-9:   #setting tollence to save computation time
        for j in range(n-1-i):
            x[i+j]=x[i+1]
            u[i+j]=u[0]+(i+j)
            
        break
    
t=u/(1-u)
print('x at t=3.5e6 is',x[n-2])
plt.subplots()
plt.plot(t,x,'g')
plt.xlim([0,100])
plt.plot(t,x,'--r')
plt.show()

