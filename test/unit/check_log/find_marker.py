#!/usr/bin/python
# Classification (U)

"""Program:  find_marker.py

    Description:  Unit testing of find_marker in check_log.py.

    Usage:
        test/unit/check_log/find_marker.py

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
        test_empty_ln_marker -> Empty line marker check.
        test_no_find_marker -> Does not find the marker.
        test_find_marker_2 -> Finds the line marker in second file.
        test_find_marker -> Finds the line marker.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        data = ["This is the first line", "This is the second line",
                "This is the third line", "This is the fourth line",
                "This is the fifth line", "This is the sixth line",
                "This is the seventh line"]
        self.log = gen_class.LogFile()
        self.log.loglist = data
        self.result = ["This is the fourth line",
                       "This is the fifth line",
                       "This is the sixth line",
                       "This is the seventh line"]
        self.result2 = ["This is the seventh line"]
        self.result3 = data

    def test_empty_ln_marker(self):

        """Function:  test_empty_ln_marker

        Description:  Empty line marker check.

        Arguments:

        """

        check_log.find_marker(self.log)

        self.assertEqual(self.log.loglist, self.result3)

    def test_no_find_marker(self):

        """Function:  test_no_find_marker

        Description:  Does not find the marker.

        Arguments:

        """

        self.log.marker = "This is the tenth line"
        check_log.find_marker(self.log)

        self.assertEqual(self.log.loglist, self.result3)

    def test_find_marker_2(self):

        """Function:  test_find_marker_2

        Description:  Finds the line marker.

        Arguments:

        """

        self.log.marker = "This is the sixth line"
        check_log.find_marker(self.log)

        self.assertEqual(self.log.loglist, self.result2)

    def test_find_marker(self):

        """Function:  test_find_marker

        Description:  Finds the line marker.

        Arguments:

        """

        self.log.marker = "This is the third line"
        check_log.find_marker(self.log)

        self.assertEqual(self.log.loglist, self.result)


if __name__ == "__main__":
    unittest.main()
