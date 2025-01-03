# Classification (U)

"""Program:  main.py

    Description:  Integration testing of main in check_log.py.

    Usage:
        test/integration/check_log/main.py

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
import check_log                    # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_or_search_offset
        test_or_search
        test_and_search_offset
        test_and_search
        test_stdin_marker
        test_stdin_marker_empty
        test_stdin
        test_marker_offset
        test_marker
        test_file_offset
        test_file
        test_arg_file_chk
        test_arg_cond_req_or
        test_help
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.prt_format = "ERROR:  Test environment setup failed. Message: %s"
        self.skip_msg = "Pre-conditions not met."
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
        status, err_msg = gen_libs.cp_file(
            base_marker, self.test_path, self.test_path, marker_name)

        if not status:
            print(self.prt_format % (err_msg))
            self.skipTest(self.skip_msg)

        status, err_msg = gen_libs.cp_file(
            filename1, self.test_path, self.test_path, logname1)

        if not status:
            os.remove(self.file_marker)
            print(self.prt_format % (err_msg))
            self.skipTest(self.skip_msg)

        status, err_msg = gen_libs.cp_file(
            filename2, self.test_path, self.test_path, logname2)

        if not status:
            os.remove(self.file_marker)
            os.remove(self.log_file1)
            print(self.prt_format % (err_msg))
            self.skipTest(self.skip_msg)

        self.argv_list = [os.path.join(self.base_dir, "main.py")]
        self.results = "This is the sixth line\nThis is the seventh line\n"

    def test_or_search_offset(self):

        """Function:  test_or_search_offset

        Description:  Test with or search clause and offset option.

        Arguments:

        """

        self.argv_list.extend(
            ["-f", self.log_file2, "-o", self.test_out, "-S", "sixth", "tenth",
             "-k", "or", "-R", "offset"])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, "This is the sixth line\n")

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    def test_or_search(self):

        """Function:  test_or_search

        Description:  Test with or search clause.

        Arguments:

        """

        self.argv_list.extend(
            ["-f", self.log_file2, "-o", self.test_out, "-S", "sixth", "tenth",
             "-k", "or"])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, "This is the sixth line\n")

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    def test_and_search_offset(self):

        """Function:  test_and_search_offset

        Description:  Test with and search clause and offset option.

        Arguments:

        """

        self.argv_list.extend(
            ["-f", self.log_file2, "-o", self.test_out, "-S", "is", "line",
             "-k", "and", "-R", "offset"])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results)

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    def test_and_search(self):

        """Function:  test_and_search

        Description:  Test with and search clause.

        Arguments:

        """

        self.argv_list.extend(
            ["-f", self.log_file2, "-o", self.test_out, "-S", "is", "line",
             "-k", "and"])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results)

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    @mock.patch("check_log.sys.stdin", io.StringIO("Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_marker(self, mock_atty):

        """Function:  test_stdin_marker

        Description:  Test with standard in with marker file.

        Arguments:

        """

        mock_atty.isatty.return_value = False
        self.argv_list.extend(["-o", self.test_out, "-n", "-z",
                               "-m", self.file_marker2])
        sys.argv = self.argv_list

        check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read().rstrip()

            self.assertEqual(out_str, "Line two")

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    @mock.patch("check_log.sys.stdin", io.StringIO("Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin_marker_empty(self, mock_atty):

        """Function:  test_stdin_marker_empty

        Description:  Test with standard in with an empty marker file.

        Arguments:

        """

        mock_atty.isatty.return_value = False
        self.argv_list.extend(["-o", self.test_out, "-n", "-z",
                               "-m", os.path.join(self.test_path,
                                                  self.base_marker3)])
        sys.argv = self.argv_list

        check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read().rstrip()

            self.assertEqual(out_str, "Line one\nLine two")

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    @mock.patch("check_log.sys.stdin", io.StringIO("Line one\nLine two\n"))
    @mock.patch("check_log.sys.stdin")
    def test_stdin(self, mock_atty):

        """Function:  test_stdin

        Description:  Test with standard in.

        Arguments:

        """

        mock_atty.isatty.return_value = False
        self.argv_list.extend(["-o", self.test_out, "-z"])
        sys.argv = self.argv_list

        check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, "Line one\nLine two\n")

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    def test_clear_marker(self):

        """Function:  test_clear_marker

        Description:  Test clear marker file.

        Arguments:

        """

        self.argv_list.extend(["-c", "-m", self.file_marker])
        sys.argv = self.argv_list

        check_log.main()

        self.assertEqual(os.stat(self.file_marker).st_size, 0)

    def test_marker_offset(self):

        """Function:  test_marker_offset

        Description:  Test file log with marker and offset option.

        Arguments:

        """

        self.argv_list.extend(
            ["-f", self.log_file1, "-m", self.test_out, "-R", "offset"])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        inode = os.stat(self.log_file1).st_ino
        offset = 117

        with open(self.test_out, encoding="UTF-8") as f_hdlr:
            out_str = f_hdlr.read()

        inode2, offset2 = map(int, out_str.split(":"))
        self.assertEqual((inode, offset), (inode2, offset2))

    def test_marker(self):

        """Function:  test_marker

        Description:  Test file log with marker.

        Arguments:

        """

        self.argv_list.extend(["-f", self.log_file1, self.log_file2, "-o",
                               self.test_out, "-m", self.file_marker])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, "This is the seventh line\n")

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    def test_file_offset(self):

        """Function:  test_file_offset

        Description:  Test file log with the offset option.

        Arguments:

        """

        self.argv_list.extend(
            ["-f", self.log_file2, "-o", self.test_out, "-R", "offset"])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results)

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    def test_file(self):

        """Function:  test_file

        Description:  Test file log.

        Arguments:

        """

        self.argv_list.extend(["-f", self.log_file2, "-o", self.test_out])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            check_log.main()

        if os.path.isfile(self.test_out):
            with open(self.test_out, encoding="UTF-8") as f_hdlr:
                out_str = f_hdlr.read()

            self.assertEqual(out_str, self.results)

        else:
            self.assertTrue(os.path.isfile(self.test_out))

    def test_arg_file_chk(self):

        """Function:  test_arg_file_chk

        Description:  Test arg_file_chk function.

        Arguments:

        """

        self.argv_list.extend(
            ["-f", os.path.join(self.test_path, "main_dummy.txt")])
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(check_log.main())

    def test_arg_cond_req_or(self):

        """Function:  test_arg_cond_req_or

        Description:  Test arg_cond_req_or function.

        Arguments:

        """

        self.argv_list.append("-c")
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(check_log.main())

    def test_help(self):

        """Function:  test_help

        Description:  Test help_func function.

        Arguments:

        """

        self.argv_list.append("-h")
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(check_log.main())

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
