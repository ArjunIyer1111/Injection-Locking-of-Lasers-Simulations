#---------Attempt at solving laser rate equations using python
# Importing required Packages
from math import sqrt
import cmath
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.size']=20
import time
from scipy import signal
from scipy import interpolate
from scipy.integrate import odeint
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
phi=-0.8
#Defining kappa parameter as defined in documents
kappa=k*R_inj
#Analytically calculating steady state values
#Calculating roots to solve for steady state output amplitude
roots=np.roots([1, -2*kappa*A_fr*np.cos(phi)/gamma_p, -A_fr**2, -gamma_n*2*kappa*A_fr*np.cos(phi)/g/gamma_p])
#selecting the positive real root
A0=np.asscalar(roots[np.isreal(roots) & (0<roots)])
#solving for steady state detuning
del_om_0=-kappa*np.sqrt(1+alpha**2)*A_fr*np.sin(phi+np.arctan(alpha))/A0/2/np.pi
#solving for steady state carrier density
del_N=-2*kappa*A_fr/A0/g*np.cos(phi);
#defining the function to be solved
omega1=1e9*2*np.pi
t_fin=5e5*1e-9
t_step=0.01e-9
trange=np.arange(0.,t_fin,t_step)
sig=signal.square(omega1*trange)
def bessel_lowpass(f_cut, f_samp, order):
	nyq=0.5*f_samp
	normal_cutoff=f_cut/nyq
	b,a =signal.bessel(order,normal_cutoff,'low',analog=False)
	return b,a
def bessel_filtered(sig,fs,order,f_cut):
	b,a=bessel_lowpass(f_cut,fs,order)
	y= signal.lfilter(b,a,sig)
	return y
y=bessel_filtered(sig,1/t_step,3,10e9)


#function to be used to give signal to the solver
z=lambda t1:np.interp(t1,trange,y)
def f(y,t):
 #amplitude differential equations for real and imaginary parts
 dyAr= 0.5*g*(y[2]-N_th)*(y[0]-alpha*y[1])+kappa*A_fr*np.cos(z(t))+del_om_0*2*np.pi*y[1]
 dyAi=0.5*g*(y[2]-N_th)*(y[0]*alpha+y[1])-del_om_0*2*np.pi*y[0]+kappa*A_fr*np.sin(z(t))
 #Carrier density equation
 dyN= J-gamma_n*y[2]-(gamma_p+g*(y[2]-N_th))*(y[0]**2+y[1]**2)
 return  np.asarray([dyAr, dyAi, dyN])

# Declaring initial conditions
ini_cond=np.array([A_fr, 0., N_th])
psol=odeint(f,ini_cond,trange ,rtol=1.e-3)
print("------Total Solver Time = %s seconds-----"%(time.time()-start_time))
out_phase=np.unwrap(2*np.arctan(np.divide(psol[:,1],psol[:,0])))/2+0.8
#plotting the solution
#plt.plot(trange/1.e-9,np.unwrap(2*np.arctan(np.divide(psol[:,1],psol[:,0])))/2+0.8,trange/1.e-9,y,'b-')
#plt.plot(trange/1.e-9,sqrt(np.square(psol[:,1])+np.square(psol[:,0])),'b-')
#plt.xlabel('time(ns)')
#plt.ylabel('amplitude(arbitrary units)')
#plt.title('solution')
#plt.ylim(-3,3)

show()