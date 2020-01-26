ifeq ($(OS), Windows_NT)
	remove = del /s
	magick = magick.exe convert
	sep = \\
else
	remove = rm -f
	magick = convert
	sep = /
endif

file = presentation.tex
out = presentation
tex_dir = tex

svg_img = $(sort $(wildcard img/*.svg))
imgs    = $(patsubst img/%.svg, img/%, $(svg_img))
pdf_img = $(patsubst img/%, img/%.pdf, $(imgs))

gif_img = $(sort $(wildcard img/*.gif))
gif_split = $(patsubst img/%.gif, gif/%-0.png, $(gif_img))

all: presentation

convert_img: $(pdf_img)

img/%.pdf: img/%.svg
	inkscape -D -z --file=$< --export-pdf=$@ --export-latex

gif/%-0.png: img/%.gif
	@mkdir -p gif
	$(magick) -coalesce $< gif/$*.png

presentation: $(file) \
			$(pdf_img) $(gif_split)
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf $(basename $(file)) -jobname=$(out)
	$(MAKE) clean


.PHONY: clean
clean:
	$(remove) $(out).blg
	$(remove) $(out).fls
	$(remove) $(out).log
	$(remove) $(out).out
	$(remove) $(out).snm
	$(remove) $(out).synctex.gz


.PHONY: cleanall
cleanall: clean
	@$(remove) $(out).aux
	@$(remove) $(out).fdb_latexmk
	@$(remove) $(out).bbl
	@$(remove) $(out).nav
	@$(remove) $(out).toc
