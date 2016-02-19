#import time
import numpy as np
#-------Parameter File------------
#start_time=time.time()
def f():
  q=1.6022e-19
  Lambda=1550e-9
  g=1e4
  N_th=2.214e8
  gamma_p = 1/3.2e-12
  gamma_n = 0.5e9
  t_in = 7e-12
  r0 = 0.548
  alpha =3
  V = 120e-18
  Ith = 33.5e-3
  J_th = Ith/q
  J = 5*J_th
#Einj = 0
#dwinj = 0
#Rin = 4
#Rout = 50
  k=(1/t_in)*(1-r0**2)/r0
  A_fr=np.sqrt((J-gamma_n*N_th)/gamma_p)
  params= np.array([g, N_th, gamma_p, gamma_n, alpha, J_th, J, k, A_fr])
  return params 
  
#z= 5+1j*6
#print(time.time()-start_time)