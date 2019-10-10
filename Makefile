ifeq ($(OS), Windows_NT)
	remove = del /s
	sep = \\
else
	remove = rm -f
	sep = /
endif

thesisfile = main.tex
tesiout = PhDThesis
tex_dir = tex

chapter1 = Chapter1.tex
chapter1out = Chapter1

chapter2 = Chapter2.tex
chapter2out = Chapter2

chapter3 = Chapter3.tex
chapter3out = Chapter3

Appendix = Appendix.tex
appendixout = Appendix

svg_img = $(sort $(wildcard img/*.svg))
imgs    = $(patsubst img/%.svg, img/%, $(svg_img))
pdf_img = $(patsubst img/%, img/%.pdf, $(imgs))


all: thesis chapter1 chapter2 chapter3 appendix

convert_img: $(pdf_img)

img/%.pdf: img/%.svg
	inkscape -D -z --file=$< --export-pdf=$@ --export-latex

thesis: $(thesisfile) \
	    $(pdf_img)
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf $(basename $(thesisfile)) -jobname=$(tesiout)
	$(MAKE) clean

chapter1: $(chapter1) \
	    		$(pdf_img)
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf $(basename $(chapter1)) -jobname=$(chapter1out)
	$(MAKE) clean

chapter2: $(chapter2) \
	    		$(pdf_img)
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf $(basename $(chapter2)) -jobname=$(chapter2out)
	$(MAKE) clean

chapter3: $(chapter3) \
	    		$(pdf_img)
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf $(basename $(chapter3)) -jobname=$(chapter3out)
	$(MAKE) clean

appendix: $(Appendix) \
	    		$(pdf_img)
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf $(basename $(Appendix)) -jobname=$(appendixout)
	$(MAKE) clean

.PHONY: clean
clean:
	$(remove) $(tesiout).blg
	$(remove) $(tesiout).log
	$(remove) $(tesiout).out
	$(remove) $(tesiout).fls
	$(remove) $(tesiout).synctex.gz

	$(remove) $(chapter1out).blg
	$(remove) $(chapter1out).log
	$(remove) $(chapter1out).out
	$(remove) $(chapter1out).fls
	$(remove) $(chapter1out).synctex.gz

	$(remove) $(chapter2out).blg
	$(remove) $(chapter2out).log
	$(remove) $(chapter2out).out
	$(remove) $(chapter2out).fls
	$(remove) $(chapter2out).synctex.gz

	$(remove) $(chapter3out).blg
	$(remove) $(chapter3out).log
	$(remove) $(chapter3out).out
	$(remove) $(chapter3out).fls
	$(remove) $(chapter3out).synctex.gz

	$(remove) $(appendixout).blg
	$(remove) $(appendixout).log
	$(remove) $(appendixout).out
	$(remove) $(appendixout).fls
	$(remove) $(appendixout).synctex.gz

.PHONY: cleanall
cleanall: clean
	@$(remove) $(tesiout).aux
	@$(remove) $(tesiout).bbl
	@$(remove) $(tesiout).toc
	@$(remove) $(tesiout).fdb_latexmk

	@$(remove) $(chapter1out).aux
	@$(remove) $(chapter1out).bbl
	@$(remove) $(chapter1out).toc
	@$(remove) $(chapter1out).fdb_latexmk

	@$(remove) $(chapter2out).aux
	@$(remove) $(chapter2out).bbl
	@$(remove) $(chapter2out).toc
	@$(remove) $(chapter2out).fdb_latexmk

	@$(remove) $(chapter3out).aux
	@$(remove) $(chapter3out).bbl
	@$(remove) $(chapter3out).toc
	@$(remove) $(chapter3out).fdb_latexmk

	@$(remove) $(appendixout).aux
	@$(remove) $(appendixout).bbl
	@$(remove) $(appendixout).toc
	@$(remove) $(appendixout).fdb_latexmk