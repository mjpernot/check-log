#!/usr/bin/python
# Classification (U)

"""Program:  fetch_log.py

    Description:  Integration testing of fetch_log in check_log.py.

    Usage:
        test/integration/check_log/fetch_log.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import time

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

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
        setUp -> Integration testing initilization.
        test_search_and -> Return log entries with and search clause.
        test_search_or -> Return log entries with or search clause.
        test_fetch_log_all -> Return log entries from all log files.
        test_fetch_log -> Return log entries from some log files.
        tearDown -> Clean up of integration testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/check_log"
        self.test_path = os.path.join(os.getcwd(), self.base_dir, "testfiles")

        filename1 = "fetch_log_base_file.txt"
        filename2 = "fetch_log_base_file2.txt"

        self.logname1 = "fetch_log_file.txt"
        self.logname2 = "fetch_log_file2.txt"

        self.file_marker = os.path.join(self.test_path, "fetch_log_entry.txt")

        status, err_msg = gen_libs.cp_file(filename1, self.test_path,
                                           self.test_path, self.logname1)

        if not status:
            print("ERROR:  Test environment setup failed. Message: %s"
                  % (self.err_msg))
            self.skipTest("Pre-conditions not met.")

        status, err_msg = gen_libs.cp_file(filename2, self.test_path,
                                           self.test_path, self.logname2)

        if not status:
            os.remove(os.path.join(self.test_path, self.logname1))
            print("ERROR:  Test environment setup failed. Message: %s"
                  % (self.err_msg))
            self.skipTest("Pre-conditions not met.")

        self.args_array = {"-f": [os.path.join(self.test_path, self.logname2),
                                  os.path.join(self.test_path, self.logname1)]}
        self.args_array2 = {"-f": [os.path.join(self.test_path, self.logname2),
                            os.path.join(self.test_path, self.logname1)],
                            "-S": ["third", "sixth"], "-k": "or"}
        self.args_array3 = {"-f": [os.path.join(self.test_path, self.logname2),
                            os.path.join(self.test_path, self.logname1)],
                            "-S": ["third", "line"], "-k": "and"}

        self.results = ["This is the sixth line", "This is the seventh line"]
        self.results2 = ["This is the first line", "This is the second line",
                         "This is the third line", "This is the fourth line",
                         "This is the fifth line", "This is the sixth line",
                         "This is the seventh line"]
        self.results3 = ["This is the third line", "This is the sixth line"]
        self.results4 = ["This is the third line"]

        # Touch files to set correct time order, require sleep.
        gen_libs.touch(os.path.join(self.test_path, self.logname1))
        time.sleep(1)
        gen_libs.touch(os.path.join(self.test_path, self.logname2))

    def test_search_and(self):

        """Function:  test_search_and

        Description:  Return log entries with and search clause.

        Arguments:

        """

        self.assertEqual(check_log.fetch_log(self.args_array3), self.results4)

    def test_search_or(self):

        """Function:  test_search_or

        Description:  Return log entries with or search clause.

        Arguments:

        """

        self.assertEqual(check_log.fetch_log(self.args_array2), self.results3)

    def test_fetch_log_all(self):

        """Function:  test_fetch_log_all

        Description:  Return log entries from all log files.

        Arguments:

        """

        self.assertEqual(check_log.fetch_log(self.args_array), self.results2)

    def test_fetch_log(self):

        """Function:  test_fetch_log

        Description:  Return log entries from some log files.

        Arguments:

        """

        self.args_array["-m"] = self.file_marker

        self.assertEqual(check_log.fetch_log(self.args_array), self.results)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        os.remove(os.path.join(self.test_path, self.logname1))
        os.remove(os.path.join(self.test_path, self.logname2))


if __name__ == "__main__":
    unittest.main()
