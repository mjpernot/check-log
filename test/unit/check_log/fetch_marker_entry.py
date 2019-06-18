#!/usr/bin/python
# Classification (U)

"""Program:  fetch_marker_entry.py

    Description:  Unit testing of fetch_marker_entry in check_log.py.

    Usage:
        test/unit/check_log/fetch_marker_entry.py

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
        test_marker_line -> Return marker with single line.
        test_empty_marker -> Return an empty marker.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.file_0 = "test/unit/check_log/testfiles/fetch_marker_entry0.txt"
        self.file_1 = "test/unit/check_log/testfiles/fetch_marker_entry1.txt"

        self.results0 = ""
        self.results1 = "This is line marker one"

    def test_marker_line(self):

        """Function:  test_marker_line

        Description:  Return marker with single line.

        Arguments:

        """

        self.assertEqual(check_log.fetch_marker_entry(self.file_1),
                         self.results1)

    def test_empty_marker(self):

        """Function:  test_empty_marker

        Description:  Return an empty marker.

        Arguments:

        """

        self.assertEqual(check_log.fetch_marker_entry(self.file_0),
                         self.results0)


if __name__ == "__main__":
    unittest.main()
