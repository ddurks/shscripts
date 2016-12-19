reset
set term png truecolor
set output "results.png"
set xrange [0:7]
set yrange [1:200]
set grid
set boxwidth .95 relative
set style fill solid 0.5 noborder
plot "results.dat" u 1:2 w boxes lc rgb"blue" notitle

