#!/usr/bin/python
# Classification (U)

"""Program:  fetch_marker_entry.py

    Description:  Integration testing of fetch_marker_entry in check_log.py.

    Usage:
        test/integration/check_log/fetch_marker_entry.py

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
        setUp -> Integration testing initilization.
        test_fetch_marker_entry -> Return returning data from marker file.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        self.fname = os.path.join(self.test_path,
                                  "fetch_marker_entry_file.txt")

        self.results = "This is line marker one"

    def test_fetch_marker_entry(self):

        """Function:  test_fetch_marker_entry

        Description:  Return returning data from marker file.

        Arguments:

        """

        self.assertEqual(check_log.fetch_marker_entry(self.fname),
                         self.results)


if __name__ == "__main__":
    unittest.main()
