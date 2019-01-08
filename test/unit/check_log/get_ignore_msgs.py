#!/usr/bin/python
# Classification (U)

"""Program:  get_ignore_msgs.py

    Description:  Unit testing of get_ignore_msgs in check_log.py.

    Usage:
        test/unit/check_log/get_ignore_msgs.py

    Arguments:
        None

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

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_no_i_option_set -> Test with no -i option in args_array.
        test_multi_line_list -> Test with multiple lines in list.
        test_single_line_list -> Test with a single line list.
        test_empty_list -> Test with an empty ignore list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args_array = {"-i": "Place_Holder"}
        self.file = "test/unit/check_log/testfiles/get_ignore_msgs_file.txt"
        self.file2 = "test/unit/check_log/testfiles/get_ignore_msgs_file2.txt"
        self.file3 = "test/unit/check_log/testfiles/get_ignore_msgs_file3.txt"

        self.result = []
        self.result2 = ["first line to ignore"]
        self.result3 = ["first line to ignore", "second line to ignore"]

    def test_no_i_option_set(self):

        """Function:  test_no_i_option_set

        Description:  Test with no -i option in args_array.

        Arguments:
            None

        """

        self.assertEqual(check_log.get_ignore_msgs({}), self.result)

    def test_multi_line_list(self):

        """Function:  test_multi_line_list

        Description:  Test with multiple lines in list.

        Arguments:
            None

        """

        self.args_array["-i"] = self.file3

        self.assertEqual(check_log.get_ignore_msgs(self.args_array),
                         self.result3)

    def test_single_line_list(self):

        """Function:  test_single_line_list

        Description:  Test with a single line list.

        Arguments:
            None

        """

        self.args_array["-i"] = self.file2

        self.assertEqual(check_log.get_ignore_msgs(self.args_array),
                         self.result2)

    def test_empty_list(self):

        """Function:  test_empty_list

        Description:  Test with an empty ignore list.

        Arguments:
            None

        """

        self.args_array["-i"] = self.file

        self.assertEqual(check_log.get_ignore_msgs(self.args_array),
                         self.result)


if __name__ == "__main__":
    unittest.main()
