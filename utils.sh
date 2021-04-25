function replace_in_file() { 
    sed -i -e "s!$2!$3!g" "$1"
}

function substitute() {
    name=$1
    name="${name:1:-1}"
    echo ${name^^}
}

function item_in_array() {
    # first argument (required): name of array
    # second argument (required): item

    local -n my_array=$1
    local item=$2
    local status=1

#    echo "looking for $item in ${my_array[@]}"
    for i in ${my_array[@]}; do 
        if [ $i == "$item" ]; then
#	    echo "$item same as $i"
            status=0
            break
        else
#           echo "$item not same as $i "
            true    
        fi
    done
#    echo "returning $status"
    return $status
}

function confirm() {
    # first argument (optional): question
    # second argument (optional, default="No"): default answer
    # third argument (optional): variable to store answer 

    if [ $# -gt 0 ]; then 
       echo -e "$1"
    fi

    if [ $# -gt 1 ]; then 
         default=$2
    else
         default="No"
    fi
    local  __answervar=$3

    local  answer=''
    if [[ "$__answervar" ]]; then
        eval $__answervar="'$answer'"
    else
        echo "$answer"
    fi

    while true
    do
        read -r -p "Are You Sure? [Y/N] [$default] >" input
 
        case $input in 
            [yY][eE][sS]|[yY])
        answer="Yes"
        break
        ;;
            [nN][oO]|[nN])
        answer="No"
        break
        ;;
            "")
	answer="$default"
        break
        ;;
            *)
        echo "Invalid input..."
        ;;
        esac
    done

    if [[ "$__answervar" ]]; then
        eval $__answervar="'$answer'"
	echo "$answer"
    else
        echo "$answer"
    fi
}

#v="$1"
#s="$(substitute $v)"
#echo -e "$s"

