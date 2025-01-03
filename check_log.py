#!/usr/bin/python
# Classification (U)

"""Program:  check_log.py

    Description:  The check_log program checks log files or "standard in" for
        new data since the last run as determined by the contents of the marker
        file.  The program can also setup filtering options to either ignore
        specific messages, search for specific formatted messages, and/or
        do multiple keyword searching using the and | or predicate search.
        See -F, -S, and -i options below for further details.

    Usage:
        check_log.py [-f {file* file1 file2 ...}] |
            -F file |
            -S {keyword1 keyword2 ...} {-k and|or} |
            -m file {-n} {-c} {-r} |
            -t email {email2 email3 ...} {-s subject_line} {-u} |
            -o file {-g {a|w}} {-w} |
            -i file | -y flavor_id | -z ]
           [-v | -h]

        standard in | check_log.py ...

    Arguments:
        -f file(s) => Name(s) of the log files to check.  Can also use
            wildcard expansion for file names.  Can include both normal
            flat files or .gz compressed files.

        -F file => Name of file that contains regex format expression.  The
            file will contain one or more regex expressions to be used to
            filter out data that does not match the regex string.  If
            multiple regex expressions are present will use "or" logic.
            See NOTES below for formatting of regex expressions.

        -S keyword(s) => Search for keywords.  List of keywords are
                space-delimited and are case-insensitive.
            -k and|or => Keyword search logic.  Default is "or".

        -m file => Name of the file that contains marker tag in file.
            -n => Flag option not to update the marker file.
            -c => Flag option to clear the contents in the marker file.
            -r => Flag option to recheck the entire log file.

        -t email_address(es) => Send output to one or more email addresses.
            -s subject_line => Subject line of email.
            -u => Override the default mail command and use mailx.

        -o file => Name of the out file.
            -g a|w => Append or write/overwrite to a log file. Default is "w".
            -w => No write if empty.  Do not write to a file if no data was
                found.

        -R run_type => offset | lastline -> The offset option uses the inode of
            the file and offset to determine the last location checked in a
            file.  The lastline is the current method of checking a file by
            recording the last line checked in a file.
            NOTE:  When using the offset option, multiple files and wildcard
                in the -f option is not allowed.
                Default is lastline so as to be comptabile with older versions.

        -i file => Name of the file that contains entries to be ignored.  The
            entries are case-insensitive.
        -z => Suppress standard out.
        -y value => A flavor id for the program lock.  To create unique lock.

        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  -c requires -m option to be included.
        NOTE 3:  -s requires -t option to be included.

        NOTE 4:  Regex expression formatting: Uses standard regex formatting.
            The regex expression can contain multiple expressions, but will use
            "or" logic to determine whether a data string is allowed through.
            Use the "|" as the delimitered between expressions or place each
            regex expression on a line by itself in the file.

            Example of checking for a format such as this:
                2017-04-04T11:24:32.345+0000

            Regex format string:
                \\d{4}\\-\\d{2}\\-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}\\+0000

            Example of checking for a date or time format such as:
                2017-04-04
                22:24:32
            Regex format strings:
                \\d{4}\\-\\d{2}\\-\\d{2}|d{2}:\\d{2}:\\d{2}

        NOTE 5:  The log files can be normal flat files or compressed files
            (e.g. ending with .gz) or a combination there of.  Any other type
            of compressed file will not work.

    Examples:
        File input example:
            check_log.py -f /opt/sybase/errorlog* -o /tmp/out_file -n

        Standard in example:
            cat errorlog | check_log.py -o /tmp/out_file -S Error Warn

"""

# Libraries and Global Variables

# Standard
import sys
import os
import socket
import getpass
import glob

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def full_chk(args):

    """Function:  full_chk

    Description:  Sets the full check flag depending on options selected.

    Arguments:
        (input) args -> ArgParser class instance
        (output) full_chk_flag -> True|False - Run a full check of log?

    """

    full_chk_flag = True

    if args.arg_exist("-m") and not args.arg_exist("-r") \
       and not gen_libs.is_empty_file(args.get_val("-m")):

        full_chk_flag = False

    return full_chk_flag


def find_marker(log):

    """Function:  find_marker

    Description:  Locates the file marker.

    Arguments:
        (input) log -> LogFile class instance

    """

    if log.marker:
        log.find_marker(update=True)


def update_marker(args, line):

    """Function:  update_marker

    Description:  Writes the last line of the log to the marker file, if the
        marker option is selected and not the no_update option.

    Arguments:
        (input) args -> ArgParser class instance
        (input) line -> Last line of log

    """

    if args.arg_exist("-m") and not args.arg_exist("-n"):
        gen_libs.write_file(args.get_val("-m"), mode="w", data=line)


def log_2_output(log, args):

    """Function:  log_2_output

    Description:  Sends the log array to output depending on command line
        option.

    Arguments:
        (input) log -> LogFile class instance
        (input) args -> ArgParser class instance

    """

    # Send output to email.
    if args.arg_exist("-t") and log.loglist:
        host = socket.gethostname()
        frm_line = getpass.getuser() + "@" + host

        mail = gen_class.Mail(
            args.get_val("-t"), "".join(args.get_val(
                "-s", def_val="check_log: " + host)), frm_line)
        mail.add_2_msg("\n".join(log.loglist))
        mail.send_mail(use_mailx=args.get_val("-u", def_val=False))

    # Write output to file.
    if args.arg_exist("-o") and (log.loglist or not args.arg_exist("-w")):

        with open(args.get_val("-o"), mode=args.get_val("-g"),
                  encoding="UTF-8") as f_hdlr:
            for item in log.loglist:
                print(item, file=f_hdlr)

    # Suppress standard out.
    if not args.arg_exist("-z"):
        for item in log.loglist:
            print(item, file=sys.stdout)


def fetch_log(log, args):

    """Function:  fetch_log

    Description:  Sorts the log files from oldest to newest, finds the place to
        start pulling the log entries; either at the marker or the
        oldest log file.  Appends the log entries to an array which is
        passed to the calling function.

    Arguments:
        (input) log -> LogFile class instance
        (input) args -> ArgParser class instance

    """

    # Sort files from oldest to newest.
    args.update_arg(
        "-f", sorted(args.get_val("-f"), key=os.path.getmtime, reverse=False),
        insert=True)

    log_file = gen_libs.openfile(args.get_val("-f")[0], "r")

    # Start with the log file returned by open_log function call.
    for item in args.get_val("-f")[
            args.get_val("-f").index(log_file.name):]:

        # If file is closed, open up next one.
        if log_file.closed:
            log_file = gen_libs.openfile(item, "r")

        log.load_loglist(log_file)
        log_file.close()


def fetch_log_stdin(log):

    """Function:  fetch_log_stdin

    Description:  Reads 'standard in' into an array, finds the place to start
        pulling the log entries; either at the marker or at the start of
        the array.

    Arguments:
        (input) log -> LogFile class instance

    """

    for item in sys.stdin:
        log.load_loglist(str(item))


def load_attributes(log, args):

    """Function:  load_attributes

    Description:  Checks for certain program options to be loaded into the
        LogFile class attributes.

    Arguments:
        (input) log -> LogFile class instance
        (input) args -> ArgParser class instance

    """

    if args.arg_exist("-S"):
        log.load_keyword(args.get_val("-S"))

    if args.arg_exist("-k"):
        log.set_predicate(args.get_val("-k"))

    if args.arg_exist("-m"):
        fhdr = gen_libs.openfile(args.get_val("-m"))
        log.load_marker(fhdr)
        fhdr.close()

    if args.arg_exist("-F"):
        fhdr = gen_libs.openfile(args.get_val("-F"))
        log.load_regex(fhdr)
        fhdr.close()

    if args.arg_exist("-i"):
        fhdr = gen_libs.openfile(args.get_val("-i"))
        log.load_ignore(fhdr)
        fhdr.close()


def read_file(log, fname, inode, offset):

    """Function:  read_file

    Description:  Locates the starting point in the file, reads data from file,
        and updates the LogFile class with the data and ending offset.

    Arguments:
        (input) log -> LogFile class instance
        (input) fname -> File name being read
        (input) inode -> Inode of the file name
        (input) offset -> Starting point in the file, value in bytes

    """

    with open(fname, "r", encoding="UTF-8") as f_hldr:
        f_hldr.seek(0, os.SEEK_END)
        file_size = f_hldr.tell()
        f_hldr.seek(offset)
        data = f_hldr.read(file_size - offset)

    if data:
        log.load_loglist(data)

    log.lastline = str(inode) + ":" + str(file_size)


def fetch_log2(log, args):

    """Function:  fetch_log2

    Description:  Gets the inode and offset value, determines if the inode is
        current log file.  Finds the amount to read in the log file by
        checking log file size with current offset value and reads any
        difference into the LogFile class.

    Arguments:
        (input) log -> LogFile class instance
        (input) args -> ArgParser class instance

    """

    inode2 = os.stat(args.get_val("-f")[0]).st_ino
    # Start with current inode and offset or with new inode and start of file
    # Note: Ignore the 2to3 warning for map(), results are parsed out
    inode, offset = \
        map(int, log.marker.split(":")) if log.marker else (inode2, 0)

    if inode == inode2:
        read_file(log, args.get_val("-f")[0], inode, offset)

    else:
        # Find old inode and read in remaining lines in old file
        for t_file in glob.glob(args.get_val("-f")[0] + "*"):
            if inode == os.stat(t_file).st_ino:
                read_file(log, t_file, inode, offset)
                break

        read_file(log, args.get_val("-f")[0], inode2, 0)


def run_program(args):

    """Function:  run_program

    Description:  Controls the running of the program by fetching the log
        entries, updating the file marker, and sending the log entries to
        output.

    Arguments:
        (input) args -> ArgParser class instance

    """

    if args.arg_exist("-c") and args.arg_exist("-m"):
        gen_libs.clear_file(args.get_val("-m"))

    log = gen_class.LogFile()
    load_attributes(log, args)

    if args.get_val("-R") == "offset":
        fetch_log2(log, args)

        if log.loglist:
            log.filter_keyword()
            log.filter_ignore()
            log.filter_regex()
            log_2_output(log, args)
            update_marker(args, log.lastline)

    else:
        if args.arg_exist("-f"):
            fetch_log(log, args)

        elif not sys.stdin.isatty():
            fetch_log_stdin(log)

        if log.loglist:
            if not full_chk(args):
                find_marker(log)

            log.filter_keyword()
            log.filter_ignore()
            log.filter_regex()
            log_2_output(log, args)
            update_marker(args, log.lastline)


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        defaults -> Dictionary of required options with their default values
        file_crt -> List of options which require files to be created
        file_perm -> File check options with their perms in octal
        multi_val -> List of options that will have multiple values
        opt_con_or -> Dictionary of options requiring other options
        opt_def -> Dictionary of optional options with their default values
        opt_req -> List of options that are required for default values
        opt_val -> List of options which require values
        opt_valid_val -> Dictionary of options with their valid values

    Arguments:
        (input) argv -> Arguments from the command line

    """

    defaults = {"-g": "w", "-R": "lastline"}
    file_crt = ["-m"]
    file_perm = {"-f": 4, "-i": 4, "-m": 6, "-F": 4}
    multi_val = ["-f", "-s", "-t", "-S"]
    opt_con_or = {"-c": ["-m"], "-s": ["-t"]}
    opt_def = {"-k": "or"}
    opt_req = ["-g"]
    opt_val = [
        "-i", "-m", "-o", "-s", "-t", "-y", "-F", "-S", "-k", "-g", "-R"]
    opt_valid_val = {"-k": ["and", "or"], "-g": ["a", "w"]}

    # Process argument list from command line
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val, multi_val=multi_val, do_parse=True)

    # Set default search logic
    if args.arg_exist("-S") and not args.arg_exist("-k"):
        args.arg_default("-k", opt_def=opt_def)

    # Set default write file mode
    args.arg_add_def(defaults=defaults, opt_req=opt_req)

    if not gen_libs.help_func(args, __version__, help_message)              \
       and args.arg_cond_req_or(opt_con_or=opt_con_or)                      \
       and args.arg_file_chk(file_perm_chk=file_perm, file_crt=file_crt)    \
       and args.arg_valid_val(opt_valid_val=opt_valid_val):

        try:
            prog_lock = gen_class.ProgramLock(
                sys.argv, args.get_val("-y", def_val=""))
            run_program(args)
            del prog_lock

        except gen_class.SingleInstanceException:
            print(f'WARNING:  lock in place for check_log with id of:'
                  f' {args.get_val("-y", def_val="")}')


if __name__ == "__main__":
    sys.exit(main())
