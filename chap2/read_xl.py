import openpyxl

book=openpyxl.load_workbook('chap2/excell_file/coordinate_xl.xlsx')
sheet=book.active

#1つ目
print(sheet['A1'].value)

#2つ目
print(sheet.cell(row=1,column=1).value)
