import openpyxl

book=openpyxl.load_workbook(r"C:\Users\1612h\Downloads\0src\samples\ch3\date-sample.xlsx")
sheet=book.active
print(sheet["A4"].number_format)
print(sheet["A4"].value)
print(type(sheet["A4"].value))