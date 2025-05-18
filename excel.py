import openpyxl
from openpyxl.utils import get_column_letter,column_index_from_string
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
print(tuple(sheet['a1':'c3']))
