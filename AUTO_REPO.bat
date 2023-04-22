mkdir data
cd data
mkdir in, out
cd in
echo 2> .gitignore
echo * > .gitignore
echo !.gitignore >> .gitignore
cd.. 
cd out 
echo 2> .gitignore
echo * > .gitignore
echo !.gitignore >> .gitignore
cd..
cd.. 
mkdir doc, src, viz
cd doc 
echo * > .gitignore
echo !.gitignore >> .gitignore
cd..
cd src
mkdir py, sql
cd py 
cd doc 
echo * > .gitignore
echo !.gitignore >> .gitignore
cd..
cd sql
cd doc 
echo * > .gitignore
echo !.gitignore >> .gitignore
cd..
cd..
cd viz
echo * > .gitignore
echo !.gitignore >> .gitignore
cd..
echo 2> requirements.txt
echo 2> .gitignore
echo .venv > .gitignore
py -m venv .venv 

