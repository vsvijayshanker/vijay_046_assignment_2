import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

f1=solve_ivp(lambda t, y: t*np.exp(3*t)-2*y, [0, 1], [0],t_eval=np.linspace(0,1))
t=np.linspace(0,1)
ytr=(5*t-1)*np.exp(3*t)/25-np.exp(-2*t)/25
plt.plot(f1.t,f1.y[0],'--b',label='1.Using solve_ivp')
plt.plot(t,ytr,'--r',label='1.Analytic Solution')
plt.legend()
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
#Frist part end

#second part start
f1=solve_ivp(lambda t, y: 1-(t-y)**2, [2, 3], [1],t_eval=np.linspace(2,3))
t=np.linspace(2,3)
ytr=t
plt.subplots()
plt.plot(f1.t,f1.y[0],'--b',label='2.Using solve_ivp')
plt.plot(t,ytr,'--r',label='2.Analytical Solution')
plt.legend()
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
#second part end

#third part start
f1=solve_ivp(lambda t, y: 1+y/t, [1, 2], [2],t_eval=np.linspace(1,2))
t=np.linspace(1,2)
ytr=t*(2+np.log(t))
plt.subplots()
plt.plot(f1.t,f1.y[0],'b',label='3.Using solve_ivp')
plt.plot(t,ytr,'--r',label='3.Analytical Solution')
plt.legend()
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
#third part end

#fourth part stard
f1=solve_ivp(lambda t, y: np.cos(2*t)+np.sin(3*t), [0, 1], [1],t_eval=np.linspace(0,1))
t=np.linspace(0,1)
ytr=np.sin(2*t)/2-np.cos(3*t)/3+4/3
plt.subplots()
plt.plot(f1.t,f1.y[0],'b',label='4.Using solve_ivp')
plt.plot(t,ytr,'--r',label='4.Analytical Solution')
plt.legend()
plt.grid(True,)
plt.minorticks_on()
plt.grid(which='major',linewidth='0.5')
plt.grid(which='minor',linewidth='0.2')
plt.show()

