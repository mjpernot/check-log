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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_search_logic_present -> Test with -k option present.
        test_search_logic_miss -> Test with missing -k option.
        test_valid_val_true -> Test with arg_valid_val returns True.
        test_valid_val_false -> Test with arg_valid_val returns False.
        test_programlock_id -> Test ProgramLock fails with flavor id.
        test_programlock_fail -> Test ProgramLock fails to lock.
        test_cond_req_or_true -> Test with arg_cond_req_or returns True.
        test_cond_req_or_false -> Test with arg_cond_req_or returns False.
        test_file_chk_false -> Test with arg_file_chk returns False.
        test_file_chk_true -> Test with arg_file_chk returns True.
        test_help_false ->  Test with help_func returns False.
        test_help_true -> Test with help_func returns True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.key_msg = "File Place Holder"
        self.args = {"-f": self.key_msg, "-c": True}
        self.args2 = {"-f": self.key_msg, "-c": True, "-S": ["a"]}
        self.args3 = {"-f": self.key_msg, "-c": True, "-S": ["a"], "-k": "and"}

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser.arg_parse2")
    def test_search_logic_present(self, mock_arg, mock_help):

        """Function:  test_search_logic_present

        Description:  Test with -k option present.

        Arguments:

        """

        mock_arg.return_value = self.args3
        mock_help.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser.arg_parse2")
    def test_search_logic_miss(self, mock_arg, mock_help):

        """Function:  test_search_logic_miss

        Description:  Test with missing -k option.

        Arguments:

        """

        mock_arg.return_value = self.args2
        mock_help.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_class.ProgramLock")
    @mock.patch("check_log.run_program")
    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser")
    def test_valid_val_true(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_valid_val_true

        Description:  Test with arg_valid_val returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_cond_req_or.return_value = True
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_valid_val.return_value = True
        mock_run.return_value = True
        mock_lock.side_effect = None

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser")
    def test_valid_val_false(self, mock_arg, mock_help):

        """Function:  test_valid_val_false

        Description:  Test with arg_valid_val returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_cond_req_or.return_value = True
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_valid_val.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_class.ProgramLock")
    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser")
    def test_programlock_id(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_id

        Description:  Test ProgramLock fails with flavor id.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_cond_req_or.return_value = True
        mock_arg.arg_file_chk.return_value = False
        mock_lock.side_effect = check_log.gen_class.SingleInstanceException

        self.args["-y"] = "FlavorID"

        with gen_libs.no_std_out():
            self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_class.ProgramLock")
    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser")
    def test_programlock_fail(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_fail

        Description:  Test ProgramLock fails to lock.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_cond_req_or.return_value = True
        mock_arg.arg_file_chk.return_value = False
        mock_lock.side_effect = check_log.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser")
    def test_cond_req_or_true(self, mock_arg, mock_help):

        """Function:  test_cond_req_or_true

        Description:  Test with arg_cond_req_or returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_cond_req_or.return_value = True
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser")
    def test_cond_req_or_false(self, mock_arg, mock_help):

        """Function:  test_cond_req_or_false

        Description:  Test with arg_cond_req_or returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_cond_req_or.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser")
    def test_file_chk_false(self, mock_arg, mock_help):

        """Function:  test_file_chk_false

        Description:  Test with arg_file_chk returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_cond_req_or.return_value = True
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_valid_val.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser")
    def test_file_chk_true(self, mock_arg, mock_help):

        """Function:  test_file_chk_true

        Description:  Test with arg_file_chk returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_cond_req_or.return_value = True
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_cond_req_or.return_value = False

        self.assertFalse(check_log.main())

    @mock.patch("check_log.gen_libs.help_func")
    @mock.patch("check_log.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(check_log.main())


if __name__ == "__main__":
    unittest.main()
