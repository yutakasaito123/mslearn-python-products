import openpyxl
from openpyxl.utils import get_column_letter,column_index_from_string
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
for cell_obj in tuple(sheet.rows)[1]:
    print(cell_obj.value)
