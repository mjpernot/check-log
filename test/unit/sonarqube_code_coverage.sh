#!/bin/bash
# Unit test code coverage for SonarQube to cover all modules.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=check_log test/unit/check_log/help_message.py
coverage run -a --source=check_log test/unit/check_log/full_chk.py
coverage run -a --source=check_log test/unit/check_log/open_log.py
coverage run -a --source=check_log test/unit/check_log/find_marker.py
coverage run -a --source=check_log test/unit/check_log/update_marker.py
coverage run -a --source=check_log test/unit/check_log/get_ignore_msgs.py
coverage run -a --source=check_log test/unit/check_log/ignore_msgs.py
coverage run -a --source=check_log test/unit/check_log/log_2_output.py
coverage run -a --source=check_log test/unit/check_log/fetch_log.py
coverage run -a --source=check_log test/unit/check_log/fetch_marker_entry.py
coverage run -a --source=check_log test/unit/check_log/find_marker_array.py
coverage run -a --source=check_log test/unit/check_log/fetch_log_stdin.py
coverage run -a --source=check_log test/unit/check_log/get_filter_data.py
coverage run -a --source=check_log test/unit/check_log/filter_data.py
coverage run -a --source=check_log test/unit/check_log/run_program.py
coverage run -a --source=check_log test/unit/check_log/main.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

