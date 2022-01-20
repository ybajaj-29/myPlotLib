# Stretched Exponential (KWW) Function - Parametric Fitting
# Will be interfaced with Gnuplot.py

gnuplot
reset session

set term pngcairo background "#ffffff" enhanced font "Arial-Bold, 10" fontscale 1.0 size 500, 500
set output “fsqt_q(file_name).png”
set title "Stretched Exponential (KWW) Curve Fit"
set xlabel "time (fs)" rotate parallel
set ylabel "Simulated S (q, t)" rotate parallel

f(x) = exp(-(x/tau)**beta)
tau = approx_fit; beta = approx_fit; fit g(x) “file_name” via tau, beta

set log x
p g(x) lw 2, “file_name”