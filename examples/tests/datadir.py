#!/usr/bin/env python

import os
import shutil

from avocado import Test
from avocado import main
from avocado.utils import build
from avocado.utils import process


class DataDirTest(Test):

    """
    Test that uses resources from the data dir.

    :avocado: tags=requires_c_compiler
    """

    def setUp(self):
        """
        Build 'datadir'.
        """
        source = self.params.get('source', default='datadir.c')
        c_file = self.get_data(source)
        if c_file is None:
            self.cancel('Test is missing data file %s' % source)
        c_file_name = os.path.basename(c_file)
        dest_c_file = os.path.join(self.srcdir, c_file_name)
        shutil.copy(c_file, dest_c_file)
        build.make(self.srcdir,
                   env={'CFLAGS': '-g -O0'},
                   extra_args='datadir')

    def test(self):
        """
        Execute 'datadir'.
        """
        cmd = os.path.join(self.srcdir, 'datadir')
        cmd_result = process.run(cmd)
        self.log.info(cmd_result)


if __name__ == "__main__":
    main()
