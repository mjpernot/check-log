# Python project for the monitoring of general log activity.
# Classification (U)

# Description:
  This program is used to monitor ASCII text logs or standard in for activity and report any new activity.  This program is typically used in conjunction with other project programs which may produce logs that need to be monitored for new activity.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Monitor ASCII type logs for changes.
  * Monitor standard in for new entries.
  * Use a marker log file to maintain location within a log file.
  * Filter out specific entries.
  * Regular expression capability for message searching.


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/gen_class
    - lib/arg_parser
    - lib/gen_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/check-log.git
```

Install/upgrade system modules.

```
cd check-log
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Program Descriptions:
### Program: check_log.py
##### Description: The check_log program checks log files or "standard in" for new data since the last run as determined by the contents of the marker file.  The program can also setup filtering options to either ignore specific messages and/or allow specific formatted messages through.  See -F and -i options below for further details.


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/check-log/check_log.py -h
```


# Help Message:
  Below is the help message for each of the programs along with the current version for the program.  Recommend running the -h option on the command line to ensure you have the latest help message for the program.

    Program:  check_log.py

    Description:  The check_log program checks log files or "standard in" for
        new data since the last run as determined by the contents of the marker
        file.  The program can also setup filtering options to either ignore
        specific messages and/or allow specific formatted messages through.
        See -F and -i options below for further details.

    Usage:
         stdin | check_log.py [ -f { file* file1 file2 ... } ] [ -F file
            | -i file | -m file | -o file | -n | -r | -c | -y flavor_id]
            [-t email {email2 email3 ...} {-s subject_line}] [-v | -h]
`

    Arguments:
        -f file(s) => Name(s) of the log files to check.  Can also use
            wildcard expansion for file names.
        -F file => Name of file that contains regex format expression.  The
            file will contain one or more regex expressions to be used to
            filter out data that does not match the regex string.  The
            matching will be only for the beginning of the data line.  If
            multiple regex expressions will be using "or" logic.  See NOTE 2
            for formatting of regex expression.
        -t email_address(es) => Send output to one or more email addresses.
        -s subject_line => Subject line of email.  Requires -t option.
        -i file => Name of the file that contains entries to be ignored.
        -m file => Name of the file that contains marker tag in file.
        -o file => Name of the out file.
        -n => Flag option - not to update the marker file.
        -r => Flag option - to recheck the entire log file.
        -c => Flag option - to clear the contents in the marker file.  Requires
            -m option.
        -y value => A flavor id for the program lock.  To create unique lock.
        -z => Suppress standard out.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  -c requires -m option to be included.
        NOTE 3:  -s requires -t option to be included.

        NOTE 4:  Regex expression formatting.  Uses standard regex formatting.
            The regex expression can contain multiple expressions, but will use
            "or" logic to determine whether a data string is allowed through.
            Matching will only be done from the beginning of a data string.
            Use the "|" as the delimitered between expressions.  All regex
            expressions must be on a single line in a file, all other lines are
            ignored.

            Example of checking for a format such as this:
                2017-04-04T11:24:32.345+0000

            Regex format string:
                \d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+0000

            Example of checking for a date or time format such as:
                2017-04-04
                22:24:32

            Regex format strings:
                \d{4}\-\d{2}\-\d{2}|d{2}:\d{2}:\d{2}

    Example:
        File input
            check_log.py -f /opt/sybase/errorlog* -o /tmp/out_file -n
        Standard in input
            cat errorlog | check_log.py -o /tmp/out_file -n


# Testing:

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the check_log.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/check-log.git
```

Install/upgrade system modules.

```
cd check-log
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit test runs for check_log.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/check-log
```

### Unit:  help_message
```
test/unit/check_log/help_message.py
```

### Unit:  open_log
```
test/unit/check_log/open_log.py
```

### Unit:  find_marker
```
test/unit/check_log/find_marker.py
```

### Unit:  update_marker
```
test/unit/check_log/update_marker.py
```

### Unit:  get_ignore_msgs
```
test/unit/check_log/get_ignore_msgs.py
```

### Unit:  ignore_msgs
```
test/unit/check_log/ignore_msgs.py
```

### Unit:  log_2_output
```
test/unit/check_log/log_2_output.py
```

### Unit:  fetch_log
```
test/unit/check_log/fetch_log.py
```

### Unit:  fetch_marker_entry
```
test/unit/check_log/fetch_marker_entry.py
```

### Unit:  find_marker_array
```
test/unit/check_log/find_marker_array.py
```

### Unit:  fetch_log_stdin
```
test/unit/check_log/fetch_log_stdin.py
```

### Unit:  get_filter_data
```
test/unit/check_log/get_filter_data.py
```

### Unit:  filter_data
```
test/unit/check_log/filter_data.py
```

### Unit:  run_program
```
test/unit/check_log/run_program.py
```

### Unit:  main
```
test/unit/check_log/main.py
```

### All unit testing
```
test/unit/check_log/unit_test_run.sh
```

### Code coverage program
```
test/unit/check_log/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the check_log.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/check-log.git
```

Install/upgrade system modules.

```
cd check-log
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Integration test runs for check_log.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/check-log
```

### Integration:  full_chk
```
test/integration/check_log/full_chk.py
```

### Integration:  update_marker
```
test/integration/check_log/update_marker.py
```

### Integration:  get_ignore_msgs
```
test/integration/check_log/get_ignore_msgs.py
```

### Integration:  fetch_marker_entry
```
test/integration/check_log/fetch_marker_entry.py
```

### Integration:  find_marker_array
```
test/integration/check_log/find_marker_array.py
```

### Integration:  get_filter_data
```
test/integration/check_log/get_filter_data.py
```

### Integration:  find_marker
```
test/integration/check_log/find_marker.py
```

### Integration:  open_log
```
test/integration/check_log/open_log.py
```

### Integration:  log_2_output
```
test/integration/check_log/log_2_output.py
```

### Integration:  fetch_log
```
test/integration/check_log/fetch_log.py
```

### Integration:  fetch_log_stdin
```
test/integration/check_log/fetch_log_stdin.py
```

### Integration:  run_program
```
test/integration/check_log/run_program.py
```

### Integration:  main
```
test/integration/check_log/main.py
```

### All integration testing
```
test/integration/check_log/integration_test_run.sh
```

### Code coverage program
```
test/integration/check_log/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the check_log.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/check-log.git
```

Install/upgrade system modules.

```
cd check-log
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Blackbox test run for check_log.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/check-log
```

### Blackbox:  
```
test/blackbox/check_log/blackbox_test.sh
```

