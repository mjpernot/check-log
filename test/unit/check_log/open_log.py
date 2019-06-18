#!/usr/bin/python
# Classification (U)

"""Program:  open_log.py

    Description:  Unit testing of open_log in check_log.py.

    Usage:
        test/unit/check_log/open_log.py

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
import mock

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
        test_fill_chk_false -> Full check returns False.
        test_fill_chk_true -> Full check returns True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-f": "Test_File"}

    @mock.patch("check_log.full_chk")
    @mock.patch("check_log.find_marker")
    def test_fill_chk_false(self, mock_marker, mock_chk):

        """Function:  test_fill_chk_false

        Description:  Full check returns False.

        Arguments:

        """

        mock_chk.return_value = False
        mock_marker.return_value = "File_Handler2"

        self.assertEqual(check_log.open_log(self.args_array), "File_Handler2")

    @mock.patch("check_log.full_chk")
    @mock.patch("check_log.open")
    def test_fill_chk_true(self, mock_open, mock_chk):

        """Function:  test_fill_chk_true

        Description:  Full check returns True.

        Arguments:

        """

        mock_chk.return_value = True
        mock_open.return_value = "File_Handler"

        self.assertEqual(check_log.open_log(self.args_array), "File_Handler")


if __name__ == "__main__":
    unittest.main()
