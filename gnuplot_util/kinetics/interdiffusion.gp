# Gold (Au) and Silver (Ag) Interdiffusion; Fig. 11.6 (R.)
set term pngcairo background "#ffffff" enhanced font "Arial-Bold, 10" fontscale 1.0 size 500, 500
set output "path/to/file_name.png"
set title "Gold (Au) and Silver (Ag) Interdiffusion; Fig. 11.6 (R.)"
set xrange [-100:100]
set yrange [0:1]
set xlabel "Distance (um)" rotate parallel
set ylabel "Scaled Concentration (unitless)" rotate parallel
D_avg = 0.373
C(x,t) = 0.5*erfc(x/((4*D_avg*t)**0.5))
plot for [t=100:100] C(x,t) t "t=100", for [t=500:500] C(x,t) t "t=500", for [t=1000:1000] C(x,t) t "t=1000", for [t=2000:2000] C(x,t) t "t=2000"
