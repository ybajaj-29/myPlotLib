# Enhanced EPS Output Terminal

gnuplot
reset session

set term postscript eps background "#ffffff" enhanced color font "Arial-Bold, 10" fontscale 1.0
set output "*.eps"

set key left bottom
set key box lw 5 width 2 height 3 opaque
set key font ",20"

set xlabel 'q (nm^{-1})' font "Arial-Bold, 16"
set xtics (2, 3, 4, 5, 6, 7, 8, 9, 10, "2" 20)
set xrange [1:20]

set ylabel '{/Symbol t}_{kww(ns)}' font "Arial-Bold, 16"
set format y "10^{%L}"

set log xy
plot  "data_1.txt" u 2:($1*0.6) w l lw 3 lc rgb 'red' title 'data_1',
      "data_2.txt" u 2:($1*0.6) w l lw 3 dt 4 lc rgb 'red' title 'data_2',
      "data_3.txt" u 2:($1*0.6) w l lw 3 lc rgb 'orange' title 'data_3',
      "data_4.txt" u 2:($1*0.6) w l lw 3 dt 4 lc rgb 'orange' title 'data_4'
