import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
h = 0.1
n = int(1+(b-a)/h) #number of points

#defining the true function
y0 = np.exp(1)
def y_true(t):
    return y0*(np.exp(-9*t))

#defining first order differntiation
def y1(y,t):
    return -9*y

t = np.linspace(a,b,n) #range of t

yb=np.zeros(n)      #array of function for backward integration
ytr=np.zeros(n)     #array of true function
ydiff=np.zeros(n)   #array of differential function

for i in range(np.size(t)):     #evaluating the true function
    ytr[i]=y_true(h*i)

for i in range(np.size(t)-1):   #evaluating the backward integration
    yb[0]=y0
    yb[i+1]=yb[i]/(1+9*h)
print('\n\nt is\n',t,'\n\ntrue function is \n',ytr,'\n\n backward calculated function is\n', yb)
plt.subplots()
plt.plot(t,ytr,'--r',label='True Function')
plt.plot(t,yb,'--b',label='Calculated Function')
plt.legend()
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
#first part end
#
#second part start
#defining the true function
y0 = 1/3
def y_true(t):
    return y0*(np.exp(-20*t))+t**2

#defining first order differntiation
def y1(y,t):
    return -20*(y-t**2)+2*t


t = np.linspace(a,b,n) #range of t

yb=np.zeros(n)      #array of function for backward integration
ytr=np.zeros(n)     #array of true function
ydiff=np.zeros(n)   #array of differential function

for i in range(np.size(t)):     #evaluating the true function
    ytr[i]=y_true(h*i)


for i in range(np.size(t)-1):   #evaluating the backward integration
    yb[0]=y0
    yb[i+1]=(yb[i]+20*h*t[i]**2+2*h*t[i])/(1+20*h)
print('\n\nt is\n',t,'\n\ntrue function is \n',ytr,'\n\n backward calculated function is\n', yb)
plt.subplots()
plt.plot(t,ytr,'--r',label='True Function')
plt.plot(t,yb,'--b',label='Calculated Function')
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.legend()
plt.show()

