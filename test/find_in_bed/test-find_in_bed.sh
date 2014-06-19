RUN=../../bin/find_in_bed

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
    EXP=${2}_${3}_${4}.txt
    $RUN $@ > obs
    check obs $EXP
    rm obs
}

#################################################

echo -n " find_in_bed.t1: "
exe a.bed chr1 1 10

echo -n " find_in_bed.t2: "
exe a.bed chr1 1 20

echo -n " find_in_bed.t3: "
exe a.bed chr2 1000 1011

echo -n " find_in_bed.t4: "
exe a.bed chr2 999 1001

echo -n " find_in_bed.t5: "
exe a.bed chr2 999 1012
