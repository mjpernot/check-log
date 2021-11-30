#!/usr/bin/python
# Classification (U)

"""Program:  update_marker.py

    Description:  Integration testing of update_marker in check_log.py.

    Usage:
        test/integration/check_log/update_marker.py

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
        test_update_marker
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        self.args_array = {"-m": os.path.join(self.test_path,
                                              "update_marker_file.txt")}

        self.marker_line = "This is the last line"

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

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isfile(self.args_array["-m"]):
            os.remove(self.args_array["-m"])


if __name__ == "__main__":
    unittest.main()
