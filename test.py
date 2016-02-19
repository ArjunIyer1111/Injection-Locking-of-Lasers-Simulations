import numpy as np
t_fin=3.e-9
t_step=0.01e-10
t=np.arange(0.,t_fin,t_step)
omega1=1e9*2*np.pi
sig=np.sin(omega1*t)
def h(t1):
 return np.asscalar(sig[np.where(t==t1)])

print(h(t[256]))