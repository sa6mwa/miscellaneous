set xtics 1
unset ytics
set grid
set xlabel 'Wire Length (meters)'
set title 'Random Wire Lengths to Avoid'
set term png size 5000,120
set output 'f.png'
plot [:][:1] 'f' with filledcurves notitle
