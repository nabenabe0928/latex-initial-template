while getopts ":d:" o; do
    case "${o}" in
        d) dir=${OPTARG};;
    esac
done


for target in .vscode settings sections appendices figs
do
    cp -r $target $dir
done

for target in appendix.tex ref.bib splncs04.bst submission.tex
do
    cp -r $target $dir
done
