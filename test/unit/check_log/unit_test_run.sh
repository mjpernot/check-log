#!/bin/bash
# Unit testing program for the check_log.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  help_message"
test/unit/check_log/help_message.py

echo ""
echo "Unit test:  full_chk"
test/unit/check_log/full_chk.py

echo ""
echo "Unit test:  open_log"
test/unit/check_log/open_log.py

echo ""
echo "Unit test:  find_marker"
test/unit/check_log/find_marker.py

echo ""
echo "Unit test:  update_marker"
test/unit/check_log/update_marker.py

echo ""
echo "Unit test:  get_ignore_msgs"
test/unit/check_log/get_ignore_msgs.py

echo ""
echo "Unit test:  ignore_msgs"
test/unit/check_log/ignore_msgs.py

echo ""
echo "Unit test:  log_2_output"
test/unit/check_log/log_2_output.py

echo ""
echo "Unit test:  fetch_log"
test/unit/check_log/fetch_log.py

echo ""
echo "Unit test:  fetch_marker_entry"
test/unit/check_log/fetch_marker_entry.py

echo ""
echo "Unit test:  find_marker_array"
test/unit/check_log/find_marker_array.py

echo ""
echo "Unit test:  fetch_log_stdin"
test/unit/check_log/fetch_log_stdin.py

echo ""
echo "Unit test:  get_filter_data"
test/unit/check_log/get_filter_data.py

echo ""
echo "Unit test:  filter_data"
test/unit/check_log/filter_data.py

echo ""
echo "Unit test:  run_program"
test/unit/check_log/run_program.py

echo ""
echo "Unit test:  main"
test/unit/check_log/main.py

