#!/usr/bin/python
# Classification (U)

"""Program:  full_chk.py

    Description:  Integration testing of full_chk in check_log.py.

    Usage:
        test/integration/check_log/full_chk.py

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

    Methods:
        setUp
        test_file_not_empty
        test_file_is_empty

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

    def test_file_not_empty(self):

        """Function:  test_file_not_empty

        Description:  Test if file is not empty.

        Arguments:

        """

        args_array = {"-m": os.path.join(self.test_path,
                                         "full_chk_not_empty.txt")}

        self.assertFalse(check_log.full_chk(args_array))

    def test_file_is_empty(self):

        """Function:  test_file_is_empty

        Description:  Test if file is empty.

        Arguments:

        """

        args_array = {"-m": os.path.join(self.test_path, "full_chk_empty.txt")}

        self.assertTrue(check_log.full_chk(args_array))


if __name__ == "__main__":
    unittest.main()
