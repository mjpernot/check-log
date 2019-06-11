#!/usr/bin/python
# Classification (U)

"""Program:  search.py

    Description:  Unit testing of search in check_log.py.

    Usage:
        test/unit/check_log/search.py

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
import mock

# Local
sys.path.append(os.getcwd())
import check_log
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_none_found -> Test with no keywords found.
        test_all_key -> Test with "all" search logic.
        test_any_key -> Test with "any" search logic.
        test_multi_key -> Test with multiple items in key list.
        test_single_key -> Test with single item in key list.
        test_empty_key -> Test with empty key list.
        test_empty_log -> Test with empty log array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.logarray = []
        self.logarray2 = ["this is a test", "another test", "yet something"]
        self.logarray3 = ["this is a test", "another test", "yet something",
                          "and something else", "what about this test"]

        self.keylist = []
        self.keylist2 = ["this"]
        self.keylist3 = ["this", "yet"]
        self.keylist4 = ["a", "test"]
        self.keylist5 = ["strange"]

        self.results = []
        self.results2 = ["this is a test"]
        self.results3 = ["this is a test", "yet something"]
        self.results4 = ["this is a test", "yet something",
                         "what about this test"]
        self.results5 = ["this is a test", "another test",
                         "what about this test"]

    def test_none_found(self):

        """Function:  test_none_found

        Description:  Test with no keywords found.

        Arguments:

        """

        self.assertEqual(check_log.search(self.logarray3, self.keylist5, any),
                         self.results)

    def test_all_key(self):

        """Function:  test_all_key

        Description:  Test with "all" search logic.

        Arguments:

        """

        self.assertEqual(check_log.search(self.logarray3, self.keylist4, all),
                         self.results5)

    def test_any_key(self):

        """Function:  test_any_key

        Description:  Test with "any" search logic.

        Arguments:

        """

        self.assertEqual(check_log.search(self.logarray3, self.keylist3, any),
                         self.results4)

    def test_multi_key(self):

        """Function:  test_multi_key

        Description:  Test with multiple items in key list.

        Arguments:

        """

        self.assertEqual(check_log.search(self.logarray2, self.keylist2, any),
                         self.results2)

    def test_single_key(self):

        """Function:  test_single_key

        Description:  Test with single item in key list.

        Arguments:

        """

        self.assertEqual(check_log.search(self.logarray2, self.keylist2, any),
                         self.results2)

    def test_empty_key(self):

        """Function:  test_empty_key

        Description:  Test with empty key list.

        Arguments:

        """

        self.assertEqual(check_log.search(self.logarray2, self.keylist, any),
                         self.results)

    def test_empty_log(self):

        """Function:  test_empty_log

        Description:  Test with empty log array.

        Arguments:

        """

        self.assertEqual(check_log.search(self.logarray, self.keylist2, any),
                         self.results)


if __name__ == "__main__":
    unittest.main()
