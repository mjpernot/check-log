#!/usr/bin/python
# Classification (U)

"""Program:  fetch_log.py

    Description:  Unit testing of fetch_log in check_log.py.

    Usage:
        test/unit/check_log/fetch_log.py

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

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_fetch_all_log -> Return log entries from all log files.
        test_fetch_partial_log -> Return log entries from some log files.
        test_fetch_empty_log -> Return an empty log.
        test_fetch_one_log -> Return log entries from one log file.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.log = gen_class.LogFile()
        self.file_0 = "test/unit/check_log/testfiles/fetch_log_file0.txt"
        self.file_1 = "test/unit/check_log/testfiles/fetch_log_file1.txt"
        self.file_2 = "test/unit/check_log/testfiles/fetch_log_file2.txt"
        self.file_3 = "test/unit/check_log/testfiles/fetch_log_file3.txt"
        self.args_array = {"-f": [self.file_1, self.file_2, self.file_3]}
        self.args_array2 = {"-f": [self.file_1, self.file_2, self.file_3],
                            "-S": ["a"], "-k": "and"}
        self.args_array3 = {"-f": [self.file_1, self.file_2, self.file_3],
                            "-S": ["a"], "-k": "or"}
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

        mock_open.side_effect = [open(self.args_array["-f"][0], "r"),
                                 open(self.args_array["-f"][1], "r"),
                                 open(self.args_array["-f"][2], "r")]

        check_log.fetch_log(self.log, self.args_array)
        self.assertEqual(self.log.loglist, self.results3)

    @mock.patch("check_log.gen_libs.openfile")
    def test_fetch_partial_log(self, mock_open):

        """Function:  test_fetch_partial_log

        Description:  Return log entries from some log files.

        Arguments:

        """

        mock_open.side_effect = [open(self.args_array["-f"][1], "r"),
                                 open(self.args_array["-f"][2], "r")]

        check_log.fetch_log(self.log, self.args_array)
        self.assertEqual(self.log.loglist, self.results2)

    @mock.patch("check_log.gen_libs.openfile")
    def test_fetch_empty_log(self, mock_open):

        """Function:  test_fetch_empty_log

        Description:  Return an empty log.

        Arguments:

        """

        self.args_array = {"-f": [self.file_0]}
        mock_open.return_value = open(self.args_array["-f"][0], "r")

        check_log.fetch_log(self.log, self.args_array)
        self.assertEqual(self.log.loglist, self.results0)

    @mock.patch("check_log.gen_libs.openfile")
    def test_fetch_one_log(self, mock_open):

        """Function:  test_fetch_one_log

        Description:  Return log entries from one log file.

        Arguments:

        """

        self.args_array = {"-f": [self.file_1]}
        mock_open.return_value = open(self.args_array["-f"][0], "r")

        check_log.fetch_log(self.log, self.args_array)
        self.assertEqual(self.log.loglist, self.results1)


if __name__ == "__main__":
    unittest.main()
