# -*- coding: utf-8 -*-
# this is xlsx handling module
import settings as stt
import json
from openpyxl import load_workbook

class XlHandler(object):
    def __init__(self):
        self.file = None
        self.js_data = None
        self.wb = None
        self.ws = None
        self.data =[]
    def loadFile(self, file_):
        'Loads workbook file and sets it as class '
        bfile = open(file_, 'rb')
        self.wb = load_workbook(filename=bfile,read_only=True)
    def parseFile(self):
        self.ws = self.wb.active
        for row in self.ws.iter_rows(min_row=2, max_col=5, max_row=8):
            drow = {}
            for cell in row:
                print cell.column, ':', cell.value
                if cell.column == 1:
                    drow['part_no']=cell.value
                if cell.column == 2:
                    drow['description']=cell.value
                if cell.column == 4:
                    drow['qty']=cell.value
            self.data.append(dict(line=drow))
