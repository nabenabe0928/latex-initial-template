for fn in submission appendix
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
done
