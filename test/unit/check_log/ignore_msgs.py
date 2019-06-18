#!/usr/bin/python
# Classification (U)

"""Program:  ignore_msgs.py

    Description:  Unit testing of ignore_msgs in check_log.py.

    Usage:
        test/unit/check_log/ignore_msgs.py

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
        test_empty_log_array -> Test with empty log array.
        test_all_lines_remove -> Test with all lines removed from log array.
        test_two_ignores_found -> Test with two ignore lines found.
        test_one_ignore_found -> Test with one ignore line found.
        test_no_ignores_found -> Test with ignore not finding any lines.
        test_empty_ignore_array -> Test with empty ignore array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.log_array = ["first line to ignore", "second line to ignore",
                          "third line to ignore"]

        self.ignore_array = []
        self.ignore_array2 = ["nothing is found"]
        self.ignore_array3 = ["first line to ignore"]
        self.ignore_array4 = ["first line to ignore", "second line to ignore"]
        self.ignore_array5 = ["first line to ignore", "second line to ignore",
                              "third line to ignore"]

        self.return_array = ["first line to ignore", "second line to ignore",
                             "third line to ignore"]
        self.return_array3 = ["second line to ignore", "third line to ignore"]
        self.return_array4 = ["third line to ignore"]
        self.return_array5 = []

    def test_empty_log_array(self):

        """Function:  test_empty_log_array

        Description:  Test with empty log array.

        Arguments:

        """

        self.assertEqual(check_log.ignore_msgs([], self.ignore_array), [])

    def test_all_lines_remove(self):

        """Function:  test_all_lines_remove

        Description:  Test with all lines removed from log array.

        Arguments:

        """

        self.assertEqual(check_log.ignore_msgs(self.log_array,
                                               self.ignore_array5),
                         self.return_array5)

    def test_two_ignores_found(self):

        """Function:  test_two_ignores_found

        Description:  Test with two ignore lines found.

        Arguments:

        """

        self.assertEqual(check_log.ignore_msgs(self.log_array,
                                               self.ignore_array4),
                         self.return_array4)

    def test_one_ignore_found(self):

        """Function:  test_one_ignore_found

        Description:  Test with one ignore line found.

        Arguments:

        """

        self.assertEqual(check_log.ignore_msgs(self.log_array,
                                               self.ignore_array3),
                         self.return_array3)

    def test_no_ignores_found(self):

        """Function:  test_no_ignores_found

        Description:  Test with ignore not finding any lines.

        Arguments:

        """

        self.assertEqual(check_log.ignore_msgs(self.log_array,
                                               self.ignore_array2),
                         self.return_array)

    def test_empty_ignore_array(self):

        """Function:  test_empty_ignore_array

        Description:  Test with empty ignore array.

        Arguments:

        """

        self.assertEqual(check_log.ignore_msgs(self.log_array,
                                               self.ignore_array),
                         self.return_array)


if __name__ == "__main__":
    unittest.main()
