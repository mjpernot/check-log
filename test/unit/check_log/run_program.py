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
import lib.gen_class as gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_clear_option -> Test with -c and -m options.
        test_full_chk -> Test with full_chk returning True.
        test_loglist_data -> Test with loglist having data.
        test_stdin -> Test with standard in option.
        test_f_option_set -> Test with -f option in args_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.log = gen_class.LogFile()
        self.log.loglist = ["Testdata"]
        self.log_file = "/opt/local/check-log/logfile"

    @mock.patch("check_log.gen_libs.clear_file", mock.Mock(return_value=True))
    def test_clear_option(self):

        """Function:  test_clear_option

        Description:  Test with -c and -m options.

        Arguments:

        """

        self.args_array["-c"] = True
        self.args_array["-m"] = "/opt/local/check-log/markerfile"

        self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.update_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.log_2_output", mock.Mock(return_value=True))
    @mock.patch("check_log.find_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.full_chk", mock.Mock(return_value=True))
    @mock.patch("check_log.fetch_log", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    @mock.patch("check_log.gen_class.LogFile")
    def test_full_chk(self, mock_log):

        """Function:  test_full_chk

        Description:  Test with full_chk returning True.

        Arguments:

        """

        mock_log.return_value = self.log
        self.args_array["-f"] = self.log_file

        self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.update_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.log_2_output", mock.Mock(return_value=True))
    @mock.patch("check_log.full_chk", mock.Mock(return_value=False))
    @mock.patch("check_log.fetch_log", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    @mock.patch("check_log.gen_class.LogFile")
    def test_loglist_data(self, mock_log):

        """Function:  test_loglist_data

        Description:  Test with loglist having data.

        Arguments:

        """

        mock_log.return_value = self.log
        self.args_array["-f"] = self.log_file

        self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.fetch_log_stdin", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    @mock.patch("check_log.sys.stdin")
    def test_stdin(self, mock_sys):

        """Function:  test_stdin

        Description:  Test with standard in option.

        Arguments:

        """

        mock_sys.isatty.return_value = False

        self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.fetch_log", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    def test_f_option_set(self):

        """Function:  test_f_option_set

        Description:  Test with -f option in args_array.

        Arguments:

        """

        self.args_array["-f"] = self.log_file

        self.assertFalse(check_log.run_program(self.args_array))


if __name__ == "__main__":
    unittest.main()
