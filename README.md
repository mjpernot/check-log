# Python project for the monitoring of general log activity.
# Classification (U)

# Description:
  The check_log program checks log files or "standard in" for new data since the last run as determined by the contents of the marker file.  This program is used to monitor ASCII text logs or standard in for any new activity.  The program can also setup filtering options to either ignore specific messages and/or allow specific formatted messages through.  It also has the capability for keyword searching based on an 'and|or' search logic.

###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Program Help Function
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
  * Keyword searching of files using 'and|or' search logic.
  * Can search gzipped files.


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
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


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/check-log/check_log.py -h
```


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

### Unit testing:
```
cd {Python_Project}/check-log
test/unit/check_log/unit_test_run.sh
```

### Code coverage unit testing:
```
cd {Python_Project}/check-log
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

### Integration testing:
```
cd {Python_Project}/check-log
test/integration/check_log/integration_test_run.sh
```

### Code coverage integration testing:
```
cd {Python_Project}/check-log
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

### Blackbox:testing:  
```
cd {Python_Project}/check-log
test/blackbox/check_log/blackbox_test.sh
```

