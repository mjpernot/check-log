# Classification (U)

"""Program:  load_attributes.py

    Description:  Unit testing of load_attributes in check_log.py.

    Usage:
        test/unit/check_log/load_attributes.py

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


class ArgParser():

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

        self.args_array = {}

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

    Description:  Class which is a representation of unit testing.

    Methods:
        setUp
        test_load_ignore
        test_load_regex
        test_load_marker
        test_set_predicate
        test_load_keyword

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argspar = ArgParser()
        self.log = gen_class.LogFile()
        self.ign_file = "test/unit/check_log/testfiles/loadignore.txt"
        self.filter_file = "test/unit/check_log/testfiles/loadregex.txt"
        self.marker_file = "test/unit/check_log/testfiles/loadmarker.txt"

    def test_load_ignore(self):

        """Function:  test_load_ignore

        Description:  Test loading the ignore entries.

        Arguments:

        """

        self.argspar.args_array["-i"] = self.ign_file

        check_log.load_attributes(self.log, self.argspar)

        self.assertEqual(self.log.ignore, ["this is a test ignore entry"])

    def test_load_regex(self):

        """Function:  test_load_regex

        Description:  Test loading the regex statement.

        Arguments:

        """

        self.argspar.args_array["-F"] = self.filter_file

        check_log.load_attributes(self.log, self.argspar)

        self.assertEqual(self.log.regex, "\\d{4}\\-\\d{2}\\-\\d{2}")

    def test_load_marker(self):

        """Function:  test_load_marker

        Description:  Test loading the log marker.

        Arguments:

        """

        self.argspar.args_array["-m"] = self.marker_file

        check_log.load_attributes(self.log, self.argspar)

        self.assertEqual(self.log.marker, "This is a test marker")

    def test_set_predicate(self):

        """Function:  test_set_predicate

        Description:  Test setting the predicate.

        Arguments:

        """

        self.argspar.args_array["-k"] = "and"

        check_log.load_attributes(self.log, self.argspar)

        self.assertEqual(self.log.predicate, all)

    def test_load_keyword(self):

        """Function:  test_load_keyword

        Description:  Test loading keyword.

        Arguments:

        """

        self.argspar.args_array["-S"] = "testkeyword"

        check_log.load_attributes(self.log, self.argspar)

        self.assertEqual(self.log.keyword, ["testkeyword"])


if __name__ == "__main__":
    unittest.main()
