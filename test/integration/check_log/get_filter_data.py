#!/usr/bin/python
# Classification (U)

"""Program:  get_filter_data.py

    Description:  Integration testing of get_filter_data in check_log.py.

    Usage:
        test/integration/check_log/get_filter_data.py

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
        test_get_filter_data -> Test getting expression.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        self.args_array = {"-F": os.path.join(self.test_path,
                                              "get_filter_data_file.txt")}

        self.results = "\d{4}\-\d{2}\-\d{2}|d{2}:\d{2}:\d{2}"

    def test_get_filter_data(self):

        """Function:  test_get_filter_data

        Description:  Test getting expression.

        Arguments:

        """

        self.assertEqual(check_log.get_filter_data(self.args_array),
                         self.results)


if __name__ == "__main__":
    unittest.main()
