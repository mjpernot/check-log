# Classification (U)

"""Program:  full_chk.py

    Description:  Integration testing of full_chk in check_log.py.

    Usage:
        test/integration/check_log/full_chk.py

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
        test_file_not_empty
        test_file_is_empty

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")
        self.opt_val = [
            "-i", "-m", "-o", "-s", "-t", "-y", "-F", "-S", "-k", "-g"]
        self.argv = [
            "check_log.py", "-m",
            os.path.join(self.test_path, "full_chk_not_empty.txt")]
        self.argv2 = [
            "check_log.py", "-m",
            os.path.join(self.test_path, "full_chk_empty.txt")]

    def test_file_not_empty(self):

        """Function:  test_file_not_empty

        Description:  Test if file is not empty.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertFalse(check_log.full_chk(args))

    def test_file_is_empty(self):

        """Function:  test_file_is_empty

        Description:  Test if file is empty.

        Arguments:

        """

        args = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertTrue(check_log.full_chk(args))


if __name__ == "__main__":
    unittest.main()
