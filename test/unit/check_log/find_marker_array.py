#!/usr/bin/python
# Classification (U)

"""Program:  find_marker_array.py

    Description:  Unit testing of find_marker_array in check_log.py.

    Usage:
        test/unit/check_log/find_marker_array.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_empty_ln_marker -> Empty line marker checked.
        test_empty_log_array -> Empty log array checked.
        test_no_find_marker -> Does not find line marker in array.
        test_find_marker_last -> Find line marker on last line of array.
        test_find_marker_first -> Find line marker in first line of array.
        test_find_marker_line -> Find the line marker in the array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-m": "Marker file"}

        self.log_array1 = ["This is log line one", "This is log line two",
                           "This is log line three",
                           "This is log line four", "This is log line five"]

        self.results1 = ["This is log line three", "This is log line four",
                         "This is log line five"]
        self.results2 = ["This is log line two", "This is log line three",
                         "This is log line four", "This is log line five"]
        self.results3 = []
        self.results4 = ["This is log line one", "This is log line two",
                         "This is log line three", "This is log line four",
                         "This is log line five"]

    @mock.patch("check_log.fetch_marker_entry")
    def test_empty_ln_marker(self, mock_fetch):

        """Function:  test_empty_ln_marker

        Description:  Empty line marker checked.

        Arguments:

        """

        mock_fetch.return_value = None

        self.assertEqual(check_log.find_marker_array(self.args_array,
                                                     self.log_array1),
                         self.results4)

    @mock.patch("check_log.fetch_marker_entry")
    def test_empty_log_array(self, mock_fetch):

        """Function:  test_empty_log_array

        Description:  Empty log array checked.

        Arguments:

        """

        mock_fetch.return_value = "This is no log line"

        self.assertEqual(check_log.find_marker_array(self.args_array, []),
                         self.results3)

    @mock.patch("check_log.fetch_marker_entry")
    def test_no_find_marker(self, mock_fetch):

        """Function:  test_no_find_marker

        Description:  Does not find line marker in array.

        Arguments:

        """

        mock_fetch.return_value = "This is no log line"

        self.assertEqual(check_log.find_marker_array(self.args_array,
                                                     self.log_array1),
                         self.results4)

    @mock.patch("check_log.fetch_marker_entry")
    def test_find_marker_last(self, mock_fetch):

        """Function:  test_find_marker_last

        Description:  Find line marker on last line of array.

        Arguments:

        """

        mock_fetch.return_value = "This is log line five"

        self.assertEqual(check_log.find_marker_array(self.args_array,
                                                     self.log_array1),
                         self.results3)

    @mock.patch("check_log.fetch_marker_entry")
    def test_find_marker_first(self, mock_fetch):

        """Function:  test_find_marker_first

        Description:  Find line marker in first line of array.

        Arguments:

        """

        mock_fetch.return_value = "This is log line one"

        self.assertEqual(check_log.find_marker_array(self.args_array,
                                                     self.log_array1),
                         self.results2)

    @mock.patch("check_log.fetch_marker_entry")
    def test_find_marker_line(self, mock_fetch):

        """Function:  test_find_marker_line

        Description:  Find the line marker in the array.

        Arguments:

        """

        mock_fetch.return_value = "This is log line two"

        self.assertEqual(check_log.find_marker_array(self.args_array,
                                                     self.log_array1),
                         self.results1)


if __name__ == "__main__":
    unittest.main()
