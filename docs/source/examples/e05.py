# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys
import time


CNT = 5

for i in range(CNT):
    sys.stdout.write(' '*100 + '\r')  # 在输出之前先清空缓冲区
    sys.stdout.flush()

    print('现在下载到第%d个' % (i+1))

    sys.stdout.write('现在进行到：%d/%d\r' % (i+1, CNT))  # 往标准输出缓冲区打印字符
    sys.stdout.flush()  # 把缓冲区里面的字符打印到标准输出
    time.sleep(1)  # 模拟耗时操作
