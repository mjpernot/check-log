#!/usr/bin/python
# Classification (U)

"""Program:  find_marker.py

    Description:  Integration testing of find_marker in check_log.py.

    Usage:
        test/integration/check_log/find_marker.py

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
        setUp -> Integration testing initilization.
        test_no_find_marker -> Does not find the line marker.
        test_find_marker -> Finds the line marker.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        self.file_name1 = os.path.join(self.test_path, "find_marker_file.txt")
        self.file_name2 = os.path.join(self.test_path, "find_marker_file2.txt")

        self.args_array = {"-f": [self.file_name1, self.file_name2]}

    def test_no_find_marker(self):

        """Function:  test_no_find_marker

        Description:  Does not find the line marker.

        Arguments:
            None

        """

        self.args_array["-m"] = os.path.join(self.test_path,
                                             "find_marker_entry_file2.txt")

        f_hdlr = check_log.find_marker(self.args_array)
        file_name = f_hdlr.name
        f_hdlr.close()

        self.assertEqual(file_name, self.file_name1)

    def test_find_marker(self):

        """Function:  test_find_marker

        Description:  Finds the line marker.

        Arguments:
            None

        """

        self.args_array["-m"] = os.path.join(self.test_path,
                                             "find_marker_entry_file.txt")

        f_hdlr = check_log.find_marker(self.args_array)
        file_name = f_hdlr.name
        f_hdlr.close()

        self.assertEqual(file_name, self.file_name2)


if __name__ == "__main__":
    unittest.main()
