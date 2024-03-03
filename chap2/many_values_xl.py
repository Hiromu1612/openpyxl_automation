import openpyxl

book=openpyxl.Workbook()
sheet=book.active

for i in range(0,10): #(1,10)は1から9までの9回繰り返す
    sheet.cell(row=i+1,column=1,value=i+1)

book.save('chap2/many_values_xl.xlsx')