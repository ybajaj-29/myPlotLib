# erf(x) and erfc(x); -3 <= x <= 3
set term pngcairo background "#ffffff" enhanced font "Arial-Bold, 10" fontscale 1.0 size 500, 500
set output "path/to/file_name.png"
set xrange [-3:3]
set grid xtics ytics
set xlabel "x" rotate parallel
set ylabel "erf(x)" rotate parallel
plot erf(x)
set output "path/to/new_file_name.png"
set ylabel "erfc(x)" rotate parallel
plot erfc(x)
