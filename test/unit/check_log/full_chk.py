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

import mock

# Local
sys.path.append(os.getcwd())
import check_log
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = dict()

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_default.

        Arguments:

        """

        if arg in self.args_array:
            return True

        return False

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_m_and_r_options
        test_m_option_selected2
        test_m_option_selected
        test_r_option_selected
        test_no_options_selected

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argspar = ArgParser()

    def test_m_and_r_options(self):

        """Function:  test_m_and_r_options

        Description:  Test with -m and -r options selected.

        Arguments:

        """

        self.argspar.args_array = {"-m": "test_file", "-r": True}

        self.assertEqual(check_log.full_chk(self.argspar), True)

    @mock.patch("check_log.gen_libs.is_empty_file")
    def test_m_option_selected2(self, mock_file):

        """Function:  test_m_option_selected2

        Description:  Test -m option with non-empty file.

        Arguments:

        """

        self.argspar.args_array = {"-m": "test_file"}

        mock_file.return_value = False

        self.assertEqual(check_log.full_chk(self.argspar), False)

    @mock.patch("check_log.gen_libs.is_empty_file")
    def test_m_option_selected(self, mock_file):

        """Function:  test_m_option_selected

        Description:  Test -m option in args_array with empty file.

        Arguments:

        """

        self.argspar.args_array = {"-m": "test_file"}

        mock_file.return_value = True

        self.assertEqual(check_log.full_chk(self.argspar), True)

    def test_r_option_selected(self):

        """Function:  test_r_option_selected

        Description:  Test with -r option in args_array only.

        Arguments:

        """

        self.argspar.args_array = {"-r": True}

        self.assertEqual(check_log.full_chk(self.argspar), True)

    def test_no_options_selected(self):

        """Function:  test_no_options_selected

        Description:  Test with no arguments in args_array.

        Arguments:

        """

        self.assertEqual(check_log.full_chk(self.argspar), True)


if __name__ == "__main__":
    unittest.main()
