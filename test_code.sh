CWD="${PWD}"
TSD="$CWD/tests"

cd "$TSD"
shopt -s nullglob

Files=(test_*.py)

pytest ${Files[@]}

cd "$CWD"


