# Classification (U)

"""Program:  fetch_log.py

    Description:  Unit testing of fetch_log in check_log.py.

    Usage:
        test/unit/check_log/fetch_log.py

    Arguments:

"""

# Libraries and Global Variables

# Pylint errors to ignore for entire file
# pylint:disable=R1732

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import check_log                    # pylint:disable=E0401,C0413
import lib.gen_class as gen_class   # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val
        update_arg

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def update_arg(self, skey, data, insert=False):

        """Method:  update_arg

        Description:  Method stub holder for gen_class.ArgParser.update_arg.

        Arguments:

        """

        if insert:
            self.args_array[skey] = data


class UnitTest(unittest.TestCase):      # pylint:disable=R0902

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_fetch_all_log
        test_fetch_partial_log
        test_fetch_empty_log
        test_fetch_one_log

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argspar = ArgParser()
        self.log = gen_class.LogFile()
        self.file_0 = "test/unit/check_log/testfiles/fetch_log_file0.txt"
        self.file_1 = "test/unit/check_log/testfiles/fetch_log_file1.txt"
        self.file_2 = "test/unit/check_log/testfiles/fetch_log_file2.txt"
        self.file_3 = "test/unit/check_log/testfiles/fetch_log_file3.txt"
        self.args_array = {"-f": [self.file_1, self.file_2, self.file_3]}
        self.argspar.args_array = self.args_array
        self.results0 = []
        self.results1 = ["This is line one of log", "This is line two of log",
                         "This is line three of log"]
        self.results2 = ["This is line four of log",
                         "This is line five of log", "This is line six of log",
                         "This is line seven of log"]
        self.results3 = ["This is line one of log", "This is line two of log",
                         "This is line three of log",
                         "This is line four of log",
                         "This is line five of log", "This is line six of log",
                         "This is line seven of log"]

    @mock.patch("check_log.gen_libs.openfile")
    def test_fetch_all_log(self, mock_open):

        """Function:  test_fetch_all_log

        Description:  Return log entries from all log files.

        Arguments:

        """

        mock_open.side_effect = [
            open(self.argspar.args_array["-f"][0], "r", encoding="UTF-8"),
            open(self.argspar.args_array["-f"][1], "r", encoding="UTF-8"),
            open(self.argspar.args_array["-f"][2], "r", encoding="UTF-8")]

        check_log.fetch_log(self.log, self.argspar)

        self.assertEqual(self.log.loglist, self.results3)

    @mock.patch("check_log.gen_libs.openfile")
    def test_fetch_partial_log(self, mock_open):

        """Function:  test_fetch_partial_log

        Description:  Return log entries from some log files.

        Arguments:

        """

        mock_open.side_effect = [
            open(self.argspar.args_array["-f"][1], "r", encoding="UTF-8"),
            open(self.argspar.args_array["-f"][2], "r", encoding="UTF-8")]

        check_log.fetch_log(self.log, self.argspar)

        self.assertEqual(self.log.loglist, self.results2)

    @mock.patch("check_log.gen_libs.openfile")
    def test_fetch_empty_log(self, mock_open):

        """Function:  test_fetch_empty_log

        Description:  Return an empty log.

        Arguments:

        """

        self.argspar.args_array = {"-f": [self.file_0]}

        mock_open.return_value = open(
            self.argspar.args_array["-f"][0], "r", encoding="UTF-8")

        check_log.fetch_log(self.log, self.argspar)

        self.assertEqual(self.log.loglist, self.results0)

    @mock.patch("check_log.gen_libs.openfile")
    def test_fetch_one_log(self, mock_open):

        """Function:  test_fetch_one_log

        Description:  Return log entries from one log file.

        Arguments:

        """

        self.argspar.args_array = {"-f": [self.file_1]}

        mock_open.return_value = open(
            self.argspar.args_array["-f"][0], "r", encoding="UTF-8")

        check_log.fetch_log(self.log, self.argspar)

        self.assertEqual(self.log.loglist, self.results1)


if __name__ == "__main__":
    unittest.main()
