#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in check_log.py.

    Usage:
        test/unit/check_log/main.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_add_def
        arg_cond_req_or
        arg_default
        arg_exist
        arg_file_chk
        arg_valid_val
        get_val
        get_args

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()
        self.opt_val = None
        self.multi_val = None
        self.do_parse = None
        self.opt = None
        self.opt_def = None
        self.defaults = None
        self.opt_req = None
        self.opt_con_or = None
        self.file_chk = None
        self.file_crt = None
        self.opt_valid_val = None
        self.arg_cond_req_or2 = True
        self.arg_file_chk2 = True
        self.arg_valid_val2 = True
        self.arg = None

    def arg_add_def(self, defaults, opt_req):

        """Method:  arg_add_def

        Description:  Method stub holder for gen_class.ArgParser.arg_add_def.

        Arguments:

        """

        self.defaults = defaults
        self.opt_req = opt_req

    def arg_cond_req_or(self, opt_con_or):

        """Method:  arg_cond_req_or

        Description:  Method stub holder for
            gen_class.ArgParser.arg_cond_req_or.

        Arguments:

        """

        self.opt_con_or = opt_con_or

        return self.arg_cond_req_or2

    def arg_default(self, opt, opt_def):

        """Method:  arg_default

        Description:  Method stub holder for gen_class.ArgParser.arg_default.

        Arguments:

        """

        self.opt = opt
        self.opt_def = opt_def

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_default.

        Arguments:

        """

        if arg in self.args_array:
            return True

        return False

    def arg_file_chk(self, file_chk, file_crt):

        """Method:  arg_file_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_file_chk.

        Arguments:

        """

        self.file_chk = file_chk
        self.file_crt = file_crt

        return self.arg_file_chk2

    def arg_valid_val(self, opt_valid_val):

        """Method:  arg_valid_val

        Description:  Method stub holder for gen_class.ArgParser.arg_valid_val.

        Arguments:

        """

        self.opt_valid_val = opt_valid_val

        return self.arg_valid_val2

    def get_val(self, skey, def_val):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def get_args(self):

        """Method:  get_args

        Description:  Method stub holder for gen_class.ArgParser.get_args.

        Arguments:

        """

        return self.args_array


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            (input) cmdline
            (input) flavor

        """

        self.cmdline = cmdline
        self.flavor = flavor


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_arg_exist3
        test_arg_exist2
        test_arg_exist
        test_search_logic_present
        test_search_logic_miss
        test_programlock_true
        test_programlock_id
        test_programlock_fail
        test_valid_val_true
        test_valid_val_false
        test_file_chk_true
        test_file_chk_false
        test_cond_req_or_true
        test_cond_req_or_false
        test_help_false
        test_help_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argspar = ArgParser()
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_arg_exist3(self, mock_arg, mock_help):

        """Function:  test_arg_exist3

        Description:  Test with no args -S or -k present.

        Arguments:

        """

        mock_arg.return_value = self.argspar
        mock_help.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_arg_exist2(self, mock_arg, mock_help):

        """Function:  test_arg_exist2

        Description:  Test with args -S only present.

        Arguments:

        """

        self.argspar.args_array["-S"] = ["a"]

        mock_arg.return_value = self.argspar
        mock_help.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_arg_exist(self, mock_arg, mock_help):

        """Function:  test_arg_exist

        Description:  Test with args -S and -k present.

        Arguments:

        """

        self.argspar.args_array["-S"] = ["a"]
        self.argspar.args_array["-k"] = "and"

        mock_arg.return_value = self.argspar
        mock_help.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_search_logic_present(self, mock_arg, mock_help):

        """Function:  test_search_logic_present

        Description:  Test with -k option present.

        Arguments:

        """

        self.argspar.args_array["-S"] = ["a"]
        self.argspar.args_array["-k"] = "and"

        mock_arg.return_value = self.argspar
        mock_help.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_search_logic_miss(self, mock_arg, mock_help):

        """Function:  test_search_logic_miss

        Description:  Test with missing -k option.

        Arguments:

        """

        self.argspar.args_array["-S"] = ["a"]

        mock_arg.return_value = self.argspar
        mock_help.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_class.ProgramLock")
    @mock.patch("check_log.run_program")
    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_programlock_true(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_arg.return_value = self.argspar
        mock_help.return_value = False
        mock_lock.return_value = self.proglock
        mock_run.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_class.ProgramLock")
    @mock.patch("check_log.run_program")
    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_programlock_id(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_programlock_id

        Description:  Test ProgramLock fails with flavor id.

        Arguments:

        """

        self.argspar.args_array["-y"] = "FlavorID"

        mock_arg.return_value = self.argspar
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_class.ProgramLock")
    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_programlock_fail(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_fail

        Description:  Test ProgramLock fails to lock.

        Arguments:

        """

        mock_arg.return_value = self.argspar
        mock_help.return_value = False
        mock_lock.side_effect = check_log.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_class.ProgramLock")
    @mock.patch("check_log.run_program")
    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_valid_val_true(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_valid_val_true

        Description:  Test with arg_valid_val returns True.

        Arguments:

        """

        mock_arg.return_value = self.argspar
        mock_help.return_value = False
        mock_lock.return_value = self.proglock
        mock_run.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_valid_val_false(self, mock_arg, mock_help):

        """Function:  test_valid_val_false

        Description:  Test with arg_valid_val returns False.

        Arguments:

        """

        self.argspar.arg_valid_val2 = False

        mock_arg.return_value = self.argspar
        mock_help.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_file_chk_true(self, mock_arg, mock_help):

        """Function:  test_file_chk_true

        Description:  Test with arg_file_chk returns True.

        Arguments:

        """

        self.argspar.arg_valid_val2 = False

        mock_arg.return_value = self.argspar
        mock_help.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_file_chk_false(self, mock_arg, mock_help):

        """Function:  test_file_chk_false

        Description:  Test with arg_file_chk returns False.

        Arguments:

        """

        self.argspar.arg_file_chk2 = False

        mock_arg.return_value = self.argspar
        mock_help.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_cond_req_or_true(self, mock_arg, mock_help):

        """Function:  test_cond_req_or_true

        Description:  Test with arg_cond_req_or returns True.

        Arguments:

        """

        self.argspar.arg_file_chk2 = False

        mock_arg.return_value = self.argspar
        mock_help.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_cond_req_or_false(self, mock_arg, mock_help):

        """Function:  test_cond_req_or_false

        Description:  Test with arg_cond_req_or returns False.

        Arguments:

        """

        self.argspar.arg_cond_req_or2 = False

        mock_arg.return_value = self.argspar
        mock_help.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:

        """

        self.argspar.arg_cond_req_or2 = False

        mock_arg.return_value = self.argspar
        mock_help.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:

        """

        mock_arg.return_value = self.argspar
        mock_help.return_value = True

        self.assertFalse(check_log.main())


if __name__ == "__main__":
    unittest.main()
