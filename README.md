# py-tcg-spec-scraper

A very simple tool that scrapes TCG PC TPM Client specification and outputs whether
each algorithm, command or ecc curve has been mentioned in the supplied revisions. 

May be used for different pdf files too.

`constants.py` contains a dictionary of available TPM capabilities from the newest TCG specification (as of May 2021).

Structure in the `pdf` folder must be followed, if a new revision is added, add folder `rev{x+1}` and within file `alg.pdf` 
(TCG TPM Algorithm Registry) and `comm.pdf` (TCG TPM Commands Specification) in their respective folders. Dictionary `res` in `main.py` 
needs to be updated as well.

## How to run it:

No arguments or parameters are available, however, you first have to install PyPDF2:

    pip install PyPDF2

Run:

    python3 main.py

Output is then printed to console (as json)