#!/usr/bin/python
# Classification (U)

"""Program:  full_chk.py

    Description:  Unit testing of full_chk in check_log.py.

    Usage:
        test/unit/check_log/full_chk.py

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

    Methods:
        setUp -> Unit testing initilization.
        test_m_and_r_options -> Test with -m and -r options selected.
        test_m_option_selected2 -> Test -m option with non-empty file.
        test_m_option_selected -> Test -m option in args_array with empty file.
        test_r_option_selected -> Test with -r option in args_array only.
        test_no_options_selected -> Test with no arguments in args_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}

    def test_m_and_r_options(self):

        """Function:  test_m_and_r_options

        Description:  Test with -m and -r options selected.

        Arguments:

        """

        self.args_array = {"-m": "test_file", "-r": True}

        self.assertEqual(check_log.full_chk(self.args_array), True)

    @mock.patch("check_log.gen_libs.is_empty_file")
    def test_m_option_selected2(self, mock_file):

        """Function:  test_m_option_selected2

        Description:  Test -m option with non-empty file.

        Arguments:

        """

        self.args_array = {"-m": "test_file"}

        mock_file.return_value = False

        self.assertEqual(check_log.full_chk(self.args_array), False)

    @mock.patch("check_log.gen_libs.is_empty_file")
    def test_m_option_selected(self, mock_file):

        """Function:  test_m_option_selected

        Description:  Test -m option in args_array with empty file.

        Arguments:

        """

        self.args_array = {"-m": "test_file"}

        mock_file.return_value = True

        self.assertEqual(check_log.full_chk(self.args_array), True)

    def test_r_option_selected(self):

        """Function:  test_r_option_selected

        Description:  Test with -r option in args_array only.

        Arguments:

        """

        self.args_array = {"-r": True}

        self.assertEqual(check_log.full_chk(self.args_array), True)

    def test_no_options_selected(self):

        """Function:  test_no_options_selected

        Description:  Test with no arguments in args_array.

        Arguments:

        """

        self.assertEqual(check_log.full_chk(self.args_array), True)


if __name__ == "__main__":
    unittest.main()
