reset
dx=5.
n=2
total_box_width_relative=0.35
gap_width_relative=0.1
d_width=(gap_width_relative+total_box_width_relative)*dx/2.
reset
set term png truecolor
set output "ethnicity.png"
set xlabel "Year"
set ylabel "Number of Students"
set xrange [2012:2019]
set yrange [0:100]
set grid
set boxwidth total_box_width_relative/n relative
set style fill solid 0.5 noborder
plot "ethnicresults.dat" u 1:2 w boxes lc rgb"green" notitle,\
     "ethnicresults.dat" u ($1+.1):3 w boxes lc rgb"red" notitle,\
     "ethnicresults.dat" u ($1+.2):4 w boxes lc rgb"orange" notitle,\
     "ethnicresults.dat" u ($1+.3):5 w boxes lc rgb"blue" notitle,\
     "ethnicresults.dat" u ($1+.4):6 w boxes lc rgb"black" notitle,\
     "ethnicresults.dat" u ($1+.5):7 w boxes lc rgb"yellow" notitle,\
     "ethnicresults.dat" u ($1+.6):8 w boxes lc rgb"purple" notitle
