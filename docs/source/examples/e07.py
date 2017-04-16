from __future__ import absolute_import, unicode_literals
import time
from progressbar import ProgressBar


CNT = 100

with ProgressBar(max_value=CNT) as bar:
    for i in range(CNT):
        bar.update(i+1)
        time.sleep(1)
