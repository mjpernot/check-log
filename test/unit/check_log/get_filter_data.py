#!/usr/bin/python
# Classification (U)

"""Program:  get_filter_data.py

    Description:  Unit testing of get_filter_data in check_log.py.

    Usage:
        test/unit/check_log/get_filter_data.py

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
        setUp -> Unit testing initilization.
        test_no_f_option_set -> Test with no -F option in args_array.
        test_empty_filter_file -> Test with empty expression file.
        test_get_filter_data2 -> Test multiple line expression file.
        test_get_filter_data -> Test getting single line expression.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.file0 = "test/unit/check_log/testfiles/get_filter_data0.txt"
        self.file1 = "test/unit/check_log/testfiles/get_filter_data.txt"
        self.file2 = "test/unit/check_log/testfiles/get_filter_data2.txt"
        self.args_array = {"-F": "Place Holder"}

        self.results0 = ""
        self.results1 = "\d{4}\-\d{2}\-\d{2}|d{2}:\d{2}:\d{2}"

    def test_no_f_option_set(self):

        """Function:  test_no_f_option_set

        Description:  Test with no -F option in args_array.

        Arguments:

        """

        self.args_array = {}

        self.assertEqual(check_log.get_filter_data(self.args_array),
                         self.results0)

    def test_empty_filter_file(self):

        """Function:  test_empty_filter_file

        Description:  Test with empty expression file.

        Arguments:

        """

        self.args_array["-F"] = self.file0

        self.assertEqual(check_log.get_filter_data(self.args_array),
                         self.results0)

    def test_get_filter_data2(self):

        """Function:  test_get_filter_data2

        Description:  Test multiple line expression file.

        Arguments:

        """

        self.args_array["-F"] = self.file2

        self.assertEqual(check_log.get_filter_data(self.args_array),
                         self.results1)

    def test_get_filter_data(self):

        """Function:  test_get_filter_data

        Description:  Test getting single line expression.

        Arguments:

        """

        self.args_array["-F"] = self.file1

        self.assertEqual(check_log.get_filter_data(self.args_array),
                         self.results1)


if __name__ == "__main__":
    unittest.main()
