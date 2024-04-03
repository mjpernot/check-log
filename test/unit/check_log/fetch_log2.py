# Classification (U)

"""Program:  fetch_log2.py

    Description:  Unit testing of fetch_log2 in check_log.py.

    Usage:
        test/unit/check_log/fetch_log2.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import check_log
import lib.gen_class as gen_class
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val
        update_arg

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = dict()

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def update_arg(self, skey, data, insert=False):

        """Method:  update_arg

        Description:  Method stub holder for gen_class.ArgParser.update_arg.

        Arguments:

        """

        if insert:
            self.args_array[skey] = data


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_log_file_rotate
        test_fetch_partial_log
        test_fetch_empty_log
        test_fetch_one_log

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argspar = ArgParser()
        self.log = gen_class.LogFile()
        self.file_0 = "test/unit/check_log/testfiles/fetch_log2_file0.txt"
        self.file_1 = "test/unit/check_log/testfiles/fetch_log2_file1.txt"
        self.file_2 = "test/unit/check_log/testfiles/fetch_log2_file2.txt"
        self.file_3 = "test/unit/check_log/testfiles/fetch_log2_mfile.txt2"
        self.file_4 = "test/unit/check_log/testfiles/fetch_log2_mfile.txt"
        self.results0 = []
        self.results1 = ["This is line one of log", "This is line two of log",
                         "This is line three of log"]
        self.results2 = ["This is line five of log"]
        self.results3 = ["This is line five of log", "This is line six of log",
                         "This is line seven of log"]

    def test_log_file_rotate(self):

        """Function:  test_log_file_rotate

        Description:  Return log entries from new log file and check old log.

        Arguments:

        """

        self.argspar.args_array = {"-f": [self.file_3]}

        check_log.fetch_log2(self.log, self.argspar)

        inode, offset = self.log.lastline.split(":")
        self.log.marker = inode + ":" + "25"
        self.log.loglist = list()
        self.argspar.args_array = {"-f": [self.file_4]}

        check_log.fetch_log2(self.log, self.argspar)

        self.assertEqual(self.log.loglist, self.results3)

    def test_fetch_partial_log(self):

        """Function:  test_fetch_partial_log

        Description:  Return some log entries from a log file.

        Arguments:

        """

        self.argspar.args_array = {"-f": [self.file_2]}

        check_log.fetch_log2(self.log, self.argspar)

        inode, offset = self.log.lastline.split(":")
        self.log.marker = inode + ":" + "25"
        self.log.loglist = list()

        check_log.fetch_log2(self.log, self.argspar)

        self.assertEqual(self.log.loglist, self.results2)

    def test_fetch_empty_log(self):

        """Function:  test_fetch_empty_log

        Description:  Return an empty log.

        Arguments:

        """

        self.argspar.args_array = {"-f": [self.file_0]}

        check_log.fetch_log2(self.log, self.argspar)

        self.assertEqual(self.log.loglist, self.results0)

    def test_fetch_one_log(self):

        """Function:  test_fetch_one_log

        Description:  Return log entries from one log file.

        Arguments:

        """

        self.argspar.args_array = {"-f": [self.file_1]}

        check_log.fetch_log2(self.log, self.argspar)

        self.assertEqual(self.log.loglist, self.results1)


if __name__ == "__main__":
    unittest.main()
