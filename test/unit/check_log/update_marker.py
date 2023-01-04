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

# Local
sys.path.append(os.getcwd())
import check_log
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = dict()

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_default.

        Arguments:

        """

        if arg in self.args_array:
            return True

        return False

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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

        self.argspar = ArgParser()

        self.marker_line = "This is the first line"
        self.file_name = "test/unit/check_log/testfiles/update_marker_file.txt"

    def test_m_option_not_set(self):

        """Function:  test_m_option_not_set

        Description:  Test with -m option not set.

        Arguments:

        """

        self.assertFalse(
            check_log.update_marker(self.argspar, self.marker_line))

    def test_n_option_set(self):

        """Function:  test_n_option_set

        Description:  Test with -n option set to True.

        Arguments:

        """

        self.argspar.args_array = {"-m": self.file_name}
        self.argspar.args_array["-n"] = True

        check_log.update_marker(self.argspar, self.marker_line)

        if os.path.isfile(self.argspar.args_array["-m"]):
            status = False

        else:
            status = True

        self.assertTrue(status)

    def test_update_marker(self):

        """Function:  test_update_marker

        Description:  Write correct entry to file marker file.

        Arguments:

        """

        self.argspar.args_array = {"-m": self.file_name}

        check_log.update_marker(self.argspar, self.marker_line)

        with open(self.argspar.args_array["-m"], "r") as f_hdlr:
            marker_str = f_hdlr.readline().strip("\n")

        self.assertEqual(marker_str, self.marker_line)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.file_name):
            os.remove(self.file_name)


if __name__ == "__main__":
    unittest.main()
