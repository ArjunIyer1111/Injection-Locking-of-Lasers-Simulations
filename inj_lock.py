#---------Attempt at solving laser rate equations using python
# Importing required Packages
import cmath
import numpy as np
from odeintw import odeintw
import matplotlib.pyplot as plt
plt.rcParams['font.size']=20
import time
from pylab import *
#importing parameters from another file called Params.py
#from Param import f
# Starting CPU clock for timing the program
start_time=time.time()
#declaring and importing parameters
q=1.6022e-19
g=1e4
N_th=2.214e8
gamma_p = 1/3.2e-12
gamma_n = 0.5e9
alpha =3
J_th = 33.5e-3/q
J = 5*J_th
k=(1/7e-12)*(1-0.548**2)/0.548
A_fr=np.sqrt((J-gamma_n*N_th)/gamma_p)
#intiliazing injection power
R_inj= np.power(10,(-20/20))
#intializing phase
phi=-0.5
#Defining kappa parameter as defined in documents
kappa=k*R_inj
#Analytically calculating steady state values
#Calculating roots to solve for steady state output amplitude
roots=np.roots([1, -2*kappa*A_fr*np.cos(phi)/gamma_p, -A_fr**2, -gamma_n*2*kappa*A_fr*np.cos(phi)/g/gamma_p])
#selecting the positive real root
A0=np.asscalar(roots[np.isreal(roots) & (0<roots)])
#solving for steady state detuning
del_om_0=-kappa*np.sqrt(1+alpha**2)*A_fr*np.sin(phi+np.arctan(alpha))/A0/2/np.pi
#defining the function to be solved
def f(y,t):
  #Complex amplitude differential equation
 dyA= 0.5*g*(y[1]-N_th)*(1+1j*alpha)*y[0]+kappa*A_fr-1j*del_om_0*2*np.pi*y[0]
 #Carrier density equation
 dyN= J-gamma_n*y[1]-(gamma_p+g*(y[1]-N_th))*abs(y[0])**2
 return  np.asarray([dyA, dyN])

# Declaring initial conditions
ini_cond=np.array([A_fr, N_th], dtype=complex128)
t_fin=3.e-9
t_step=0.05e-10
t=np.arange(0.,t_fin,t_step)

psol=odeintw(f,ini_cond,t, rtol=1.e-4)
print("------Total Solver Time = %s seconds-----"%(time.time()-start_time))
#plotting the solution
plt.plot(t/1.e-9,abs(psol[:,0]),'rx-')
plt.xlabel('time(ns)')
plt.ylabel('amplitude(arbitrary units)')
plt.title('solution')

show()