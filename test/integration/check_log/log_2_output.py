#!/usr/bin/python
# Classification (U)

"""Program:  log_2_output.py

    Description:  Integration testing of log_2_output in check_log.py.

    Usage:
        test/integration/check_log/log_2_output.py

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
import mock

# Local
sys.path.append(os.getcwd())
import check_log
import lib.gen_libs as gen_libs
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
        test_mail -> Test sending via mail.
        test_write_to_log -> Test writing data to log.
        tearDown -> Clean up of integration testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        self.file_name = os.path.join(self.test_path, "log_2_output_file.out")
        self.args_array = {}

        self.log_array = ["first line of log", "second line of log"]

        if os.access(self.file_name, os.W_OK):
            os.remove(self.file_name)

        elif os.path.isfile(self.file_name):
            print("ERROR:  Test environment not clean - file: %s exists"
                  % (self.file_name))
            self.skipTest("Pre-conditions not met.")

    @mock.patch("check_log.gen_class.Mail.send_mail")
    def test_mail(self, mock_mail):

        """Function:  test_mail

        Description:  Test sending via mail.

        Arguments:
            mock_mail -> Mock Ref:  check_log.gen_class.Mail.send_mail

        """

        mock_mail.return_value = True

        self.args_array = {"-t": "user@domain.name", "-z": True}

        self.assertFalse(check_log.log_2_output(self.log_array,
                                                self.args_array))

    def test_write_to_log(self):

        """Function:  test_write_to_log

        Description:  Test writing data to log.

        Arguments:
            None

        """

        self.args_array["-o"] = self.file_name

        with gen_libs.no_std_out():
            check_log.log_2_output(self.log_array, self.args_array)

        if os.path.isfile(self.args_array["-o"]):
            status = True

        else:
            status = False

        self.assertTrue(status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:
            None

        """

        if "-o" in self.args_array and os.path.isfile(self.args_array["-o"]):
            os.remove(self.args_array["-o"])


if __name__ == "__main__":
    unittest.main()
