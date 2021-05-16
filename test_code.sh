CWD="${PWD}"
TSD="$CWD/tests"

cd "$TSD" || exit 1
shopt -s nullglob

Files=(test_*.py)

pytest ${Files[@]}

cd "$CWD" || exit 1
