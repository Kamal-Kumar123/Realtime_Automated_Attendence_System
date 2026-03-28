import xlrd
from xlutils.copy import copy
import os
import datetime
import xlsxwriter


def mark_present(st_name):
	_base = os.path.dirname(os.path.abspath(__file__))
	output_dir = os.path.join(_base, 'output')
	attendance_dir = os.path.join(_base, 'attendance')
	os.makedirs(output_dir, exist_ok=True)
	os.makedirs(attendance_dir, exist_ok=True)

	names = os.listdir(output_dir)
	print(names)

	sub = 'SAMPLE'
	xlsx_path = os.path.join(attendance_dir, sub + '.xlsx')

	if not os.path.exists(xlsx_path):
		count = 2
		workbook = xlsxwriter.Workbook(xlsx_path)
		print("Creating Spreadsheet with Title: " + sub)
		sheet = workbook.add_worksheet()
		for i in names:
		    sheet.write(count, 0, i)
		    count += 1
		workbook.close()

	rb = xlrd.open_workbook(xlsx_path)
	wb = copy(rb)
	sheet = wb.get_sheet(0)
	sheet.write(1,1,str(datetime.datetime.now()))


	count = 2
	for i in names:
	    if i in st_name:
              sheet.write(count, 1, 'P')
	    else:
              sheet.write(count, 1, 'A')
	    sheet.write(count, 0, i)
	    count += 1

	wb.save(xlsx_path)
