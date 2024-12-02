# Classification (U)

"""Program:  read_file.py

    Description:  Unit testing of read_file in check_log.py.

    Usage:
        test/unit/check_log/read_file.py

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
        test_read_partial_file2
        test_read_partial_file
        test_read_file2
        test_read_file
        test_read_empty_file2
        test_read_empty_file

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.log = gen_class.LogFile()
        self.file_0 = "test/unit/check_log/testfiles/read_file_file0.txt"
        self.file_1 = "test/unit/check_log/testfiles/read_file_file1.txt"
        self.file_2 = "test/unit/check_log/testfiles/read_file_file2.txt"
        self.results0 = []
        self.results1 = ["This is line one of log", "This is line two of log",
                         "This is line three of log"]
        self.results2 = ["This is line five of log"]

    def test_read_partial_file2(self):

        """Function:  test_read_partial_file2

        Description:  Return some entries from log file.

        Arguments:

        """

        inode = os.stat(self.file_2).st_ino

        check_log.read_file(self.log, self.file_2, inode, 25)

        self.assertEqual(self.log.lastline, str(inode) + ":" + str(50))

    def test_read_partial_file(self):

        """Function:  test_read_partial_file

        Description:  Return some entries from log file.

        Arguments:

        """

        inode = os.stat(self.file_2).st_ino

        check_log.read_file(self.log, self.file_2, inode, 25)

        self.assertEqual(self.log.loglist, self.results2)

    def test_read_file2(self):

        """Function:  test_read_file2

        Description:  Return entries from log file.

        Arguments:

        """

        inode = os.stat(self.file_0).st_ino

        check_log.read_file(self.log, self.file_1, inode, 0)

        self.assertEqual(self.log.lastline, str(inode) + ":" + str(74))

    def test_read_file(self):

        """Function:  test_read_file

        Description:  Return entries from log file.

        Arguments:

        """

        inode = os.stat(self.file_0).st_ino

        check_log.read_file(self.log, self.file_1, inode, 0)

        self.assertEqual(self.log.loglist, self.results1)

    def test_read_empty_file2(self):

        """Function:  test_read_empty_file2

        Description:  Return empty log file.

        Arguments:

        """

        inode = os.stat(self.file_0).st_ino

        check_log.read_file(self.log, self.file_0, inode, 0)

        self.assertEqual(self.log.lastline, str(inode) + ":" + str(0))

    def test_read_empty_file(self):

        """Function:  test_read_empty_file

        Description:  Return empty log file.

        Arguments:

        """

        inode = os.stat(self.file_0).st_ino

        check_log.read_file(self.log, self.file_0, inode, 0)

        self.assertEqual(self.log.loglist, self.results0)


if __name__ == "__main__":
    unittest.main()
