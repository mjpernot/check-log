#!/bin/bash
# Unit testing program for the check_log.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  check_log.py"
test/unit/check_log/fetch_log.py
test/unit/check_log/fetch_log_stdin.py
test/unit/check_log/find_marker.py
test/unit/check_log/full_chk.py
test/unit/check_log/help_message.py
test/unit/check_log/load_attributes.py
test/unit/check_log/log_2_output.py
test/unit/check_log/main.py
test/unit/check_log/run_program.py
test/unit/check_log/update_marker.py

