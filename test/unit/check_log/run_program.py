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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import check_log
import lib.gen_class as gen_class
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = dict()

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_default.

        Arguments:

        """

        if arg in self.args_array:
            return True

        return False

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of unit testing.

    Methods:
        setUp
        test_offset2
        test_offset
        test_clear_option4
        test_clear_option3
        test_clear_option2
        test_clear_option
        test_full_chk
        test_loglist_data
        test_stdin
        test_f_option_not_set
        test_f_option_set

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argspar = ArgParser()
        self.log = gen_class.LogFile()
        self.log.loglist = ["Testdata"]
        self.log_file = "/opt/local/check-log/logfile"

    @mock.patch("check_log.update_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.log_2_output", mock.Mock(return_value=True))
    @mock.patch("check_log.fetch_log2", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    @mock.patch("check_log.gen_class.LogFile")
    def test_offset2(self, mock_log):

        """Function:  test_offset2

        Description:  Test with offset option and log entries.

        Arguments:

        """

        self.argspar.args_array["-R"] = "offset"

        mock_log.return_value = self.log

        self.assertFalse(check_log.run_program(self.argspar))

    @mock.patch("check_log.fetch_log2", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    @mock.patch("check_log.gen_class.LogFile")
    def test_offset(self, mock_log):

        """Function:  test_offset

        Description:  Test with offset option.

        Arguments:

        """

        self.argspar.args_array["-R"] = "offset"

        mock_log.return_value = self.log

        self.log.loglist = list()

        self.assertFalse(check_log.run_program(self.argspar))

    @mock.patch("check_log.update_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.log_2_output", mock.Mock(return_value=True))
    @mock.patch("check_log.find_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.full_chk", mock.Mock(return_value=True))
    @mock.patch("check_log.fetch_log", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    @mock.patch("check_log.gen_class.LogFile")
    def test_clear_option4(self, mock_log):

        """Function:  test_clear_option4

        Description:  Test with no -c or -m arguments.

        Arguments:

        """

        mock_log.return_value = self.log

        self.assertFalse(check_log.run_program(self.argspar))

    @mock.patch("check_log.update_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.log_2_output", mock.Mock(return_value=True))
    @mock.patch("check_log.find_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.full_chk", mock.Mock(return_value=True))
    @mock.patch("check_log.fetch_log", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    @mock.patch("check_log.gen_class.LogFile")
    def test_clear_option3(self, mock_log):

        """Function:  test_clear_option3

        Description:  Test with -m argument only.

        Arguments:

        """

        self.argspar.args_array["-m"] = "/opt/local/check-log/markerfile"

        mock_log.return_value = self.log

        self.assertFalse(check_log.run_program(self.argspar))

    @mock.patch("check_log.update_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.log_2_output", mock.Mock(return_value=True))
    @mock.patch("check_log.find_marker", mock.Mock(return_value=True))
    @mock.patch("check_log.full_chk", mock.Mock(return_value=True))
    @mock.patch("check_log.fetch_log", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    @mock.patch("check_log.gen_class.LogFile")
    def test_clear_option2(self, mock_log):

        """Function:  test_clear_option2

        Description:  Test with -c argument only.

        Arguments:

        """

        self.argspar.args_array["-c"] = True

        mock_log.return_value = self.log

        self.assertFalse(check_log.run_program(self.argspar))

    @mock.patch("check_log.gen_libs.clear_file", mock.Mock(return_value=True))
    def test_clear_option(self):

        """Function:  test_clear_option

        Description:  Test with -c and -m options.

        Arguments:

        """

        self.argspar.args_array["-c"] = True
        self.argspar.args_array["-m"] = "/opt/local/check-log/markerfile"

        self.assertFalse(check_log.run_program(self.argspar))

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
        self.argspar.args_array["-f"] = self.log_file

        self.assertFalse(check_log.run_program(self.argspar))

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
        self.argspar.args_array["-f"] = self.log_file

        self.assertFalse(check_log.run_program(self.argspar))

    @mock.patch("check_log.fetch_log_stdin", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    @mock.patch("check_log.sys.stdin")
    def test_stdin(self, mock_sys):

        """Function:  test_stdin

        Description:  Test with standard in option.

        Arguments:

        """

        mock_sys.isatty.return_value = False

        self.assertFalse(check_log.run_program(self.argspar))

    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    def test_f_option_not_set(self):

        """Function:  test_f_option_not_set

        Description:  Test with -f option not in args_array.

        Arguments:

        """

        self.assertFalse(check_log.run_program(self.argspar))

    @mock.patch("check_log.fetch_log", mock.Mock(return_value=True))
    @mock.patch("check_log.load_attributes", mock.Mock(return_value=True))
    def test_f_option_set(self):

        """Function:  test_f_option_set

        Description:  Test with -f option in args_array.

        Arguments:

        """

        self.argspar.args_array["-f"] = self.log_file

        self.assertFalse(check_log.run_program(self.argspar))


if __name__ == "__main__":
    unittest.main()
