#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import check_log
import lib.gen_class as gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_load_ignore -> Test loading the ignore entries.
        test_load_regex -> Test loading the regex statement.
        test_load_marker -> Test loading the log marker.
        test_set_predicate -> Test setting the predicate.
        test_load_keyword -> Test loading keyword.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.log = gen_class.LogFile()
        self.args_array = {}

    def test_load_ignore(self):

        """Function:  test_load_ignore

        Description:  Test loading the ignore entries.

        Arguments:

        """

        self.args_array["-i"] = "test/unit/check_log/testfiles/loadignore.txt"
        check_log.load_attributes(self.log, self.args_array)

        self.assertEqual(self.log.ignore, ["this is a test ignore entry"])

    def test_load_regex(self):

        """Function:  test_load_regex

        Description:  Test loading the regex statement.

        Arguments:

        """

        self.args_array["-F"] = "test/unit/check_log/testfiles/loadregex.txt"
        check_log.load_attributes(self.log, self.args_array)

        self.assertEqual(self.log.regex, "\\d{4}\\-\\d{2}\\-\\d{2}")

    def test_load_marker(self):

        """Function:  test_load_marker

        Description:  Test loading the log marker.

        Arguments:

        """

        self.args_array["-m"] = "test/unit/check_log/testfiles/loadmarker.txt"
        check_log.load_attributes(self.log, self.args_array)

        self.assertEqual(self.log.marker, "This is a test marker")

    def test_set_predicate(self):

        """Function:  test_set_predicate

        Description:  Test setting the predicate.

        Arguments:

        """

        self.args_array["-k"] = "and"
        check_log.load_attributes(self.log, self.args_array)

        self.assertEqual(self.log.predicate, all)

    def test_load_keyword(self):

        """Function:  test_load_keyword

        Description:  Test loading keyword.

        Arguments:

        """

        self.args_array["-S"] = "testkeyword"
        check_log.load_attributes(self.log, self.args_array)

        self.assertEqual(self.log.keyword, ["testkeyword"])


if __name__ == "__main__":
    unittest.main()
