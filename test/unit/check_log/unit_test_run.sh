#!/bin/bash
# Unit testing program for the check_log.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  check_log.py"
/usr/bin/python ./test/unit/check_log/fetch_log.py
/usr/bin/python ./test/unit/check_log/fetch_log2.py
/usr/bin/python ./test/unit/check_log/fetch_log_stdin.py
/usr/bin/python ./test/unit/check_log/find_marker.py
/usr/bin/python ./test/unit/check_log/full_chk.py
/usr/bin/python ./test/unit/check_log/help_message.py
/usr/bin/python ./test/unit/check_log/load_attributes.py
/usr/bin/python ./test/unit/check_log/log_2_output.py
/usr/bin/python ./test/unit/check_log/main.py
/usr/bin/python ./test/unit/check_log/read_file.py
/usr/bin/python ./test/unit/check_log/run_program.py
/usr/bin/python ./test/unit/check_log/update_marker.py

