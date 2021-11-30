#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Integration testing of run_program in check_log.py.

    Usage:
        test/integration/check_log/run_program.py

    Arguments:

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

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_search_or
        test_search_and
        test_file_suppress
        test_stdin_marker_empty
        test_filter_data
        test_ignore_msg
        test_marker
        test_file_g_option_write
        test_file_g_option_append
        test_file_w_option_empty
        test_file_w_option
        test_file
        test_stdin_empty
        test_stdin_marker
        test_stdin
        test_clear_marker
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.line3 = "This is the third line"
        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")
        filename1 = "run_program_base_file.txt"
        filename2 = "run_program_base_file2.txt"
        filename3 = "run_program_base_file3.txt"
        filename4 = "run_program_base_file4.txt"
        filename5 = "run_program_base_file5.txt"
        logname1 = "run_program_file.txt"
        logname2 = "run_program_file2.txt"
        base_marker = "run_program_entry_file.txt"
        base_marker2 = "run_program_stdin_entry_file.txt"
        self.base_marker3 = "run_program_entry_file2.txt"
        marker_name = "run_program_marker.txt"
        self.test_out = os.path.join(self.test_path, "test_out.txt")
        self.ignore_msgs = os.path.join(self.test_path,
                                        "run_program_ignore_file.txt")
        self.filter_data = os.path.join(self.test_path,
                                        "run_program_filter_file.txt")
        self.file_marker = os.path.join(self.test_path, marker_name)
        self.file_marker2 = os.path.join(self.test_path, base_marker2)
        self.log_file1 = os.path.join(self.test_path, logname1)
        self.log_file2 = os.path.join(self.test_path, logname2)
        self.log_file3 = os.path.join(self.test_path, filename3)
        self.log_file4 = os.path.join(self.test_path, filename4)
        self.log_file5 = os.path.join(self.test_path, filename5)
        status, err_msg = gen_libs.cp_file(base_marker, self.test_path,
                                           self.test_path, marker_name)
        self.prt_format = "ERROR:  Test environment setup failed. Message: %s"
        self.pre_cond = "Pre-conditions not met."

        if not status:
            print(self.prt_format % (err_msg))
            self.skipTest(self.pre_cond)

        status, err_msg = gen_libs.cp_file(filename1, self.test_path,
                                           self.test_path, logname1)

        if not status:
            os.remove(self.file_marker)
            print(self.prt_format % (err_msg))
            self.skipTest(self.pre_cond)

        status, err_msg = gen_libs.cp_file(filename2, self.test_path,
                                           self.test_path, logname2)

        if not status:
            os.remove(self.file_marker)
            os.remove(self.log_file1)
            print(self.prt_format % (err_msg))
            self.skipTest(self.pre_cond)

        self.args_array = {"-f": [self.log_file1, self.log_file2], "-g": "w"}
        self.args_array2 = {"-f": [self.log_file1, self.log_file2],
                            "-S": ["third", "line"], "-k": "and",
                            "-o": self.test_out, "-g": "w"}
        self.args_array3 = {"-f": [self.log_file1, self.log_file2],
                            "-S": ["sixth", "new"], "-k": "or",
                            "-o": self.test_out, "-g": "w"}

    def test_search_or(self):

        """Function:  test_search_or

        Description:  Test with or search clause.

        Arguments:

        """

        with gen_libs.no_std_out():
            check_log.run_program(self.args_array3)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, "This is the sixth line")

        else:
            self.assertTrue(False)

    def test_search_and(self):

        """Function:  test_search_and

        Description:  Test with and search clause.

        Arguments:

        """

        with gen_libs.no_std_out():
            check_log.run_program(self.args_array2)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line3)

        else:
            self.assertTrue(False)

    def test_file_suppress(self):

        """Function:  test_file_suppress

        Description:  Test file logs with standard out suppression.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(check_log.run_program(self.args_array))

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_marker_empty(self, mock_atty):

        """Function:  test_stdin_marker_empty

        Description:  Test with standard in with an empty marker file.

        Arguments:

        """

        mock_atty.isatty.return_value = False
        args_array = {"-o": self.test_out, "-n": True, "-z": True,
                      "-m": os.path.join(self.test_path, self.base_marker3),
                      "-g": "w"}

        check_log.run_program(args_array)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read().rstrip()

            self.assertEqual(out_str, "Line one\nLine two")

        else:
            self.assertTrue(False)

    def test_filter_data(self):

        """Function:  test_filter_data

        Description:  Test filter data.

        Arguments:

        """

        self.args_array.update({"-F": self.filter_data, "-o": self.test_out})

        with gen_libs.no_std_out():
            check_log.run_program(self.args_array)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line3)

        else:
            self.assertTrue(False)

    def test_ignore_msg(self):

        """Function:  test_ignore_msg

        Description:  Test ignore messages.

        Arguments:

        """

        self.args_array.update({"-i": self.ignore_msgs, "-o": self.test_out})

        with gen_libs.no_std_out():
            check_log.run_program(self.args_array)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line3)

        else:
            self.assertTrue(False)

    def test_marker(self):

        """Function:  test_marker

        Description:  Test file log marker.

        Arguments:

        """

        self.args_array.update({"-z": True, "-m": self.file_marker})

        check_log.run_program(self.args_array)

        with open(self.file_marker) as f_hdlr:
            out_str = f_hdlr.readline().rstrip()

        self.assertEqual(out_str, "This is the seventh line")

    def test_file_g_option_write(self):

        """Function:  test_file_g_option_write

        Description:  Test file logs with -w option with write value.

        Arguments:

        """

        self.args_array.update({"-f": [self.log_file4], "-o": self.test_out,
                                "-z": True, "-g": "w"})
        check_log.run_program(self.args_array)
        self.args_array["-f"] = [self.log_file5]
        check_log.run_program(self.args_array)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(
                out_str, "Line 2\n")

        else:
            self.assertTrue(False)

    def test_file_g_option_append(self):

        """Function:  test_file_g_option_append

        Description:  Test file logs with -w option with append value.

        Arguments:

        """

        self.args_array.update({"-f": [self.log_file4], "-o": self.test_out,
                                "-z": True, "-g": "a"})
        check_log.run_program(self.args_array)
        self.args_array["-f"] = [self.log_file5]
        check_log.run_program(self.args_array)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(
                out_str, "Line 1\nLine 2\n")

        else:
            self.assertTrue(False)

    def test_file_w_option_empty(self):

        """Function:  test_file_w_option_empty

        Description:  Test file logs with -w option and no data.

        Arguments:

        """

        self.args_array.update({"-f": [self.log_file3], "-o": self.test_out,
                                "-z": True, "-w": True})
        check_log.run_program(self.args_array)

        self.assertFalse(os.path.isfile(self.test_out))

    def test_file_w_option(self):

        """Function:  test_file_w_option

        Description:  Test file logs with -w option.

        Arguments:

        """

        self.args_array.update({"-f": [self.log_file2], "-o": self.test_out,
                                "-z": True, "-w": True, "-g": "w"})
        check_log.run_program(self.args_array)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(
                out_str, "This is the sixth line\nThis is the seventh line\n")

        else:
            self.assertTrue(False)

    def test_file(self):

        """Function:  test_file

        Description:  Test file logs.

        Arguments:

        """

        self.args_array.update({"-f": [self.log_file2], "-o": self.test_out})

        with gen_libs.no_std_out():
            check_log.run_program(self.args_array)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(
                out_str, "This is the sixth line\nThis is the seventh line\n")

        else:
            self.assertTrue(False)

    @mock.patch("check_log.sys.stdin", io.StringIO(u""))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_empty(self, mock_atty):

        """Function:  test_stdin_empty

        Description:  Test with standard in no data.

        Arguments:

        """

        mock_atty.isatty.return_value = False

        self.assertFalse(check_log.run_program({}))

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_marker(self, mock_atty):

        """Function:  test_stdin_marker

        Description:  Test with standard in with marker file.

        Arguments:

        """

        mock_atty.isatty.return_value = False
        args_array = {"-o": self.test_out, "-m": self.file_marker2, "-n": True,
                      "-z": True, "-g": "w"}

        check_log.run_program(args_array)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read().rstrip()

            self.assertEqual(out_str, "Line two")

        else:
            self.assertTrue(False)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin(self, mock_atty):

        """Function:  test_stdin

        Description:  Test with standard in.

        Arguments:

        """

        mock_atty.isatty.return_value = False
        args_array = {"-o": self.test_out, "-z": True, "-g": "w"}

        check_log.run_program(args_array)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, "Line one\nLine two\n")

        else:
            self.assertTrue(False)

    def test_clear_marker(self):

        """Function:  test_clear_marker

        Description:  Test clearing the marker file.

        Arguments:

        """

        args_array = {"-c": True, "-m": self.file_marker}

        check_log.run_program(args_array)
        self.assertTrue(os.stat(self.file_marker).st_size == 0)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        os.remove(self.file_marker)
        os.remove(self.log_file1)
        os.remove(self.log_file2)

        if os.path.isfile(self.test_out):
            os.remove(self.test_out)


if __name__ == "__main__":
    unittest.main()
