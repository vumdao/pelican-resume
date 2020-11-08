rm -r output
pelican content/ -s pelicanconf.py -p 8000
pelican -l content -o output -s pelicanconf.py -p 8000 -r
