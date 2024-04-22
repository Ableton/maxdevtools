# A utility method to capture the output of the textconv stripts as strings

import sys
import os.path
from unittest.mock import patch
from io import StringIO

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import amxd_textconv
import maxpat_textconv
import als_textconv


def parse(path):
    mains = {
        ".amxd": amxd_textconv.main,
        ".maxpat": maxpat_textconv.main,
        ".als": als_textconv.main,
    }

    file_extension = os.path.splitext(path)[1]
    if file_extension in mains:
        # route std output to a cystom StringIO
        old_stdout = sys.stdout
        sys.stdout = actualStringIo = StringIO()

        # set the main arguments
        old_sys_argv = sys.argv
        sys.argv = [old_sys_argv[0]] + [path]

        # call the main function of the appropriate script
        try:
            patch("sys.argv", ["prog", path])
            mains[file_extension]()
        finally:
            sys.argv = old_sys_argv
            sys.stdout = old_stdout
        return actualStringIo.getvalue()[:-1]
    return ""
