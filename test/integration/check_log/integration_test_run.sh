#!/bin/bash
# Integration testing program for the check_log.py module.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Integration test:  check_log.py"
test/integration/check_log/fetch_log.py
test/integration/check_log/fetch_log_stdin.py
test/integration/check_log/find_marker.py
test/integration/check_log/full_chk.py
test/integration/check_log/log_2_output.py
test/integration/check_log/main.py
test/integration/check_log/run_program.py
test/integration/check_log/update_marker.py

