#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import xlrd
import sys
if(len(sys.argv) < 2):
	print "please pass the file name in the command"
	sys.exit(0)
FILE_NAME = sys.argv[1]
data = xlrd.open_workbook(FILE_NAME)
sheets = data.sheets()
for table in sheets:
	print "行数 = " + str(table.nrows) + " 列数" + str(table.ncols)
	# for index in range(0, table.nrows):
	# 	print table.row_values(index)
	# for index in range(0, table.ncols):
	# 	print table.col_values(index)
	for row in range(0, table.nrows):
		for col in range(0, table.ncols):
			print table.cell(row, col).value