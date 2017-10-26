# -*- coding: utf-8 -*-
from xl import XlHandler

xl = XlHandler()
xl.loadFile('stellio.xlsx')
xl.parseFile()
print xl.data