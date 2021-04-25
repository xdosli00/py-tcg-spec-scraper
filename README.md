# py-tcg-spec-scraper

A very simple tool that scrapes TCG PC TPM Client specification and outputs whether
each algorithm, command or ecc curve has been mentioned in the supplied revisions. 

May be used for different pdf files too.

`constants.py` contains a dictionary of available TPM capabilities from the newest TCG specification (as of May 2021).

## How to run it:

No arguments or parameters are available, however, you first have to install PyPDF2:

    pip install PyPDF2

Output is then printed to console (as json)