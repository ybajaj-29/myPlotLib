# Stretched Exponential (KWW) Function - Parametric Fitting
# Will be interfaced with Gnuplot.py

gnuplot
reset session

set term pngcairo background "#ffffff" enhanced font "Arial-Bold, 10" fontscale 1.0 size 500, 500
set output "fsqt_q(file_name).png"
set title "Stretched Exponential (KWW) Curve Fit"
set xlabel "time (fs)" rotate parallel
set ylabel "Simulated S (q, t)" rotate parallel

f(x) = exp(-(x/tau)**beta)
tau = your_approx; beta = your_approx; fit f(x) "file_name" via tau, beta

set log x
p f(x) lw 3, "file_name"
