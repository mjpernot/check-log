#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in check_log.py.

    Usage:
        test/unit/check_log/run_program.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import check_log
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_no_log_files -> Test with no log files to scan.
        test_exit_option -> Test sys.exit check.
        test_clear_option -> Test -c and -m options.
        test_stdin_empty -> Test with standard in and with empty log array.
        test_f_option_empty -> Test with -f option and with empty log array.
        test_f_option_set -> Test with -f option in args_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args_array = {}

    @mock.patch("check_log.fetch_log_stdin")
    @mock.patch("check_log.sys.stdin")
    def test_no_log_files(self, mock_sys, mock_log):

        """Function:  test_no_log_files

        Description:  Test with no log files to scan.

        Arguments:
            None

        """

        mock_sys.isatty.return_value = True
        mock_log.return_value = []

        with gen_libs.no_std_out():
            self.assertFalse(check_log.run_program(self.args_array))

    def test_exit_option(self):

        """Function:  test_exit_option

        Description:  Test sys.exit check.

        Arguments:
            None

        """

        self.args_array["-c"] = True

        with gen_libs.no_std_out():
            self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.gen_libs")
    def test_clear_option(self, mock_lib):

        """Function:  test_clear_option

        Description:  Test -c and -m options.

        Arguments:
            None

        """

        self.args_array["-c"] = True
        self.args_array["-m"] = "File Place Holder"

        mock_lib.clear_files.return_value = True

        self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.fetch_log_stdin")
    @mock.patch("check_log.sys.stdin")
    def test_stdin_empty(self, mock_sys, mock_log):

        """Function:  test_stdin_empty

        Description:  Test with standard in and with empty log array.

        Arguments:
            None

        """

        mock_sys.isatty.return_value = False
        mock_log.return_value = []

        self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.fetch_log")
    def test_f_option_empty(self, mock_log):

        """Function:  test_f_option_empty

        Description:  Test with -f option and with empty log array.

        Arguments:
            None

        """

        self.args_array["-f"] = "File_Place_Holder"

        mock_log.return_value = []

        self.assertFalse(check_log.run_program(self.args_array))

    def mock_out(log_array, args_array):

        """Function:  mock_out

        Description:  Mock of check_log.log_2_output function.

        Arguments:
            (input) log_array -> Array of log entries.
            (input) args_array -> Array of command line options and values.
            (output)  Return True.

        """

        return True

    @mock.patch("check_log.log_2_output", mock_out)
    @mock.patch("check_log.filter_data")
    @mock.patch("check_log.get_filter_data")
    @mock.patch("check_log.ignore_msgs")
    @mock.patch("check_log.get_ignore_msgs")
    @mock.patch("check_log.update_marker")
    @mock.patch("check_log.fetch_log")
    def test_f_option_set(self, mock_log, mock_marker, mock_getign,
                          mock_ignore, mock_getflt, mock_filter):

        """Function:  test_f_option_set

        Description:  Test with -f option in args_array.

        Arguments:
            None

        """

        self.args_array["-f"] = "File_Place_Holder"

        mock_log.return_value = ["2018-09-19 This is log line one"]
        mock_marker.return_value = True
        mock_getign.return_value = True
        mock_ignore.return_value = ["2018-09-19 This is log line one"]
        mock_getflt.return_value = True
        mock_filter.return_value = ["2018-09-19 This is log line one"]

        self.assertFalse(check_log.run_program(self.args_array))


if __name__ == "__main__":
    unittest.main()
