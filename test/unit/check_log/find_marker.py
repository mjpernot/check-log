#!/usr/bin/python
# Classification (U)

"""Program:  find_marker.py

    Description:  Unit testing of find_marker in check_log.py.

    Usage:
        test/unit/check_log/find_marker.py

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
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_empty_ln_marker -> Empty line marker check.
        test_no_find_marker -> Does not find the marker.
        test_find_marker_2 -> Finds the line marker in second file.
        test_find_marker -> Finds the line marker.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args_array = \
            {"-f": ["test/unit/check_log/testfiles/find_marker_file.txt",
                    "test/unit/check_log/testfiles/find_marker_file2.txt"],
             "-m": "Marker_File_Name"}

        self.next_line = "This is the fourth line"
        self.next_line2 = "This is the seventh line"
        self.no_line = "This is the first line"

    @mock.patch("check_log.fetch_marker_entry")
    def test_empty_ln_marker(self, mock_marker):

        """Function:  test_empty_ln_marker

        Description:  Empty line marker check.

        Arguments:
            mock_marker -> Mock Ref:  check_log.fetch_marker_entry

        """

        mock_marker.return_value = None

        f_hdlr = check_log.find_marker(self.args_array)

        data_line = f_hdlr.next().rstrip()
        f_hdlr.close()

        self.assertEqual(data_line, self.no_line)

    @mock.patch("check_log.fetch_marker_entry")
    def test_no_find_marker(self, mock_marker):

        """Function:  test_no_find_marker

        Description:  Does not find the marker.

        Arguments:
            mock_marker -> Mock Ref:  check_log.fetch_marker_entry

        """

        mock_marker.return_value = "This is the tenth line"

        f_hdlr = check_log.find_marker(self.args_array)

        data_line = f_hdlr.next().rstrip()
        f_hdlr.close()

        self.assertEqual(data_line, self.no_line)

    @mock.patch("check_log.fetch_marker_entry")
    def test_find_marker_2(self, mock_marker):

        """Function:  test_find_marker_2

        Description:  Finds the line marker in second file.

        Arguments:
            mock_marker -> Mock Ref:  check_log.fetch_marker_entry

        """

        mock_marker.return_value = "This is the sixth line"

        f_hdlr = check_log.find_marker(self.args_array)

        data_line = f_hdlr.next().rstrip()
        f_hdlr.close()

        self.assertEqual(data_line, self.next_line2)

    @mock.patch("check_log.fetch_marker_entry")
    def test_find_marker(self, mock_marker):

        """Function:  test_find_marker

        Description:  Finds the line marker.

        Arguments:
            mock_marker -> Mock Ref:  check_log.fetch_marker_entry

        """

        mock_marker.return_value = "This is the third line"

        f_hdlr = check_log.find_marker(self.args_array)

        data_line = f_hdlr.next().rstrip()
        f_hdlr.close()

        self.assertEqual(data_line, self.next_line)


if __name__ == "__main__":
    unittest.main()
