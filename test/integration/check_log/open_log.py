#!/usr/bin/python
# Classification (U)

"""Program:  open_log.py

    Description:  Integration testing of open_log in check_log.py.

    Usage:
        test/integration/check_log/open_log.py

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
        test_open_log_find -> Finds log marker in file.
        test_open_log_full -> Full check returns true.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        self.file_name1 = os.path.join(self.test_path, "find_marker_file.txt")
        self.file_name2 = os.path.join(self.test_path, "find_marker_file2.txt")

        self.args_array = {"-f": [self.file_name1, self.file_name2]}

    def test_open_log_find(self):

        """Function:  test_open_log_find

        Description:  Finds log marker in file.

        Arguments:

        """

        f_hdlr = check_log.open_log(self.args_array)
        file_name = f_hdlr.name
        f_hdlr.close()

        self.assertEqual(file_name, self.file_name1)

    def test_open_log_full(self):

        """Function:  test_open_log_full

        Description:  Full check returns true.

        Arguments:

        """

        self.args_array["-m"] = os.path.join(self.test_path,
                                             "open_log_entry_file.txt")

        f_hdlr = check_log.open_log(self.args_array)
        file_name = f_hdlr.name
        f_hdlr.close()

        self.assertEqual(file_name, self.file_name2)


if __name__ == "__main__":
    unittest.main()
