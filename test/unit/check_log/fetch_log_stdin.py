#!/usr/bin/python
# Classification (U)

"""Program:  fetch_log_stdin.py

    Description:  Unit testing of fetch_log_stdin in check_log.py.

    Usage:
        test/unit/check_log/fetch_log_stdin.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import io
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import check_log
import lib.gen_class as gen_class
import version

__version__ = version.__version__

if sys.version_info < (3, 0):
    DATA = u"Line one\nLine two\n"
    DATA2 = u""
    DATA3 = u"\n"
    DATA4 = u"Line one\n"

else:
    DATA = "Line one\nLine two\n"
    DATA2 = ""
    DATA3 = "\n"
    DATA4 = "Line one\n"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_lines
        test_multiple_lines
        test_single_line_empty_line
        test_single_line_found

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.log = gen_class.LogFile()
        self.results0 = [""]
        self.results1 = ["Line one"]
        self.results2 = ["Line one", "Line two"]

    @mock.patch("check_log.sys.stdin", io.StringIO(DATA2))
    def test_no_lines(self):

        """Function:  test_no_lines

        Description:  Passing in no lines.

        Arguments:

        """

        check_log.fetch_log_stdin(self.log)

        self.assertEqual(self.log.loglist, [])

    @mock.patch("check_log.sys.stdin", io.StringIO(DATA))
    def test_multiple_lines(self):

        """Function:  test_multiple_lines

        Description:  Passing in multiple lines.

        Arguments:

        """

        check_log.fetch_log_stdin(self.log)

        self.assertEqual(self.log.loglist, self.results2)

    @mock.patch("check_log.sys.stdin", io.StringIO(DATA3))
    def test_single_line_empty_line(self):

        """Function:  test_single_line_empty_line

        Description:  Single line from standard - empty line.

        Arguments:

        """

        check_log.fetch_log_stdin(self.log)

        self.assertEqual(self.log.loglist, self.results0)

    @mock.patch("check_log.sys.stdin", io.StringIO(DATA4))
    def test_single_line_found(self):

        """Function:  test_single_line_found

        Description:  Single line from standard - found.

        Arguments:

        """

        check_log.fetch_log_stdin(self.log)

        self.assertEqual(self.log.loglist, self.results1)


if __name__ == "__main__":
    unittest.main()
