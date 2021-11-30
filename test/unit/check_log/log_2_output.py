#!/usr/bin/python
# Classification (U)

"""Program:  log_2_output.py

    Description:  Unit testing of log_2_output in check_log.py.

    Usage:
        test/unit/check_log/log_2_output.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
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
import lib.gen_class as gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_t_u_options_set
        test_g_option_write
        test_g_option_append
        test_w_option_data_log
        test_w_option_empty_log
        test_t_z_options_set
        test_t_s_options_set
        test_t_o_options_set
        test_t_option_set
        test_write_to_log_empty_log
        test_write_to_log
        test_o_option_empty_log
        test_o_option_not_set
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.line1 = "first line of log"
        self.line2 = "second line of log"
        self.outfile = "test/unit/check_log/testfiles/log_2_output_file.out"
        self.log = gen_class.LogFile()
        self.log.loglist = [self.line1, self.line2]
        self.args_array = {"-o": self.outfile, "-g": "w"}
        self.args_array2 = {"-o": self.outfile, "-z": True, "-w": True,
                            "-g": "w"}
        self.args_array3 = {"-o": self.outfile, "-z": True, "-g": "a"}
        self.args_array4 = {"-o": self.outfile, "-z": True, "-g": "w"}
        self.msg = "Email Addresses"

    @mock.patch("check_log.gen_class.Mail")
    def test_t_u_options_set(self, mock_mail):

        """Function:  test_t_u_options_set

        Description:  Test with -t and -u options set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True
        self.args_array = {"-t": self.msg, "-z": True, "-u": True}

        self.assertFalse(check_log.log_2_output(self.log, self.args_array))

    def test_g_option_write(self):

        """Function:  test_g_option_write

        Description:  Test with -g option with write value.

        Arguments:

        """

        self.log.loglist = [self.line1]
        check_log.log_2_output(self.log, self.args_array4)
        self.log.loglist = [self.line2]
        check_log.log_2_output(self.log, self.args_array4)

        if os.path.isfile(self.args_array4["-o"]):
            with open(self.args_array4["-o"]) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line2)

        else:
            self.assertTrue(False)

    def test_g_option_append(self):

        """Function:  test_g_option_append

        Description:  Test with -g option with append value.

        Arguments:

        """

        self.log.loglist = [self.line1]
        check_log.log_2_output(self.log, self.args_array3)
        self.log.loglist = [self.line2]
        check_log.log_2_output(self.log, self.args_array3)

        if os.path.isfile(self.args_array3["-o"]):
            with open(self.args_array3["-o"]) as f_hdlr:
                out_str = f_hdlr.read().rstrip()

            self.assertEqual(out_str,
                             "first line of log\nsecond line of log")

        else:
            self.assertTrue(False)

    def test_w_option_data_log(self):

        """Function:  test_w_option_data_log

        Description:  Test with -w option and data log.

        Arguments:

        """

        check_log.log_2_output(self.log, self.args_array2)
        self.assertTrue(os.path.isfile(self.args_array2["-o"]))

    def test_w_option_empty_log(self):

        """Function:  test_w_option_empty_log

        Description:  Test with -w option and empty log.

        Arguments:

        """

        self.log.loglist = []
        check_log.log_2_output(self.log, self.args_array2)
        self.assertFalse(os.path.isfile(self.args_array2["-o"]))

    @mock.patch("check_log.gen_class.Mail")
    def test_t_z_options_set(self, mock_mail):

        """Function:  test_t_z_options_set

        Description:  Test with -t and -z options set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True
        self.args_array = {"-t": self.msg, "-z": True}

        self.assertFalse(check_log.log_2_output(self.log, self.args_array))

    @mock.patch("check_log.gen_class.Mail")
    def test_t_s_options_set(self, mock_mail):

        """Function:  test_t_s_options_set

        Description:  Test with -t and -s options set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True
        self.args_array = {"-t": self.msg, "-s": "Subject Line"}

        with gen_libs.no_std_out():
            self.assertFalse(check_log.log_2_output(self.log, self.args_array))

    @mock.patch("check_log.gen_class.Mail")
    def test_t_o_options_set(self, mock_mail):

        """Function:  test_t_o_options_set

        Description:  Test with -t and -o options set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True
        self.args_array["-t"] = self.msg

        with gen_libs.no_std_out():
            check_log.log_2_output(self.log, self.args_array)

        self.assertTrue(os.path.isfile(self.args_array["-o"]))

    @mock.patch("check_log.gen_class.Mail")
    def test_t_option_set(self, mock_mail):

        """Function:  test_t_option_set

        Description:  Test with -t option set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True
        self.args_array = {"-t": self.msg}

        with gen_libs.no_std_out():
            self.assertFalse(check_log.log_2_output(self.log, self.args_array))

    def test_z_option_set(self):

        """Function:  test_z_option_set

        Description:  Test with -z option set.

        Arguments:

        """

        self.args_array = {"-z": True}

        self.assertFalse(check_log.log_2_output(self.log, self.args_array))

    def test_write_to_log_empty_log(self):

        """Function:  test_write_to_log_empty_log

        Description:  Test writing data to log and empty log.

        Arguments:

        """

        self.log.loglist = []
        check_log.log_2_output(self.log, self.args_array)

        self.assertTrue(os.path.isfile(self.args_array["-o"]) and
                        os.stat(self.args_array["-o"]).st_size == 0)

    def test_write_to_log(self):

        """Function:  test_write_to_log

        Description:  Test writing data to log.

        Arguments:

        """

        with gen_libs.no_std_out():
            check_log.log_2_output(self.log, self.args_array)

        self.assertTrue(os.path.isfile(self.args_array["-o"]))

    def test_o_option_empty_log(self):

        """Function:  test_o_option_empty_log

        Description:  Test with -o option and empty log.

        Arguments:

        """

        self.log.loglist = []
        self.assertFalse(check_log.log_2_output(self.log, {}))

    def test_o_option_not_set(self):

        """Function:  test_o_option_not_set

        Description:  Test with -o option not set.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(check_log.log_2_output(self.log, {}))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if "-o" in self.args_array and os.path.isfile(self.args_array["-o"]):
            os.remove(self.args_array["-o"])


if __name__ == "__main__":
    unittest.main()
