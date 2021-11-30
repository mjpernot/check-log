#!/usr/bin/python
# Classification (U)

"""Program:  update_marker.py

    Description:  Unit testing of update_marker in check_log.py.

    Usage:
        test/unit/check_log/update_marker.py

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

# Local
sys.path.append(os.getcwd())
import check_log
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_m_option_not_set
        test_n_option_set
        test_update_marker
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = \
            {"-m": "test/unit/check_log/testfiles/update_marker_file.txt"}

        self.marker_line = "This is the first line"

    def test_m_option_not_set(self):

        """Function:  test_m_option_not_set

        Description:  Test with -m option not set.

        Arguments:

        """

        self.assertFalse(check_log.update_marker({}, self.marker_line))

    def test_n_option_set(self):

        """Function:  test_n_option_set

        Description:  Test with -n option set to True.

        Arguments:

        """

        self.args_array["-n"] = True

        check_log.update_marker(self.args_array, self.marker_line)

        if os.path.isfile(self.args_array["-m"]):
            status = False

        else:
            status = True

        self.assertTrue(status)

    def test_update_marker(self):

        """Function:  test_update_marker

        Description:  Write correct entry to file marker file.

        Arguments:

        """

        check_log.update_marker(self.args_array, self.marker_line)

        with open(self.args_array["-m"], "r") as f_hdlr:
            marker_str = f_hdlr.readline().strip("\n")

        self.assertEqual(marker_str, self.marker_line)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.args_array["-m"]):
            os.remove(self.args_array["-m"])


if __name__ == "__main__":
    unittest.main()
