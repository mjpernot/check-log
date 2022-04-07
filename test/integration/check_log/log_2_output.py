#!/usr/bin/python
# Classification (U)

"""Program:  log_2_output.py

    Description:  Integration testing of log_2_output in check_log.py.

    Usage:
        test/integration/check_log/log_2_output.py

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
import lib.gen_class as gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mail
        test_write_to_log
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "check_log.py"

        self.log = gen_class.LogFile()
        self.log.loglist = ["first line of log", "second line of log"]
        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")
        self.file_name = os.path.join(self.test_path, "log_2_output_file.out")
        self.args_array = {}

        if os.access(self.file_name, os.W_OK):
            os.remove(self.file_name)

        elif os.path.isfile(self.file_name):
            print("ERROR:  Test environment not clean - file: %s exists"
                  % (self.file_name))
            self.skipTest("Pre-conditions not met.")

        self.opt_val = [
            "-i", "-m", "-o", "-s", "-t", "-y", "-F", "-S", "-k", "-g"]
        self.argv = [p_name, "-t", "user@domain.name", "-z", "-u"]
        self.argv2 = [p_name, "-t", "user@domain.name", "-z"]
        self.argv3 = [p_name, "-o", self.file_name, "-g", "w"]

    @mock.patch("check_log.gen_class.Mail.send_mail")
    def test_mail2(self, mock_mail):

        """Function:  test_mail2

        Description:  Test sending via mail with -u option.

        Arguments:

        """

        mock_mail.return_value = True

        args = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertFalse(check_log.log_2_output(self.log, args))

    @mock.patch("check_log.gen_class.Mail.send_mail")
    def test_mail(self, mock_mail):

        """Function:  test_mail

        Description:  Test sending via mail.

        Arguments:

        """

        mock_mail.return_value = True

        args = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertFalse(check_log.log_2_output(self.log, args))

    def test_write_to_log(self):

        """Function:  test_write_to_log

        Description:  Test writing data to log.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, do_parse=True)

        with gen_libs.no_std_out():
            check_log.log_2_output(self.log, args)

        self.assertTrue(os.path.isfile(args.args_array["-o"]))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isfile(self.file_name):
            os.remove(self.file_name)


if __name__ == "__main__":
    unittest.main()
