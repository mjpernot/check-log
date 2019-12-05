#!/bin/bash
# Blackbox testing program for the check_log.py program.

BASE_PATH=$PWD

printf "Scenario 1:  check_log blackbox testing...One file check\n"
printf "\tFull check\n"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -z
$(cmp -s test/blackbox/check_log/basefiles/test1a_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "\n\tPartial check\n"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -m test/blackbox/check_log/basefiles/test1b_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test1b_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "\n\tNo Entry Found check\n"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -m test/blackbox/check_log/basefiles/test1c_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test1c_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "\n\tIgnore Message check\n"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -i test/blackbox/check_log/basefiles/test1d_ignore.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test1d_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "\n\tRegular Expression check\n"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -F test/blackbox/check_log/basefiles/test1e_filter.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test1e_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "\n\tRecheck Entire Log check\n"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -m test/blackbox/check_log/basefiles/test1f_marker.txt -n -r -z
$(cmp -s test/blackbox/check_log/basefiles/test1f_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "\n\nScenario 2:  check_log blackbox testing...Two file check\n"
printf "\tFull check\n"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -z
$(cmp -s test/blackbox/check_log/basefiles/test2a_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "\n\tPartial check\n"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -m test/blackbox/check_log/basefiles/test2b_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test2b_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "\n\tNo Entry Found check\n"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -m test/blackbox/check_log/basefiles/test2c_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test2c_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "\n\tIgnore Message check\n"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -i test/blackbox/check_log/basefiles/test2d_ignore.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test2d_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "\n\tRegular Expression check\n"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -F test/blackbox/check_log/basefiles/test2e_filter.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test2e_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "\n\tRecheck Entire Log check\n"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -m test/blackbox/check_log/basefiles/test2f_marker.txt -n -r -z
$(cmp -s test/blackbox/check_log/basefiles/test2f_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "\n\nScenario 3:  check_log blackbox testing...Wildcard file check\n"
touch test/blackbox/check_log/logfiles/log3a.txt
touch test/blackbox/check_log/logfiles/log3b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log3*.txt -o test/blackbox/check_log/testfiles/test3.out -m test/blackbox/check_log/basefiles/test3a_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test3a_base.txt test/blackbox/check_log/testfiles/test3.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test3.out

printf "\n\nScenario 4:  check_log blackbox testing...Standard in check\n"
cat test/blackbox/check_log/logfiles/log4.txt | ./check_log.py -o test/blackbox/check_log/testfiles/test4.out -m test/blackbox/check_log/basefiles/test4a_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test4a_base.txt test/blackbox/check_log/testfiles/test4.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test4.out

printf "\n\nScenario 5:  check_log blackbox testing...Output file check\n"
./check_log.py -f test/blackbox/check_log/logfiles/log5.txt -o test/blackbox/check_log/testfiles/test5.out -z
$(cmp -s test/blackbox/check_log/basefiles/test5a_base.txt test/blackbox/check_log/testfiles/test5.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test5.out

printf "\n\nScenario 6:  check_log blackbox testing...Marker file check\n"
printf "\tNo update of marker file check\n"
./check_log.py -f test/blackbox/check_log/logfiles/log6.txt -z -m test/blackbox/check_log/basefiles/test6a_marker.txt -n
$(cmp -s test/blackbox/check_log/basefiles/test6a_marker.txt test/blackbox/check_log/basefiles/test6a_marker_base.txt)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi

printf "\n\tUpdate of marker file check\n"
head -1 test/blackbox/check_log/logfiles/log6.txt >> test/blackbox/check_log/testfiles/test6b_marker.txt
./check_log.py -f test/blackbox/check_log/logfiles/log6.txt -z -m test/blackbox/check_log/testfiles/test6b_marker.txt
$(cmp -s test/blackbox/check_log/testfiles/test6b_marker.txt test/blackbox/check_log/basefiles/test6b_marker_base.txt)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test6b_marker.txt

printf "\n\nScenario 7:  check_log blackbox testing...Clear marker check\n"
head -1 test/blackbox/check_log/logfiles/log6.txt >> test/blackbox/check_log/testfiles/test7a_marker.txt
./check_log.py -m test/blackbox/check_log/testfiles/test7a_marker.txt -c
if [ -s test/blackbox/check_log/testfiles/test7a_marker.txt ] ; then
    printf "\t\tTest Failure\n"
else
    printf "\t\tTest Successful\n"
fi
rm test/blackbox/check_log/testfiles/test7a_marker.txt

printf "\n\nScenario 8:  check_log blackbox testing...Search check\n"
printf "\tAnd search check\n"
touch test/blackbox/check_log/logfiles/log8a.txt
touch test/blackbox/check_log/logfiles/log8b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log8a.txt test/blackbox/check_log/logfiles/log8b.txt -o test/blackbox/check_log/testfiles/test8.out -z -S three line -k and
$(cmp -s test/blackbox/check_log/basefiles/test8a_base.txt test/blackbox/check_log/testfiles/test8.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test8.out

printf "\tOr search check\n"
touch test/blackbox/check_log/logfiles/log8a.txt
touch test/blackbox/check_log/logfiles/log8b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log8a.txt test/blackbox/check_log/logfiles/log8b.txt -o test/blackbox/check_log/testfiles/test8.out -z -S three six -k or
$(cmp -s test/blackbox/check_log/basefiles/test8b_base.txt test/blackbox/check_log/testfiles/test8.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test8.out

printf "\n\nScenario 9:  check_log blackbox testing...Compressed file check\n"
touch test/blackbox/check_log/logfiles/log9a.txt
touch test/blackbox/check_log/logfiles/log9b.txt
gzip test/blackbox/check_log/logfiles/log9b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log9* -o test/blackbox/check_log/testfiles/test9.out -m test/blackbox/check_log/basefiles/test9a_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test9a_base.txt test/blackbox/check_log/testfiles/test9.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
gunzip test/blackbox/check_log/logfiles/log9b.txt.gz
rm test/blackbox/check_log/testfiles/test9.out

printf "\n\nScenario 10:  check_log blackbox testing...Case-insensitive check\n"
./check_log.py -f test/blackbox/check_log/logfiles/log10* -o test/blackbox/check_log/testfiles/test10.out -S TEST -z
$(cmp -s test/blackbox/check_log/basefiles/test10a_base.txt test/blackbox/check_log/testfiles/test10.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test10.out

printf "\n\nScenario 11:  check_log blackbox testing...multiple options check (-S and -i options)\n"
./check_log.py -f test/blackbox/check_log/logfiles/log10* -o test/blackbox/check_log/testfiles/test10.out -S TEST -i test/blackbox/check_log/basefiles/test10a_ignore.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test10b_base.txt test/blackbox/check_log/testfiles/test10.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test10.out

printf "\n\nScenario 12:  check_log blackbox testing...multiple options check (-S, -F, and -i options)\n"
./check_log.py -f test/blackbox/check_log/logfiles/log10* -o test/blackbox/check_log/testfiles/test10.out -S TEST -i test/blackbox/check_log/basefiles/test10a_ignore.txt -F test/blackbox/check_log/basefiles/test10a_filter.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test10c_base.txt test/blackbox/check_log/testfiles/test10.out)
if [ $? == 0 ] ; then
    printf "\t\tTest Successful\n"
else
    printf "\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test10.out
