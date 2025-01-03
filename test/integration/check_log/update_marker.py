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
import unittest

# Local
sys.path.append(os.getcwd())
import check_log                    # pylint:disable=E0401,C0413
import lib.gen_class as gen_class   # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

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
        self.file_name = os.path.join(self.test_path, "update_marker_file.txt")
        self.argv = ["check_log.py", "-m", self.file_name]
        self.opt_val = [
            "-i", "-m", "-o", "-s", "-t", "-y", "-F", "-S", "-k", "-g"]
        self.marker_line = "This is the last line"

    def test_update_marker(self):

        """Function:  test_update_marker

        Description:  Write correct entry to file marker file.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)
        check_log.update_marker(args, self.marker_line)

        with open(args.args_array["-m"], mode="r", encoding="UTF-8") as f_hdlr:
            marker_str = f_hdlr.readline().strip("\n")

        self.assertEqual(marker_str, self.marker_line)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isfile(self.file_name):
            os.remove(self.file_name)


if __name__ == "__main__":
    unittest.main()
