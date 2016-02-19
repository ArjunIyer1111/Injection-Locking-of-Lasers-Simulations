#---------Attempt at integrating using python
import cmath
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
from pylab import *
start_time=time.time()
def f(y,t):
   derivs= t*t
   return derivs   

y0=1;
t_s=0.01;
psol=[]
psol2=[]
psol.append(y0)
psol2.append(y0)
t_fin=10;
trange=np.asarray(np.arange(0.,t_fin,t_s))
l=len(trange)
for i in range(l-1):
   psol.append(psol[i]+t_s*f(psol[i],trange[i]))
   psol[i+1]=psol[i]+t_s*(f(psol[i+1],trange[i+1])+f(psol[i],trange[i]))/2
   psol2.append(psol[i]-(trange[i]**3/3)-1)
print("------%s seconds-----"%(time.time()-start_time))
subplot(121)
#plt.figure(1)
plt.plot(trange,psol,'-')
plt.xlabel('Independent variable')
plt.ylabel('Dependent Variable')
plt.title('solution')
subplot(122)
#plt.figure(1)
plt.plot(trange,psol2,'-')
ylim(-3e-4,3e-4)
plt.xlabel('Independent variable')
plt.ylabel('error')
plt.title('Error')
show()