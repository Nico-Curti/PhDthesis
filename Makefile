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

svg_img = $(sort $(wildcard img/*.svg))
imgs    = $(patsubst img/%.svg, img/%, $(svg_img))
pdf_img = $(patsubst img/%, img/%.pdf, $(imgs))


all: thesis

convert_img: $(pdf_img)

img/%.pdf: img/%.svg
	inkscape -D -z --file=$< --export-pdf=$@ --export-latex

thesis: $(thesisfile) \
	    $(pdf_img)
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf $(basename $(thesisfile)) -jobname=$(tesiout)
	$(MAKE) clean

relazione:
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf relazione.tex -jobname=relazione
	$(MAKE) clean

.PHONY: clean
clean:
	$(remove) $(tesiout).blg
	$(remove) $(tesiout).log
	$(remove) $(tesiout).out
	$(remove) $(tesiout).fls
	$(remove) $(tesiout).synctex.gz


.PHONY: cleanall
cleanall: clean
	@$(remove) $(tesiout).aux
	@$(remove) $(tesiout).bbl
	@$(remove) $(tesiout).toc
	@$(remove) $(tesiout).fdb_latexmk
