# Stretched Exponential (KWW) Function - Parametric Fitting
# Will be interfaced with Gnuplot.py (when I have time)

gnuplot
reset session

set term pngcairo background "#ffffff" enhanced font "Arial-Bold, 10" fontscale 1.0 size 500, 500
set output "path/to/new_file_name.png"
set title "Stretched Exponential (KWW) Curve Fit"
set xlabel "time (fs)" rotate parallel
set ylabel "Simulated S (q, t)" rotate parallel

f(x) = exp(-(x/tau_kww)**beta) # [base function]
f(x) = A * exp(-(x/tau1)**beta1) + (1-A) * exp(-(x/tau2)**beta2) # [double function]

a1 = 1; tau1 = guess; beta1 = guess; tau2 = guess; beta2 = guess; fit f(x) "fsqt_q0.100.txt" via tau1, beta1, tau2, beta2, a1
# S(q,0) = 1, so there is no need to instantiate a second ‘a’ parameter.

set log x
p f(x) lw 3, "file_name.txt"
