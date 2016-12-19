reset
n=2
total_box_width_relative=0.75
gap_width_relative=0.1
reset
set term png truecolor
set output "gender.png"
set xlabel "Year"
set ylabel "Number of Students"
set xrange [2012:2019]
set yrange [0:100]
set grid
set boxwidth total_box_width_relative/n relative
set style fill solid 0.5 noborder
plot "results.dat" u 1:2 w boxes lc rgb"red" notitle,\
     "results.dat" u ($1+.3):3 w boxes lc rgb"blue" notitle
