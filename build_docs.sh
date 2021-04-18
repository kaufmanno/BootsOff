CWD="${PWD}"  # project directory
DCD="$CWD/docs"
ULD="$CWD/uml_diagrams"

. test_code.sh
cp "$CWD/definitions.py" "$DCD/source/definitions.py" # for publication on https://readthedocs.org
cd "$ULD"
python3 update_uml_in_docs.py
cd "$DCD"
make html
cd "$CWD"
firefox "file://$DCD/build/html/index.html"
git add "$DCD/*"
git commit -m "Build docs"
git push
