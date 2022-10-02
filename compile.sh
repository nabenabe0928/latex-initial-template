ref=ref  # the bibtex file name

for fn in submission
# for fn in appendix
# for fn in submission appendix
do
    mkdir out/
    pdflatex ${fn}.tex
    pbibtex ${fn}
    pbibtex appx
    pdflatex ${fn}.tex
    pdflatex ${fn}.tex
    mv ${fn}.* out/
    mv appx.* out/
    mv out/${fn}.tex .
    python label_extractor.py --file ${fn} --ref ${ref}
done
