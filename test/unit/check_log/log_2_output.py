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
        setUp -> Unit testing initilization.
        test_g_option_append -> Test with -g option with append value.
        test_w_option_data_log -> Test with -w option and data log.
        test_w_option_empty_log -> Test with -w option and empty log.
        test_t_z_options_set -> Test with -t and -z options set.
        test_t_s_options_set -> Test with -t and -s options set.
        test_t_o_options_set -> Test with -t and -o options set.
        test_t_option_set -> Test with -t option set.
        test_write_to_log_empty_log -> Test writing data to log and empty log.
        test_write_to_log -> Test writing data to log.
        test_o_option_empty_log -> Test with -o option and empty log.
        test_o_option_not_set -> Test with -o option not set.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.log = gen_class.LogFile()
        self.log.loglist = ["first line of log", "second line of log"]
        self.args_array = \
            {"-o": "test/unit/check_log/testfiles/log_2_output_file.out",
             "-g": "w"}
        self.args_array2 = \
            {"-o": "test/unit/check_log/testfiles/log_2_output_file.out",
            "-z": True, "-w": True, "-g": "w"}
        self.args_array3 = \
            {"-o": "test/unit/check_log/testfiles/log_2_output_file.out",
            "-z": True, "-g": "a"}
        self.args_array4 = \
            {"-o": "test/unit/check_log/testfiles/log_2_output_file.out",
            "-z": True, "-g": "w"}

    def test_g_option_write(self):

        """Function:  test_g_option_write

        Description:  Test with -g option with write value.

        Arguments:

        """

        self.log.loglist = ["first line of log"]
        check_log.log_2_output(self.log, self.args_array4)
        self.log.loglist = ["second line of log"]
        check_log.log_2_output(self.log, self.args_array4)

        if os.path.isfile(self.args_array4["-o"]):
            with open(self.args_array4["-o"]) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, "second line of log")

        else:
            self.assertTrue(False)

    def test_g_option_append(self):

        """Function:  test_g_option_append

        Description:  Test with -g option with append value.

        Arguments:

        """

        self.log.loglist = ["first line of log"]
        #check_log.log_2_output(self.log, self.args_array3)
        with open(self.args_array3["-o"], self.args_array3["-g"]) as f_hdlr:
            for x in self.log.loglist:
                print(x, file=f_hdlr)
        self.log.loglist = ["second line of log"]
        check_log.log_2_output(self.log, self.args_array3)

        if os.path.isfile(self.args_array3["-o"]):
            with open(self.args_array3["-o"]) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str,
                "first line of log\nsecond line of log\n")

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
        self.args_array = {"-t": "Email Addresses", "-z": True}

        self.assertFalse(check_log.log_2_output(self.log, self.args_array))

    @mock.patch("check_log.gen_class.Mail")
    def test_t_s_options_set(self, mock_mail):

        """Function:  test_t_s_options_set

        Description:  Test with -t and -s options set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True
        self.args_array = {"-t": "Email Addresses", "-s": "Subject Line"}

        with gen_libs.no_std_out():
            self.assertFalse(check_log.log_2_output(self.log, self.args_array))

    @mock.patch("check_log.gen_class.Mail")
    def test_t_o_options_set(self, mock_mail):

        """Function:  test_t_o_options_set

        Description:  Test with -t and -o options set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True
        self.args_array["-t"] = "Email Addresses"

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
        self.args_array = {"-t": "Email Addresses"}

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
