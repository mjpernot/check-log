# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.1.3] - 2020-04-07
### Changed
- Removed "re" module, not required any more.
- Documentation update.

### Fixed
- fetch_log_stdin:  Fixed handling command standard in from SonarQube scan finding.
- main:  Fixed handling command line arguments from SonarQube scan finding.


## [3.1.2] - 2020-03-04
### Added
- \_\_init\_\_.py:  Added file to allow check_log to support other programs as a library module

### Changed
- setup.py:  Added py_modules section to allow check_log to be pip installed.


## [3.1.1] - 2020-02-14
### Fixed
- main:  Fixed a formatting issue with the opt_valid_val variable.
-   NOTE:  This fix is only required for Python 2.6.6.  Original code will work in Python 2.7.5 without issue.


## [3.1.0] - 2020-02-05
### Changed
- log_2_output:  Changed the file mode on the output log file to be dynamic.
- log_2_output:  Added -w option not to write no data to a log file.
- main:  Added -g option and set default write file mode.
- main:  Removed output file being checked and created immediately at start of program.
- Documentation update.


## [3.0.0] - 2019-11-25
Breaking Change
- Integrating the gen_class.LogFile class into the program.

### Added
- load_attributes:  Load program options values into LogFile class attributes.

### Changed
- main:  Removed -S option from requiring other options as they are no longer required or handled by other sections of the code.
- find_marker:  Replaced args_array with LogFile class instance, fetch_marker_entry call was moved to load_attributes function, removed loop to find marker in files as it's no longer required.
- log_2_output:  Replaced log_array with LogFile class instance.
- fetch_log:  Replaced log_array with LogFile class instance, replace open_log call with calling the first log file, keyword search was moved to the LogFile class method.
- fetch_log_stdin:  Replaced log_array with LogFile class instance, moved full_chk to run_program, and find marker call was moved to LogFile class method.
- run_program:  Refactored function to setup and use LogFile class and added check for full_chk on loglist in LogFile class.
- main:  Converted variable name to standard naming convention.
- Documentation updates.

### Removed
- open_log:  No longer required by program.
- ignore_msgs:  No longer required by program.
- get_ignore_msgs:  No longer required by program.
- search:  No longer required by program.
- find_marker_array:  No longer required by program.
- fetch_marker_entry:  No longer required by program.
- filter_data:  No longer required by program.
- get_filter_data:  No longer required by program.


## [2.2.1] - 2019-06-18
- Added capability to open compressed (e.g. .gz) files.

### Changed
- open_log:  Replace open call with gen_libs.openfile call.
- find_marker:  Replace open calls with gen_libs.openfile calls.
- get_ignore_msgs:  Replace open call with gen_libs.openfile call.
- fetch_log:  Replace open call with gen_libs.openfile call.
- get_filter_data:  Replace open call with gen_libs.openfile call.


## [2.2.0] - 2019-06-11
- Added ability to do keyword searching.

### Added
- search:  Returns only those log entries that match the keyword search.

### Changed
- fetch_log:  Call to search() for keyword search.
- main:  Added -S option -> List of keywords to search for.
- main:  Added -k option -> Type of search as 'and' or 'or'.


## [2.1.3] - 2019-05-16
### Fixed
- full_chk:  Fixed problem with mutable default arguments issue.
- open_log:  Fixed problem with mutable default arguments issue.
- find_marker:  Fixed problem with mutable default arguments issue.
- update_marker:  Fixed problem with mutable default arguments issue.
- get_ignore_msgs:  Fixed problem with mutable default arguments issue.
- ignore_msgs:  Fixed problem with mutable default arguments issue.
- log_2_output:  Fixed problem with mutable default arguments issue.
- fetch_log:  Fixed problem with mutable default arguments issue.
- find_marker_array:  Fixed problem with mutable default arguments issue.
- fetch_log_stdin:  Fixed problem with mutable default arguments issue.
- get_filter_data:  Fixed problem with mutable default arguments issue.
- filter_data:  Fixed problem with mutable default arguments issue.
- run_program:  Fixed problem with mutable default arguments issue.

 
## [2.1.2] - 2019-01-22
### Changed
- main:  Refactored code.


## [2.1.1] - 2018-11-01
### Changed
- log_2_output:  Made "-z" option its own "if" statement to allow for better flexibility.
- log_2_output:  Changed Mail instance name from "EMAIL" to "mail".


## [2.1.0] - 2018-09-27
### Changed
- find_marker:  Added check for ln_marker to improve performance.
- find_marker_array:  Added check for ln_marker to improve performance.
- ignore_msgs:  Added log_array to check to improve performance.
- get_ignore_msgs:  Changed "open/close" to "with open" command and changed "for" loop to loop comphrension.
- log_2_output:  Refactored code - made cleaner and easier to understand.
- log_2_output:  Added "-t" option to email output and also to suppress standard out.
- main:  Setup a conditional requirement check for "-c" option.
- main:  Added new options -s, -t, -y and -z to the program.
- main:  Added program lock functionality to program.
- update_marker:  Replaced open write with "gen_libs.write_file" call.
- fetch_marker_entry:  Refactored to use "gen_libs.file_2_list" function.
- filter_data:  Added check to ensure the filter string has data.
- full_chk:  Refactored function to improve performance and readability.
- full_chk:  Removed "-c" option from the full check.
- run_program:  Initialized log_array and replaced sys.exit error with warning.
- run_program:  Removed "clr_files" call.
- run_program:  Moved check for "-c" and "-m" options to forefront.
- fetch_log:  Replaced "get_log" call with "gen_libs.get_data" call.

### Removed
- clr_files:  No longer required, replaced by "gen_libs.clear_file".
- get_log:  No longer required, replaced by "gen_libs.get_data".


## [2.0.0] - 2018-04-18
Breaking Change

### Changed
- Added "kwargs" to all function definitions.
- Changed "arg_parser" calls to new naming schema.
- Changed "gen_libs" calls to new naming schema.
- run_program:  Changed "gen_libs.Empty_File" to "gen_libs.clear_file" call.
- Changed function names from uppercase to lowercase.


## [1.8.0] - 2017-08-24
### Changed
- Run_Program:  Added check for "-c" option to clear log marker file.

## [1.7.0] - 2017-08-16
### Changed
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.
- Add classification line for Sunspear use.
- Convert program to use local libraries from ./lib directory.


## [1.6.1] - 2017-05-30
### Fixed
- Error:  Log array was being cleared if "-i" option was not selected on the command line.
- Ignore_Msgs:  Replaced list1 with log_array as log_array was being cleared if no ignore_array was selected.


## [1.6.0] - 2017-04-04
### Changed
- Added functionality to allow the log data to be checked for a specific format at the beginning of each line.  If the data line does not match that format, then it is dropped.  Multiple formats are allowed, but will use "or" logic to determine if the line matches the format.  The format line is a regex expression.
- Run_Program: Added Filter_Data function call.
- main:  Added -F option to the argument list as the new formatting option.
- Help_Message:  Updated documentation.

### Added
- Get_Filter_Data.
- Filter_Data.


## [1.5.0] - 2017-03-31
### Changed
- Performance of the program was very slow after getting too large of a file to check.  Found Big-O was Exponential.
- Ignore_Msgs:  Replace a double nested loop with a single list comprenhension loop.  Performance is now at Big-O Logarithmic.


## [1.4.0] - 2016-04-27
### Added
- Find_Marker_Entry.
- Find_Marker_Array.
- Fetch_Log_Stdin.

### Changed
- Modified the program to accept input from 'standard in' or from log files.
- Find_Marker:  Replaced code with call to Find_Marker_Entry function.
- Help_Message:  Changed to reflect accepting input from stdin or files.
- main:  Removed Arg_Require function call and variables.
- Run_Program: Added "if" to determine whether to get log entries from file or stdin.


## [1.3.0] - 2016-04-21
### Added
- Fetch_Log.

### Changed
- Added capability to check multiple files using multiple names or wildcard expansion.
- main:  Added opt_multi_list variable, moved "-f" to opt_multi_list variable, and added named argument to Arg_Parse2 function call.
- Find_Marker:  Made a number of changes to handle the processing of multiple log files.
- Open_Log:  Reversed "if" statement boolean check and set "open" to handle lists.
- Help_Message:  Changed to reflect the processing of multiple files.
- Run_Program:  Replaced log_array code with call to Fetch_Log function.


## [1.2.0] - 2016-04-12
### Changed
- main:  Added exit call.
- main:  Made a number of changes to streamline the code and argument process to include converting from Arg_Parse to Arg_Parse2, add a Help_Func call, added call to Run_Program to control running of program, removed a number of "else" statements and the opt_noval_list variable.
- Full_Chk:  Replaced all returns with a single return and used a flag to determine whether a full check is required.
- Log_2_Output:  Added "sys." to stdout.

### Added
- Help_Message.
- Run_Program:  To control running of program.


## [1.1.0] - 2015-10-01
### Changed
- Replaced the Arg_Parse, Arg_Require, and Arg_File_Chk functions with calls to the arg_parser library module.


## [1.0.0] - 2015-09-23
- Initial creation.

