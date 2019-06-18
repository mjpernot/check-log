#!/usr/bin/python
# Classification (U)

"""Program:  filter_data.py

    Description:  Unit testing of filter_data in check_log.py.

    Usage:
        test/unit/check_log/filter_data.py

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
        test_empty_filter -> Check for empty filter string.
        test_match_some -> Regex matches some of the log entries.
        test_no_match -> Regex matches no log entries.
        test_match_all -> Regex matches all log entries.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.filter_str0 = ""
        self.filter_str = "\d{4}\-\d{2}\-\d{2}"
        self.filter_str2 = "d{2}:\d{2}:\d{2}"

        self.log_array = ["2018-09-19 This is log line one",
                          "2018-09-19 This is log line two"]
        self.log_array2 = ["2018-09-19 This is log line one",
                           "11:11:11 This line to be removed",
                           "2018-09-19 This is log line two"]

        self.results0 = []
        self.results1 = ["2018-09-19 This is log line one",
                         "2018-09-19 This is log line two"]
        self.results2 = ["2018-09-19 This is log line one",
                         "11:11:11 This line to be removed",
                         "2018-09-19 This is log line two"]

    def test_empty_filter(self):

        """Function:  test_empty_filter

        Description:  Check for empty filter string.

        Arguments:

        """

        self.assertEqual(check_log.filter_data(self.log_array2,
                                               self.filter_str0),
                         self.results2)

    def test_match_some(self):

        """Function:  test_match_some

        Description:  Regex matches some of the log entries.

        Arguments:

        """

        self.assertEqual(check_log.filter_data(self.log_array2,
                                               self.filter_str), self.results1)

    def test_no_match(self):

        """Function:  test_no_match

        Description:  Regex matches no log entries.

        Arguments:

        """

        self.assertEqual(check_log.filter_data(self.log_array,
                                               self.filter_str2),
                         self.results0)

    def test_match_all(self):

        """Function:  test_match_all

        Description:  Regex matches all log entries.

        Arguments:

        """

        self.assertEqual(check_log.filter_data(self.log_array,
                                               self.filter_str), self.results1)


if __name__ == "__main__":
    unittest.main()
