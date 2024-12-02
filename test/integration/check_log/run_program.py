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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import check_log
import lib.gen_class as gen_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_search_or_offset
        test_search_or
        test_search_and_offset
        test_search_and
        test_file_suppress_offset
        test_file_suppress
        test_stdin_marker_empty
        test_filter_data_offset
        test_filter_data
        test_ignore_msg_offset
        test_ignore_msg
        test_marker_offset
        test_marker
        test_file_g_option_write_offset
        test_file_g_option_write
        test_file_g_option_append_offset
        test_file_g_option_append
        test_file_w_option_empty_offset
        test_file_w_option_empty
        test_file_w_option_offset
        test_file_w_option
        test_file_offset
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

        p_name = "check_log.py"

        self.line3 = "This is the third line"
        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")
        filename1 = "run_program_base_file.txt"
        filename1a = "run_program_base_file1a.txt"
        filename2 = "run_program_base_file2.txt"
        filename3 = "run_program_base_file3.txt"
        filename4 = "run_program_base_file4.txt"
        filename5 = "run_program_base_file5.txt"
        logname1 = "run_program_file.txt"
        logname1a = "run_program_file1a.txt"
        logname2 = "run_program_file2.txt"
        base_marker = "run_program_entry_file.txt"
        base_marker2 = "run_program_stdin_entry_file.txt"
        self.base_marker3 = "run_program_entry_file2.txt"
        marker_name = "run_program_marker.txt"
        self.test_out = os.path.join(self.test_path, "test_out.txt")
        self.ignore_msgs = os.path.join(
            self.test_path, "run_program_ignore_file.txt")
        self.filter_data = os.path.join(
            self.test_path, "run_program_filter_file.txt")
        self.file_marker = os.path.join(self.test_path, marker_name)
        self.file_marker2 = os.path.join(self.test_path, base_marker2)
        self.log_file1 = os.path.join(self.test_path, logname1)
        self.log_file1a = os.path.join(self.test_path, logname1a)
        self.log_file2 = os.path.join(self.test_path, logname2)
        self.log_file3 = os.path.join(self.test_path, filename3)
        self.log_file4 = os.path.join(self.test_path, filename4)
        self.log_file5 = os.path.join(self.test_path, filename5)
        status, err_msg = gen_libs.cp_file(
            base_marker, self.test_path, self.test_path, marker_name)
        self.prt_format = "ERROR:  Test environment setup failed. Message: %s"
        self.pre_cond = "Pre-conditions not met."

        if not status:
            print(self.prt_format % (err_msg))
            self.skipTest(self.pre_cond)

        status, err_msg = gen_libs.cp_file(
            filename1, self.test_path, self.test_path, logname1)

        if not status:
            print(self.prt_format % (err_msg))
            self.skipTest(self.pre_cond)

        status, err_msg = gen_libs.cp_file(
            filename1a, self.test_path, self.test_path, logname1a)

        if not status:
            os.remove(self.file_marker)
            print(self.prt_format % (err_msg))
            self.skipTest(self.pre_cond)

        status, err_msg = gen_libs.cp_file(
            filename2, self.test_path, self.test_path, logname2)

        if not status:
            os.remove(self.file_marker)
            os.remove(self.log_file1)
            print(self.prt_format % (err_msg))
            self.skipTest(self.pre_cond)

        # Lastline option
        self.argv = [p_name, "-f", self.log_file1, self.log_file2, "-g", "w"]
        self.argv2 = [
            p_name, "-f", self.log_file1, self.log_file2, "-S", "third",
            "line", "-k", "and", "-o", self.test_out, "-g", "w"]
        self.argv3 = [
            p_name, "-f", self.log_file1, self.log_file2, "-S", "sixth", "new",
            "-k", "or", "-o", self.test_out, "-g", "w"]
        self.argv4 = [
            p_name, "-o", self.test_out, "-n", "-z", "-m",
            os.path.join(self.test_path, self.base_marker3), "-g", "w"]
        self.argv5 = [
            p_name, "-f", self.log_file1, self.log_file2, "-g", "w", "-F",
            self.filter_data, "-o", self.test_out]
        self.argv6 = [
            p_name, "-f", self.log_file1, self.log_file2, "-g", "w", "-i",
            self.ignore_msgs, "-o", self.test_out]
        self.argv7 = [
            p_name, "-f", self.log_file1, self.log_file2, "-g", "w", "-z",
            "-m", self.file_marker]
        self.argv8 = [
            p_name, "-f", self.log_file4, "-o", self.test_out, "-z", "-g", "w"]
        self.argv9 = [
            p_name, "-f", self.log_file5, "-o", self.test_out, "-z", "-g", "w"]
        self.argv10 = [
            p_name, "-f", self.log_file4, "-g", "a", "-o", self.test_out, "-z"]
        self.argv11 = [
            p_name, "-f", self.log_file5, "-g", "a", "-o", self.test_out, "-z"]
        self.argv12 = [
            p_name, "-f", self.log_file3, "-g", "w", "-o", self.test_out, "-z",
            "-w"]
        self.argv13 = [
            p_name, "-f", self.log_file2, "-g", "w", "-o", self.test_out, "-z",
            "-w", "-g", "w"]
        self.argv14 = [
            p_name, "-f", self.log_file2, "-g", "w", "-o", self.test_out]
        self.argv15 = [p_name]
        self.argv16 = [
            p_name, "-o", self.test_out, "-m", self.file_marker2, "-n", "-z",
            "-g", "w"]
        self.argv17 = [p_name, "-o", self.test_out, "-z", "-g", "w"]
        self.argv18 = [p_name, "-c", "-m", self.file_marker]

        # Offset option
        self.argva = [
            p_name, "-f", self.log_file1, self.log_file2, "-g", "w", "-R",
            "offset"]
        self.argv2a = [
            p_name, "-f", self.log_file1a, "-S", "third",
            "line", "-k", "and", "-o", self.test_out, "-g", "w", "-R",
            "offset"]
        self.argv3a = [
            p_name, "-f", self.log_file1a, "-S", "sixth", "new",
            "-k", "or", "-o", self.test_out, "-g", "w", "-R", "offset"]
        self.argv5a = [
            p_name, "-f", self.log_file1, self.log_file2, "-g", "w", "-F",
            self.filter_data, "-o", self.test_out, "-R", "offset"]
        self.argv6a = [
            p_name, "-f", self.log_file1, self.log_file2, "-g", "w", "-i",
            self.ignore_msgs, "-o", self.test_out, "-R", "offset"]
        self.argv7a = [
            p_name, "-f", self.log_file1, self.log_file2, "-g", "w", "-z",
            "-m", self.file_marker, "-R", "offset"]
        self.argv8a = [
            p_name, "-f", self.log_file4, "-o", self.test_out, "-z", "-g", "w",
            "-R", "offset"]
        self.argv9a = [
            p_name, "-f", self.log_file5, "-o", self.test_out, "-z", "-g", "w",
            "-R", "offset"]
        self.argv10a = [
            p_name, "-f", self.log_file4, "-g", "a", "-o", self.test_out, "-z",
            "-R", "offset"]
        self.argv11a = [
            p_name, "-f", self.log_file5, "-g", "a", "-o", self.test_out, "-z",
            "-R", "offset"]
        self.argv12a = [
            p_name, "-f", self.log_file3, "-g", "w", "-o", self.test_out, "-z",
            "-w", "-R", "offset"]
        self.argv13a = [
            p_name, "-f", self.log_file2, "-g", "w", "-o", self.test_out, "-z",
            "-w", "-g", "w", "-R", "offset"]
        self.argv14a = [
            p_name, "-f", self.log_file2, "-g", "w", "-o", self.test_out,
            "-R", "offset"]

        self.opt_val = [
            "-i", "-m", "-o", "-s", "-t", "-y", "-F", "-S", "-k", "-g"]
        self.multi_val = ["-f", "-s", "-t", "-S"]

        self.results = "This is the sixth line"
        self.results2 = "Line one\nLine two"
        self.results3 = "This is the seventh line"
        self.results4 = "Line 2\n"
        self.results5 = "Line 1\nLine 2\n"
        self.results6 = "This is the sixth line\nThis is the seventh line\n"
        self.results7 = "This is the sixth line\nThis is the seventh line\n"
        self.results8 = "Line two"
        self.results9 = "Line one\nLine two\n"

    def test_search_or_offset(self):

        """Function:  test_search_or_offset

        Description:  Test with or search clause with offset option.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv3a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.results)

        else:
            self.assertEqual("", self.results)

    def test_search_or(self):

        """Function:  test_search_or

        Description:  Test with or search clause.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.results)

        else:
            self.assertEqual("", self.results)

    def test_search_and_offset(self):

        """Function:  test_search_and_offset

        Description:  Test with and search clause with offset option.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv2a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line3)

        else:
            self.assertEqual("", self.line3)

    def test_search_and(self):

        """Function:  test_search_and

        Description:  Test with and search clause.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line3)

        else:
            self.assertEqual("", self.line3)

    def test_file_suppress_offset(self):

        """Function:  test_file_suppress_offset

        Description:  Test file logs with standard out suppression with offset
            option.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argva, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(check_log.run_program(args))

    def test_file_suppress(self):

        """Function:  test_file_suppress

        Description:  Test file logs with standard out suppression.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(check_log.run_program(args))

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_marker_empty(self, mock_atty):

        """Function:  test_stdin_marker_empty

        Description:  Test with standard in with an empty marker file.

        Arguments:

        """

        mock_atty.isatty.return_value = False

        args = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read().rstrip()

            self.assertEqual(out_str, self.results2)

        else:
            self.assertEqual("", self.results2)

    def test_filter_data_offset(self):

        """Function:  test_filter_data_offset

        Description:  Test filter data with offset option.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv5a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line3)

        else:
            self.assertEqual("", self.line3)

    def test_filter_data(self):

        """Function:  test_filter_data

        Description:  Test filter data.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv5, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line3)

        else:
            self.assertEqual("", self.line3)

    def test_ignore_msg_offset(self):

        """Function:  test_ignore_msg_offset

        Description:  Test ignore messages with offset option.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv6a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line3)

        else:
            self.assertEqual("", self.line3)

    def test_ignore_msg(self):

        """Function:  test_ignore_msg

        Description:  Test ignore messages.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.readline().rstrip()

            self.assertEqual(out_str, self.line3)

        else:
            self.assertEqual("", self.line3)

    def test_marker_offset(self):

        """Function:  test_marker_offset

        Description:  Test file log marker with offset option.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv7a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        check_log.run_program(args)

        with open(self.file_marker) as f_hdlr:
            out_str = f_hdlr.readline().rstrip()

        self.assertEqual(out_str, self.results3)

    def test_marker(self):

        """Function:  test_marker

        Description:  Test file log marker.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv7, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        check_log.run_program(args)

        with open(self.file_marker) as f_hdlr:
            out_str = f_hdlr.readline().rstrip()

        self.assertEqual(out_str, self.results3)

    def test_file_g_option_write_offset(self):

        """Function:  test_file_g_option_write_offset

        Description:  Test file logs with -w and offset options with write
            value.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv8a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        args2 = gen_class.ArgParser(
            self.argv9a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args2)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results4)

        else:
            self.assertEqual("", self.results4)

    def test_file_g_option_write(self):

        """Function:  test_file_g_option_write

        Description:  Test file logs with -w option with write value.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv8, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        args2 = gen_class.ArgParser(
            self.argv9, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args2)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results4)

        else:
            self.assertEqual("", self.results4)

    def test_file_g_option_append_offset(self):

        """Function:  test_file_g_option_append_offset

        Description:  Test file logs with -w and offset options with append
            value.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv10a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        args2 = gen_class.ArgParser(
            self.argv11a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args2)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results5)

        else:
            self.assertEqual("", self.results5)

    def test_file_g_option_append(self):

        """Function:  test_file_g_option_append

        Description:  Test file logs with -w option with append value.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv10, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        args2 = gen_class.ArgParser(
            self.argv11, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args2)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results5)

        else:
            self.assertEqual("", self.results5)

    def test_file_w_option_empty_offset(self):

        """Function:  test_file_w_option_empty_offset

        Description:  Test file logs with -w and offset options and no data.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv12a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        self.assertFalse(os.path.isfile(self.test_out))

    def test_file_w_option_empty(self):

        """Function:  test_file_w_option_empty

        Description:  Test file logs with -w option and no data.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv12, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        self.assertFalse(os.path.isfile(self.test_out))

    def test_file_w_option_offset(self):

        """Function:  test_file_w_option_offset

        Description:  Test file logs with -w and offset options.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv13a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results6)

        else:
            self.assertEqual("", self.results6)

    def test_file_w_option(self):

        """Function:  test_file_w_option

        Description:  Test file logs with -w option.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv13, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results6)

        else:
            self.assertEqual("", self.results6)

    def test_file_offset(self):

        """Function:  test_file_offset

        Description:  Test file logs with offset option.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv14a, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results7)

        else:
            self.assertEqual("", self.results7)

    def test_file(self):

        """Function:  test_file

        Description:  Test file logs.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv14, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        with gen_libs.no_std_out():
            check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results7)

        else:
            self.assertEqual("", self.results7)

    @mock.patch("check_log.sys.stdin", io.StringIO(u""))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_empty(self, mock_atty):

        """Function:  test_stdin_empty

        Description:  Test with standard in no data.

        Arguments:

        """

        mock_atty.isatty.return_value = False

        args = gen_class.ArgParser(
            self.argv15, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        self.assertFalse(check_log.run_program(args))

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_marker(self, mock_atty):

        """Function:  test_stdin_marker

        Description:  Test with standard in with marker file.

        Arguments:

        """

        mock_atty.isatty.return_value = False

        args = gen_class.ArgParser(
            self.argv16, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read().rstrip()

            self.assertEqual(out_str, self.results8)

        else:
            self.assertEqual("", self.results8)

    @mock.patch("check_log.sys.stdin", io.StringIO(u"Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin(self, mock_atty):

        """Function:  test_stdin

        Description:  Test with standard in.

        Arguments:

        """

        mock_atty.isatty.return_value = False

        args = gen_class.ArgParser(
            self.argv17, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        if os.path.isfile(self.test_out):
            with open(self.test_out) as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results9)

        else:
            self.assertEqual("", self.results9)

    def test_clear_marker(self):

        """Function:  test_clear_marker

        Description:  Test clearing the marker file.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv18, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)
        check_log.run_program(args)

        self.assertEqual(os.stat(self.file_marker).st_size, 0)

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
