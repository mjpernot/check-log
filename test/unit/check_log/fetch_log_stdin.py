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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import check_log
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_no_lines -> Passing in no lines.
        test_multiple_lines -> Passing in multiple lines.
        test_single_line_no_find -> Single line from standard - no find.
        test_single_line_found -> Single line from standard - found.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-f": "Log file"}

        self.results0 = []
        self.results1 = ["Line one"]
        self.results2 = ["Line one", "Line two"]

    @mock.patch("check_log.sys.stdin", io.StringIO(u""))
    @mock.patch("check_log.full_chk")
    def test_no_lines(self, mock_chk):

        """Function:  test_no_lines

        Description:  Passing in no lines.

        Arguments:

        """

        mock_chk.return_value = True

        self.assertEqual(check_log.fetch_log_stdin(self.args_array),
                         self.results0)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.full_chk")
    def test_multiple_lines(self, mock_chk):

        """Function:  test_multiple_lines

        Description:  Passing in multiple lines.

        Arguments:

        """

        mock_chk.return_value = True

        self.assertEqual(check_log.fetch_log_stdin(self.args_array),
                         self.results2)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\n"))
    @mock.patch("check_log.find_marker_array")
    @mock.patch("check_log.full_chk")
    def test_single_line_no_find(self, mock_chk, mock_find):

        """Function:  test_single_line_no_find

        Description:  Single line from standard - no find.

        Arguments:

        """

        mock_chk.return_value = False
        mock_find.return_value = []

        self.assertEqual(check_log.fetch_log_stdin(self.args_array),
                         self.results0)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\n"))
    @mock.patch("check_log.full_chk")
    def test_single_line_found(self, mock_chk):

        """Function:  test_single_line_found

        Description:  Single line from standard - found.

        Arguments:

        """

        mock_chk.return_value = True

        self.assertEqual(check_log.fetch_log_stdin(self.args_array),
                         self.results1)


if __name__ == "__main__":
    unittest.main()
