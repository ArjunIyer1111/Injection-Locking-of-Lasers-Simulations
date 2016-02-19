#----------Using pythons solver packages-----------
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

y0=0;
t_s=0.001;
psol=[]
psol2=[]
psol.append(y0)
psol2.append(y0)
t_fin=100;
trange=np.asarray(np.arange(0.,t_fin,t_s))
l=len(trange)
psol=odeint(f,y0,trange)
#psol2= np.power(trange,3)/3
#psol2.tolist()
print("------%s seconds-----"%(time.time()-start_time))
#print(psol2)
#subplot(121)
#plt.figure(1)
plt.plot(trange,psol,'-')
plt.xlabel('Independent variable')
plt.ylabel('Dependent Variable')
plt.title('solution')
#subplot(122)
#plt.figure(1)
#plt.plot(trange,psol2,'-')
#xlim(-3e-4,3e-4)
#plt.xlabel('Independent variable')
#plt.ylabel('error')
#plt.title('Error')
show()