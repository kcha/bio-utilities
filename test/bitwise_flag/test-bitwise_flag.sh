RUN=../../bin/bitwise_flag

check()
{
    if diff $1 $2; then
        echo ok
        return 1
    else
        echo fail
        return 0
    fi
}

exe()
{
    EXP=${1}.txt
    $RUN $1 | grep -oP "\\w+$" - > obs
    check obs $EXP
    rm obs
}

#################################################

echo -n " bitwise_flag.t1: "
exe 0

echo -n " bitwise_flag.t2: "
exe 83

echo -n " bitwise_flag.t3: "
exe 99

echo -n " bitwise_flag.t4: "
exe 1030

echo -n " bitwise_flag.t5: "
exe 3073
