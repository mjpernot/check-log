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
import lib.gen_class as gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_lines
        test_multiple_lines
        test_single_line

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.log = gen_class.LogFile()
        self.results0 = []
        self.results1 = ["Line one"]
        self.results2 = ["Line one", "Line two"]

    @mock.patch("check_log.sys.stdin", io.StringIO(u""))
    def test_no_lines(self):

        """Function:  test_no_lines

        Description:  Passing in no lines.

        Arguments:

        """

        check_log.fetch_log_stdin(self.log)
        self.assertEqual(self.log.loglist, self.results0)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    def test_multiple_lines(self):

        """Function:  test_multiple_lines

        Description:  Passing in multiple lines.

        Arguments:

        """

        check_log.fetch_log_stdin(self.log)
        self.assertEqual(self.log.loglist, self.results2)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\n"))
    def test_single_line(self):

        """Function:  test_single_line

        Description:  Single line from standard in.

        Arguments:

        """

        check_log.fetch_log_stdin(self.log)
        self.assertEqual(self.log.loglist, self.results1)


if __name__ == "__main__":
    unittest.main()
