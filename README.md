# Checklist for paper writing
1. Capitalize title, sections, and subsections by [APA](https://capitalizemytitle.com/style/APA/),
2. Itemize with appropriate punctuations,
3. Start captions with a summary without a subject,
4. Describe the instructions of how to read figures or tables with the bolded indicator (Right, Left and so on),
5. For 3x3 figures, use Center for the $x$-axis and Middle for the $y$-axis,
6. Number all the equations,
7. Do not use low-level information in Abstract,
8. Cite papers in Introduction if using any terms that might be not common in the field, and
9. Do not explain in Introduction, but write only why and how in two sentences at most.

# Usage
1. Tap the `Use this template` button to clone this repository for a new repository
2. Change the `bibliographystyle` path of both `submission.tex` and `appendix-full-contents.tex`
3. Add codes required for `preamble.tex` and `user-commands.tex`
4. Add conference specific packages and format to `packages.tex` if required
5. Change the `documentclass` for conference submissions

**NOTE:**

For arXiv upload, `\pdfoutput=1` and `\documentclass{something}` must appear in the first five lines of submission.tex.
Additionally, `ref.bbl` and `appx.bbl` must be included in the zip file for the upload.

# Descriptions of each file
Here are the descriptions for each file in this repository.

```
root
|_ settings/ -- The directory that includes setting files.
|   |_ appendix-information.tex -- The file that we can refer to data labels by \customlabel in Appendix. We need to hard-code the information.
|   |_ author-info.tex -- The file that includes the author information and the paper title.
|   |_ labels-in-main.tex -- The file that defines data labels by \customlabel in the main paper. This information will be used for Appendix.
|   |_ layout.tex -- The file that controls the paper layout. It must be deactivated for conference papers.
|   |_ packages.tex -- The file that defines packages used in the main paper and appendix.
|   |_ paper-status.tex -- The file that controls whether the compile is for underreview (*1), the compile is for submission (*2), and the compile should include appendix in the main paper.
|   |_ preamble.tex -- The file that collects all information needed in preamble.
|   |_ user-commands.tex -- The file that includes user commands used in the main paper and appendix.
|
|_ sections/ -- The directory that includes contents for the main paper and those files must be defined by users.
|   |_ ... (user defined section file 1)
|   :
|   |_ ... (user defined section file N)
|
|_ appendices/ -- The directory that includes contents for the appendix and those files, except appendix-full-contents.tex must be defined by users.
|   |_ appendix-full-contents.tex -- The file that defines the contents to include for the appendix.
|   |_ ... (user defined appendix file 1)
|   :
|   |_ ... (user defined appendix file M)
| 
|_ figs/ -- The directory that includes figures used for the paper.
|   |_ ... (user defined figure file 1)
|   :
|   |_ ... (user defined figure file M)
|
|_ appendix.tex -- The file that defines separated appendix file. Contents will be extracted from appendix-full-contents.tex.
|_ submission.tex -- The file that defines the main content and appendix. Whether including Appendix or not will be determined based on paper-status.tex.
|_ compile.sh -- The shell file to compile both appendix.tex and submission.tex.
|_ ref.bib -- The bibtex file.
|_ splncs04.bst -- The bib style file. Basically this file must be replaced for conference papers.
```

*1 Anonymous or not.

*2 Most likely some comments will be invisible.

# Some rules for readable latex coding
1. Use the following format for each label name:
```
<main/appx>:<section name>:<data format, e.g. tab, fig>:<attribute name>
```
2. Name every single data and add `*` later (we can remove the numbering later anyways)
3. Each Table, Algorithm, Figure should be defined in a separated file to make location changes quicker and easier
4. Equations should be defined in a separated file as it enhances the readability
5. Longer symbols in equations should be defined as a user command for the readability

# Mathematical statements
1. Theorem: a mathematical statement that is proved using rigorous mathematical reasoning
2. Corollary: a result in which the (usually short) proof relies heavily on a given theorem
3. Proposition: a proved and often interesting result, but generally less important than a theorem
4. Lemma: a minor result whose sole purpose is to help in proving a theorem
5. Claim: an assertion that is then proved
