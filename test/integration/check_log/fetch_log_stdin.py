#!/usr/bin/python
# Classification (U)

"""Program:  fetch_log_stdin.py

    Description:  Integration testing of fetch_log_stdin in check_log.py.

    Usage:
        test/integration/check_log/fetch_log_stdin.py

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
        setUp -> Integration testing initilization.
        test_multiple_lines2 -> Passing in multiple lines, partial find.
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

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        self.file_marker = os.path.join(self.test_path,
                                        "fetch_log_stdin_entry.txt")

        self.args_array = {}

        self.results0 = []
        self.results1 = ["Line one"]
        self.results2 = ["Line one", "Line two"]
        self.results3 = ["Line two"]

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    def test_multiple_lines2(self):

        """Function:  test_multiple_lines2

        Description:  Passing in multiple lines, partial find.

        Arguments:

        """

        self.args_array["-m"] = self.file_marker

        self.assertEqual(check_log.fetch_log_stdin(self.args_array),
                         self.results3)

    @mock.patch("check_log.sys.stdin", io.StringIO(u""))
    def test_no_lines(self):

        """Function:  test_no_lines

        Description:  Passing in no lines.

        Arguments:

        """

        self.assertEqual(check_log.fetch_log_stdin(self.args_array),
                         self.results0)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    def test_multiple_lines(self):

        """Function:  test_multiple_lines

        Description:  Passing in multiple lines.

        Arguments:

        """

        self.assertEqual(check_log.fetch_log_stdin(self.args_array),
                         self.results2)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\n"))
    def test_single_line_no_find(self):

        """Function:  test_single_line_no_find

        Description:  Single line from standard - no find.

        Arguments:

        """

        self.args_array["-m"] = self.file_marker

        self.assertEqual(check_log.fetch_log_stdin(self.args_array),
                         self.results0)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\n"))
    def test_single_line_found(self):

        """Function:  test_single_line_found

        Description:  Single line from standard - found.

        Arguments:

        """

        self.assertEqual(check_log.fetch_log_stdin(self.args_array),
                         self.results1)


if __name__ == "__main__":
    unittest.main()
