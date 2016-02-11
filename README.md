# Injection-Locking-of-Lasers-Simulations
These are MATLAB codes which simulate Injection Locking in laser cavity for the purpose of regeneration of Phase Shift Keying signals. 
These codes are an attempt to understand the process of regenearation and simulate and estimate performances in such a regeneration system.
This specific repository deals with optimizing a rate equation code for a laser injection locked system, injection locked with a BPSK signal. 
Now to accurately estimate the BER of such a process one needs to solve this for 10^6 pulses of BPSK data and that means solving rate equation for 10^6 and that is a lot of computation.
Through this repository I wish to describe how I optimized a 'bad' Matlab code which took about 1 minute to 20 seconds, just by suitably optimising my code. 
We wish to optimize a lot more and this repository captures that process. We would like to have additional speedup of about 5 times or so.
