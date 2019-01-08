#!/bin/bash
# Integration testing program for the check_log.py module.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Integration test:  full_chk"
test/integration/check_log/full_chk.py

echo ""
echo "Integration test:  update_marker"
test/integration/check_log/update_marker.py

echo ""
echo "Integration test:  get_ignore_msgs"
test/integration/check_log/get_ignore_msgs.py

echo ""
echo "Integration test:  fetch_marker_entry"
test/integration/check_log/fetch_marker_entry.py

echo ""
echo "Integration test:  find_marker_array"
test/integration/check_log/find_marker_array.py

echo ""
echo "Integration test:  get_filter_data"
test/integration/check_log/get_filter_data.py

echo ""
echo "Integration test:  find_marker"
test/integration/check_log/find_marker.py

echo ""
echo "Integration test:  open_log"
test/integration/check_log/open_log.py

echo ""
echo "Integration test:  log_2_output"
test/integration/check_log/log_2_output.py

echo ""
echo "Integration test:  fetch_log"
test/integration/check_log/fetch_log.py

echo ""
echo "Integration test:  fetch_log_stdin"
test/integration/check_log/fetch_log_stdin.py

echo ""
echo "Integration test:  run_program"
test/integration/check_log/run_program.py

echo ""
echo "Integration test:  main"
test/integration/check_log/main.py

