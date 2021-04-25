CWD="${PWD}"
TSD="$CWD/bootsoff/tests"

cd "$TSD"
shopt -s nullglob

Files=(test_*.py)

pytest ${Files[@]}

cd "$CWD"


