#!/bin/bash
# Blackbox testing program for the check_log.py program.

BASE_PATH=$PWD

printf "check_log blackbox testing...\n"
printf "Scenario 1:  testing...One file check\n"
printf "Full check"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -z
$(cmp -s test/blackbox/check_log/basefiles/test1a_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "Partial check"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -m test/blackbox/check_log/basefiles/test1b_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test1b_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "No Entry Found check"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -m test/blackbox/check_log/basefiles/test1c_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test1c_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "Ignore Message check"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -i test/blackbox/check_log/basefiles/test1d_ignore.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test1d_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "Regular Expression check"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -F test/blackbox/check_log/basefiles/test1e_filter.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test1e_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "Recheck Entire Log check"
./check_log.py -f test/blackbox/check_log/logfiles/log1.txt -o test/blackbox/check_log/testfiles/test1.out -m test/blackbox/check_log/basefiles/test1f_marker.txt -n -r -z
$(cmp -s test/blackbox/check_log/basefiles/test1f_base.txt test/blackbox/check_log/testfiles/test1.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test1.out

printf "\nScenario 2:  testing...Two file check\n"
printf "Full check"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -z
$(cmp -s test/blackbox/check_log/basefiles/test2a_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "Partial check"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -m test/blackbox/check_log/basefiles/test2b_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test2b_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "No Entry Found check"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -m test/blackbox/check_log/basefiles/test2c_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test2c_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "Ignore Message check"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -i test/blackbox/check_log/basefiles/test2d_ignore.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test2d_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "Regular Expression check"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -F test/blackbox/check_log/basefiles/test2e_filter.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test2e_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "Recheck Entire Log check"
touch test/blackbox/check_log/logfiles/log2a.txt
touch test/blackbox/check_log/logfiles/log2b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log2a.txt test/blackbox/check_log/logfiles/log2b.txt -o test/blackbox/check_log/testfiles/test2.out -m test/blackbox/check_log/basefiles/test2f_marker.txt -n -r -z
$(cmp -s test/blackbox/check_log/basefiles/test2f_base.txt test/blackbox/check_log/testfiles/test2.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test2.out

printf "\nScenario 3:  testing...Wildcard\n"
printf "File check"
touch test/blackbox/check_log/logfiles/log3a.txt
touch test/blackbox/check_log/logfiles/log3b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log3*.txt -o test/blackbox/check_log/testfiles/test3.out -m test/blackbox/check_log/basefiles/test3a_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test3a_base.txt test/blackbox/check_log/testfiles/test3.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test3.out

printf "\nScenario 4:  testing...Standard In\n"
printf "Standard In check"
cat test/blackbox/check_log/logfiles/log4.txt | ./check_log.py -o test/blackbox/check_log/testfiles/test4.out -m test/blackbox/check_log/basefiles/test4a_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test4a_base.txt test/blackbox/check_log/testfiles/test4.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test4.out

printf "\nScenario 5:  testing...Output File\n"
printf "File check"
./check_log.py -f test/blackbox/check_log/logfiles/log5.txt -o test/blackbox/check_log/testfiles/test5.out -z
$(cmp -s test/blackbox/check_log/basefiles/test5a_base.txt test/blackbox/check_log/testfiles/test5.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test5.out

printf "\nScenario 6:  testing...Marker file check\n"
printf "No update of marker file check"
./check_log.py -f test/blackbox/check_log/logfiles/log6.txt -z -m test/blackbox/check_log/basefiles/test6a_marker.txt -n
$(cmp -s test/blackbox/check_log/basefiles/test6a_marker.txt test/blackbox/check_log/basefiles/test6a_marker_base.txt)
if [ $? == 0 ] ; then
    printf "\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\tTest Failure\n"
fi

printf "Update of marker file check"
head -1 test/blackbox/check_log/logfiles/log6.txt >> test/blackbox/check_log/testfiles/test6b_marker.txt
./check_log.py -f test/blackbox/check_log/logfiles/log6.txt -z -m test/blackbox/check_log/testfiles/test6b_marker.txt
$(cmp -s test/blackbox/check_log/testfiles/test6b_marker.txt test/blackbox/check_log/basefiles/test6b_marker_base.txt)
if [ $? == 0 ] ; then
    printf "\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test6b_marker.txt

printf "\nScenario 7:  testing...Clear marker\n"
printf "Marker check"
head -1 test/blackbox/check_log/logfiles/log6.txt >> test/blackbox/check_log/testfiles/test7a_marker.txt
./check_log.py -m test/blackbox/check_log/testfiles/test7a_marker.txt -c
if [ -s test/blackbox/check_log/testfiles/test7a_marker.txt ] ; then
    printf "\t\t\t\t\t\tTest Failure\n"
else
    printf "\t\t\t\t\t\tTest Successful\n"
fi
rm test/blackbox/check_log/testfiles/test7a_marker.txt

printf "\nScenario 8:  testing...Search check\n"
printf "And search check"
touch test/blackbox/check_log/logfiles/log8a.txt
touch test/blackbox/check_log/logfiles/log8b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log8a.txt test/blackbox/check_log/logfiles/log8b.txt -o test/blackbox/check_log/testfiles/test8.out -z -S three line -k and
$(cmp -s test/blackbox/check_log/basefiles/test8a_base.txt test/blackbox/check_log/testfiles/test8.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test8.out

printf "Or search check"
touch test/blackbox/check_log/logfiles/log8a.txt
touch test/blackbox/check_log/logfiles/log8b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log8a.txt test/blackbox/check_log/logfiles/log8b.txt -o test/blackbox/check_log/testfiles/test8.out -z -S three six -k or
$(cmp -s test/blackbox/check_log/basefiles/test8b_base.txt test/blackbox/check_log/testfiles/test8.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test8.out

printf "\nScenario 9:  testing...Compressed file\n"
printf "Compress file check"
touch test/blackbox/check_log/logfiles/log9a.txt
touch test/blackbox/check_log/logfiles/log9b.txt
gzip test/blackbox/check_log/logfiles/log9b.txt
./check_log.py -f test/blackbox/check_log/logfiles/log9* -o test/blackbox/check_log/testfiles/test9.out -m test/blackbox/check_log/basefiles/test9a_marker.txt -n -z
$(cmp -s test/blackbox/check_log/basefiles/test9a_base.txt test/blackbox/check_log/testfiles/test9.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\tTest Failure\n"
fi
gunzip test/blackbox/check_log/logfiles/log9b.txt.gz
rm test/blackbox/check_log/testfiles/test9.out

printf "\nScenario 10:  testing...Case-insensitive\n"
printf "Case check"
./check_log.py -f test/blackbox/check_log/logfiles/log10* -o test/blackbox/check_log/testfiles/test10.out -S TEST -z
$(cmp -s test/blackbox/check_log/basefiles/test10a_base.txt test/blackbox/check_log/testfiles/test10.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test10.out

printf "\nScenario 11:  testing...multiple options (-S and -i)\n"
printf "Multiple option check"
./check_log.py -f test/blackbox/check_log/logfiles/log10* -o test/blackbox/check_log/testfiles/test10.out -S TEST -i test/blackbox/check_log/basefiles/test10a_ignore.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test10b_base.txt test/blackbox/check_log/testfiles/test10.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test10.out

printf "\nScenario 12:  testing...multiple options (-S, -F, and -i)\n"
printf "Multiple option check"
./check_log.py -f test/blackbox/check_log/logfiles/log10* -o test/blackbox/check_log/testfiles/test10.out -S TEST -i test/blackbox/check_log/basefiles/test10a_ignore.txt -F test/blackbox/check_log/basefiles/test10a_filter.txt -z
$(cmp -s test/blackbox/check_log/basefiles/test10c_base.txt test/blackbox/check_log/testfiles/test10.out)
if [ $? == 0 ] ; then
    printf "\t\t\t\t\tTest Successful\n"
else
    printf "\t\t\t\t\tTest Failure\n"
fi
rm test/blackbox/check_log/testfiles/test10.out
