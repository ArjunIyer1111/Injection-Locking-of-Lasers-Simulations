#----------Using pythons solver packages-----------
#---------Attempt at integrating coupled differential equations using python
import cmath
import numpy as np
import scipy.integrate 
import matplotlib.pyplot as plt
plt.rcParams['font.size']=20
import time
from pylab import *

start_time=time.time()
def f(y,t):
   dy0=y[1]
   dy1=-y[0]
   derivs= array([dy0, dy1])
   return derivs   

def jac(y,t):
 j1=[0, 1]
 j2=[-1, 0]
 return np.asarray([j1, j2])

y0=array([0,1])
t_s=0.01
#psol=[]
#psol2=[]
#psol.append(y0)
#psol2.append(y0)
t_fin=100
trange=np.asarray(np.arange(0.,t_fin,t_s))
#l=len(trange)
psol=scipy.integrate.odeint(f,y0,trange, Dfun=jac)
#psol2= np.power(trange,3)/3
#psol2.tolist()
print("------%s seconds-----"%(time.time()-start_time))
#print(psol2)
subplot(121)
#plt.figure(1)
plt.plot(trange,psol[:,0],'-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('solution')
subplot(122)
#plt.figure(1)
plt.plot(trange,(psol[:,0]-np.sin(trange))/1.e-6,'-')
#xlim(-3e-4,3e-4)
plt.xlabel('x')
plt.ylabel('error(1e-6)')
plt.title('Error')
show()