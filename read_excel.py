import xlrd

workbook = xlrd.open_workbook('D:\ToriCode\Python\sample.xlsx')
sheet = workbook.sheet_by_index(0)

for row in range(sheet.nrows):
    values = []
    for col in range(sheet.ncols):
        cell_value = sheet.cell_value(row, col)
        values.append(cell_value)
    print(','.join(values))
