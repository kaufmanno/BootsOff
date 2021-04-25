. utils.sh

CWD="${PWD}"  # project directory
DCD="$CWD/docs"
ULD="$CWD/uml_diagrams"

. test_code.sh
cp "$CWD/definitions.py" "$DCD/source/definitions.py" # for publication on https://readthedocs.org
cd "$ULD" || exit 1
python3 update_uml_in_docs.py
cd "$DCD" || exit 1
rm -rf build/*
make html
cd "$CWD" || exit 1
git add "$DCD/*"
git commit -m "Build docs"
PUSH=""
confirm "You are about to push your remote repository.\nDo you really want to do this now?" "Yes" PUSH
if [[ "$PUSH" == "Yes" ]]; then 
    echo -e "\nPushing to remote\n"
    git push
else
    echo -e "\nA commit was done but changes have not been pushed to remote...\n"
fi

firefox "file://$DCD/build/html/index.html"

