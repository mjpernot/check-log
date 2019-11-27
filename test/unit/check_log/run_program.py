#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in check_log.py.

    Usage:
        test/unit/check_log/run_program.py

    Arguments:

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

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_no_log_files -> Test with no log files to scan.
        test_exit_option -> Test sys.exit check.
        test_clear_option -> Test -c and -m options.
        test_stdin -> Test with standard in option.
        test_f_option_set -> Test with -f option in args_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}

    @mock.patch("check_log.fetch_log_stdin")
    @mock.patch("check_log.sys.stdin")
    def test_no_log_files(self, mock_sys, mock_log):

        """Function:  test_no_log_files

        Description:  Test with no log files to scan.

        Arguments:

        """

        mock_sys.isatty.return_value = True
        mock_log.return_value = []

        with gen_libs.no_std_out():
            self.assertFalse(check_log.run_program(self.args_array))

    def test_exit_option(self):

        """Function:  test_exit_option

        Description:  Test sys.exit check.

        Arguments:

        """

        self.args_array["-c"] = True

        with gen_libs.no_std_out():
            self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.gen_libs")
    def test_clear_option(self, mock_lib):

        """Function:  test_clear_option

        Description:  Test -c and -m options.

        Arguments:

        """

        self.args_array["-c"] = True
        self.args_array["-m"] = "File Place Holder"

        mock_lib.clear_files.return_value = True

        self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.fetch_log_stdin", mock.Mock(return_value=True))
    @mock.patch("check_log.sys.stdin")
    def test_stdin(self, mock_sys):

        """Function:  test_stdin

        Description:  Test with standard in option.

        Arguments:

        """

        mock_sys.isatty.return_value = False

        self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.update_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.log_2_output", mock.Mock(return_value=True))
    @mock.patch("check_log.find_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.full_chk", mock.Mock(return_value=False))
    @mock.patch("check_log.fetch_log", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    def test_f_option_set(self):

        """Function:  test_f_option_set

        Description:  Test with -f option in args_array.

        Arguments:

        """

        self.args_array["-f"] = "/tmp/logfile"

        self.assertFalse(check_log.run_program(self.args_array))


if __name__ == "__main__":
    unittest.main()
