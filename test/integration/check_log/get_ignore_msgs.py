#!/usr/bin/python
# Classification (U)

"""Program:  get_ignore_msgs.py

    Description:  Integration testing of get_ignore_msgs in check_log.py.

    Usage:
        test/integration/check_log/get_ignore_msgs.py

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
        test_get_ignore_msgs -> Test reading data from file.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        self.args_array = {"-i": os.path.join(self.test_path,
                                              "get_ignore_msgs_file.txt")}

        self.result = ["first line to ignore", "second line to ignore"]

    def test_get_ignore_msgs(self):

        """Function:  test_get_ignore_msgs

        Description:  Test reading data from file.

        Arguments:
            None

        """

        self.assertEqual(check_log.get_ignore_msgs(self.args_array),
                         self.result)


if __name__ == "__main__":
    unittest.main()
