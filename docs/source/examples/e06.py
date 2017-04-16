# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys
import time

CNT = 100

for i in range(CNT):
    sys.stdout.write(' '*100 + '\r')
    sys.stdout.flush()

    sys.stdout.write('%d/%d [' % (i+1, CNT) + '#'*i + ' ]\r')
    sys.stdout.flush()
    time.sleep(1)
