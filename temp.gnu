set terminal postscript eps color solid linewidth 2 "Helvetica" 22 
set out 'e.eps'
set size 1.2, 0.72

set xlabel 'Guess times'
set ylabel 'Probability' 
set xrange [0:20]
set xtics 2 
plot "aa" u 1:2 w lp pt 7 ps 2 t "10^6"
