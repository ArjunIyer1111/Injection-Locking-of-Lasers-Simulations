import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
t=np.linspace(0,1,1000)
sq_fun=signal.square(2*np.pi*t*10)
sam_rate=len(t)/1;
def bessel_lowpass(f_cut, f_samp, order):
	nyq=0.5*f_samp
	normal_cutoff=f_cut/nyq
	b,a =signal.bessel(order,normal_cutoff,'low',analog=False)
	return b,a
def bessel_filtered(sig,fs,order,f_cut):
	b,a=bessel_lowpass(f_cut,fs,order)
	y= signal.lfilter(b,a,sig)
	return y
y=bessel_filtered(sq_fun,sam_rate,2,30)
plt.plot(t,y)
#plt.xlim(0,0.5*30)
show()