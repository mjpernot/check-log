#!/usr/bin/python
# Classification (U)

"""Program:  find_marker_array.py

    Description:  Integration testing of find_marker_array in check_log.py.

    Usage:
        test/integration/check_log/find_marker_array.py

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
        test_find_marker_array -> Find the line marker in the array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        self.args_array = {"-m": os.path.join(self.test_path,
                                              "find_marker_array_file.txt")}

        self.log_array = ["This is log line one", "This is log line two",
                          "This is log line three", "This is log line four",
                          "This is log line five"]

        self.results = ["This is log line three", "This is log line four",
                        "This is log line five"]

    def test_find_marker_array(self):

        """Function:  test_find_marker_array

        Description:  Find the line marker in the array.

        Arguments:

        """

        self.assertEqual(check_log.find_marker_array(self.args_array,
                                                     self.log_array),
                         self.results)


if __name__ == "__main__":
    unittest.main()
