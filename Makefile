ifeq ($(OS), Windows_NT)
	remove = del /s
	sep = \\
else
	remove = rm -f
	sep = /
endif

tesifile = main.tex
tesiout = PhDThesis
tex_dir = tex

tesi: $(tesifile) \
	   $(wildcard img/**/*)
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf $(basename $(tesifile)) -jobname=$(tesiout)
	$(MAKE) clean

.PHONY: clean
clean: $(paper_out)
	$(remove) $(tesiout).blg
	$(remove) $(tesiout).log
	$(remove) $(tesiout).out
	$(remove) $(tesiout).fls
	$(remove) $(tesiout).synctex.gz

.PHONY: cleanall
cleanall: $(paper_out) clean
	@$(remove) $(tesiout).aux
	@$(remove) $(tesiout).bbl
	@$(remove) $(tesiout).fdb_latexmk
