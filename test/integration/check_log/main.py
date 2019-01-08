#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Integration testing of main in check_log.py.

    Usage:
        test/integration/check_log/main.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os
import io

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
        test_stdin_marker -> Test with standard in with marker file.
        test_stdin_marker_empty -> Test standard in with an empty marker file.
        test_stdin -> Test with standard in.
        test_marker -> Test file log with marker.
        test_file -> Test file log.
        test_arg_file_chk -> Test arg_file_chk function.
        test_arg_cond_req_or -> Test arg_cond_req_or function.
        test_help -> Test help_func function.
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

        filename1 = "main_base_file.txt"
        filename2 = "main_base_file2.txt"
        logname1 = "main_file.txt"
        logname2 = "main_file2.txt"
        marker_name = "main_marker.txt"
        base_marker = "main_entry_file.txt"
        base_marker2 = "main_stdin_entry_file.txt"

        self.test_out = os.path.join(self.test_path, "test_out.txt")
        self.file_marker = os.path.join(self.test_path, marker_name)
        self.file_marker2 = os.path.join(self.test_path, base_marker2)
        self.log_file1 = os.path.join(self.test_path, logname1)
        self.log_file2 = os.path.join(self.test_path, logname2)
        self.marker = os.path.join(self.test_path, base_marker)
        self.base_marker3 = "main_entry_file2.txt"

        status, err_msg = gen_libs.cp_file(base_marker, self.test_path,
                                           self.test_path, marker_name)

        if not status:
            print("ERROR:  Test environment setup failed. Message: %s"
                  % (self.err_msg))
            self.skipTest("Pre-conditions not met.")

        status, err_msg = gen_libs.cp_file(filename1, self.test_path,
                                           self.test_path, logname1)

        if not status:
            os.remove(self.file_marker)
            print("ERROR:  Test environment setup failed. Message: %s"
                  % (self.err_msg))
            self.skipTest("Pre-conditions not met.")

        status, err_msg = gen_libs.cp_file(filename2, self.test_path,
                                           self.test_path, logname2)

        if not status:
            os.remove(self.file_marker)
            os.remove(self.log_file1)
            print("ERROR:  Test environment setup failed. Message: %s"
                  % (self.err_msg))
            self.skipTest("Pre-conditions not met.")

        self.argv_list = [os.path.join(self.base_dir, "main.py")]

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_marker(self, mock_atty):

        """Function:  test_stdin_marker

        Description:  Test with standard in with marker file.

        Arguments:
            mock_atty -> Mock Ref:  check_log.sys.stdin

        """

        mock_atty.isatty.return_value = False

        self.argv_list.extend(["-o", self.test_out, "-n", "-z",
                               "-m", self.file_marker2])
        sys.argv = self.argv_list

        check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read().rstrip()

            self.assertEqual(out_str, "Line two")

        else:
            self.assertTrue(False)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_marker_empty(self, mock_atty):

        """Function:  test_stdin_marker_empty

        Description:  Test with standard in with an empty marker file.

        Arguments:
            mock_atty -> Mock Ref:  check_log.sys.stdin

        """

        mock_atty.isatty.return_value = False

        self.argv_list.extend(["-o", self.test_out, "-n", "-z",
                               "-m", os.path.join(self.test_path,
                                                  self.base_marker3)])
        sys.argv = self.argv_list

        check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read().rstrip()

            self.assertEqual(out_str, "Line one\nLine two")

        else:
            self.assertTrue(False)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin(self, mock_atty):

        """Function:  test_stdin

        Description:  Test with standard in.

        Arguments:
            mock_atty -> Mock Ref:  check_log.sys.stdin

        """

        mock_atty.isatty.return_value = False

        self.argv_list.extend(["-o", self.test_out, "-z"])
        sys.argv = self.argv_list

        check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, "Line one\nLine two\n")

        else:
            self.assertTrue(False)

    def test_clear_marker(self):

        """Function:  test_clear_marker

        Description:  Test clear marker file.

        Arguments:
            None

        """

        self.argv_list.extend(["-c", "-m", self.file_marker])
        sys.argv = self.argv_list

        check_log.main()

        if os.stat(self.file_marker).st_size == 0:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_marker(self):

        """Function:  test_marker

        Description:  Test file log with marker.

        Arguments:
            None

        """

        self.argv_list.extend(["-f", self.log_file1, self.log_file2, "-o",
                               self.test_out, "-m", self.file_marker])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, "This is the seventh line\n")

        else:
            self.assertTrue(False)

    def test_file(self):

        """Function:  test_file

        Description:  Test file log.

        Arguments:
            None

        """

        self.argv_list.extend(["-f", self.log_file2, "-o", self.test_out])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(
                out_str, "This is the sixth line\nThis is the seventh line\n")

        else:
            self.assertTrue(False)

    def test_arg_file_chk(self):

        """Function:  test_arg_file_chk

        Description:  Test arg_file_chk function.

        Arguments:
            None

        """

        self.argv_list.extend(["-f",
                              os.path.join(self.test_path, "main_dummy.txt")])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(check_log.main())

    def test_arg_cond_req_or(self):

        """Function:  test_arg_cond_req_or

        Description:  Test arg_cond_req_or function.

        Arguments:
            None

        """

        self.argv_list.append("-c")
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(check_log.main())

    def test_help(self):

        """Function:  test_help

        Description:  Test help_func function.

        Arguments:
            None

        """

        self.argv_list.append("-h")
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(check_log.main())

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:
            None

        """

        os.remove(self.file_marker)
        os.remove(self.log_file1)
        os.remove(self.log_file2)

        if os.path.isfile(self.test_out):
            os.remove(self.test_out)


if __name__ == "__main__":
    unittest.main()
