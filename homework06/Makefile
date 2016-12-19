all: diversity.pdf

diversity.pdf: gender.png ethnicity.png
	pdflatex diversity.tex
	
gender.png: histogram.plt
	gnuplot histogram.plt

ethnicity.png: histogram1.plt
	gnuplot histogram1.plt
	
clean:
	rm -f diversity.pdf gender.png ethnicity.png
