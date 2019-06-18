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

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
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

        self.args_array = \
            {"-o": "test/unit/check_log/testfiles/log_2_output_file.out"}

        self.log_array = ["first line of log", "second line of log"]

    @mock.patch("check_log.gen_class.Mail")
    def test_t_z_options_set(self, mock_mail):

        """Function:  test_t_z_options_set

        Description:  Test with -t and -z options set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True

        self.args_array = {"-t": "Email Addresses", "-z": True}

        self.assertFalse(check_log.log_2_output(self.log_array,
                                                self.args_array))

    @mock.patch("check_log.gen_class.Mail")
    def test_t_s_options_set(self, mock_mail):

        """Function:  test_t_s_options_set

        Description:  Test with -t and -s options set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True

        self.args_array = {"-t": "Email Addresses", "-s": "Subject Line"}

        with gen_libs.no_std_out():
            self.assertFalse(check_log.log_2_output(self.log_array,
                                                    self.args_array))

    @mock.patch("check_log.gen_class.Mail")
    def test_t_o_options_set(self, mock_mail):

        """Function:  test_t_o_options_set

        Description:  Test with -t and -o options set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True

        self.args_array["-t"] = "Email Addresses"

        with gen_libs.no_std_out():
            check_log.log_2_output(self.log_array, self.args_array)

        if os.path.isfile(self.args_array["-o"]):
            status = True

        else:
            status = False

        self.assertTrue(status)

    @mock.patch("check_log.gen_class.Mail")
    def test_t_option_set(self, mock_mail):

        """Function:  test_t_option_set

        Description:  Test with -t option set.

        Arguments:

        """

        mock_mail.send_mail.return_value = True

        self.args_array = {"-t": "Email Addresses"}

        with gen_libs.no_std_out():
            self.assertFalse(check_log.log_2_output(self.log_array,
                                                    self.args_array))

    def test_z_option_set(self):

        """Function:  test_z_option_set

        Description:  Test with -z option set.

        Arguments:

        """

        self.args_array = {"-z": True}

        self.assertFalse(check_log.log_2_output(self.log_array,
                                                self.args_array))

    def test_write_to_log_empty_log(self):

        """Function:  test_write_to_log_empty_log

        Description:  Test writing data to log and empty log.

        Arguments:

        """

        check_log.log_2_output([], self.args_array)

        if os.path.isfile(self.args_array["-o"]) \
           and os.stat(self.args_array["-o"]).st_size == 0:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_write_to_log(self):

        """Function:  test_write_to_log

        Description:  Test writing data to log.

        Arguments:

        """

        with gen_libs.no_std_out():
            check_log.log_2_output(self.log_array, self.args_array)

        if os.path.isfile(self.args_array["-o"]):
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_o_option_empty_log(self):

        """Function:  test_o_option_empty_log

        Description:  Test with -o option and empty log.

        Arguments:

        """

        self.assertFalse(check_log.log_2_output([], {}))

    def test_o_option_not_set(self):

        """Function:  test_o_option_not_set

        Description:  Test with -o option not set.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(check_log.log_2_output(self.log_array, {}))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if "-o" in self.args_array and os.path.isfile(self.args_array["-o"]):
            os.remove(self.args_array["-o"])


if __name__ == "__main__":
    unittest.main()
