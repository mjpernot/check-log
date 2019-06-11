#!/usr/bin/python
# Classification (U)

"""Program:  check_log.py

    Description:  The check_log program checks log files or "standard in" for
        new data since the last run as determined by the contents of the marker
        file.  The program can also setup filtering options to either ignore
        specific messages and/or allow specific formatted messages through.
        See -F and -i options below for further details.

    Usage:
         stdin | check_log.py [-f {file* file1 file2 ...}] [-F file
            | -i file | -m file | -o file | -n | -r | -c | -y flavor_id]
            [-t email {email2 email3 ...} {-s subject_line}] [-v | -h]

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
        -S keyword(s) => Search for keywords.  List of keywords are
            space-delimited.  Requires -f options.  Standard in searching is
            not available.
        -k "and"|"or" => Keyword search logic.  Default setting is "or".
        -y value => A flavor id for the program lock.  To create unique lock.
        -z => Suppress standard out.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  -c requires -m option to be included.
        NOTE 3:  -s requires -t option to be included.
        NOTE 4:  -S requires -f option to be included.

        NOTE 5:  Regex expression formatting.  Uses standard regex formatting.
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

    Examples:
        File input
            check_log.py -f /opt/sybase/errorlog* -o /tmp/out_file -n
        Standard in input
            cat errorlog | check_log.py -o /tmp/out_file -n

"""

# Libraries and Global Variables

# Standard
# For Python 2.6/2.7: Redirection of stdout in a print command.
from __future__ import print_function
import sys
import os
import re
import socket
import getpass

# Third-party

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def full_chk(args_array, **kwargs):

    """Function:  full_chk

    Description:  Sets the full check flag depending on options selected.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.
        (output) True|False -> Determine full check of log.

    """

    args_array = dict(args_array)
    full_chk_flag = True

    if "-m" in args_array and "-r" not in args_array \
       and not gen_libs.is_empty_file(args_array["-m"]):

        full_chk_flag = False

    return full_chk_flag


def open_log(args_array, **kwargs):

    """Function:  open_log

    Description:  Opens the log file at the tag marker or at the beginning of
        the file.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.
        (output) Log file handler.

    """

    args_array = dict(args_array)

    if full_chk(args_array):
        return open(args_array["-f"][0], "r")

    else:
        return find_marker(args_array)


def find_marker(args_array, **kwargs):

    """Function:  find_marker

    Description:  Locates the marker file entry in the log file.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.
        (output) log_file -> Log file handler.

    """

    args_array = dict(args_array)
    ln_marker = fetch_marker_entry(args_array["-m"])

    if ln_marker:
        for fname in args_array["-f"]:
            log_file = open(fname, "r")

            for line in log_file:
                if line.rstrip() == ln_marker:
                    return log_file

            log_file.close()

    # No marker found, return first file.
    return open(args_array["-f"][0], "r")


def update_marker(args_array, line, **kwargs):

    """Function:  update_marker

    Description:  Writes the last line of the log to the marker file, if the
        marker option is selected and not the no_update option.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.
        (input) line -> Last line of log.

    """

    args_array = dict(args_array)

    if "-m" in args_array and "-n" not in args_array:
        gen_libs.write_file(args_array["-m"], mode="w", data=line)


def get_ignore_msgs(args_array, **kwargs):

    """Function:  get_ignore_msgs

    Description:  Copies the ignore file into the ignore array.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.
        (output) ignore_array -> List of ignore messages.

    """

    args_array = dict(args_array)
    ignore_array = []

    if "-i" in args_array:
        with open(args_array["-i"], "r") as f_hldr:
            ignore_array = [x.lower().rstrip() for x in f_hldr]

    return ignore_array


def ignore_msgs(log_array, ignore_array, **kwargs):

    """Function:  ignore_msgs

    Description:  Removes all ignore messages from the log array.

    Arguments:
        (input) log_array -> List of log entries.
        (input) ignore_array -> List of ignore messages.
        (output) log_array -> Modified list of log entries.

    """

    log_array = list(log_array)
    ignore_array = list(ignore_array)

    if ignore_array and log_array:
        log_array = [sa for sa in log_array
                     if not any(sb in sa.lower() for sb in ignore_array)]

    return log_array


def log_2_output(log_array, args_array, **kwargs):

    """Function:  log_2_output

    Description:  Sends the log array to output depending on command line
        option.

    Arguments:
        (input) log_array -> List of log entries.
        (input) args_array -> Dictionary of command line options and values.

    """

    log_array = list(log_array)
    args_array = dict(args_array)

    # Send output to email.
    if "-t" in args_array:
        host = socket.gethostname()
        frm_line = getpass.getuser() + "@" + host

        mail = gen_class.Mail(args_array["-t"],
                              "".join(args_array.get("-s",
                                                     "check_log: " + host)),
                              frm_line)
        mail.add_2_msg("\n".join(log_array))
        mail.send_mail()

    # Write output to file.
    if "-o" in args_array:
        with open(args_array["-o"], "w") as f_hdlr:
            for x in log_array:
                print(x, file=f_hdlr)

    # Suppress standard out.
    if "-z" not in args_array:
        for x in log_array:
            print(x, file=sys.stdout)


def fetch_log(args_array, **kwargs):

    """Function:  fetch_log

    Description:  Sorts the log files from oldest to newest, finds the place to
        start pulling the log entries; either at the marker or the
        oldest log file.  Appends the log entries to an array which is
        passed to the calling function.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.
        (output) log_array -> List of log entries.

    """

    args_array = dict(args_array)
    log_array = []

    # Sort files from oldest to newest.
    args_array["-f"] = sorted(args_array["-f"], key=os.path.getmtime,
                              reverse=False)

    log_file = open_log(args_array)

    # Start with the log file returned by open_log function call.
    for x in args_array["-f"][args_array["-f"].index(log_file.name):]:

        # If file is closed, open up next one.
        if log_file.closed:
            log_file = open(x, "r")

        log_array.extend(gen_libs.get_data(log_file))
        log_file.close()

    # Keyword search
    if "-S" in args_array.keys():
        if args_array["-k"] == "and":
            logs_array = search(logs_array, args_array["-S"], all)

        else:
            logs_array = search(logs_array, args_array["-S"], any)

    return log_array


def fetch_marker_entry(fname, **kwargs):

    """Function:  fetch_marker_entry

    Description:  Gets and returns marker line entry from marker file.

    Arguments:
        (input) fname -> Marker file.
        (output) ln_marker -> Marker line entry.

    """

    return ''.join(gen_libs.file_2_list(fname))


def find_marker_array(args_array, log_array, **kwargs):

    """Function:  find_marker_array

    Description:  Locate the marker file entry in the log file array or return
        the entire array.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.
        (input) log_array -> List of log entries.
        (output) log_array -> Modified list of log entries.

    """

    args_array = dict(args_array)
    log_array = list(log_array)
    ln_marker = fetch_marker_entry(args_array["-m"])

    if ln_marker:

        # Return log array from marker onward.
        for cnt, ln in enumerate(log_array):
            if ln.rstrip() == ln_marker:
                return log_array[cnt + 1:]

    # No marker found.
    return log_array


def fetch_log_stdin(args_array, **kwargs):

    """Function:  fetch_log_stdin

    Description:  Reads 'standard in' into an array, finds the place to start
        pulling the log entries; either at the marker or at the start of
        the array.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.
        (output) log_array or list -> List of log entries.

    """

    args_array = dict(args_array)
    log_array = []

    for ln in sys.stdin:
        log_array.append(ln.rstrip("\n"))

    if full_chk(args_array):
        return log_array

    else:
        return find_marker_array(args_array, log_array, **kwargs)


def get_filter_data(args_array, **kwargs):

    """Function:  get_filter_data

    Description:  Read in a formatted regex expression to be used for filtering
        data.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.
        (output) filter_str -> Formatted filter string in regex format.

    """

    args_array = dict(args_array)
    filter_str = ""

    if "-F" in args_array:

        # Only read the first line, all others ignored.
        with open(args_array["-F"], "r") as f_hdlr:
            filter_str = f_hdlr.readline().strip("\n")

    return filter_str


def filter_data(log_array, filter_str, **kwargs):

    """Function:  filter_data

    Description:  Filters out data of an array using regex.  Designed to match
        from the beginning of each string line and can do multiple "or"
        matching.  Will remove any line that does not match the regex
        formatted expression(s).

    Arguments:
        (input) log_array -> List of log entries.
        (input) filter_str -> Formatted filter string in regex format.
        (output) log_array -> Modified list of log entries.

    """

    log_array = list(log_array)

    # Only filter if there is something to filter with.
    if len(filter_str) > 0:
        for x in log_array[:]:

            # Must match format to stay.
            if not re.match(filter_str, x):
                log_array.remove(x)

    return log_array


def run_program(args_array, **kwargs):

    """Function:  run_program

    Description:  Controls the running of the program by fetching the log
        entries, updating the file marker, and sending the log entries to
        output.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.

    """

    args_array = dict(args_array)
    log_array = []

    if "-c" in args_array and "-m" in args_array:
        gen_libs.clear_file(args_array["-m"])

    elif "-f" in args_array:
        log_array = fetch_log(args_array, **kwargs)

    elif not sys.stdin.isatty():
        log_array = fetch_log_stdin(args_array, **kwargs)

    else:
        print("Warning:  No log files or 'standard in' to process.")

    if log_array:
        update_marker(args_array, log_array[len(log_array) - 1])
        log_array = ignore_msgs(log_array, get_ignore_msgs(args_array))
        log_array = filter_data(log_array, get_filter_data(args_array))
        log_2_output(log_array, args_array)


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        file_chk_list -> contains the options which will have files included.
        file_crt_list -> contains options which require files to be created.
        opt_con_req_dict -> contains options requiring other options.
        opt_multi_list -> contains the options that will have multiple values.
        opt_val_list -> contains options which require values.
        opt_valid_val -> contains options with their valid values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    file_chk_list = ["-f", "-i", "-m", "-o", "-F"]
    file_crt_list = ["-m", "-o"]
    opt_con_req_dict = {"-c": ["-m"], "-s": ["-t"], "-S": ["-f", "-k"]}
    opt_multi_list = ["-f", "-s", "-t", "-S"]
    opt_val_list = ["-i", "-m", "-o", "-s", "-t", "-y", "-F", "-S"]
    opt_valid_val = {"-k": ["and", "or"]}

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list,
                                       multi_val=opt_multi_list)

    # Set default search logic.
    if "-S" in args_array.keys() and "-k" not in args_array.keys():
        args_array["-k"] = "or"

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and arg_parser.arg_cond_req_or(args_array, opt_con_req_dict) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                       file_crt_list) \
       and arg_parser.arg_valid_val(args_array, opt_valid_val):

        try:
            PROG_LOCK = gen_class.ProgramLock(sys.argv,
                                              args_array.get("-y", ""))
            run_program(args_array)
            del PROG_LOCK

        except gen_class.SingleInstanceException:
            print("WARNING:  lock in place for check_log with id of: %s"
                  % (args_array.get("-y", "")))


if __name__ == "__main__":
    sys.exit(main())
